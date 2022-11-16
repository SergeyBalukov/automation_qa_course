import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install()) #Благодаря этой каманде запускается и открывается браузер
    driver.maximize_window() #открываем браузер на весь экран
    yield driver
    driver.quit()
