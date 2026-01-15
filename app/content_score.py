CLICKBAIT_WORDS = [
    "shocking", "breaking", "unbelievable", "you won't believe",
    "must read", "exposed"
]


def content_consistency(text):
    score = 1.0

    if text.count("!") > 3:
        score -= 0.2

    uppercase_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
    if uppercase_ratio > 0.3:
        score -= 0.2

    for word in CLICKBAIT_WORDS:
        if word in text.lower():
            score -= 0.15

    return max(score, 0.1)
