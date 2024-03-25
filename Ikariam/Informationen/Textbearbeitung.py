def schreiben(y):
    
    datei = open('IkariamDaten.txt' , 'r')
    datei.close()
    x = datei.readlines()

    if y == 'Ress':
        l

    if y == 'Truppen':
        l

    if y == 'Schiffe':
        l

    if y == 'Forschung':
        l

    if y == 'Bürger':
        l

def leseK(Spieler, Typ):

    Dateik = open('Keeper.txt', 'r')
    lines = Dateik.readlines()
    Dateik.close()

    for i in range(len(lines)):
        if lines[i][:4] == '---' + str(Spieler):
            for j in range(len(lines[i:])):
                if lines[i+j][:len(Typ)+1] == '-' + Typ:
                    print(lines[i] + lines[i+j+1])
                    print()
                    break

def lesenK(Typ):
    for i in range(11):
        leseK(i,Typ)

def schreibenK(Spieler, Typ):
    Dateik = open('Keeper.txt','r')
    lines = Dateik.readlines()
    Dateik.close()
    Dateik = open('Keeper.txt','a')
    Dateik.write(str(lines))
    Dateik.close()
    return lines
