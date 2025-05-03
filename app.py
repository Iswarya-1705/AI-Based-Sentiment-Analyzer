from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = ""
    text = ""
    if request.method == 'POST':
        text = request.form['text']
        # Sentiment analysis
        blob = TextBlob(text)
        sentiment = "Positive" if blob.sentiment.polarity > 0 else "Negative" if blob.sentiment.polarity < 0 else "Neutral"
    
    return render_template('index.html', sentiment=sentiment, text=text)

if __name__ == "__main__":
    app.run(debug=True)
