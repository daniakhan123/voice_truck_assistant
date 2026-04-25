from voice_input import listen
from intent_handler import handle_intent
from voice_output import speak

while True:
    user_text = listen()
    
    if user_text:
        response = handle_intent(user_text)
        print("Assistant:", response)
        speak(response)
