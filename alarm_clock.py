#ALARM CLOCK
import time
import datetime
import pygame
def set_alarm():
    sound='ayooo-sayip-op.mp3'
    is_True=True
    while is_True:
        crt_time=datetime.datetime.now().strftime('%H:%M:%S')
        print(f'current time is {crt_time}')
        if crt_time==alarm:
            print('Wake UP !!! alarm is ringing')
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_True=False

if __name__=='__main__':
    alarm=input('enter the time for alarm:(HH:MM:SS)')
    print(f'alarm is set for{alarm}')
    set_alarm()