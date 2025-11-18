

print("\nDet har oppstått flere konflikter innad i gruppen, prosjektleder Erling må nå ta tak i disse for å sikre fremdrift i prosjektet.")
print("\nKonflikt 1: Hamdi og Jabir\nKonflikt 2: Silje og Sivert\nKonflikt 3: Noa og Hallgeir")

Konflikt = input("Skriv (1, 2 eller 3) for å velge hvilken konflikt du vil håndtere først: ")

# Konflikt 1: Hamdi og Jabir
def Ordne_konflikt_1():
    print("\nDu har valgt å håndtere konflikten mellom Hamdi og Jabir.")
    print("\nHamdi og Jabir er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter. Den dårlige steminingen har spred seg til alle i teamet! \nDet ser ut til at prototypen ikke blir klar til tiden")
    print ()
    print("1: Kalle inn til et felles møte med hele teamet.")
    print("2: Ikke involvere seg og avventer situasjonen.")
    valg = input("Hva velger du å gjøre? Skriv (1 eller 2): ")
    if valg == "1":
        print("\nErling kaller alle medlemmene i teamet inn til et felles møte, her får både Hamdi og Jabir høre meningene til de andre i teamet\nErling kommer med en løsning på problemet, Prototypen blir levert til fristen.")
    
    elif valg == "2":
        print("\nErling avventer situasjonen og håper problemene løser seg selv. Konflikten eskalerer og prototypen blir ikke ferdig til fristen.")
    else:
        print("\nUgyldig valg. Vennligst start på nytt og velg 1 eller 2.")

# Konflikt 2: Silje og Sivert
def Ordne_konflikt_2():
    print("\nDu har valgt å håndtere konflikten mellom Silje og Sivert.")
    print("\nSilje og Sivert er svært uenige om design og teknologivalget til innbyggerplattformen, de mener selvsagt at de selv har den beste løsningen.")
    print ()
    print("1: Kalle inn til et felles møte. De får begge presentere sine løsninger.")
    print("2: Holde samtaler med partene induviduelt, Erling bestemmer uten å dele dette videre med gruppen.")
    valg = input("Hva velger du å gjøre? Skriv (1 eller 2): ")
    if valg == "1":
        print("\nSituasjonen ender med et kompromiss etter en lang diskusjon i et felles møte.\n Prosjektet fortsetter igjen med orginal fremgangsplan.")
    elif valg == "2":
        print("\nSilje føler ingenting har endret seg, Sivert føler varslene ikke ble tatt på alvor.\nArbeidsmoralen svekkes, og Erling mister autoriteten! Prosjektet blir forsinket.")
    else:
        print("\nUgyldig valg. Vennligst start på nytt og velg 1 eller 2.")

# Konflikt 3: Noa og Hallgeir
def Ordne_konflikt_3():
    print("\nDu har valgt å håndtere konflikten mellom Noa og Hallgeir.")
    print("\nNoa og Hallgeir er uenige om hvordan innspill fra medborgerplatformen skal være.\nHallgeir vil ha åpenhet og tilgjengelighet, mens Noa er bekymret for personvern og datasikkerheten.")
    print ()
    print("1: Setter av tid til en felles konflikshåndteringsøkt med megling og en felles løsning.")
    print("2: Autoritær beslutning. Erling tar en sjefsavgjørelse.")
    valg = input("Hva velger du å gjøre? (1 eller 2): ")
    if valg == "1":
        print("\nErling bestemmer å seg for å invitere til en felles konfliktshåndteringsøkt, de finner en felles løsning - Et kompromiss.\nSamholdet og produktiviteten øker igjen.")
    elif valg == "2":
        print("\nErling er lei av diskusjoner i gruppen og tar en sjefsavgjøselse. Fremdriften øker, men bare på kort sikt.\nPrototypen leveres til tiden, men det kommer både etiske og juridiske probmlemer etter lanseringen.")
    else:
        print("\nUgyldig valg. Vennligst start på nytt og velg 1 eller 2.")


#Håndtering av de andre konfliktene uavhengig av hvilken som ble valgt først

if Konflikt == "1":
    Ordne_konflikt_1()
    neste = input("\nVil du gå videre til konflikt 2 eller 3?\n Skriv 2 eller 3: ")
    if neste == "2":
        Ordne_konflikt_2()
        print("\nNå gjenstår bare konflikt 3.")
        Ordne_konflikt_3()
        print ("Bra jobba! Du har nå løst alle konfliktene i gruppen, men ble alt bra?")

    elif neste == "3":
        Ordne_konflikt_3()
        print("\nNå gjenstår bare konflikt 2.")
        Ordne_konflikt_2()
        print ("Bra jobba! Du har nå løst alle konfliktene i gruppen, men ble alt bra?")

    else:
        print("\nDette er ikke et alternativ, velg 2 eller 3.")


elif Konflikt == "2":
    Ordne_konflikt_2()
    neste = input("\nVil du gå videre til konflikt 1 eller 3?\n Skriv 1 eller 3:")
    if neste == "1":
        Ordne_konflikt_1()
        print("\nNå gjenstår bare konflikt 3.")
        Ordne_konflikt_3()
        print ("Bra jobba! Du har nå løst alle konfliktene i gruppen, men ble alt bra?")

    elif neste == "3":
        Ordne_konflikt_3()
        print("\nNå gjenstår bare konflikt 1.")
        Ordne_konflikt_1()
        print ("Bra jobba! Du har nå løst alle konfliktene i gruppen, men ble alt bra?")

    else:
       print ("\nDette er ikke et alternativ, velg 1 eller 3.")

elif Konflikt == "3":
    Ordne_konflikt_3()
    neste = input("\nVil du gå videre til konflikt 1 eller 2?\n Skriv 1 eller 2:")
    if neste == "1":
        Ordne_konflikt_1()
        print("\nNå gjenstår bare konflikt 2.")
        Ordne_konflikt_2()
        print ("Bra jobba! Du har nå løst alle konfliktene i gruppen, men ble alt bra?")

    elif neste == "2":
        Ordne_konflikt_2()
        print("\nNå gjenstår bare konflikt 1.")
        Ordne_konflikt_1()
        print ("Bra jobba! Du har nå løst alle konfliktene i gruppen, men ble alt bra?")

    else:
        print("\nDette er ikke et alternativ, velg 1 eller 2.")

else:
    print("\nUgyldig valg. Vennligst start på nytt og velg 1, 2 eller 3.")