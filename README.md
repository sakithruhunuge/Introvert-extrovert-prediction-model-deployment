# Personality Predictor API

Predicts whether a person is an **Introvert** or **Extrovert** based on behavioural features.

## Endpoints

### `GET /` - Health check
Returns model info and expected input fields.

### `POST /predict` - Predict personality

**Request body (JSON):**
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
  "confidence": 0.9312,
  "probabilities": {
    "Extrovert": 0.0688,
    "Introvert": 0.9312
  }
}
```

## Deploy to Render (free)
1. Push this folder to a GitHub repo.
2. Go to https://render.com -> **New Web Service**.
3. Connect your repo, set **Start Command** to `gunicorn app:app`.
4. Deploy - your public URL is ready in ~2 minutes.
