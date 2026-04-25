from data import get_next_stop, get_traffic, send_message

def handle_intent(text):
    if "next stop" in text:
        return get_next_stop()
    
    elif "traffic" in text:
        return get_traffic()
    
    elif "delay" in text:
        return send_message()
    
    else:
        return "Sorry, I didn’t understand."
