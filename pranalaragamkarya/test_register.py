from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# @pytest.fixture
# def setup():
driver= webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://stage.mobipaid.com/en/register")
    # yield driver
    # driver.quit()

# Testcase 1 Valid User
def test_registerValid():
    driver.find_element(By.NAME, "signatory_first_name").send_keys("jeje")
    driver.find_element(By.NAME, "signatory_last_name").send_keys("jarwati")
    driver.find_element(By.ID, "email").send_keys("jeje.jarwati95@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Dicob@1ni")
    driver.find_element(By.NAME, "name").send_keys("PT. Pranala Ragam Karya")
    driver.find_element(By.XPATH, "//*[@id='formRegister']/div[5]/div[2]/div/input").send_keys("82144393990")
    driver.find_element(By.XPATH, "//select[@name='region']/option[7]").click()
    driver.find_element(By.NAME, "state").send_keys("Jawa Timur")
    driver.find_element(By.CLASS_NAME, "psa-checkbox").click()
    driver.find_element(By.ID, "btn-register").click()
    time.sleep(5)
    Title = driver.title
    assert Title == "Mobipaid :: Merchant Application"


# testcase 2 invalid user (email salah, password salah, )
Kunci = [ ('jeje', 'jarwati', 'jeje.jarwati#gmail.com', 'Dicob@1ni', 'PT. Pranala ragam karya', '82144393990', 'Indonesia', 'Jawa Timur'),
    ('jeje', 'jarwati', 'jeje.jarwati#gmail.com', 'Dicob@1ni1', 'PT. Pranala ragam karya', '82144393990', 'Indonesia', 'Jawa Timur')
    
]
    



