from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import requests

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    user_input = request.form.get('SpeechResult') or "Hello"
    
    # Replace this with your actual CrewAI endpoint URL
    ai_response = requests.post(
        "https://your-crewai-endpoint/api",
        json={"customer_input": user_input}
    ).text

    twiml = VoiceResponse()
    twiml.say(ai_response, voice='Polly.Joanna', language='en-US')
    return Response(str(twiml), mimetype="text/xml")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
