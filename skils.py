import os, sys, webbrowser, requests, subprocess, pyttsx3, voice, time
from main import main


engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speaker(text):
    engine.say(text)
    engine.setProperty("voice",180)
    engine.runAndWait()
def browser(data):
    """Открывает браузер по умолчанию с url заданным здесь"""
    webbrowser.open('https://' + data, new=2)

def youTube():
    """открывает ютуб"""
    webbrowser.open('https://www.youtube.com', new=2)

def windy():
    webbrowser.open('https://www.windy.com/ru/-%D0%94%D0%BE%D0%B6%D0%B4%D1%8C-%D0%B3%D1%80%D0%BE%D0%B7%D0%B0-rain?rain,'
                    '44.020,43.077,10', new=2)
def game():
    """Открывает любую программу если здесь указан путь exe к нужному файлу"""
    try:
        subprocess.Popen('D:\python\python project\game\venv.exe')
    except:
        speaker('Путь к файлу не найден, проверьте правильный ли он')

def offpc():
    """Откулючает PC"""
    os.system('shutdown \s')
    print('Пк выключен')

def weather():
    """Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое"""
    print('weather')

def offBot():
    """Выключает бота"""
    sys.exit()

def timer():
    """ставит таймер"""

def passive():
    """Функция заглушки при простом диалоге с ботом"""
    print(passive)