from pygame import mixer

mixer.init()

mixer.music.load("song_path")
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("enter 'p' to pause and 'r' to resume")
    print("enter 'e' and 's' to exit the program")

    task = input("comand : ")

    if task == 'p':
        mixer.music.pause()
    elif task == 'r':
        mixer.music.unpause()
    elif task == 'e' or task == 's':
        mixer.music.stop()
        break
