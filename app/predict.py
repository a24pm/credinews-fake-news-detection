import joblib
import os

from source_scores import SOURCE_SCORES
from content_score import content_consistency

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "fake_news_model.pkl")

model = joblib.load(MODEL_PATH)
print("Model loaded successfully")


def credibility_score(confidence, source_score, content_score):
    score = (
        0.6 * confidence +
        0.25 * source_score * 100 +
        0.15 * content_score * 100
    )
    return round(float(score), 2)


def predict_news(text, source="unknown"):
    pred = model.predict([text])[0]
    prob = float(model.predict_proba([text])[0].max() * 100)

    source_score = SOURCE_SCORES.get(source.lower(), 0.4)
    content_score_val = content_consistency(text)

    credibility = credibility_score(prob, source_score, content_score_val)

    return {
        "prediction": "Fake" if pred == 1 else "Real",
        "model_confidence": round(prob, 2),
        "credibility_score": credibility
    }


if __name__ == "__main__":
    text = input("Enter news text: ")
    source = input("Enter source (bbc/cnn/blog/etc): ")
    print(predict_news(text, source))
