def Namen(liste,driver):
    
    nam = driver.find_element_by_xpath('//*[@id="GF_toolbar"]/ul/li[1]/a[2]')
    liste.append(nam.text)

    return liste

def Ipsenden(x,liste,driver):

    high = driver.find_element_by_xpath('//*[@id="GF_toolbar"]/ul/li[4]/a')
    high.click()

    try:
        sear = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="tab_highscore"]/div[1]/form/div/div/div[3]/div/input'))
        )        
    except:
        print('error')
        
    sear.send_keys(liste[x])
    sear.send_keys(Keys.RETURN)
    time.sleep(1)

    try:
        nach = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="tab_highscore"]/div[1]/table/tbody/tr[2]/td[5]/a'))
        )        
    except:
        print('error')

    nach.click()

    try:
        ausw = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="js_treatiesConfirm"]'))
        )        
    except:
        print('error')

    ausw.click()

    for i in range(5):
        ips = driver.find_element_by_xpath('//*[@id="js_treatiesConfirm"]/option['+str(i+1)+']')
        if ips.text == 'IP Sharing anbieten':
            break
    time.sleep(1)
    ips.click()
    time.sleep(1)

    absch = driver.find_element_by_xpath('//*[@id="js_messageSubmitButton"]')
    absch.click()

def Ipannehmen(driver):

    Berater('d',driver)

    try:
        ausw = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                'gopen'))
        )        
    except:
        print('error')
    else:
        time.sleep(1)
        z = driver.find_elements_by_class_name('subject')
        
    for i in range(len(z)):
        ll = driver.find_elements_by_class_name('subject')
        if ll[i].text == 'IP Sharing anbieten':

            ll[i].click()

            try:
                anneh = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME,
                        'answerYes'))
                )        
            except:
                print('error')

            anneh.click()

            try:
                absch = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                        '//*[@id="js_messageSubmitButton"]'))
                )        
            except:
                print('error')

            absch.click()
            time.sleep(1)
            ausw = driver.find_elements_by_class_name('gopen')
            time.sleep(1)
    
def setup11(driverliste):
    #time.sleep(1800)
    liste = []
    
    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        liste = Namen(liste,driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['20'],driver)
        ok(driver)
        ansicht('s',driver)
        Gebäude(14,driver)
        ok(driver)
        abreissen(driver)
        ok(driver)
        abreissen(driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(18,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
        ok(driver)
        time.sleep(3)
        
    time.sleep(780)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        for j in range(5):
            Ipsenden((i+j+1)%11,liste,driver)
            ok(driver)
            ansicht('s',driver)
            ok(driver)

        Gebäude(9,driver)
        ok(driver)
        abreissen(driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(18,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(1,driver)
        ok(driver)
        Hskaufen(1,driver)
        ok(driver)
        time.sleep(3)
        
    time.sleep(300)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Ipannehmen(driver)
        time.sleep(3)

    time.sleep(1200)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['26','3'],driver)
        ok(driver)
        time.sleep(3)

    time.sleep(2400)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['26','3'],driver)
        ok(driver)
        time.sleep(3)

    time.sleep(2400)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(0,driver)
        ok(driver)
        einstellen(['Forscher'],['22'],driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Berater('f',driver)
        ok(driver)
        Forschung('Wissenschaft',driver)
        ok(driver)
        time.sleep(3)

    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(1,driver)
        ok(driver)
        Hskaufen(1,driver)
        ok(driver)
        ansicht('s',driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(600)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['35','4'],driver)
        ok(driver)
        time.sleep(3)

    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(600)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['54','4'],driver)
        ok(driver)
        time.sleep(3)

    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(600)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['73','4'],driver)
        ok(driver)
        time.sleep(3)

    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(4500)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['5'],driver)
        ok(driver)

    time.sleep(600)
    
    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['90','4'],driver)
        ok(driver)
        time.sleep(3)
    
    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Speerträger'],['10'],driver)
        ok(driver)

    time.sleep(600)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(1,driver)
        ok(driver)
        Hskaufen(1,driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['92','5'],driver)
        ok(driver)
        time.sleep(3)
    
    time.sleep(9000)

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Gebäude(1,driver)
        ok(driver)
        Hskaufen(2,driver)
        ok(driver)
        ansicht('i',driver)
        ok(driver)
        InselBonus('Barbaren',driver)
        ok(driver)
        Aktion('plündern',driver)
        ok(driver)
        plündern(['Speerträger'],['90','7'],driver)
        ok(driver)
        time.sleep(3)

    time.sleep(9000)

def Palast(driverliste):

    for i in range(len(driverliste)):
        driver = driverliste[i]
        ansicht('s',driver)
        
        Tagesbelohnung(driver)
        ok(driver)
        Berater('f',driver)
        ok(driver)
        Forschung('Militär',driver)
        ok(driver)
        Forschung('Wirtschaft',driver)
        ok(driver)
        Forschung('Wirtschaft',driver)
        ok(driver)
        Forschung('Seefahrt',driver)
        ok(driver)
        Forschung('Seefahrt',driver)
        ok(driver)
        Forschung('Seefahrt',driver)
        ok(driver)
        Forschung('Seefahrt',driver)
        ok(driver)
        Forschung('Seefahrt',driver)
        ok(driver)
        Forschung('Seefahrt',driver)
        ok(driver)
        Gebäude(19,driver)
        ok(driver)
        neuesgebäude('Palast',driver)
        ok(driver)
        ok(driver)
