from elevenlabs import generate, play, set_api_key

set_api_key("YOUR_API_KEY")

def speak(text):
    audio = generate(
        text=text,
        voice="Rachel"
    )
    play(audio)
