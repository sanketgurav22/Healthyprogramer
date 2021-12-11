from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load()
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("my log.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eye = time()
    init_exercise = time()
    watersecs = 5
    eyesecs = 10
    exsecs = 15

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Enter 'drank' to stop the alarm.")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("Drank water at")

        if time() - init_eye > eyesecs:
            print("Eyes Exercise Time. Enter 'doneeyes' to stop the alarm.")
            musiconloop("eye.mp3", "doneeyes")
            init_eye = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop("physical.mp3", "donephy")
            init_exercise = time()
            log_now("Physical Activity done at")
