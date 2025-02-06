from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)
# Route with the decorator as specified
@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    # Get the text from the request
    data = request.get_json()
    text_to_analyze = data.get("text", "")
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    # Use the emotion_detector function
    emotions = emotion_detector(text_to_analyze)
    # Format the response as requested
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    # Return the formatted message
    return jsonify({"response": response_message})
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)