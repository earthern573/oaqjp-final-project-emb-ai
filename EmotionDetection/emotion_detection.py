import requests
import json

def emotion_detector(text_to_analyze) :
    # Check if the input text is blank
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define the URL and headers
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Prepare input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the request to the API
    response = requests.post(URL, json=input_json, headers=Headers)

    # Check for blank or bad responses (status_code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Process the response if successful
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

    # Extract emotion scores
        anger_score = emotions.get("anger")
        disgust_score = emotions.get("disgust")
        fear_score = emotions.get("fear")
        joy_score = emotions.get("joy")
        sadness_score = emotions.get("sadness")

    # Determine the dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=lambda x: (emotion_scores[x] is not None, emotion_scores[x]), default=None)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        # Handle other unexpected status codes
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
