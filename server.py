from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)
# Route with the decorator as specified
@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    # Get the text from the request
    data = request.get_json()
    text_to_analyze = data.get("text", "")
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    # Check if dominant_emotion is None (invalid or blank input)
    if result['dominant_emotion'] is None:
        response_message = "Invalid text! Please try again!"
    else:
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
    app.run(host="127.0.0.1", port=5000)