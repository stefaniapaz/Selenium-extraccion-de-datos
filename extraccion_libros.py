from selenium import webdriver

url = "https://demoqa.com/books"  # Reemplaza con la URL de la página web
ruta_chromedriver = "/home/stefania/Documentos/Cursos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=ruta_chromedriver)

driver.get(url)

# Espera un tiempo para que la página se cargue completamente
# Puedes ajustar este tiempo según sea necesario
driver.implicitly_wait(10)

# Encuentra todos los elementos con la clase 'rt-tr-group'
elementos_libros = driver.find_elements_by_class_name("rt-tr-group")

# Itera sobre los elementos y extrae la información
for elemento_libro in elementos_libros:
    # Encuentra el título del libro
    titulo_libro = elemento_libro.find_element_by_css_selector('.action-buttons a').text

    # Encuentra el enlace del libro
    enlace_libro = elemento_libro.find_element_by_css_selector('.action-buttons a').get_attribute('href')
   
    # Imprime o almacena los datos como desees
    print(f"Título del libro: {titulo_libro}")
    print(f"Enlace del libro: {enlace_libro}")
    print("-" * 30)

# Cierra el navegador al finalizar
driver.quit()


