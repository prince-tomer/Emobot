def detect_emotion(message):
    msg = message.lower()
    if any(word in msg for word in ['sad', 'depressed', 'cry']):
        return 'sad'
    elif any(word in msg for word in ['anxious', 'nervous', 'panic']):
        return 'anxious'
    elif any(word in msg for word in ['happy', 'joy', 'excited']):
        return 'happy'
    else:
        return 'default'
