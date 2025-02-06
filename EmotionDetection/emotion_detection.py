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
        anger_score = emotions.get("anger")
        disgust_score = emotions.get("disgust")
        fear_score = emotions.get("fear")
        joy_score = emotions.get("joy")
        sadness_score = emotions.get("sadness")
        # Create a dictionary mapping emotions to their scores
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        # Determine the dominant emotion by finding the key with the highest score
        dominant_emotion = max(
            (emotion for emotion in emotion_scores if emotion_scores[emotion] is not None),
            key=lambda emotion: emotion_scores[emotion],
            default=None
        )
    else:
        # Return default values if the response code is not 200
        anger_score = disgust_score = fear_score = joy_score = sadness_score = None
        dominant_emotion = None
    # Return the result in the required format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }