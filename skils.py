import os, sys, webbrowser, requests, subprocess, pyttsx3, voice
import query

from words import *
from random import choice





alexa = pyttsx3.init() #инициализация голоса
voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Pavel"

# настройки синтеза речи
alexa.setProperty("rate", 180)
alexa.setProperty("volume", 1)
alexa.setProperty("voice", voice_id)

class Alexa():
    #
    def __init__(self, query):
        self.query = query
'''   def speaker(text):
        alexa.say(text)
        alexa.setProperty("voice",180)
        alexa.runAndWait()
    def browser(data):
        """Открывает браузер по умолчанию с url заданным здесь"""
        webbrowser.open('https://' + data, new=2)

    def youTube():
        """открывает ютуб"""
        webbrowser.open('https://www.youtube.com', new=2)

    def game():
        """Открывает любую программу если здесь указан путь exe к нужному файлу"""
        try:
            subprocess.Popen('D:\python\python project\game\venv.exe')
        except:
            speaker('Путь к файлу не найден, проверьте правильный ли он')


    def offBot():
        """Выключает бота"""
        sys.exit()
'''



class Talk(Alexa): # Класс для функции общения
    def answer(self):
        for func in commands:
            if func == self.query:
                alexa.say(choice(commands.get(func)))
                alexa.runAndWait()

                if self.query == 'exit':
                    alexa.stop()
                    quit()

