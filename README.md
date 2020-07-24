# UPlectures

Este es un proyecto para descargar automáticamente las clases virtuales de la UP.  
Actualmente estoy trabajando en la rama3  

## Requisitos  

* Necesitan tener instalado **Python 3**. Pueden revisar si tienen Python si van a su línea de comandos (*Símbolo de sistema* en Windows) y escriben `python --version` . Usuarios de Mac ya deberían tenerlo instalado por defecto. Si no lo tienen lo pueden descargar [aquí](https://www.python.org/downloads/).  

*  Necesitan tener descargado un navegador y un controlador (*driver*) de este. Acá usamos **ChromeDriver**. Lo pueden descargar [aquí]([https://sites.google.com/a/chromium.org/chromedriver/downloads). Deben asegurarse de descargar la misma versión que su navegador **Google Chrome**. Para ver la versión de su navegador denle click al botón de opciones en la esquina superior derecha, luego a *Ayuda* > *Información de Google Chrome*. Ahí revisen su versión (e.g. *84.0.4147.89*) y descarguen su controlador correspondiente.  

* Además necesitan tener los módulos para el proyecto, descárguenlos desde su línea de comandos (Para los que usen Anaconda vayan a Anaconda Prompt) y ejecuten:
	* `pip install selenium` para instalar **Selenium** 
	* `pip install bs4` para instalar **Beautiful Soup 4** (ya instalado para los que usan Anaconda)
	* `pip install pyautogui` para instalar **PyAutoGUI**. Posiblemente necesiten además instalar una dependencia 'wheel'; si es el caso, ejecuten `pip install wheel`
	* `pip install pandas` para instalar **Pandas** (ya instalado para los que usan Anaconda)
	* `pip install pyperclip` para instalar **Pyperclip**
	
* Necesitan un lugar dónde ejecutar Python. Pueden usar un editor de texto como [Sublime Text](https://www.sublimetext.com/) o [Visual Studio Code]((https://code.visualstudio.com/)), o un IDE como [Pycharm](https://www.jetbrains.com/pycharm/), o una aplicación web con kernel integrado como [Jupyter](https://jupyter.org/]). Por favor revisen bien cómo preparar sus ambientes correspondientes para ejecutar Python.  

## Ejecución

Clonen mi repositorio (En el botón verde de arriba pueden descargar el proyecto comprimido como .zip). Les recomiendo únicamente usar el archivo ***sololinksdownload.py***.  

Reemplacen en las líneas 13 a 28 su información correspondiente para descargar como **usuario UP**, **contraseña UP**, **nombre de los cursos a descargar** (e.g. *Microeconomía II-A*; revisar escribir el nombre igual que en la carpeta 'Marcos'), la **dirección de su controlador**, su **ratio de espera entre descargas**, y cambiar las variables de Network.png y 206.png por Networkc.png y 206c.png si su Chrome usa tema claro y no tema oscuro.  

En caso hayan tenido un problema en medio de la descarga, pueden intentar usar el archivo ***reanudar.py*** para descargar los videos que no se pudieron, pero todavía estoy trabajando en este en la rama3 del proyecto.
