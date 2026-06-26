# Personality Analyzer

This project builds a machine learning web app that predicts whether a person is more likely to be an Introvert or an Extrovert based on 7 behavioral features. The app uses Python, Flask, and Scikit-Learn.

## Project Overview

- Train a classification model on personality-related behavioral data.
- Deploy the model as a web app and REST API.
- Provide a simple UI for users to enter features and receive a prediction.

## Live Demo

- Web app: https://web-production-8799e.up.railway.app/
- API endpoint: https://web-production-8799e.up.railway.app/predict

## Model Details

- Algorithm: Logistic Regression
- Test accuracy: 0.9172
- Input features:
  - Time_spent_Alone
  - Stage_fear
  - Social_event_attendance
  - Going_outside
  - Drained_after_socializing
  - Friends_circle_size
  - Post_frequency

## Project Files

- app.py: Flask application and prediction API
- templates/index.html: interactive web interface
- personality_prediction_notebook.ipynb: data preparation and model training notebook
- model.pkl: trained model
- model_meta.json: feature list, label mapping, and model metadata

## Run Locally

### 1. Create and activate a virtual environment

Windows PowerShell:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the app
```bash
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

## API Usage

### GET /
Returns health information and the expected input fields.

### POST /predict
Accepts a JSON payload with one record or a list of records.

Example request:
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

Example response:
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

## Deployment

This project is deployed on Railway.

For deployment, the app is started using:
```bash
gunicorn app:app
```
