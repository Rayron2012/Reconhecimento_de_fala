import speech_recognition as sr

rec =sr.Recognizer()

with sr.Microphone(device_index=2) as microfone:
    rec.adjust_for_ambient_noise((microfone))
    print("Pode começar a falar!!!!")
    audio = rec.listen(microfone)

#Salvar o audio

with open("audio.wav", "wb") as arquivo:
    arquivo.write(audio.get_wav_data())