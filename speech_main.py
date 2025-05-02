import speech_recognition as sr
import pyttsx3

"""def trial():
    mic  = sr.Microphone()
    pickup = sr.Recognizer()

    with mic as audio_file:
        print("Please Talk")
        pickup.adjust_for_ambient_noise(audio_file)
        audio = pickup.listen(audio_file)
        print("Voice to text conversion...")
        print(f"You said: {pickup.recognize_google(audio, language = "en-US")}")"""

def speech_en():
    mic  = sr.Microphone()
    pickup = sr.Recognizer()

    with mic as audio_file:
        pickup.adjust_for_ambient_noise(audio_file)
        audio = pickup.listen(audio_file)
        return pickup.recognize_google(audio, language = "en-US")
    
def speech_es():
    mic  = sr.Microphone()
    pickup = sr.Recognizer()

    with mic as audio_file:
        pickup.adjust_for_ambient_noise(audio_file)
        audio = pickup.listen(audio_file)
        return pickup.recognize_google(audio, language = "es-ES")
    

def speech_probe():
    mic = sr.Microphone()
    pickup = sr.Recognizer()

    with mic as audio_file:
        print("Ajustando al ruido ambiental... espera un momento.")
        pickup.adjust_for_ambient_noise(audio_file)
        print("Listo. Habla ahora:")
        audio = pickup.listen(audio_file)

        try:
            texto = pickup.recognize_google(audio, language="es-ES")
            print("Transcripción:", texto)
            return texto
        except sr.UnknownValueError:
            print("No se entendió el audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de reconocimiento: {e}")
            return ""
    
def text_transcript(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150) # Speed of speech
    engine.setProperty("volume", 0.9) # Volume level (0.0 to 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[3].id) # Set the voice to the first one in the list

    engine.say(text)

    engine.runAndWait()

    