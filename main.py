import pygame
import serial
from pyvidplayer2 import Video

# English project specifics:

body_paragraphs = ["tradition","community","purpose"]

# TODO: FILL WITH UIDS
uids = {

}
cur_paragraph = 0


# paths to vid files
vid_paths = []
vids = []
for path in vid_paths: 
    vids.append(Video(path))
    vids[-1].set_size((1600,900))


# Serial inits
BAUDRATE = 115200
PORT = "COM5"
TIMEOUT = 1
ser = serial.Serial(baudrate=BAUDRATE,port=PORT,timeout=TIMEOUT)


# Pygame inits
screen = pygame.display.set_mode((1600,900))
running = True
clock = pygame.time.Clock()
FPS = 120
font = pygame.font.Font(None,size = 40) # default font, size 40

# functions

# call if the video has stopped and you need to play it again. Note you still need to call displayVideoFrame afterwards
def restart_video(video:Video):
    video.play() 

# Given the video file (including the file extension), displays the next frame of the video. 
def displayVideoFrame(video:Video, surface:pygame.Surface):
    video.draw(surface,(0,0))
    if video.frame >= video.frame_count:
        video.stop()
        video.restart()

def displayQuote(uid:str):
    # code ehre
    "aaa"

# Game loop
while running:
    # Iterator / tick updates
    clock.tick(FPS)


    # Input handling (including serial)
    if ser.in_waiting > 0:
        line = ser.readline().strip().decode('utf-8').split() # reads line up to newlines, strips all stuff, decodes
    
    match line[0]:
        case "uid:":
            
        case "next":
            cur_paragraph += 1
            cur_paragraph %= 3
        case "calibrate":
            cur_paragraph = 0

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # End of input handling

    # Essential display updates
    pygame.display.flip()
    


ser.close()





