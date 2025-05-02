import speech_main as sm

texto = sm.speech_probe()

if texto:
    sm.text_transcript(texto)
else:
    sm.text_transcript("No se entendió el audio.")
#     engine.runAndWait()