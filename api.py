import requests

from app import app
from config import YANDEX_CLOUD_API_KEY


def get_speech_file_from_text(text):
    url = 'https://tts.voicetech.yandex.net/generate'
    params = {
        'text': text,
        'format': 'wav',
        'lang': 'ru‑RU',
        'speaker': 'zahar',
        'key': YANDEX_CLOUD_API_KEY,
    }
    response = requests.get(url, params)
    with open(app.root_path + '/date.wav', 'wb') as f:
        for chunk in response:
            f.write(chunk)

    return
