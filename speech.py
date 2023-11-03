import speech_recognition as sr
from pydub import AudioSegment
import json

import json
with open('data.json','r') as file_json:
    data = json.load(file_json)
    formato_entrada = data["formato_entrada"]
    formato_salida = data["formato_salida"]
    audio_entrada = data["audio_entrada"]
    audio_salida = data["audio_salida"]
    text_de_salida = data["text_de_salida"]    

if formato_entrada != formato_salida:
    sound = AudioSegment.from_file(audio_entrada, format=formato_entrada)
    file_handle = sound.export(audio_salida, format=formato_salida)
    filename = audio_salida
else:
    filename = audio_entrada
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source, open(text_de_salida,'w+') as file:
    # listen for the data (load audio to memory)
    audio = r.listen(source)
    text = r.recognize_google(audio,language="es-ES")
    file.write(text)