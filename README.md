# Sentiment Classifier

A Flask web app that predicts text sentiment (positive or negative) using DistilBERT.

## Features
- Classifies text as “Positive (92%)” or “Negative (80%)”.
- Fancy UI: green for positive, red for negative.
- Responsive, accessible design.

## Installation
```bash
git clone https://github.com/ilyasxfl/Sentiment-Classifier.git
cd Sentiment-Classifier
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install flask transformers torch