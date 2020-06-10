from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"./geckodriver.exe"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        try:
            loginButton = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']")
            loginButton.click()
        except:
            print("Logado")
            pass
        userInput = driver.find_element_by_xpath("//input[@name='username']")
        userInput.clear()
        time.sleep(4)
        userInput.send_keys(self.username)
        time.sleep(4)
        passwordInput = driver.find_element_by_xpath(
            "//input[@name='password']")
        passwordInput.clear()
        passwordInput.send_keys(self.password)
        time.sleep(4)
        passwordInput.send_keys(Keys.RETURN)
        time.sleep(4)
        self.escolherPerfis()

    def escolherPerfis(self):
        pag = "bolsonaro"
        # Página Alvo
        self.driver.get(
            "https://www.instagram.com/"+pag)
        time.sleep(5)
        seguidores = self.driver.find_element_by_xpath(
            "/html/body/div/section/main/div/header/section/ul/li[2]")
        seguidores.click()
        time.sleep(10)
        buttonsSeguir = self.driver.find_elements_by_class_name("Pkbci")

        for element in buttonsSeguir:
            try:
                element.click()
            except:
                self.driver.find_element_by_tag_name('body').click()
            time.sleep(3)


diegoBot = InstagramBot(

)
# "username","password"
diegoBot.login()
