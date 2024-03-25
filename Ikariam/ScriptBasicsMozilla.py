from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


Spieler = ['royaltroll@gmx.de','noah1998']
Landeinheiten = {'Hoplit' : '303', 'Dampfgigant' : '308', 'Speerträger' : '315', 'Schwertkämpfer' : '302', 'Steinschleuderer' : '301', 'Bogenschütze' : '313', 'Scwefelbüchsen' : '304', 'Rammbock' : '307', 'Katapult' : '306', 'Mörser' : '305', 'Gyrokopter' : '312', 'Ballon' : '309', 'Koch' : '310', 'Arzt' : '311'}
Kriegsschiffe = {'Feuer' : '211', 'Dampf' : '216', 'Ramm' : '210', 'Ballista' : '213', 'Katapult' : '214', 'Mörser' : '215', 'Raketen' : '217', 'Tauch' : '212', 'Schaufel' : '218', 'Ballon' : '219', 'Tender' : '220'}
Pakete = {'Hoplit' : 'itemIcon.troopsPackage.s303.units.amount500.medium', 'Feuer' : 'itemIcon.troopsPackage.s211.ships.amount250.medium', 'Dampfgigant' : 'itemIcon.troopsPackage.s308.units.amount500.medium', 'Dampf' : 'itemIcon.troopsPackage.s216.units.amount250.medium', 'Schwefelbüchsen' : 'itemIcon.troopsPackage.s304.units.amount500.medium', 'Mörser' : 'itemIcon.troopsPackage.s215.units.amount250.medium'}

#driver = webdriver.Firefox(executable_path=r"C:\Program Files (x86)\geckodriver.exe")
#driver.get('https://addons.mozilla.org/de/firefox/addon/adblock-plus/')

def einloggen(spieler,driver):
    
    driver.execute_script("window.open('https://lobby.ikariam.gameforge.com/de_DE/')")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)

    try:
        te = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="loginRegisterTabs"]/ul/li[1]'))
        )        
    except:
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        einloggen(spieler)
    else:
        time.sleep(1)
    try:
        te = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="loginForm"]/p/button[1]'))
        )        
    except:
        time.sleep(1)
        quack = driver.find_element_by_xpath('//*[@id="loginRegisterTabs"]/ul/li[1]')
        quack.click()
    else:
        pass
    
    x = spieler[0]
    email = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div/input')
    email.send_keys(x)
    
    x = spieler[1]
    passwort = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/input')
    passwort.send_keys(x)

    einlogg = driver.find_element_by_xpath('//*[@id="loginForm"]/p/button[1]')
    einlogg.click()

#    time.sleep(2)
#    try:
#        server = WebDriverWait(driver, 10).until(
#            EC.presence_of_element_located((By.XPATH,
#                '//*[@id="joinGame"]/button'))
#        )        
#    except:
#        print('error')
#    server.click()

#    driver.switch_to.window(driver.window_handles[-1])
#    try:
#        server = WebDriverWait(driver, 10).until(
#            EC.presence_of_element_located((By.XPATH,
#                '//*[@id="js_citySelectContainer"]/span'))
#        )        
#    except:
        #ausloggen(driver)
#        time.sleep(2)
        #einloggen(spieler,driver)
#    ansicht('s',driver)
#    driver.refresh()

def ausloggen(driver):
    
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(1)
    try:
        acc = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="content"]/div/div/nav/div/ul[2]/li/div'))
        )        
    except:
        print('error')
    acc.click()
    time.sleep(2)
    
    try:
        ausloggen = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="content"]/div/div/nav/div/ul[2]/li/ul/li[6]'))
        )        
    except:
        print('error')
    ausloggen.click()

    try:
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="loginForm"]/div[1]/div/input'))
        )        
    except:
        print('error')

    time.sleep(0.3)
    
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    
def switch(x,driver):
    
    städte = driver.find_element_by_xpath('//*[@id="js_citySelectContainer"]/span')
    städte.click()

    stadt = driver.find_element_by_xpath('//*[@id="dropDown_js_citySelectContainer"]/div[1]/ul/li[' +str(x) +']')
    stadt.click()
    time.sleep(1)

