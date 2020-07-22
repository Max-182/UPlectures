import pyautogui as pg
import pyperclip as pc
import time as t


def continuarsiseencuentra(imagen):
    r4 = None
    while r4 is None:
        t.sleep(1.5)
        r4 = pg.locateCenterOnScreen(imagen)
        if r4 == None:
            print("Todavía no se encuentra su imagen %s" % imagen)
        else:
            continue


vinculos = []

# Subida del primer video
pg.hotkey('winleft', 't')
t.sleep(1.5)
for i in range(22):
    t.sleep(0.05)
    pg.press('right')
pg.press('enter')
t.sleep(6)
pg.hotkey('winleft', 'left')
t.sleep(0.2)
pg.press('esc')
t.sleep(0.5)
pg.hotkey('ctrl', 'l')
t.sleep(1)
pg.typewrite("https://studio.youtube.com/channel/UCHEs-R_W5qa3ukCuYwvRmxw")
t.sleep(1)
pg.press('enter')

len = 3
for j in range(len):
    pg.hotkey('ctrl', 'l')
    continuarsiseencuentra('crear.png')
    for i in range(4):
        t.sleep(0.2)
        pg.press('tab')
    t.sleep(2)
    pg.press('enter')
    t.sleep(1)
    pg.press('enter')
    t.sleep(1)
    for i in range(3):
        t.sleep(0.05)
        pg.press('tab')
    pg.press('enter')
    t.sleep(5)
    for i in range(3):
        pg.hotkey('shift', 'tab')
    for i in range(30):
        pg.press('up')
    for i in range(2):
        pg.press('down')
    pg.press('enter')
    pg.press('tab')
    pg.press('down')
    pg.press('up')
    if j > 0:
        pg.hotkey('shift', 'del')
        t.sleep(2)
        pg.press('enter')
        t.sleep(0.5)
        pg.press('down')
        pg.press('up')
    # for i in range(j):
    #     pg.press('down')
    pg.press('enter')
    t.sleep(1)

    # Configuración

    continuarsiseencuentra('crear2.png')
    for i in range(11):
        t.sleep(0.15)
        pg.press('tab')
    t.sleep(1)
    pg.press('down')
    t.sleep(1)
    pg.press('enter')
    for i in range(12):
        t.sleep(0.3)
        pg.hotkey('shift', 'tab')
    t.sleep(1)
    pg.press('enter')
    t.sleep(1)
    for i in range(3):
        t.sleep(0.3)
        pg.hotkey('shift', 'tab')
    t.sleep(1)
    pg.press('tab')
    t.sleep(1)
    pg.press('enter')
    for i in range(6):
        t.sleep(0.3)
        pg.press('tab')
    # Acá está el vínculo del video
    t.sleep(1)
    pg.press('enter')
    # t.sleep(1)
    # pg.hotkey('ctrl', 'l')
    # t.sleep(1)
    # pg.hotkey('ctrl', 'c')
    vinculos.append(pc.paste())
    t.sleep(1)
    # pg.hotkey('ctrl', 'w')
    for i in range(2):
        t.sleep(0.5)
        pg.press('tab')
    t.sleep(1)
    pg.press('enter')
    t.sleep(7)
    pg.press('tab')
    t.sleep(1)
    pg.press('enter')  # Ya se estaría subiendo el video
    t.sleep(2)
vinculos
