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

# Subrutinas necesaria


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


usuarioUP = "*"
contraseñaUP = "*"
cursoUP = ["econometria i(d", "Macroeconomía Int"]


for k in cursoUP:
    # Entrar a PowerCanpus
    browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver83.exe")  # Acá puse el driver
    browser.get("https://autoservicio2.up.edu.pe/ss/Home.aspx")
    barra_user = browser.find_element_by_id("ctl00_ucUserLogin_lvLoginUser_ucLoginUser_lcLoginUser_UserName")
    barra_password = browser.find_element_by_id("ctl00_ucUserLogin_lvLoginUser_ucLoginUser_lcLoginUser_Password")
    barra_user.send_keys(usuarioUP)  # Acá poner su usuario UP
    barra_password.send_keys(contraseñaUP)  # Acá la contraseña
    barra_password.send_keys(Keys.ENTER)
    boton_clases = browser.find_element_by_link_text("Clases")
    boton_clases.send_keys(Keys.ENTER)
    boton_clasesvirtuales = browser.find_element_by_link_text("Clases Virtuales")
    boton_clasesvirtuales.send_keys(Keys.ENTER)
    time.sleep(0.2)
    pg.hotkey('winleft', 'left')
    time.sleep(0.2)
    pg.press('esc')
    pagina_base = browser.current_url

    # Videos de un curso
    browser.get(pagina_base)
    boton_desplegable = browser.find_element_by_id("select2-searchCursos-container")
    boton_desplegable.click()
    busqueda = browser.find_element_by_class_name("select2-search__field")
    busqueda_desplegable = browser.find_element_by_xpath('//*[@id="ctl00_Html1"]/body/span/span/span[1]/input')
    busqueda_desplegable.send_keys(k)  # Nombre del curso
    busqueda_desplegable.send_keys(Keys.ENTER)

    # Scraping
    pg.hotkey('ctrl', 'shift', 'i')
    time.sleep(3)
    for i in range(2):
        pg.press('up')
    pg.hotkey('shift', 'f10')
    time.sleep(3)
    for i in range(5):
        pg.press('down')
    pg.press('right')
    for i in range(2):
        pg.press('down')
    pg.press('enter')
    pg.hotkey('ctrl', 'shift', 'i')
    html = pc.paste()
    soup = BeautifulSoup(html, "lxml")  # soup es el objeto, lmxl es el parser
    with open('html.html', "wb") as file:
        file.write(soup.prettify("utf-8"))

    # Obtener nombres de cursos
    cursoslista = soup.find('select', {"id": "searchCursos"})
    time.sleep(3)
    cursostexto = cursoslista.contents
    cursos = []  # Acá están los nombres de todos los cursos UP
    for i in range(1, len(cursostexto)):
        cursos.append(cursostexto[i].text)

    # Cabeceras
    tabla = soup.find('table', {"class": "table", "id": "tablaResultado"})
    cabeceraslista = tabla.thead.tr
    cabecerastexto = cabeceraslista.contents
    cabeceras = []
    for i in range(1, len(cabecerastexto) - 1, 2):
        cabeceras.append(cabecerastexto[i].text)
    cabeceras.append('Link2')

    # Datos
    datos = tabla.tbody
    claseslista = datos.contents
    curso = []
    seccion = []
    fecha = []
    nombreseccion = []
    duracion = []
    link = []  # Acá estarán los urls ca.bbcollab
    link2 = []  # Acá estarán los urls cloudfront
    datostot = [curso, seccion, fecha, nombreseccion, duracion, link, link2]
    for i in range(len(claseslista)):
        curso.append((claseslista[i].find_all('td')[0]).text)
        seccion.append((claseslista[i].find_all('td')[1]).text)
        fecha.append((claseslista[i].find_all('td')[2]).text)
        nombreseccion.append((claseslista[i].find_all('td')[3]).text)
        duracion.append((claseslista[i].find_all('td')[4]).text)
        link.append((claseslista[i].find_all('td')[5]).a.get('href'))

    # Obtener los link2
    for j in range(len(link)):
        browser.get(link[j])
        if j == 0:
            time.sleep(2)
            pg.hotkey('ctrl', 'shift', 'i')
            esperaryclickear('Network.png')
            time.sleep(1)
            for i in range(2):
                pg.press('tab')
            for i in range(5):
                pg.press('right')
            pg.press('enter')
            for i in range(5):
                time.sleep(0.2)
                pg.press('tab')
            time.sleep(1)
        continuarsiseencuentra('206.png')
        time.sleep(0.3)
        pg.press('down')
        time.sleep(1)
        pg.hotkey('shift', 'f10')
        time.sleep(1)
        pg.press('down')
        time.sleep(0.5)
        pg.press('enter')
        browser.switch_to.window(browser.window_handles[1])
        link2.append(browser.current_url)
        print("Se encontró el link2 %s/" % (j + 1) + "%s " % (len(link)) + ("(%s%%)") % (round((j + 1) * 100 / (len(link)), 2)))
        pg.hotkey('ctrl', 'w')
        browser.switch_to.window(browser.window_handles[0])
    time.sleep(1.5)
    pg.hotkey('ctrl', 'shift', 'i')

    # Marco de datos
    marco1 = pd.DataFrame()
    for i in range(len(cabeceras)):
        marco1[cabeceras[i]] = datostot[i]
    print("Se creó el marco de datos del curso %s-" % marco1['Curso'].iloc[1] + "%s" % marco1['Sección'].iloc[1])

    #ACÁ PONER SU DIRECCIÓN DE DÓNDE GUARDAR LOS MARCOS
    nombremarco = (marco1['Curso'].iloc[0]) + "-" + (marco1['Sección'].iloc[0]) + ".csv"
    direccion_marcos = "C:\\Users\\JoseMax\\Documents\\Python Scripts\\Marcos\\"
    marco1.to_csv('%s ' % direccion_marcos + '%s' % nombremarco, index=False, header=True)
    print("El marco está en %s " % direccion_marcos + "%s" % nombremarco)

    # Descargar con nombre
    for i in range(len(marco1['Link2'])):
        browser.get(marco1['Link2'].loc[i])  # Entra al enlace
        pg.hotkey('ctrl', 's')  # Guardar como
        # time.sleep(10)
        # pg.press('space')  # Pausar el video
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
            for j in range(3):
                time.sleep(0.7)
                pg.press('tab')
        pg.typewrite(marco1['Curso'].loc[i] + '_'
                     + marco1['Sección'].loc[i] + '_'
                     + "(%s de " % (i + 1) + "%s)" % (len(marco1['Link2'])) + '.mp4')  # Se guardará con el nombre 'Curso_Seccion_Nombresesion_.mp4'
        pg.press('enter')
        print("video descargándose %s" % (i + 1) + " /%s " % (len(marco1['Link2'])) + ("(%s%%)") % (round((i + 1) * 100 / (len(marco1['Link2'])), 2)))
        y = marco1['Duración'].loc[i]
        espera = int(y[0]) * 3600 + int(y[2:3]) * 60 + int(y[-2:-1])  # El tiempo de espera entre descargas dependerá de lo largo del video
        print("Este video dura %s " % marco1['Duración'].loc[i])
        print("El próximo video se descargará en %s" % round((espera / 35), 1)+" segundos")
        time.sleep(espera / 35)  # Descargará aproximadamente cuando termine el anterior
        time.sleep(2)
    time.sleep(300)  # Espera 5 minutos hasta descargar el siguiente curso
    browser.quit()