def ress(driver):
    
    liste = []

    liste.append('holz:')
    holz = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_wood"]')
    liste.append(holz.text)

    liste.append('wein:')
    wein = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_wine"]')
    liste.append(wein.text)

    liste.append('marmor:')
    marmor = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_marble"]')
    liste.append(marmor.text)

    liste.append('kristall:')
    kristall = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_crystal"]')
    liste.append(kristall.text)

    liste.append('schwefel:')
    schwefel = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_sulfur"]')
    liste.append(schwefel.text)
    return liste

def ansicht(x,driver):

    if x == 'i':
        insel = driver.find_element_by_xpath('//*[@id="js_islandLink"]')
        insel.click()

    elif x == 's':
        stadt = driver.find_element_by_xpath('//*[@id="js_cityLink"]')
        stadt.click()

    else:
        wmap = driver.find_element_by_xpath('//*[@id="js_worldMapLink"]')
        wmap.click()
        try:
            xcord = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                    '//*[@id="inputXCoord"]'))
            )        
        except:
            print('error')
        q = str(x[0])
        xcord.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + q)

        t = str(x[1])
        ycord = driver.find_element_by_xpath('//*[@id="inputYCoord"]')
        ycord.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + t + Keys.RETURN)

        time.sleep(1)
        insel = driver.find_element_by_xpath('//*[@id="linkurl_11_11"]')
        insel.click()
    
def Gebäude(x,driver):

    gebäude = driver.find_element_by_xpath('//*[@id="js_CityPosition' + str(x) + 'Link"]')
    gebäude.click()

    try:
        testt = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                'close'))
        )        
    except:
        Gebäude(x,driver)
    else:
        pass
    
def kosten(driver):

    liste = []
    stufe = driver.find_element_by_xpath('//*[@id="buildingUpgrade"]/div/ul/li[2]')
    liste.append(stufe.text[-1])
    for i in range(6):
        try:
            ress = WebDriverWait(driver, 0.1).until(
                EC.presence_of_element_located((By.XPATH,
                    '//*[@id="buildingUpgrade"]/ul/li['+ str(i+1) +']'))
            )        
        except:
            pass
        else:
            liste.append(ress.text)

    return liste

def ausbauen(driver):

    upgrade = driver.find_element_by_xpath('//*[@id="js_buildingUpgradeButton"]')
    upgrade.click()
    try:
        x = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="upgradeCountDown"]'))
        )        
    except:
        ausbauen(driver)
    else:
        return
    
def verschicken(x,y,z,v,driver): # von x nach y z liste der ress v liste der anzahl

    städte = driver.find_elements_by_class_name('cityBox')
    if x < y:
        stadt = städte[y-2]
    else:
        stadt = städte[y-1]
    stadt.click()

    try:
        lol = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="textfield_wood"]'))
        )        
    except:
        print('error')
    time.sleep(1)
    
    for i in range(len(z)):
        if z[i] == 'h':
            anzahl = driver.find_element_by_xpath('//*[@id="textfield_wood"]')
        if z[i] == 'w':
            anzahl = driver.find_element_by_xpath('//*[@id="textfield_wine"]')
        if z[i] == 'm':
            anzahl = driver.find_element_by_xpath('//*[@id="textfield_marble"]')        
        if z[i] == 'k':
            anzahl = driver.find_element_by_xpath('//*[@id="textfield_glass"]')
        if z[i] == 's':
            anzahl = driver.find_element_by_xpath('//*[@id="textfield_sulfur"]')
        q = str(v[i])
        anzahl.send_keys(q)
    time.sleep(0.5)
    
    #runter = driver.find_element_by_xpath('/html/body/div[1]/div[16]/div/div[2]/div[1]/div[3]')
    #for i in range(15):
    #    runter.click()
    
    verla = driver.find_element_by_xpath('//*[@id="loadingTime"]')
    verlad = verla.text

    reis = driver.find_element_by_xpath('//*[@id="journeyTime"]')
    reise = reis.text

    senden = driver.find_element_by_xpath('//*[@id="submit"]')
    senden.click()

    return (verlad,reise)
            
