import vosk
import sounddevice as sd
import queue
import json
import  words
import skils
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


q = queue.Queue()
model = vosk.Model('vosk-model-small')

device = sd.default.device = 0, 4
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
print(samplerate)

def callback(indata, frames, time, status):
    """при достижение лими в blocksize создается очередь и конвертируется все в байты
    хранится все в indata
    чем меньше значение в blocksize тем быстрее будет обрабатываться запрос"""
    q.put(bytes(indata))


def recognize(data, vectorizer, clf, speaker=None):
    """обрабатывает запросы, проверяет свое имя
    Дата отвечает за чтение записи с микрофона"""
    trg = words.name.intersection(data.split())
    if not trg:
        return

    data.replace(list(trg)[0],'')
    text_vector = vectorizer.transform([data]). toarray()[0]
    answer = clf.predict([text_vector])[0]
    func_name = answer.split()[0]
    speaker(answer.replace(func_name, ''))
    exec(func_name + '()')

def main():
    """получаем ключи враз из словаря для машиного обучения
    конвертирует это все в список и передает в модуль"""
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.commands.keys()))
    clf = LogisticRegression()
    clf.fit(vectors, list(words.commands.values()))

    del words.commands


    with sd.RawInputStream(samplerate=samplerate, blocksize= 2000, device=device[0], dtype= 'int16',
                           channels= 1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)

if __name__ == '__main__':
    main()