import wave
import datetime

from pydub import AudioSegment

from api import get_speech_file_from_text

mouth_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
              'ноября', 'декабря']

month_map = dict(zip(range(1, 13), mouth_list))


def add_to_output(filename, output):
    w = wave.open(filename, 'rb')
    output.writeframes(w.readframes(w.getnframes()))
    w.close()


def make_file():
    now = datetime.datetime.now()
    month = month_map[now.month]
    day = now.day
    current_date = '{}-ое {}'.format(day, month)

    get_speech_file_from_text(current_date)

    date = 'date.mp3'
    infiles = ['samples/{}.mp3'.format(name) for name in range(1, 10)]
    outfile = "<{}>.mp3".format(current_date)

    date = AudioSegment.from_mp3(date)

    output = AudioSegment.silent(duration=100)
    for infile in infiles:
        segment = AudioSegment.from_mp3(infile)
        output += segment
        output += date

    output.export(outfile)
    return outfile

make_file()
