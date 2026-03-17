""" Flask app for emotion detection using NLP model. """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def sent_detector():
    """Analyze text and return detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)
    anger = resp['anger']
    disgust = resp['disgust']
    fear = resp['fear']
    joy = resp['joy']
    sadness = resp['sadness']
    dominant_emotion = resp['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return ("For the given statement, the system response is "
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
    f"'joy': {joy}, and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}")


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    