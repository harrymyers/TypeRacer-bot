import pyautogui
from bs4 import BeautifulSoup
import keyboard
import time
from selenium import webdriver


def get_text_to_type(driver):
    time.sleep(1)
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    tags = soup.find_all('span', {'unselectable': 'on'})
    if tags:
        print(tags[0].get_text() + tags[1].get_text() + tags[2].get_text())
        return tags[0].get_text() + tags[1].get_text() + tags[2].get_text()
    return ""

            
def type_text(text):
    pyautogui.typewrite(text, interval=0.04)

def main():
    driver = webdriver.Chrome()
    driver.get('https://play.typeracer.com/')
    keyboard.wait('ctrl+shift+t')
    text_string = get_text_to_type(driver)
    if text_string:
        type_text(text_string)
        time.sleep(100)
    

    

if __name__=="__main__":
    main()