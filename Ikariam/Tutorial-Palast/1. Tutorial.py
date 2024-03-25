def firstlogin(spieler,y,driver):

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
        firstlogin(spieler,y,driver)
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

    time.sleep(2)
    
    try:
        server = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="joinGame"]/a/button'))
        )        
    except:
        print('error')
    else:
        server.click()
    time.sleep(1)

    try:
        servliste = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="newAccount"]/div[2]/a'))
        )        
    except:
        print('error')
    else:
        servliste.click()
    time.sleep(1)

    try:
        check = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                'rt-td.name-cell'))
        )        
    except:
        print('error')
    else:
        sliste = driver.find_elements_by_class_name('rt-td.name-cell')
    time.sleep(1)

    for i in range(len(sliste)):
        if sliste[i].text == y:
            q = driver.find_element_by_xpath('//*[@id="serverlist"]/div/div[1]/div[2]/div[' + str((i+1)) + ']/div/div[8]/button')
            time.sleep(1)
            q.click()
            time.sleep(1)
            break

    driver.switch_to.window(driver.window_handles[-1])
    try:
        server = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_citySelectContainer"]/span'))
        )        
    except:
        ausloggen(driver)
        time.sleep(2)
        einloggen(spieler,driver)
    ansicht('s',driver)
    driver.refresh()
        
def Tutorialok(driver):
    try:
        ok = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_tutorialOkButton_reward"]'))
        )        
    except:
        print('error')
    else:
        time.sleep(1)
        ok = driver.find_element_by_xpath('//*[@id="js_tutorialOkButton_reward"]')
        ok.click()    


def Tutorial(driverliste):

    for i in range(len(driverliste)):
        driver = driverliste[i]
        #firstlogin(x[i],y,driver)
        Tagesbelohnung(driver)
        ok(driver)
        q = driver.find_element_by_xpath('//*[@id="js_tutorialOkButton_quest"]')
        q.click()
        ok(driver)
        l = driver.find_element_by_xpath('//*[@id="GF_toolbar"]/ul/li[5]/a')
        l.click()
        try:
            de = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                    '//*[@id="Img"]'))
            )        
        except:
            print('error')
        else:
            dea = driver.find_elements_by_xpath('//*[@id="Img"]')
        ok(driver)
        dea[1].click()
        time.sleep(1)
        ok(driver)
        p = driver.find_element_by_xpath('//*[@id="tab_options"]/div[1]/div[1]/form/div[2]/input')
        p.click()
        time.sleep(3)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(18,driver)
        ok(driver)
        neuesgebäude('Akademie',driver)
        ok(driver)
        ok(driver)
        buildingspeed(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        neuesgebäude('Kaserne',driver)
        ok(driver)
        ok(driver)
        buildingspeed(driver)
        ok(driver)
        Gebäude(14,driver)
        ok(driver)
        neuesgebäude('Stadtmauer',driver)
        ok(driver)
        ok(driver)
        buildingspeed(driver)
        ok(driver)
        Gebäude(0,driver)
        ok(driver)
        einstellen(['Holz'],['1'],driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        Berater('f',driver)
        ok(driver)
        Forschung('Wirtschaft',driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(9,driver)
        ok(driver)
        neuesgebäude('Lagerhaus',driver)
        ok(driver)
        buildingspeed(driver)
        ok(driver)
        Gebäude(0,driver)
        ok(driver)
        einstellen(['Forscher'],['12'],driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['3'],driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(1,driver)
        ok(driver)
        neuesgebäude('Handelshafen',driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        time.sleep(120)
        ok(driver)
        buildingspeed(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        Gebäude(1,driver)
        ok(driver)
        Hskaufen(1,driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(9,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)

        ac = ActionChains(driver)
        elem = driver.find_element_by_xpath('//*[@id="js_islandBarbarianPlundering"]')
        ac.move_to_element(elem).move_by_offset(2, 4).click().perform()
        
        ok(driver)
        plündern(['Speerträger'],['6','1'],driver)
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        
        try:
            ambr = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                    '//*[@id="js_GlobalMenu_ambrosia"]'))
            )        
        except:
            print('error')
        else:
            ambr.click()
        
        ok(driver)
        ok(driver)
        Tutorialok(driver)
        ok(driver)
        time.sleep(3)




        
        
    
