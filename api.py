import requests

from config import YANDEX_CLOUD_API_KEY


def get_speech_file_from_text(text):
    url = 'https://tts.voicetech.yandex.net/generate'
    params = {
        'text': text,
        'format': 'mp3',
        'lang': 'ru‑RU',
        'speaker': 'zahar',
        'key': YANDEX_CLOUD_API_KEY,
    }
    response = requests.get(url, params)
    with open('date.mp3', 'wb') as f:
        for chunk in response:
            f.write(chunk)
