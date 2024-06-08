from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os

@pytest.fixture
def driver(): 
    # Iniciar o Streamlit em backgroud
    process = subprocess.Popen (["streamlit", "run", "src/app.py"])
    
    # Definindo o driver que vamos utilizar 
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o Webdriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens (driver): 
    # Verificar se a página abriu
    driver.get("http://localhost:8501")
    sleep(2)

def test_check_title_is (driver):
    # Verificar se a página abriu
    driver.get("http://localhost:8501")
    sleep(2)
    page_title = driver.title

    expected_title = "Validador de schema excel"
    assert page_title == expected_title

def test_check_streamlit_h1(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(2)  # Espera 5 segundos

    # Capturar o primeiro elemento <h1> da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> é o esperado
    expected_text = "Insira o seu excel para validação"
    assert h1_element.text == expected_text

def test_check_usuario_pode_inserir_um_excel_e_receber_uma_mensagem(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(2)  # Espera 5 segundos

    # Realizar o upload do arquivo de sucesso
    success_file_path = os.path.abspath("data/arquivo_excel.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

    # Aguardar a mensagem de sucesso
    sleep(2)
    assert "O schema do arquivo Excel está correto!" in driver.page_source

  