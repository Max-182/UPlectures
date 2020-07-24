# Importar módulos
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import pyautogui as pg
import pyperclip as pc
import time
import os

usuarioUP = "jm.huamanpi"
contraseñaUP = "831134DD"
cursoUP = [" Microeconomía II-B", " Microeconomía II-A"]
# cursoUP = [" Economía General I-A", " Economía General II-A", " Economía Pública-A", " Economía y Derecho-A"]
respera = 55  # Este es el ratio de espera, dice qué tanto tardará en descargar el siguiente video
# Si su valor es más alto, se demorará menos en descargar el siguiente
# Ajustar este ratio a su velocidad de internet de descarga
# 55 está bien para ~4MB/s
network = "Network.png"  # Acá poner "Networkc.png" si su Chrome está en modo claro
numero = "206.png"  # Acá poner "206c.png" si su Chrome está en modo claro

# Subrutinas necesarias


def esperaryclickear(imagen):
    r2 = None
    while r2 is None:
        time.sleep(0.1)
        r2 = pg.locateCenterOnScreen(imagen)
        if r2 == None:
            print("Todavía no se encuentra su imagen %s" % imagen)
        else:
            pg.click(r2)


def continuarsiseencuentra(imagen):
    r4 = None
    while r4 is None:
        time.sleep(2)
        r4 = pg.locateCenterOnScreen(imagen)
        if r4 == None:
            print("Todavía no se encuentra su imagen %s" % imagen)
        else:
            continue


def esperaryclickearderecha(imagen):
    r3 = None
    while r3 is None:
        time.sleep(0.1)
        r3 = pg.locateCenterOnScreen(imagen)
        if r3 == None:
            print("Todavía no se encuentra su imagen %s" % imagen)
        else:
            pg.click(r3, button='right')


diractual = os.getcwd()

for k in cursoUP:
    # Entrar a powercampus
    browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver83.exe")  # Acá puse el driver
    browser.get("https://autoservicio2.up.edu.pe/ss/Home.aspx")
    barra_user = browser.find_element_by_id("ctl00_ucUserLogin_lvLoginUser_ucLoginUser_lcLoginUser_UserName")
    barra_password = browser.find_element_by_id("ctl00_ucUserLogin_lvLoginUser_ucLoginUser_lcLoginUser_Password")
    barra_user.send_keys(usuarioUP)  # Acá poner su usuario UP
    barra_password.send_keys(contraseñaUP)  # Acá la contraseña
    barra_password.send_keys(Keys.ENTER)
    time.sleep(2)
    pg.hotkey('ctrl', 'shift', 'i')
    time.sleep(0.2)
    pg.hotkey('winleft', 'left')
    time.sleep(0.2)
    pg.press('esc')

    os.chdir("%s" % diractual + "\\Marcos")
    marco1 = pd.read_csv("%s" % k + ".csv")
    link = marco1['Link']
    curso = marco1['Curso']
    seccion = marco1['Sección']
    fecha = marco1['Fecha']
    nombreseccion = marco1['Nombre de la sesión']
    duracion = marco1['Duración']
    link2 = []
    os.chdir("%s" % diractual)

    # Obtener los link2
    for j in range(len(link)):
        browser.get(link[j])
        if j == 0:
            time.sleep(2)
            os.chdir("%s" % diractual + "\\imagenes")
            esperaryclickear(network)
            os.chdir("%s" % diractual)
            time.sleep(1)
            for i in range(2):
                pg.press('tab')
            for i in range(5):
                pg.press('right')
            pg.press('enter')
            for i in range(5):
                time.sleep(0.7)
                pg.press('tab')
            os.chdir("%s" % diractual + "\\imagenes")
            esperaryclickear(numero)
            os.chdir("%s" % diractual)
            time.sleep(1.5)
        else:
            os.chdir("%s" % diractual + "\\imagenes")
            continuarsiseencuentra(numero)
            os.chdir("%s" % diractual)
            time.sleep(0.3)
            pg.press('down')
        time.sleep(0.5)
        pg.hotkey('shift', 'f10')
        time.sleep(0.5)
        pg.press('down')
        time.sleep(0.5)
        pg.press('enter')
        time.sleep(0.05)
        pg.hotkey('ctrl', 'l')
        time.sleep(0.4)
        pg.hotkey('ctrl', 'c')
        time.sleep(0.2)
        link2.append(pc.paste())
        if link2[j] == link2[j - 1]:
            x = "Sí"
        elif len(link2) == 0:
            x = "No había anterior"
        else:
            x = "No"
        print("Hay " + str(len(link2)) + " links2 guardados ¿es igual al último? %s" % x)
        # browser.switch_to.window(browser.window_handles[1])
        # link2.append(browser.current_url)
        print("Se encontró el link2 %s/" % (j + 1) + "%s " % (len(link)) + ("(%s%%)") % (round((j + 1) * 100 / (len(link)), 2)))
        pg.hotkey('ctrl', 'w')
        # browser.switch_to.window(browser.window_handles[0])
    time.sleep(1.5)
    pg.hotkey('ctrl', 'shift', 'i')

    # Nueva columna al marco de datos
    marco1['Link2'] = link2
    print("Se agregó la columna Link2 al marco de datos de %s-" % marco1['Curso'].iloc[1] + "%s" % marco1['Sección'].iloc[1])

    # ACÁ PONER SU DIRECCIÓN DE DÓNDE GUARDAR LOS MARCOS
    nombremarco = (marco1['Curso'].iloc[0]) + "-" + (marco1['Sección'].iloc[0]) + ".csv"
    direccion_marcos = "C:\\Users\\JoseMax\\Documents\\Python Scripts\\Marcos2\\"
    marco1.to_csv('%s ' % direccion_marcos + '%s' % nombremarco, index=False, header=True)
    print("El marco está en %s " % direccion_marcos + "%s" % nombremarco)

    # Descargar con nombre
    for i in range(0, len(marco1['Link2'])):
        try:
            browser.get(marco1['Link2'].loc[i])  # Entra al enlace
        except:
            pg.hotkey('ctrl','r') #Esto por si la página no carga
            browser.get(marco1['Link2'].loc[i])
        pg.hotkey('ctrl', 's')  # Guardar como
        time.sleep(10)
        # Esto siguiente lo pongo para descargarlo a mi disco duro externo
        if i == 0:
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
    browser.quit()
