def Schritt1(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(9,driver)
        ok(driver)
        neuesgebäude('Lagerhaus',driver)
        ok(driver)

def Schritt2(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(8,driver)
        ok(driver)
        neuesgebäude('Lagerhaus',driver)
        ok(driver)

def Schritt3(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        neuesgebäude('Kaserne',driver)
        ok(driver)

def Schritt4(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)

def Schritt5(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)

def Schritt6(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
    print('nächster Schritt ist für 1 Hoplit')


def Schritt7(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Hoplit'],['1'],driver)
        ok(driver)
    print('Hoplit Packete holen und Barbaren anfangen')

def Schritt10(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(10,driver)
        ok(driver)
        Truppen(['Rammbock'],['12'],driver)
        ok(driver)
    print('12 Rammböcke Bauzeit 2h. Danach Barbaren weiter. Handelsschiffe auf 20 bringen.')

def Schritt11(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(8,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
    l = Gebäudestufe(driver)
    print('repeat bis Stufe 4. Aktuell:' + l[-1])

def Schritt12(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(9,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
    l = Gebäudestufe(driver)
    print('repeat bis Stufe 4. Aktuell:' + l[-1])

def Schritt13(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(19,driver)
        ok(driver)
        neuesgebäude('Statthaltersitz',driver)
        ok(driver)

def Schritt14(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(0,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
    l = Gebäudestufe(driver)
    print('repeat bis Stufe 3. Aktuell:' + l[-1])

def Handelsschiff(x,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(1,driver)
        ok(driver)
        Gebäude(1,driver)
        ok(driver)
        Hskaufen(x,driver)
        ok(driver)
        switch(2,driver)
        ok(driver)
