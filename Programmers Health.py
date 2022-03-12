'''
def Func_name():
    """It reminds the user to do whatever he wants"""


    time.sleep(10)
    mixer.init()
    mixer.music.load('name to the sond u want to set.mp3')
    mixer.music.play(loops=-1)
    a = input('eg if u set this for water then- did u drank water yes- drank if no- not drank \n')
    if a == 'drank':
        mixer.music.stop()
        with open('water_log.txt', 'a') as file:
            file.write(f'you drank water at, {get_time()}\n')
    if a == 'not drank':
        mixer.music.stop()
        with open('water_log.txt', 'a') as file:
            file.write(f'you did not drank water at, {get_time()}\n')
'''




from pygame import mixer
import datetime
import time



def get_time():
    return datetime.datetime.now()




def water_reminder():
    """It reminds the user to drink water every 27 min"""


    time.sleep(10)
    mixer.init()
    mixer.music.load('Drink.mp3')
    mixer.music.play(loops=-1)
    a = input('did u drank water yes- drank if no- not drank \n')
    if a == 'drank':
        mixer.music.stop()
        with open('water_log.txt', 'a') as file:
            file.write(f'you drank water at, {get_time()}\n')
    if a == 'not drank':
        mixer.music.stop()
        with open('water_log.txt', 'a') as file:
            file.write(f'you did not drank water at, {get_time()}\n')



def eyes_exercise():
    """It reminds the user to do eyes exercise every 30 min"""


    time.sleep(5)
    mixer.init()
    mixer.music.load('Creative Exercise.mp3')
    mixer.music.play(loops=-1)
    a = input('did u did the eyes exercise if yes- done if no- not done \n')
    if a == 'done':
        mixer.music.stop()
        with open('eyes_exercise_log.txt', 'a') as file:
            file.write(f'you did eyes exercise at, {get_time()}\n')
    if a == 'not done':
        mixer.music.stop()
        with open('eyes_exercise_log.txt', 'a') as file:
           file.write(f'you did not did eyes exercise at, {get_time()}\n')


def physical_exercise():
    """It reminds the user to do physical exercise every 45 min"""


    time.sleep(10)
    mixer.init()
    mixer.music.load('Run fast music.mp3')
    mixer.music.play(loops=-1)
    a = input('did u did the physical exercise if yes- done if no- not done \n')
    if a == 'done':
        mixer.music.stop()
        with open('physical_exercise_log.txt', 'a') as file:
            file.write(f'you did physical exercise at, {get_time()}\n')
    elif a == 'not done':
        mixer.music.stop()
        with open('physical_exercise_log.txt', 'a') as file:
            file.write(f'you did physical did exercise at, {get_time()}\n')
