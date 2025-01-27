from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def configurar_driver(caminho_driver):
    # Configura o serviço do ChromeDriver
    service = Service(caminho_driver)
    driver = webdriver.Chrome(service=service)
    return driver

def login_moodle(driver, url, usuario, senha):
    driver.get(url)
    time.sleep(5)

    # Localiza os campos de login
    campo_usuario = driver.find_element(By.ID, "username")
    campo_senha = driver.find_element(By.ID, "password")

    # Preenche os campos de login
    campo_usuario.send_keys(usuario)
    campo_senha.send_keys(senha)

    # Clica no botão de login
    botao_login = driver.find_element(By.ID, "loginbtn")
    botao_login.click()

    time.sleep(5)

def acessar_curso(driver, nome_curso):
    # Procura o curso na lista de cursos
    cursos = driver.find_elements(By.CLASS_NAME, "coursebox")
    for curso in cursos:
        if nome_curso.lower() in curso.text.lower():
            curso.click()
            time.sleep(5)
            return True
    return False

def listar_secoes(driver):
    # Lista as seções dentro do curso
    secoes = driver.find_elements(By.CLASS_NAME, "sectionname")
    print("Seções disponíveis no curso:")
    for secao in secoes:
        print("-", secao.test)

def main():
    # Configuração do driver
    caminho_driver = "./chromedriver.exe"
    driver = configurar_driver(caminho_driver)

    try:
        # Dados de login e URL
        url_moodle = "https://sandbox.moodledemo.net/login/index.php"
        usuario = "student"
        senha = "sandbox24"

        # Acessa o Moodle e faz login
        login_moodle(driver, url_moodle, usuario, senha)

        # Acessa um curso específico
        nome_curso = "My first course"
        if acessar_curso(driver, nome_curso):
            listar_secoes(driver)
        else:
            print("Curso não encontrado.")
    finally:
        # Fecha o navegador
        driver.quit()

if __name__ == "__main__":
    main() 
