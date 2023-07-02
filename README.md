
# Buscador lanzable

## Sobre el código

Este buscador esta pensado para ser utilizado como un lanzador vinculado a una combinación de teclas.
Se escribio utilizando Python 3.10, Selenium y PyQt5. así que Selenium y PyQt5 es necesario para poder ejecutar el código.

Para poder instalar PyQt5 y Selenium ejecute:

    pip install PyQt5
    pip install selenium

Para más información:

. Instalar PyQt5: <https://pypi.org/project/PyQt5/>

. Instalar Selenium: <https://www.selenium.dev/documentation/webdriver/getting_started/install_library/>

## Problemas que pueden ocurrir

En el caso de que el progrma no ejecute alguno de los navegadores tenga en cuenta que los drivers tiene que estar actualizados.

Las versiones más recientes del navegador que quiere usar no iniciaran la busqueda, ya que los drivers pueden no ser compatibles con las versiones recientes de los nvegadores.

Para acutualizar los drivers de Firefox visite: <https://github.com/mozilla/geckodriver/releases>

Para actualizar los driver de Chrome visite: <https://chromedriver.chromium.org/downloads>

Una vez descargado el driver actualizado copie el contenido en las carpetas del driver correspondiente (el archivo anterior debe ser reemplazado).

También Puede intentar actualizar la librería Selenium. Para lograr esto puede intentar usar el siguiente comando:

    pip install -U selenium
