# UPlectures

Este es un proyecto para descargar automáticamente las clases virtuales de la UP.  
Actualmente estoy trabajando en la rama3.  

## Requisitos  

* Necesitan tener instalado **Python 3**. Pueden revisar si tienen Python si van a su línea de comandos (*Símbolo de sistema* en Windows) y escriben `python --version` . Usuarios de Mac ya deberían tenerlo instalado por defecto. Si no lo tienen lo pueden descargar [aquí](https://www.python.org/downloads/).  

*  Necesitan tener descargado un navegador y un controlador (*driver*) de este. Acá usamos **ChromeDriver**. Lo pueden descargar [aquí](https://sites.google.com/a/chromium.org/chromedriver/downloads). Deben asegurarse de descargar la misma versión que su navegador **Google Chrome**. Para ver la versión de su navegador denle click al botón de opciones en la esquina superior derecha, luego a *Ayuda* > *Información de Google Chrome*. Ahí revisen su versión (e.g. *84.0.4147.89*) y descarguen su controlador correspondiente.  

* Además necesitan tener los módulos para el proyecto, descárguenlos desde su terminal (Para los que usen Anaconda vayan a Anaconda Prompt) y ejecuten:
	* `pip install selenium` para instalar **Selenium** 
	* `pip install bs4` para instalar **Beautiful Soup 4** (ya instalado para los que usan Anaconda)
	* `pip install pyautogui` para instalar **PyAutoGUI**. Posiblemente necesiten además instalar una dependencia 'wheel'; si es el caso, ejecuten `pip install wheel`
	* `pip install pandas` para instalar **Pandas** (ya instalado para los que usan Anaconda)
	* `pip install pyperclip` para instalar **Pyperclip**
	
* Necesitan un lugar dónde ejecutar Python. Podrían ejecutar archivos directamente desde su línea de comandos con  `python archivo.py` en Windows, o `python3 archivo.py` en Mac y Linux, pero les sería conveniente usar un editor de texto como [Sublime Text](https://www.sublimetext.com/) o [Visual Studio Code](https://code.visualstudio.com/), o un IDE como [Pycharm](https://www.jetbrains.com/pycharm/) o [Spyder](https://www.spyder-ide.org/), o una aplicación web con kernel integrado como [Jupyter](https://jupyter.org/]). Por favor revisen bien cómo preparar sus ambientes correspondientes para ejecutar Python.  

## Ejecución

Clonen mi repositorio (En el botón verde de arriba pueden descargar el proyecto comprimido como .zip). Les recomiendo únicamente usar el archivo ***sololinksdownload.py***. Este encuentra los links de descarga de los videos, los guarda en la carpeta 'Marcos2' y luego los usa para descargarlos.  

Reemplacen en las líneas 14 a 34 su información correspondiente para descargar como **usuario UP**, **contraseña UP**, **nombres de los cursos a descargar** (e.g. *Microeconomía II-A*; revisar escribir el nombre igual que en la carpeta 'Marcos'), la **dirección de su controlador**, la **dirección de la carpeta 'Marcos2'** su **ratio de espera entre descargas**, y cambiar las variables de Network.png y 206.png por Networkc.png y 206c.png si su Chrome usa tema claro y no tema oscuro.  

Dejar el código corriendo, no mover el mouse al menos hasta que empiece la primera descarga; luego tendrán tiempo entre descargas para usarlo, ¡pero cliqueen en el controlador antes de que la siguiente descarga empiece! Los videos serán guardados en su carpeta de descargas por defecto con los nombres *Nombrecurso_Sección_(# de #).mp4*.

En caso hayan tenido un problema en medio de la descarga pero ya pudieron crear el archivo de su curso en 'Marcos2', usen el archivo ***reanudar.py*** para descargar los videos que no se pudieron bajar a la primera. Este toma los links de esa carpeta y reanuda solo los videos que les falta descargar de un curso. Especificar cuáles videos reanudar en la líneas 18, 22 y 23 y seguir las instrucciones del archivo.  

En caso prefieran hacer el procedimiento en 2 pasos (o sea primero obtener los links de descarga y luego descargarlos) usen el archivo ***sololinks2.py*** para primero obtenerlos y luego ***reanudar.py*** para descargarlos. **IMPORTANTE**: Los links de descarga ('links2') solo están disponibles por 12 horas luego de que se obtuvieron, por eso es recomendable hacerlo en 1 solo paso con ***sololinksdownload.py***, o no demorarse entre ambos pasos.

## Problemas frecuentes

* ***Todavía no se encuentra su imagen Network.png***: El código busca en su pantalla la imagen *Network.png* o *Networkc.png* de la carpeta 'imagenes' y no lo encuentra. En dicho caso tomar una captura de pantalla de este botón y reemplazarlo por el archivo original. ¡Tomar una captura de pantalla precisa de solo las letras!  

* ***Todavía no se encuentra su imagen 206.png***: El código busca en su pantalla la imagen *206.png* o *206c.png* de la carpeta 'imagenes' y no lo encuentra. En dicho caso tomar una captura de pantalla de este botón y reemplazarlo por el archivo original. ¡Tomar una captura de pantalla precisa de solo los números!  

* ***Muchas descargas a la vez***: Posiblemente su ratio espera entre descargas *respera* es muy alto para su velocidad internet de descargas y esto genere problemas al descargar videos. Como ya obtuvo el 'Marco2' de su curso puede abortar el código y usar ***reanudar.py*** para descargar los cursos que le faltan con un ratio de espera menor.  

* ***Video de un curso ya no está disponible en Blackboard Collaborate***: Hay videos de cursos que fueron removidos por los profesores o asistentes y por tanto el código se queda sin encontrar 206.png y dice ***Todavía no se encuentra su imagen 206.png***. Todavía estoy trabajando en arreglar esto.

* ***Link descargable ya no es accesible***: Se demoró mucho (más de 12 horas) en usar los links descargables y ya no son accesibles. Repita el procedimiento anterior para obtener nuevos y descargarlos.
