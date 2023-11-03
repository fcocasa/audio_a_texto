import speech_recognition as sr
from pydub import AudioSegment
from deepmultilingualpunctuation import PunctuationModel
import json
import re

import json
with open('data.json','r') as file_json:
    data = json.load(file_json)
    formato_entrada = data["formato_entrada"]
    audio_entrada = data["audio_entrada"]
    text_de_salida = data["text_de_salida"]    

if formato_entrada != 'wav':
    sound = AudioSegment.from_file(audio_entrada, format=formato_entrada)
    filename = f'{audio_entrada[:-4]}.wav'
    file_handle = sound.export(filename, format='wav')
else:
    filename = audio_entrada

r = sr.Recognizer()

with sr.AudioFile(filename) as source, open(text_de_salida,'w+') as file:
    audio = r.listen(source)
    text = r.recognize_google(audio,language="es-ES")
    file.write(text)

model = PunctuationModel(model = "kredor/punctuate-all")
result = model.restore_punctuation(text)

with open(f'puntuado_{text_de_salida}','w+') as out:
    out.write(re.sub('\.','.\n',result))