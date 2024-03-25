def farm(von,Insel,Position,Schiffe,driver):
    ok(driver)
    switch(von,driver)
    ok(driver)
    ansicht(Insel,driver)
    ok(driver)
    Inselstadt(Position,driver)
    ok(driver)
    Aktion('plündern',driver)
    ok(driver)
    plündern(['Speerträger'],['1',Schiffe],driver)
    ok(driver)

def alle(von,Insel):

    for i in range(11):
        farm(von,Insel,i,300,driver)
        ok(driver)

        Berater('m',driver)
        bewegungen = driver.find_element_by_xpath('//*[@id="js_tab_militaryAdvisor"]')
        bewegungen.click()
        zeit = driver.find_element_by_xpath('/html/body/div[1]/div[16]/div/div[2]/div[2]/div[3]/div[2]/div[2]/table/tbody/tr[2]/td[2]/span[1]')
        ankunft = zeit.text
        minutes = 0
        seconds = 0
        for i in range(len(ankunft)):
            if ankunft[i] == 'm':
                minutes = int(ankunft[:i])
		seconds = int(ankunft[i+2:-1])
        warten = (60*minutes+seconds)*2+2040
        time.sleep(warten)
    