def Tagesbelohnung(driver):
    
    try:
        schliess = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="multiPopup"]/div[2]/div[2]'))
        )        
    except:
        pass
    else:
        time.sleep(1)
        schliess.click()
    
def remaining(driver):

    try:
        x = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="upgradeCountDown"]'))
        )        
    except:
        print('done')
    else:
        return x.text

def Truppen(x,y,driver):

    runter = driver.find_element_by_xpath('//*[@id="barracks"]/div[2]/div[1]/div[3]')
    liste = driver.find_elements_by_class_name('headline')


    for i in range(len(liste)):
        
        while liste[i].text == '':
            runter.click()

        for p in x:
            if p == liste[i].text:
                q = x.index(p)
                runter.click()
                runter.click()
                ausbilden = driver.find_element_by_xpath('//*[@id="js_barracksBuyTextfield'+ str(i+1) +'"]')
                time.sleep(0.1)
                ausbilden.send_keys(y[q])

    ausbilden.send_keys(Keys.RETURN)    

def Schiffe(x,y,driver):

    runter = driver.find_element_by_xpath('//*[@id="shipyard"]/div[2]/div[1]/div[3]')
    liste = driver.find_elements_by_class_name('headline')


    for i in range(len(liste)):
        
        while liste[i].text == '':
            runter.click()

        for p in x:
            if p == liste[i].text:
                q = x.index(p)
                runter.click()
                runter.click()
                ausbilden = driver.find_element_by_xpath('//*[@id="js_barracksBuyTextfield'+ str(i+1) +'"]')
                time.sleep(0.1)
                ausbilden.send_keys(y[q])

    ausbilden.send_keys(Keys.RETURN)

def Hskaufen(x,driver):

    kaufen = driver.find_element_by_xpath('//*[@id="js_tabBuyTransporter"]')
    kaufen.click()

    try:
        kauf = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_buyTransporterAction"]'))
        )        
    except:
        print('done')    
    time.sleep(1)
    kaufe = driver.find_element_by_xpath('//*[@id="js_buyTransporterAction"]')
    time.sleep(1)
    for i in range(x):
        kaufe.click()
        time.sleep(1)

def Truppenlesen(driver):

    liste = []
    
    x = driver.find_element_by_xpath('//*[@id="js_viewCityMenu"]/ul/li[1]')
    x.click()
    time.sleep(1)
    
    try:
        y = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="tabUnits"]/div[1]/div[1]/table[1]/tbody/tr[2]'))
        )        
    except:
        print('done')

    z = driver.find_element_by_xpath('//*[@id="tabUnits"]/div[1]/div[1]/table[2]/tbody/tr[2]')
    time.sleep(1)

    for i in range(len(y.text)):
        if y.text[i] == '\n':
            liste.insert(0, y.text[i+1:])

    for i in range(len(z.text)):
        if z.text[i] == '\n':
            liste.insert(1, z.text[i+1:])

    return(liste)

def Schiffelesen(driver):

    liste = []
    
    x = driver.find_element_by_xpath('//*[@id="js_viewCityMenu"]/ul/li[1]')
    x.click()
    
    try:
        schiff = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_tabShips"]'))
        )        
    except:
        print('done')
    schiff.click()
    time.sleep(1)

    try:
        y = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="tabShips"]/div[1]/div[1]/table[1]/tbody/tr[2]'))
        )        
    except:
        print('done')
        
    z = driver.find_element_by_xpath('//*[@id="tabShips"]/div[1]/div[1]/table[2]/tbody/tr[2]')
    time.sleep(1)

    for i in range(8):
        liste.insert(0, y.text[-(i*2+1)])

    for i in range(3):
        liste.insert(8, z.text[-(i*2+1)])

    return(liste)

