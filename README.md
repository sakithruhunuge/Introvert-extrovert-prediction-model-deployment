# Personality Analyzer

An intelligent machine learning web application that predicts whether a person is an **Introvert** or **Extrovert** based on 7 key behavioral features. Built using Python, Flask, and Scikit-Learn.

---

## Features

- **Dashboard UI**: A responsive, space-themed dark mode user interface featuring glassmorphic controls and custom sliders.
- **Spectrum Comparison Chart**: Dynamic probability charts indicating the percentage match for both Introversion and Extroversion.
- **Dynamic Trait Insights**: Automatically generated text summaries explaining the classification outcome based on user input.
- **REST API Endpoint**: Standard JSON API endpoint for programmatic classification.

---

## Running Locally

### 1. Set Up Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
source venv/bin/activate      # macOS/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Flask App
```bash
python app.py
```
Open **`http://127.0.0.1:5000/`** in your browser to access the dashboard.

---

## API Documentation

### `GET /` — Health & Metadata
Returns model details and expected features. Serve HTML dashboard if requested by a browser.

**Sample JSON Response:**
```json
{
  "expected_fields": [
    "Time_spent_Alone",
    "Stage_fear",
    "Social_event_attendance",
    "Going_outside",
    "Drained_after_socializing",
    "Friends_circle_size",
    "Post_frequency"
  ],
  "model": "Logistic Regression",
  "status": "ok",
  "test_accuracy": 0.9172
}
```

### `POST /predict` — Run Classification
Accepts a JSON payload (single record or list of records) and returns predictions.

**Request Body:**
```json
{
  "Time_spent_Alone": 7,
  "Stage_fear": "Yes",
  "Social_event_attendance": 2,
  "Going_outside": 2,
  "Drained_after_socializing": "Yes",
  "Friends_circle_size": 3,
  "Post_frequency": 2
}
```

**Response:**
```json
{
  "prediction": "Introvert",
  "confidence": 0.9256,
  "probabilities": {
    "Extrovert": 0.0744,
    "Introvert": 0.9256
  }
}
```

---

## Deployment (Render)

1. Push this repository to GitHub.
2. Link the repository to a new **Web Service** on [Render](https://render.com).
3. Set the build environment to Python and the start command to:
   ```bash
   gunicorn app:app
   ```
