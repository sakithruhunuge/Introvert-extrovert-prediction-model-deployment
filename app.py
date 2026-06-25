import os
import json
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE, "model.pkl"))
with open(os.path.join(BASE, "model_meta.json")) as f:
    meta = json.load(f)

FEATURES = meta["features"]
LABEL_MAP = meta["label_map"]

@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "model": meta["best_model"],
        "test_accuracy": meta["test_accuracy"],
        "expected_fields": FEATURES
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
