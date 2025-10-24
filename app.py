from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    user_input = request.form.get('SpeechResult') or "Hello"
    user_input = user_input.lower()

    # Simple offline AI logic (no API key needed)
    if "book" in user_input or "appointment" in user_input:
        ai_response = "Sure, I can help you book an appointment. Can I know your preferred day and time?"
    elif "price" in user_input or "cost" in user_input:
        ai_response = "Our services start from fifty dollars. Would you like me to send you more details by email?"
    elif "hello" in user_input or "hi" in user_input:
        ai_response = "Hello there! Welcome to our company. How can I assist you today?"
    elif "thank" in user_input:
        ai_response = "You’re most welcome! Have a great day ahead."
    else:
        ai_response = "I’m sorry, could you please repeat that?"

    # Twilio voice reply
    twiml = VoiceResponse()
    twiml.say(ai_response, voice='Polly.Joanna', language='en-US')
    return Response(str(twiml), mimetype="text/xml")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
