from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load DistilBERT
print("Loading DistilBERT model...")
classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
print("Model loaded successfully!")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    text = data.get('text', '')

    # Validation
    if not isinstance(text, str) or not text.strip():
        return jsonify({'error': 'Text must be a non-empty string'}), 400

    # Classify
    result = classifier(text)[0]
    label = result['label']  # POSITIVE or NEGATIVE
    score = result['score']  # Confidence (0-1)

    # Format
    sentiment = label.capitalize()
    confidence = round(score * 100, 2)
    reply = f"{sentiment} ({confidence}% confidence)"

    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run(debug=True)