def Wein(x,driver):

    if x == 'all':
        q = driver.find_element_by_xpath('//*[@id="wineAssignForm"]/div[1]/div[1]/a[2]')
        q.click()

    if x == 'nothing':
        r = driver.find_element_by_xpath('//*[@id="wineAssignForm"]/div[1]/div[1]/a[1]')
        r.click()
    time.sleep(1)
    l = driver.find_element_by_xpath('//*[@id="wineAssignForm"]/div[2]/div[1]/input')
    l.click()
    time.sleep(0.5)

def einstellen(x,y,driver):

    for i in range(len(x)):
        if x[i] == 'Holz':
            q = driver.find_element_by_xpath('//*[@id="inputWood"]')
            q.clear()
            q.send_keys(y[i])
        if x[i] == 'Luxus':
            q = driver.find_element_by_xpath('//*[@id="inputLuxury"]')
            q.clear()
            q.send_keys(y[i])
        if x[i] == 'Forscher':
            q = driver.find_element_by_xpath('//*[@id="inputScientists"]')
            q.clear()
            q.send_keys(y[i])
        if x[i] == 'Priester':
            q = driver.find_element_by_xpath('//*[@id="inputPriests"]')
            q.clear()
            q.send_keys(y[i])
    time.sleep(0.5)
    q.send_keys(Keys.RETURN)
    time.sleep(1.5)
    
def Berater(x,driver):
    
    if x == 's':
        q = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_cities"]')
        q.click()
    if x == 'm':
        q = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_military"]')
        q.click()
    if x == 'f':
        q = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_research"]')
        q.click()
    if x == 'd':
        q = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_diplomacy"]')
        q.click()

def Forschunglesen(driver):

    liste = []
    x = driver.find_element_by_xpath('//*[@id="js_researchAdvisorPoints"]')
    liste.append(x.text)

    q = driver.find_elements_by_class_name('available_research_wrap')

    for i in range(4):
        liste.append(q[i].text)

    return liste

def Forschung(x,driver):

    if x == 'Seefahrt':
        y = driver.find_element_by_xpath('//*[@id="js_researchAdvisorChangeResearchType0"]')
    if x == 'Wirtschaft':
        y = driver.find_element_by_xpath('//*[@id="js_researchAdvisorChangeResearchType1"]')
    if x == 'Wissenschaft':
        y = driver.find_element_by_xpath('//*[@id="js_researchAdvisorChangeResearchType2"]')
    if x == 'Militär':
        y = driver.find_element_by_xpath('//*[@id="js_researchAdvisorChangeResearchType3"]')        

    y.click()
    time.sleep(2)
    try:
        forschen = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_researchAdvisorConservationLink"]'))
        )        
    except:
        print('done')
    time.sleep(1)
    forschen.click()

def Wunder(driver):

    x = driver.find_element_by_xpath('//*[@id="js_WonderActivateButton"]')
    x.click()
    
def Inselstadt(x,driver):

    q = driver.find_element_by_xpath('//*[@id="cityLocation'+ str(x) +'"]')
    q.click()

def Aktion(x,driver):

    if x == 'plündern':
        q = driver.find_element_by_class_name('plundering')
    if x == 'stationieren':
        q = driver.find_element_by_class_name('deploy_army')
    if x == 'verteidigen':
        q = driver.find_element_by_class_name('defend_city')
    if x == 'besetzen':
        q = driver.find_element_by_class_name('occupy_city')
    if x == 'hafenbesetzen':
        q = driver.find_element_by_class_name('blockade')
    if x == 'hafenverteidigen':
        q = driver.find_element_by_class_name('defend_port')
    if x == 'spion':
        q = driver.find_element_by_class_name('espionage')

    q.click()

def plündern(x,y,driver):

    for i in range(len(x)):
        feld = driver.find_element_by_xpath('//*[@id="cargo_army_'+ Landeinheiten[x[i]] +'"]')
        time.sleep(0.5)
        feld.send_keys(y[i])

    schiffe = driver.find_element_by_xpath('//*[@id="extraTransporter"]')
    time.sleep(0.5)
    schiffe.send_keys(y[-1])
    time.sleep(0.2)
    schiffe.send_keys(Keys.RETURN)

