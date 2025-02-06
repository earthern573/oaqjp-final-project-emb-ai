import requests
import json
def emotion_detector(text_to_analyze) :
    # Define the URL and headers
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Prepare input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Send the request to the API
    response = requests.post(URL, json=input_json, headers=Headers)
    # Process the response
    if response.status_code == 200:
        # Convert the response to a dictionary
        formatted_response = json.loads(response.text)
        # Extract emotion scores from the response
        emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})
        # Safely extract each emotion score
        anger = emotions.get("anger")
        disgust = emotions.get("disgust")
        fear = emotions.get("fear")
        joy = emotions.get("joy")
        sadness = emotions.get("sadness")
        # Determine the dominant emotion
        emotion_scores = [anger, disgust, fear, joy, sadness]
        dominant_emotion = max(emotion_scores, key=lambda x: (x is not None, x), default=None)
    else:
        # Return default values if the response code is not 200
        anger = disgust = fear = joy = sadness = None
        dominant_emotion = None
    # Return the result in the required format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }