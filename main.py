import pygame
import serial
import serial.tools.list_ports as listPorts
from pyvidplayer2 import Video

# English project specifics:

class Quotes:
    quotes = {
    "purpose":{
        "cactus":"“The next morning, Kenny rose before the baby woke and put his things together. \nHe tiptoed into her room and kissed her on the forehead, closed her door quietly \nand walked out into the early morning mist” (216)",
        "well": "\"Rose was right. This was about those people standing helpless before the law, \noften for just trying to get by in a world they’d been abandoned to, entirely unprepared.\" (223)\n\n" + "“Mr. Brocket, you are fortunate to have drawn this young woman. \nI will see you again this afternoon” (182)",
        "oasis":"“Fuck you, Harlan I quit.” (97)"

    },
    "tradition":{
        "shipwreck":"“Clara had no more tears. \nShe’d left them in the lodge and faced the world once again with an open heart.” (203)",
        "turtle":"“I could hitch north and maybe I could find some odd jobs, \nenough to buy me a horse and tack, and a few supplies. \nI didn't need more than that.” (181)",
        "coral":"The loss of Kenny and his mother's fish smoking tradition"       
    },
    "community":{
        "log":"““Maisie, you were always the strong one. You always found a way to make us laugh.” \n“Yeah, and who takes care of me?”” (75)",
        "chainsaw":"“I don’t hold it against you, Jimmy, but you gotta realize. \nShit happened there. Shit you don't even wanna know about. You weren't there. \nSo why do you have to pretend you might know something about it.” (69)",
        "oak":"“Remember this is a place of healing. \nI am your family now and this place is yours forever. \nWhen things get tough remember the medicine and never forget you will always have your angels.” (203)",
        "campfire":"““I just don’t know what to do.” Bella squeezed Kenny’s hand. \n“It’s like most of me is gone and I can’t get it back.” “(25)"
    }
    }

uids = ["49","59","34","2a","1c","16","35","1b","2b","3b"]
body_paragraphs = ["tradition","community","purpose"]
quotes = []

for para in body_paragraphs:
    pg_quotes = Quotes.quotes[para]
    for quote in pg_quotes:
        quotes.append(quote)
# TODO: FILL WITH UIDS
cur_paragraph = 0


# paths to vid files
vid_paths = []
vids = []
for path in vid_paths: 
    vids.append(Video(path))
    vids[-1].set_size((1600,900))


# Serial inits
print("File, version, and comports, in that order: ")
print(serial.__file__)
print(serial.VERSION)
for p in listPorts.comports():
    print(p.device)
BAUDRATE = 115200
PORT = "COM5"
TIMEOUT = 1
ser = serial.Serial(baudrate=BAUDRATE,port=PORT,timeout=TIMEOUT)


# Pygame inits
screen = pygame.display.set_mode((1600,900))
running = True
clock = pygame.time.Clock()
FPS = 120

class Fonts:
    default = pygame.font.Font(None,50)


class Colours:
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    black = (0,0,0)


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

def displayQuote(text:str,font=Fonts.default,colour=Colours.black):
    """
    Draws multiline text centered both horizontally and vertically.
    Newlines must be explicit ('\\n').
    """
    lines = text.split("\n")
    line_surfaces = [font.render(line, True, colour) for line in lines]

    total_height = sum(surface.get_height() for surface in line_surfaces)
    screen_rect = screen.get_rect()
    y_offset = screen_rect.centery - total_height // 2

    for surface in line_surfaces:
        x = screen_rect.centerx - surface.get_width() // 2
        screen.blit(surface, (x, y_offset))
        y_offset += surface.get_height()

# Game loop
while running:
    # Iterator / tick updates
    clock.tick(FPS)


    # Input handling (including serial)
    if ser.in_waiting > 0:
        line = ser.readline().strip().decode('utf-8').split() # reads line up to newlines, strips all stuff, decodes
    
    match line[0]:
        case "uid:":
            # TODO: add code
            uid = line[1][2:4:1] ## Isolating the unique part ofthe UIDs
            displayQuote(quotes[uids.index(uid)])
            
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





