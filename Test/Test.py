import cv2
import pyautogui as pg
import time
import keyboard
import threading
import sys

p =0
def on_key_press():
    global p
    p=1

pg.FAILSAFE = False
keyboard.add_hotkey('p', on_key_press) 
keyboard_thread = threading.Thread(target=keyboard.wait)
keyboard_thread.start()

color_coords = {'black': '1095 94', 'grey': '1128 91', 'dRed': '1159 86', 'red': '1200 88', 'orange': '1232 92',
                'yellow': '1257 90', 'green': '1288 85', 'blue': '1328 89', 'dblue': '1367 87', 'purple': '1390 87',
                'lgrey': '1127 121', 'brown': '1161 120', 'pink': '1192 124', 'gold': '1232 120', 'lyellow': '1257 120',
                'lime': '1288 120', 'lblue': '1328 120', 'blue-grey': '1367 120', 'lavender': '1390 120', 'white': '1095 121'}
colours = {'black': (0, 0, 0), 'grey': (127, 127, 127), 'dRed': (128, 0, 0), 'red': (255, 0, 0), 'orange': (255, 128, 0),
           'yellow': (255, 255, 0), 'green': (34, 177, 76), 'blue': (0, 162, 232), 'dblue': (63, 72, 204), 'purple': (128, 0, 128),
           'lgrey': (192, 192, 192), 'brown': (185, 122, 87), 'pink': (255, 174, 201), 'gold': (255, 201, 14),
           'lyellow': (239, 228, 176), 'lime': (181, 230, 29), 'lblue': (153, 217, 234), 'blue-grey': (112, 146, 190),
           'lavender': (200, 191, 231), 'white': (255, 255, 255)}
if len(sys.argv >1):
    file_path = sys.argv[1]
originalImage = cv2.imread(file_path)
x_start = 400
y_start = 350
time.sleep(3)
current_colour = None

def draw():
    global current_colour
    for y in range(len(originalImage)):
        for x in range(len(originalImage[0])):
            pixel_color = tuple(originalImage[y][x])
            closest_color = min(colours, key=lambda c: sum(abs(a-b) for a,b in zip(colours[c], pixel_color)))
            if p ==0:
                if (closest_color!= current_colour or current_colour is None):
                    pg.click(*map(int, color_coords[closest_color].split()))
                    pg.click(*map(int, color_coords[closest_color].split()))
                    current_colour = closest_color
                pg.click(x_start + x, y_start + y, _pause=False)

pg.press('win')
time.sleep(2)
pg.click(343,1061)
time.sleep(3)
pg.write('paint', interval = 0.1)
time.sleep(5)
pg.click(248, 242)
time.sleep(5)
screenWidth, screenHeight = pg.size()
currentMouseX, currentMouseY = pg.position()
print('X: ' +str(currentMouseX) + 'Y: ' + str(currentMouseY))

pg.moveTo(x_start, y_start)

draw()

