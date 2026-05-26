#importamos selenium y lo que necesitaremos para indicas si es una clase, id, etc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# con esto indicamos que usaremos edge como navegador de pruebas
#keep chrome/edge browser open after program fiishes

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

#asignamos que todo sera en edge
#create and configure the edge/Chrome wbdriver

driver = webdriver.Edge(options=edge_options)

#insertamos el link de la pagina que queremos
#Navigate to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")


#hone in on anchor tag using CSS selectors (se usan as que todo cuando no hay Clases o IDs y las cosas que buscamos estan en un Div)
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a") #el "#"" significa ID, el HTML dice: div id="articlecount". se usa CSS_SELECTOR cuando no ves ninguna clase y necesitas averiguar mas a fondo, realmente depende de muchas cosas
# article_count.click() #esto permite que, basado en la variable previamente creada y que ubicamos, clickee adentro

# Find element by Link text:
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals") #esto es para acceder a un link dentro de la pagina que queramos
# all_portals.click()


# Find the "Search" <input> by NAME: 
# 1) Clic en el botón/icono de búsqueda (abre el cuadro de texto)
wait = WebDriverWait(driver, 10)
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.search-toggle")))
search_button.click()

# 2) Escribir en el campo de búsqueda ya visible
search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.cdx-text-input__input[name='search']")))
# search_box.send_keys("Python") # Con esto hacemos que, al darle click al boton de busqueda ponga lo que pusimos en send_keys

# sending keyboard input to Selenium:
search_box.send_keys("Python", Keys.ENTER) #con esto, le asignamos lo que queremos buscar y con el ENTER, buscamos