def InselBonus(x,driver):

    if x == 'Barbaren':
        q = driver.find_element_by_xpath('//*[@id="barbarianVillage"]')
    if x == 'Holz':
        q = driver.find_element_by_xpath('//*[@id="islandresource"]')
    if x == 'Luxus':
        q = driver.find_element_by_xpath('//*[@id="islandtradegood"]')
    if x == 'Wunder':
        q = driver.find_element_by_xpath('//*[@id="islandwonder"]')

    q.click()

def stationieren(x,y,driver):
        
    for i in range(len(x)):
        feld = driver.find_element_by_xpath('//*[@id="cargo_army_'+ Landeinheiten[x[i]] +'"]')
        time.sleep(1)
        feld.send_keys(y[i])
        time.sleep(1)
    feld.send_keys(Keys.RETURN)

def verteidigen(x,y,driver):
        
    for i in range(len(x)):
        feld = driver.find_element_by_xpath('//*[@id="cargo_army_'+ Landeinheiten[x[i]] +'"]')
        time.sleep(0.5)
        feld.send_keys(y[i])
    
    zeit = driver.find_element_by_xpath('//*[@id="js_defendMissionDurationSelectContainer"]/span')
    zeit.click()

    try:
        zeitt = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="dropDown_js_defendMissionDurationSelectContainer"]/div[1]/ul/li[9]'))
        )        
    except:
        print('done')
    time.sleep(0.3)

    zeitt.click()
    time.sleep(0.2)
    feld.send_keys(Keys.RETURN)

def spenden(x,y,driver):

    if x == 'Holz':
        q = driver.find_element_by_xpath('//*[@id="donateWood"]')
        q.send_keys(y)
    if x == 'Wein':
        q = driver.find_element_by_xpath('//*[@id="tradegood1"]')
        q.send_keys(y)
    if x == 'Marmor':
        q = driver.find_element_by_xpath('//*[@id="tradegood2"]')
        q.send_keys(y)
    if x == 'Kristall':
        q = driver.find_element_by_xpath('//*[@id="tradegood3"]')
        q.send_keys(y)
    if x == 'Schwefel':
        q = driver.find_element_by_xpath('//*[@id="tradegood4"]')
        q.send_keys(y)

    time.sleep(1)
    q.send_keys(Keys.RETURN)

def gründen(x,driver):

    #runter = driver.find_element_by_xpath('//*[@id="colonize"]/div[2]/div[1]/div[3]')
    #runter.click()
    #runter.click()
    #runter.click()
    
    h = driver.find_element_by_xpath('//*[@id="textfield_wood"]')
    try:
        w = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="textfield_wine"]'))
        )        
    except:
        w = 1
    try:
        m = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="textfield_marble"]'))
        )        
    except:
        m = 1
    try:
        k = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="textfield_glass"]'))
        )        
    except:
        k = 1
    try:
        s = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="textfield_sulfur"]'))
        )        
    except:
        s = 1

    h.send_keys(x[0])
    if w != 1:
        w.send_keys(x[1])
    if m != 1:
        m.send_keys(x[2])
    if k != 1:
        k.send_keys(x[3])
    if s != 1:
        s.send_keys(x[4])

    time.sleep(1)

    h.send_keys(Keys.RETURN)

def Premiumhändler(x,driver):

    y = driver.find_element_by_xpath('//*[@id="js_viewCityMenu"]/ul/li[4]')
    y.click()

    try:
        zero = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="buttonZero"]'))
        )
    except:
        pass
    time.sleep(1)
    zero.click()

    h = driver.find_element_by_xpath('//*[@id="js_list_entry_wood"]/div[3]/a[2]')
    w = driver.find_element_by_xpath('//*[@id="js_list_entry_wine"]/div[3]/a[2]')
    m = driver.find_element_by_xpath('//*[@id="js_list_entry_marble"]/div[3]/a[2]')
    k = driver.find_element_by_xpath('//*[@id="js_list_entry_glass"]/div[3]/a[2]')
    s = driver.find_element_by_xpath('//*[@id="js_list_entry_sulfur"]/div[3]/a[2]')
    time.sleep(1)
    
    for i in range(len(x)):
        if x[i] == 'Holz':
            h.click()
        if x[i] == 'Wein':
            w.click()
        if x[i] == 'Marmor':
            m.click()
        if x[i] == 'Kristall':
            k.click()
        if x[i] == 'Schwefel':
            s.click()

    ambro = driver.find_element_by_xpath('//*[@id="js_orderButtonIcon_premium_trader"]')
    ambro.click()
    
    try:
        ok = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_popupBtn1"]'))
        )
    except:
        pass
    time.sleep(1)

    ok.click()

