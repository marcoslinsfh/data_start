from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
import pytest
import subprocess

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
    sleep(5)