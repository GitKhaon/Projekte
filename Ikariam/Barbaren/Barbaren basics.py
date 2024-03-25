def Barbar(x,y,driver):
    
    ansicht('s',driver)
    time.sleep(1)
    Tagesbelohnung(driver)
    ok(driver)
    ansicht('i',driver)
    ok(driver)
    InselBonus('Barbaren',driver)
    ok(driver)
    Aktion('plündern',driver)
    ok(driver)
    plündern(x,y,driver)
    ok(driver)
    time.sleep(1)

def Barbaren(x,y,driverliste):
    
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Barbar(x,y,driver)
    