def Hafenbesetzen(x,y,driver):

    for i in range(len(x)):
        feld = driver.find_element_by_xpath('//*[@id="cargo_fleet_' + Kriegsschiffe[x[i]] +'"]')
        time.sleep(0.5)
        feld.send_keys(y[i])

    feld.send_keys(Keys.RETURN)

def Hafenverteidigen(x,y,driver):

    zeit = driver.find_element_by_xpath('//*[@id="js_defendMissionDurationSelectContainer"]/span')
    zeit.click()

    try:
        zeitt = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="dropDown_js_defendMissionDurationSelectContainer"]/div[1]/ul/li[9]'))
        )        
    except:
        print('done')
    time.sleep(0.3)

    zeitt.click()
    time.sleep(0.2)
    Hafenbesetzen(x,y,driver)

def ok(driver):

    try:
        ok = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_popupBtn1"]'))
        )
    except:
        pass
    else:
        time.sleep(1)
        ok.click()

def abholen(driver):

    x = driver.find_element_by_xpath('//*[@id="js_selectedCityOwnerName"]')
    x.click()

    try:
        ach = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_tab_avatarDetails"]'))
        )        
    except:
        print('done')
    time.sleep(1)

    ach.click()

    try:
        abh = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="avatarDetails"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/form/input[3]'))
        )        
    except:
        print('done')    
    time.sleep(1)

    abh.click()

def einlösen(x,driver):

    inv = driver.find_element_by_xpath('//*[@id="globalResources"]/ul/li[2]/a')
    inv.click()

    try:
        paket = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                Pakete[x]))
        )        
    except:
        print('done')    
    time.sleep(1)
    paket.click()
    time.sleep(1)
    bes = driver.find_element_by_xpath('//*[@id="useItemBtn"]')
    bes.click()
    ok(driver)

def Soldatenhandel(x,y,driver):

    q = driver.find_element_by_xpath('//*[@id="js_tab_branchOfficeSoldier"]')
    q.click()

    try:
        ausw = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_typeContainer"]/span'))
        )        
    except:
        print('done')
    time.sleep(0.5)
    ausw.click()

    try:
        land = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="dropDown_js_typeContainer"]/div[1]/ul/li[1]'))
        )        
    except:
        print('done')
    time.sleep(0.5)
    land.click()

    try:
        hand = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="searchResult"]/tbody/tr[1]/td[7]/a'))
        )        
    except:
        print('done')
    time.sleep(0.5)
    hand.click()

    try:
        check = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="textfield_premium"]'))
        )        
    except:
        print('done')
    feld = driver.find_elements_by_class_name('textfield')
    time.sleep(0.5)

    for i in range(len(x)):
        feld[2*(x[i])].send_keys(y[i])

    feld[2*x[-1]].send_keys(Keys.RETURN)

def Schiffhandel(x,y,driver):

    q = driver.find_element_by_xpath('//*[@id="js_tab_branchOfficeSoldier"]')
    q.click()

    try:
        ausw = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_typeContainer"]/span'))
        )        
    except:
        print('done')
    time.sleep(0.5)
    ausw.click()

    try:
        land = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="dropDown_js_typeContainer"]/div[1]/ul/li[2]'))
        )        
    except:
        print('done')
    time.sleep(0.5)
    land.click()

    try:
        hand = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="searchResult"]/tbody/tr[1]/td[7]/a'))
        )        
    except:
        print('done')
    time.sleep(0.5)
    hand.click()

    try:
        check = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="textfield_premium"]'))
        )        
    except:
        print('done')
    feld = driver.find_elements_by_class_name('textfield')
    time.sleep(0.5)

    for i in range(len(x)):
        feld[2*(x[i])].send_keys(y[i])

    feld[2*x[-1]].send_keys(Keys.RETURN)        

