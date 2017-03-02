import wave
import datetime

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

    date = 'date.wav'
    infiles = ['samples/{}.wav'.format(name) for name in range(1, 10)]
    outfile_wav = "<{}>.wav".format(current_date)

    output = wave.open(outfile_wav, 'wb')

    with wave.open(date, 'rb') as w:
        output.setparams(w.getparams())

    for infile in infiles:
        add_to_output(infile, output)
        add_to_output(date, output)

    output.close()
    return outfile_wav

make_file()
