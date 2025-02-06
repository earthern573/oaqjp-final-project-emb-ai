"""
server.py

This file contains the Flask application for emotion detection.
It provides an endpoint to analyze the sentiment of the given text 
and returns the dominant emotion along with its respective scores.

The application uses the emotion detection function from the EmotionDetection package.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route with the decorator as specified
@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Detects the dominant emotion from the provided text input.

    The function processes the input text, calls the emotion detector function,
    and returns the dominant emotion or an error message for invalid input.

    Returns:
        jsonify: A JSON response containing the dominant emotion or an error message.
    """
    # Get the text from the request
    data = request.get_json()
    text_to_analyze = data.get('text', "")

    # Check if text is provided
    if not text_to_analyze:
        return jsonify({"response": "No text provided. Please send a valid text."})

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (invalid or blank input)
    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again!"})

    # Prepare the output message as per requirements
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the formatted message
    return jsonify({"response": response_message})


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
