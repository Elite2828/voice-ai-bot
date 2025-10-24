from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import requests
import os

app = Flask(__name__)

# URL of your CrewAI backend
CREWAI_BACKEND_URL = "https://your-crewai-backend-url.com/api/chat"  # ⬅️ Replace this with your CrewAI API endpoint

@app.route("/voice", methods=["POST"])
def voice():
    """Handle incoming call and send to CrewAI"""
    user_speech = request.form.get("SpeechResult", "Hello")
    
    # Send caller speech to CrewAI backend
    try:
        payload = {"message": user_speech}
        response = requests.post(CREWAI_BACKEND_URL, json=payload)
        response_text = response.json().get("response", "I'm sorry, I didn't get that.")
    except Exception as e:
        response_text = f"Error connecting to CrewAI: {e}"
    
    # Build Twilio voice response
    twilio_resp = VoiceResponse()
    twilio_resp.say(response_text, voice="Polly.Joanna")  # AWS Polly voices supported by Twilio

    return Response(str(twilio_resp), mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
