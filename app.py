"""
Personality Prediction API
Predicts Introvert / Extrovert from behavioural features.
"""
import os
import json
import joblib
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ── Load model & metadata ─────────────────────────────────────────────────────
BASE = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE, "model.pkl"))
with open(os.path.join(BASE, "model_meta.json")) as f:
    meta = json.load(f)

FEATURES = meta["features"]  # expected input columns
LABEL_MAP = meta["label_map"]  # {"0": "Extrovert", "1": "Introvert"}

# ── Health-check & UI ─────────────────────────────────────────────────────────
@app.route("/", methods=["GET"])
def health():
    if request.accept_mimetypes.accept_html:
        return render_template("index.html")
    return jsonify({
        "status": "ok",
        "model": meta["best_model"],
        "test_accuracy": meta["test_accuracy"],
        "expected_fields": FEATURES
    })

# ── Prediction endpoint ───────────────────────────────────────────────────────
@app.route("/predict", methods=["POST"])
def predict():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Accept a single dict OR a list of dicts
    records = body if isinstance(body, list) else [body]

    results = []
    for rec in records:
        # Build a single-row DataFrame in the exact column order the model expects
        row = {}
        for feat in FEATURES:
            val = rec.get(feat)
            row[feat] = val  # None → will be imputed by the pipeline

        df = pd.DataFrame([row])

        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0]

        results.append({
            "prediction": LABEL_MAP[str(pred)],
            "confidence": round(float(prob[pred]), 4),
            "probabilities": {
                "Extrovert": round(float(prob[0]), 4),
                "Introvert": round(float(prob[1]), 4)
            }
        })

    return jsonify(results[0] if not isinstance(body, list) else results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
