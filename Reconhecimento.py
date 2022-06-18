import speech_recognition as sr

 # Criar um "reconhecedor"
rec = sr.Recognizer()

 # Ouvir o audio do microfone
# Para saber os Microfones do seu PC
#print(sr.Microphone().list_microphone_names())

with sr.Microphone(device_index=2) as microfone:
     rec.adjust_for_ambient_noise(microfone)
     print("Pode começar a falar!!!")

     # Auemnta o tempo para reconhecimento de fim de conversa
     # rec.pause_threshold = 1 --- aumeta o tempo de pausa para finalizar de reconhecer a frase

     audio = rec.listen(microfone)

     try:
          # Reconhecer audio e traduzir para texto
          texto = rec.recognize_google(audio, language='pt-BR')
          print(texto)
     except:
          print("Fale de forma mais clara! ")