def neuesgebäude(x,driver):

    z = 's'
    q = driver.find_elements_by_class_name('headline')
    runter = driver.find_element_by_xpath('//*[@id="buildingGround"]/div[2]/div[1]/div[3]')
    
    for i in range(len(q)):
        for j in range(5):
            if q[i].text == '':
                runter.click()
            if q[i].text == x:
                z = i
                break
        if z != 's':
            break

    bau = driver.find_element_by_xpath('//*[@id="buildings"]/li[' + str(z+1) + ']/a')
    bau.click()

    try:
        spee = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                'buildingUpgradeIcon'))
        )        
    except:
        neuesgebäude(x,driver)
    else:
        return

def Goldlesen(driver):

    gold = driver.find_element_by_xpath('//*[@id="js_GlobalMenu_gold"]')
    gold.click()

    try:
        runter = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="finances"]/div[2]/div[1]/div[3]'))
        )        
    except:
        print('done')
    time.sleep(0.5)

    for i in range(11):
        runter.click()

    bilanz = driver.find_element_by_xpath('//*[@id="finances"]/div[2]/div[2]/table[5]/tbody/tr[4]/td[4]')
    return bilanz.text

def buildingspeed(driver):

    speed = driver.find_element_by_class_name('buildingSpeedupButton.free')
    speed.click()
    ok(driver)

    try:
        ook = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_buildingSpeedupActivateBtn"]'))
        )        
    except:
        print('done')
    ok(driver)
    ook.click()
    ok(driver)

    try:
        speed2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                'buildingSpeedupButton.finish.free'))
        )        
    except:
        print('done')
    else:
        ok(driver)
        speed2.click()

    try:
        ook = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_buildingSpeedupActivateBtn"]'))
        )        
    except:
        print('done')
    else:
        ok(driver)
        ook.click()    

def Bürgerlesen(driver):

    liste = []
    wohn = driver.find_element_by_xpath('//*[@id="townHall"]/div[2]/div[2]/div[3]/div[1]/div[1]/ul[1]/li[1]')
    hol = driver.find_element_by_xpath('//*[@id="js_TownHallPopulationGraphResourceWorkerCount"]')
    lux = driver.find_element_by_xpath('//*[@id="js_TownHallPopulationGraphSpecialWorkerCount"]')
    scie = driver.find_element_by_xpath('//*[@id="js_TownHallPopulationGraphScientistCount"]')
    priest = driver.find_element_by_xpath('//*[@id="js_TownHallPopulationGraphPriestCount"]')
    bürger = driver.find_element_by_xpath(' //*[@id="js_TownHallPopulationGraphCitizenCount"]')
    runter = driver.find_element_by_xpath('//*[@id="townHall"]/div[2]/div[1]/div[3]')

    liste.append(wohn.text)
    
    for i in range(7):
        runter.click()

    glück = driver.find_element_by_xpath('//*[@id="js_TownHallHappinessLargeValue"]')
    
    liste.append(hol.text)
    liste.append(lux.text)
    liste.append(scie.text)
    liste.append(priest.text)
    liste.append(bürger.text)
    liste.append(glück.text)
    return liste
                                      
def abreissen(driver):

    ab = driver.find_element_by_xpath('//*[@id="buildingUpgrade"]/div/ul/li[3]/a ')
    ab.click()
    
    try:
        okk = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_demolitionYesBtn"]'))
        )        
    except:
        print('done')
    time.sleep(0.5)
    okk.click()

def Gebäudestufe(driver):

    Stufe = driver.find_element_by_class_name('showLevel')
    return Stufe.text[6:]



    
