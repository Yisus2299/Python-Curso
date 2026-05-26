# el reto es rellenar un registro en Lab Report usando las librerias de selenium vistas en iterarion.py
#importamos selenium y lo que necesitaremos para indicas si es una clase, id, etc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# con esto indicamos que usaremos edge como navegador de pruebas
#keep chrome/edge browser open after program fiishes

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

#asignamos que todo sera en edge
#create and configure the edge/Chrome wbdriver

driver = webdriver.Edge(options=edge_options)

#insertamos el link de la pagina que queremos
driver.get("https://secure-retreat-92358.herokuapp.com/")

#organizamos el codigo para que no se vea tan desorganizado:
# 1- buscamos los elementos y los ubicamos
first_name = driver.find_element(By.NAME, value="fName")
last_name= driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sing_up = driver.find_element(By.CSS_SELECTOR, value="form button")

#2- le asignamos la informacion
first_name.send_keys("Jesus")
last_name.send_keys("Ziegler")
email.send_keys("testJesusZ@email.com")

# podemos colocar el .click() pero en este caso no es necesario ya que no nos meteremos a ningun link o parecido
sing_up.click() #en este caso si, ya que le daremos click a algo para enviarlo