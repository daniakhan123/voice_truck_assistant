from elevenlabs import generate, play, set_api_key

set_api_key("sk_2cf01b1942751f34ee1bf0c1ff16c8a1f50dcbbf31ad53db")

def speak(text):
    audio = generate(
        text=text,
        voice="Rachel"
    )
    play(audio)
