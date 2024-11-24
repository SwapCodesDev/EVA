from SpeechRecognition import speak, listen, initialize_tts_engine, sr
from IntentResolver import intent_resolve
from FileManager import update_json_key

path_eva = 'files/eva.json'     # File path for eva.json

def EVA():
    # Update status
    update_json_key(path_eva, 'status', 'idle')

    # Initialize recognizer, microphone, and TTS engine
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = initialize_tts_engine(gender='default')

    try:
        while True:
            # Update status to 'listening'
            update_json_key(path_eva, 'status', 'listening')
            text = listen(recognizer, microphone)

            if not text:
                continue
            
            update_json_key(path_eva, 'query', text)
            
            # Update status to 'processing'
            update_json_key(path_eva, 'status', 'processing')

            response = intent_resolve(text)     # Get response

            if not response:
                continue

            print(f"response: {response}")
            update_json_key(path_eva, 'response', response)
            
            # Update status to 'speaking'
            update_json_key(path_eva, 'status', 'speaking')

            speak(engine, response)     # Speak response
            
            # Update status back to 'idle'
            update_json_key(path_eva, 'status', 'idle')

    except KeyboardInterrupt:
        update_json_key(path_eva, 'status', 'terminated')
        print("Program terminated.")
