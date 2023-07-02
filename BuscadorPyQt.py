#! -*- coding: UTF-8 -*-
import time
from encodings import utf_8
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QAction
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys, os

#-------------
#   Funciona.
#-------------

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        #Herada el metodo __init__ de la clase.
        super(Ui, self).__init__()
        #Carga la UI desde archivo.
        uic.loadUi('scr/BuscadorPyQt.ui', self)
        #Barra y botón de busqueda ---------------------------
        self.SearchButton.clicked.connect(self.SearchButtonEvent)
        self.SearchTerm = self.SearchVar
        self.active = QAction("Inicio de busqueda", shortcut = QKeySequence("return"), triggered=self.SearchButtonEvent)
        self.addAction(self.active)

        #Menú Opciones ---------------------
        #Acciones del toolbar para motores de busqueda:
        #Google.
        self.addAction(self.Motor_Google)
        self.Motor_Google.triggered.connect(self.ChangeEngineG)
        #Duckduckgo
        self.addAction(self.Motor_DuckDuckGo)
        self.Motor_DuckDuckGo.triggered.connect(self.ChangeEngineDDG)
        #Bing
        self.addAction(self.Motor_Bing)
        self.Motor_Bing.triggered.connect(self.ChangeEngineB)

        #Selcción de los navegadores.
        #Google.
        self.addAction(self.Nav_Google_Chrome)
        self.Nav_Google_Chrome.setChecked(False)
        self.Nav_Google_Chrome.triggered.connect(self.ChangeBrowserG)
        #Firefox
        self.addAction(self.Nav_Firefox)
        self.Nav_Firefox.setChecked(False)
        self.Nav_Firefox.triggered.connect(self.ChangeBrowserF)
        #Edge
        self.Nav_Edge.setEnabled(False)

        #Cierre de la ventana.
        self.addAction(self.CloseWin) 
        self.CloseWin.triggered.connect(self.CloseApp)
        self.show()

    #Mensjae cambio de motor de busqueda.----------------------
    # Goolge.
    def ChangeEngineG(self):
        print("Motor de busqueda: Google. Seleccionado.")
        self.statusBar().showMessage('Motor de busqueda: Google. Seleccionado.', 2000)
        self.Motor_DuckDuckGo.setChecked(False)
        self.Motor_Bing.setChecked(False)
    #DuckDuckGo
    def ChangeEngineDDG(self):
        print("Motor de busqueda: Duckduckgo. Seleccionado.")
        self.statusBar().showMessage('Motor de busqueda: DuckDuckGo. Seleccionado.', 2000)
        self.Motor_Google.setChecked(False)
        self.Motor_Bing.setChecked(False)
    #Bing
    def ChangeEngineB(self):
        print("Motor de busqueda: Bing. Seleccionado.")
        self.statusBar().showMessage('Motor de busqueda: Bing. Seleccionado.', 2000)
        self.Motor_DuckDuckGo.setChecked(False)
        self.Motor_Google.setChecked(False)

    # Mensaje cambio de navegador.----------------------------- 
    # Chrome   
    def ChangeBrowserF(self):
            mensaje_F = "Navegador: Firefox. Selecionado."
            print(mensaje_F)
            self.statusBar().showMessage(mensaje_F,2000)
            self.Nav_Google_Chrome.setChecked(False)
    # Firefox
    def ChangeBrowserG(self):
            mensaje_G = "Navegador: Google Chrome. Seleccionado."
            print(mensaje_G)
            self.statusBar().showMessage(mensaje_G, 2000)
            self.Nav_Firefox.setChecked(False)        

    #Cierre del programa.
    def CloseApp(self):
        message_C = "Cerrando aplicación."
        print(message_C)
        self.statusBar().showMessage(message_C)
        time.sleep(1) #Tiempo en segundos.
        self.close() #Cierra el programa.


    #Boton/acción de busqueda
    def SearchButtonEvent(self):
        #Bloque de selección de motor de navegación.--------------
        if self.Motor_Google.isChecked() == True:
             self.url = "https://www.google.com"
        elif self.Motor_DuckDuckGo.isChecked() == True:
             self.url = "https://www.duckduckgo.com"
        elif self.Motor_Bing.isChecked() == True:
             self.url = "https://www.bing.com"
        else:
             Engine_message_err = "Ningún motor de busqueda fue seleccionado."
             print(Engine_message_err)
             self.statusBar().showMessage(Engine_message_err, 3000)
             return
            
        # Tomo la ruta hasta el directorio actual.
        self.pathToCurrentDir = os.getcwd()
        #Bloque de selcción de navegador.----------------
        if self.Nav_Google_Chrome.isChecked() == True:
            self.PathToChromeDriver = self.pathToCurrentDir + 'scr/chromedriver_linux64chromedriver_linux64/chromedriver'  
            #El webdriver tiene que ser ejecutado al momento de iniciar la busqueda.
            self.web = webdriver.Chrome(service = Service(self.PathToChromeDriver))
        elif self.Nav_Firefox.isChecked() == True:
            self.PathToFirefoxDriver = self.pathToCurrentDir + 'scr/FirefoxDriver/geckodriver'
            self.web = webdriver.Firefox(service = Service(self.PathToFirefoxDriver))
        else:
            Browser_message_Er = "Debe selccionar un navegador antes de iniciar la busqueda."
            self.statusBar().showMessage(Browser_message_Er, 5000)
        #-----------------------------------------------
            
        self.web.get(self.url) #busco la página que quiero utilizar.
        self.elementName = self.web.find_element(By.NAME, 'q') #busco el input de texto de la página por nombre.
        self.elementName.send_keys(self.SearchTerm.text(), Keys.ENTER) #Ingreso el termino de busqueda y comienzo.
        print("busqueda iniciada")
        self.statusBar().showMessage("Busqueda iniciada.")
        #self.web.quit() #Cerrará el navegador en cuanto termine la busqueda.
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

if __name__ == '__main__':
    main()
