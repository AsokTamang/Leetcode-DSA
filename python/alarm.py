import datetime
import time
import pygame
def alarm(alarm_time):
    print(f'Alarm is set for {alarm_time}.')
    sound='Music.mp3'
    is_running=True
    while is_running:
        current_time=datetime.datetime.now().strftime('%H:%M:%S')
        print(f'The current time is:{current_time}')
        time.sleep(1)
        if current_time == alarm_time:
            print('WAKE UP')
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            is_running=False
if __name__=="__main__":
    alarm_time=input('Enter a time(%H:%M:%S):')
    alarm(alarm_time)