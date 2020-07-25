# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import pyautogui as pg
import pyperclip as pc
import time
import os


def juntarrangos(lista, a, b):
    for u in range(a, b + 1):
        lista.append(u)


def juntarseparados(lista, a):
    for u in a:
        lista.append(u)


diractual = os.getcwd()

usuarioUP = "jm.huamanpi"
contraseñaUP = "831134DD"
cursoreanudar = " Ingeniería de Datos-B"
videosreanudar = list()
# juntarseparados(videosreanudar, [0])  # Acá videos separados a reanudar
juntarrangos(videosreanudar, 1 - 1, 30 - 1)  # Acá la cadena de videos a reanudar
respera = 40  # Este es el ratio de espera, dice qué tanto tardará en descargar el siguiente video
# Si su valor es más alto, se demorará menos en descargar el siguiente
# Ajustar este ratio a su velocidad de internet de descarga
# 55 está bien para ~4MB/s

# Entrar a powercampus
browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver83.exe")  # Acá puse el driver
# browser.get("https://autoservicio2.up.edu.pe/ss/Home.aspx")
# barra_user = browser.find_element_by_id("ctl00_ucUserLogin_lvLoginUser_ucLoginUser_lcLoginUser_UserName")
# barra_password = browser.find_element_by_id("ctl00_ucUserLogin_lvLoginUser_ucLoginUser_lcLoginUser_Password")
# barra_user.send_keys(usuarioUP)  # Acá poner su usuario UP
# barra_password.send_keys(contraseñaUP)  # Acá la contraseña
# barra_password.send_keys(Keys.ENTER)
# time.sleep(2)
# pg.hotkey('ctrl', 'shift', 'i')
# time.sleep(0.2)
# pg.hotkey('winleft', 'left')
# time.sleep(0.2)
# pg.press('esc')

os.chdir("%s" % diractual + "\\Marcos2")
marco1 = pd.read_csv("%s" % cursoreanudar + ".csv")
link = marco1['Link']
curso = marco1['Curso']
seccion = marco1['Sección']
fecha = marco1['Fecha']
nombreseccion = marco1['Nombre de la sesión']
duracion = marco1['Duración']
link2 = marco1['Link2']
os.chdir("%s" % diractual)

# Descargar con nombre
for i in videosreanudar:
    try:
        browser.get(marco1['Link2'].loc[i])  # Entra al enlace
    except:
        pg.hotkey('ctrl', 'r')  # Esto por si la página no carga
        browser.get(marco1['Link2'].loc[i])
        print('El controlador se refrescó porque no cargaba')
    if i == videosreanudar[0]:
        time.sleep(3)
        pg.hotkey('winleft', 'left')
        time.sleep(0.4)
        pg.press('enter')
        time.sleep(2)
    pg.hotkey('ctrl', 's')  # Guardar como
    time.sleep(10)
    # Esto siguiente lo pongo para descargarlo a mi disco duro externo
    if i == videosreanudar[0]:
        for j in range(3):
            time.sleep(0.5)
            pg.hotkey('shift', 'tab')
        for j in range(45):
            pg.press('down')
        time.sleep(1)
        pg.press('up')
        time.sleep(1)
        pg.press('enter')
        for j in range(2):
            time.sleep(0.3)
            pg.press('tab')
        time.sleep(3)
    pg.typewrite(marco1['Curso'].loc[i] + '_'
                 + marco1['Sección'].loc[i] + '_'
                 + "(%s de " % (i + 1) + "%s)" % (len(marco1['Link2'])) + '.mp4')  # Se guardará con el nombre 'Curso_Seccion_Nombresesion_.mp4'
    pg.press('enter')
    print("video descargándose %s" % (i + 1) + "/%s " % (len(marco1['Link2'])) + ("(%s%%)") % (round((i + 1) * 100 / (len(marco1['Link2'])), 2)))
    y = marco1['Duración'].loc[i]
    espera = int(y[0]) * 3600 + int(y[2:3]) * 60 + int(y[-2:-1])  # El tiempo de espera entre descargas dependerá de lo largo del video
    print("Este video dura %s " % marco1['Duración'].loc[i])
    print("El próximo video se descargará en %s" % round((espera / respera), 1) + " segundos")
    if i == 0:
        for j in range(2):
            time.sleep(0.7)
            pg.press('tab')
    time.sleep(2)
    pg.press('space')  # Pausar el video
    time.sleep(espera / respera)  # Descargará aproximadamente cuando termine el anterior
# time.sleep(150)  # Espera 5 minutos hasta descargar el siguiente curso
# browser.quit()
