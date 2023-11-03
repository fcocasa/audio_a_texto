## Que instalar:

 - pip3 install SpeechRecognition

 - sudo apt install ffmpeg

 - pip3 install pydub

## Ejecutar

### Cambiar datos de data.json

Por defecto estan estos valores:
{
    "formato_entrada":"m4a",
    "audio_entrada":"videoplayback.m4a",
    "text_de_salida":"transcription.txt"
}

La salida generar 3 salidas:

- conversion del audio (si ya es .wav no cambia)
- transcription.txt
- puntuado_transcription.txt

transcription.txt -> es la transcripcion directa
puntuado_transcription.txt -> a la transcripcion se le agrega puntuacion mediante un modelo de de NLP

### Comando

python speech.py


### Recomendacion

Crear un ambiente virtual

python3 -m venv /path/to/new/virtual/environment

Sustituir venv por cualquier otro nombre
