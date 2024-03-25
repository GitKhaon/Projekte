from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


spieler = ['royaltroll@gmx.de','noah1998']
Landeinheiten = {'Hoplit' : '303', 'Dampfgigant' : '308', 'Speerträger' : '315', 'Schwertkämpfer' : '302', 'Steinschleuderer' : '301', 'Bogenschütze' : '313', 'Scwefelbüchsen' : '304', 'Rammbock' : '307', 'Katapult' : '306', 'Mörser' : '305', 'Gyrokopter' : '312', 'Ballon' : '309', 'Koch' : '310', 'Arzt' : '311'}
Kriegsschiffe = {'Feuer' : '211', 'Dampf' : '216', 'Ramm' : '210', 'Ballista' : '213', 'Katapult' : '214', 'Mörser' : '215', 'Raketen' : '217', 'Tauch' : '212', 'Schaufel' : '218', 'Ballon' : '219', 'Tender' : '220'}
Pakete = {'Hoplit' : 'itemIcon.troopsPackage.s303.units.amount500.medium', 'Feuer' : 'itemIcon.troopsPackage.s211.ships.amount250.medium', 'Dampfgigant' : 'itemIcon.troopsPackage.s308.units.amount500.medium', 'Dampf' : 'itemIcon.troopsPackage.s216.units.amount250.medium', 'Schwefelbüchsen' : 'itemIcon.troopsPackage.s304.units.amount500.medium', 'Mörser' : 'itemIcon.troopsPackage.s215.units.amount250.medium'}

def einloggen(spieler,driver):
    
    driver.execute_script("window.open('https://lobby.ikariam.gameforge.com/de_DE/')")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="loginRegisterTabs"]'
                )))
        
    except:
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        einloggen(spieler,driver)

    try:
        
#sind wir schon bei einloggen statt regestrieren
        
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="loginForm"]'
                )))
        
    except:
        
#switch von regestrieren auf einloggen
        
        einloggentab = driver.find_element_by_xpath(
            '//*[@id="loginRegisterTabs"]/ul[1]/li[1]'
            )
        
        einloggentab.click()

    email = spieler[0]
    emailslot = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[2]/div[1]/input[1]'
        )
    
    emailslot.send_keys(email)
    
    passwort = spieler[1]
    passwortslot = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[3]/div[1]/input[1]'
        )
    
    passwortslot.send_keys(passwort)

    passwortslot.send_keys(Keys.ENTER)

###
### BASICS
###

def ok(driver):

    try:
        ok = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_popupBtn1"]'
                )))
        
    except:
        pass
    
    else:
        time.sleep(1)
        ok.click()

def Tagesbelohnung(driver):
    
    try:
        schliess = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="multiPopup"]/div[2]/div[2]'
                )))
        
    except:
        pass
    
    else:
        schliess.click()

#zurückkehren in den Grundzustand. Hauptstadt, Stadtansicht.
#todo

def reset(driver):
    
    try:
        button = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                'button'
                )))
        
    except:
        pass

    else:
        buttons = driver.find_elements_by_class_name(
            'button'
            )
        
        for i in range(len(buttons)):

            if buttons[i].text == 'Schließen':
                buttons[i].click()

            if buttons[i].text == 'ok':
                buttons[i].click()

            if buttons[i].text == 'close':
                buttons[i].click()
          
def Animationenausstellen(driver):

    try:
        option = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                'options'
                )))

    except:
        pass

    else:
        option.click()

    try:
        img = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID,
                'Img'
                )))

    except:
        pass

    else:

#Die aktivieren/deaktivieren slots sind schwer zu finden. Doch das 3, Img sollte Animationen deaktivieren.
        
        imgs = driver.find_elements_by_id(
            'Img'
            )
        imgs[3].click()

        down = driver.find_element_by_class_name(
            'scroll_arrow_bottom'
            )

        for i in range(13):
            down.click()
            time.sleep(0.5)

        try:
            akzeptieren = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                    '//*[@id="vacationMode"]'
                    )))

        except:
            pass

        else:

            buttons = driver.find_elements_by_class_name(
                'button'
                )

            buttons[0].click()
