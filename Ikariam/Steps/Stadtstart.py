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
        Gebäude(1,driver)
        ok(driver)
        neuesgebäude('Handelshafen',driver)
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
        Gebäude(19,driver)
        ok(driver)
        neuesgebäude('Statthaltersitz',driver)
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
        neuesgebäude('Kaserne',driver)
        ok(driver)

def Schritt6(stadt,driverliste):
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
        ausbauen(driver)
        ok(driver)

def Schritt8(stadt,driverliste):
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


def Schritt9(stadt,driverliste):
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
        Gebäude(0,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)

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

def Schritt13(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(7,driver)
        ok(driver)
        neuesgebäude('Zimmerei',driver)
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
        Gebäude(7,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
    l = Gebäudestufe(driver)
    print('repeat bis Stufe 9. Aktuell:' + l)

def Schritt15(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(6,driver)
        ok(driver)
        neuesgebäude('Architekturbüro',driver)
        ok(driver)
    print('nächster Schritt baut Rammen')


def Schritt16(stadt,driverliste):
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
        Truppen(['Rammbock'],['6'],driver)
        ok(driver)
    print('6 Rammböcke Bauzeit 1h. Danach Barbaren weiter. Handelsschiffe auf 20 bringen.')

def Schritt17(stadt,driverliste):
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
    print('repeat bis Stufe 4. Aktuell:' + l)

def Schritt18(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(18,driver)
        ok(driver)
        neuesgebäude('Akademie',driver)
        ok(driver)
    print('nächster Schritt baut 50 Hopliten')

def Schritt19(stadt,driverliste):
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
        Truppen(['Hoplit'],['50'],driver)
        ok(driver)

def Schritt20(stadt,driverliste):
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
    print('repeat bis Stufe 4. Aktuell:' + l)

def Schritt21(stadt,driverliste):
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
    print('repeat bis Stufe 4. Aktuell:' + l)

def Schritt22(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(18,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
    l = Gebäudestufe(driver)
    print('repeat bis Stufe 6. Aktuell:' + l)

def Schritt23(stadt,driverliste):
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
        einstellen(['Forscher'],['43'],driver)
        ok(driver)

def Schritt24(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(16,driver)
        ok(driver)
        neuesgebäude('Taverne',driver)
        ok(driver)

def Schritt25(stadt,driverliste):
    for i in range(len(driverliste)):
        driver = driverliste[i]
        Tagesbelohnung(driver)
        ansicht('s',driver)
        Tagesbelohnung(driver)
        ok(driver)
        switch(stadt,driver)
        ok(driver)
        Gebäude(16,driver)
        ok(driver)
        ausbauen(driver)
        ok(driver)
    l = Gebäudestufe(driver)
    print('repeat bis Stufe 6. Aktuell:' + l)

def Schritt26(stadt,driverliste):
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
    print('repeat bis Stufe 9. Aktuell:' + l)
