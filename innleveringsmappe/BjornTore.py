#IS118 - GRUPPEINNLEVERING 2 (25/11/2025)

#Erklærer variablene
valg_1 = None
valg_1A = None
valg_1B = None
valg_1C = None
valg_2 = None
valg_2A = None
valg_2B = None
valg_2C = None
valg_3 = None
valg_3A = None
valg_3B = None
valg_3C = None

#Valg 1
print("----------------------------------------------------------------------------------------------------")
print("\nEn konflikt har oppstått, og Erling må velge mellom hvordan å løse konflikt a, b og c:"
      "\n(a) - Hamdi og Jabir"
      "\n(b) - Silje og Sivert"
      "\n(c) - Noa og Halvgeir")
valg_1 = input("\n Hva skal han velge først? (a, b, c)")
print("\n -------------------------------------------------------------------------------------------------")
if valg_1 == "a" or valg_1 == "1":
    print("\n Han velger konflikt A: Uenighet har oppstått om med hva de klarer å gjøre før tidsfristen, og det har skapt stor spenning i hele teamet.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta det opp i plenum.")
    print("\n 2. Avvente situasjonen")
    valg_1A = input("\n 1 eller 2?")
    if valg_1A == "1" or valg_1A == "a":
        print("\n Han valgte løsning 1, situasjonen løses og prosjektet fortsetter som vanlig")
    elif valg_1A == "2" or valg_1A == "b":
        print("\n Han valgte løsning 2, situasjonen eskalerer og prototypen er ikke lenger klar før fristen")
    else: raise ValueError("Det er ikke et tilgjengelig valg.")

elif valg_1 == "b" or valg_1 == "2":
    print("\n Han velger konflikt B: Det har oppstått store uenigheter innenfor hvilket design som forventes å brukes innenfor den digitale medborgerportalen.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta det opp i plenum.")
    print("\n 2. Ta det opp privat med Silje og Sivert, hver for seg.")
    valg_1B = input("\n 1 eller 2?")
    if valg_1B == "1" or valg_1B == "a":
        print("\n Han valgte løsning 1, situasjonen løser seg, prosjektet fortsetter som normalt og kommunikasjonen i gruppa styrker seg.")
    elif valg_1B == "2" or valg_1B == "b":
        print("\n Han valgte løsning 2, kommunikasjonen i gruppa forverrer seg, og moral svekkes. Prototypen blir forsinket, og lederrollen din svekkes.")
    else: raise ValueError("Dette er ikke et tilgjengelig valg")

elif valg_1 == "c" or valg_1 == "3":
    print("\n Han velger konflikt C: Noa og Hallgeir er svært uenige om hvordan de skal løse situasjonene rundt innspill fra medborgere.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta en konfliktsløsningsøkt med alle i gruppa.")
    print("\n 2. Ta en rask, egen beslutning uten kommunikasjon med resten av gruppa.")
    valg_1C = input("1 eller 2?")
    if valg_1C == "1" or valg_1C == "a":
        print("\n Han valgte løsning 1, situasjonen løser seg, samarbeidsevnen og samholdet i gruppen styrker seg.")
    elif valg_1C == "2" or valg_1C == "b":
        print("\n Han valgte løsning 2, det blir lavere motivasjon og tillitt i gruppen, men prototypen blir fortsatt levert i tide.")
    else: raise ValueError("Det er ikke et tilgjengelig valg.")
else: raise ValueError("\n Det valget finnes ikke.")

# Valg 2
print("\n====================================================================================================")
valg_2 = None
if valg_1 == "a" or valg_1 == "1":
    print("\nEtt av konfliktene har blitt håndtert")
    valg_2 = input("Hva velger han nå? (b eller c) ")
elif valg_1 == "b" or valg_1 == "2":
    print("\nEtt av konfliktene har blitt håndtert")
    valg_2 = input("Hva velger han nå? (a eller c) ")
elif valg_1 == "c" or valg_1 == "3":
    print("\nEtt av konfliktene har blitt håndtert")
    valg_2 = input("Hva velger han nå? (a eller b) ")
print("\n ------------------------------------------------------------")

if valg_2 == valg_1:
    raise ValueError("Han har allerede gjennomgått dette valget. Prøv igjen.")
if valg_2 == "a" or valg_2 == "1":
    print("\n Han velger konflikt A: Uenighet har oppstått om med hva de klarer å gjøre før tidsfristen, og det har skapt stor spenning i hele teamet.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta det opp i plenum.")
    print("\n 2. Avvente situasjonen")
    valg_2A = input("\n 1 eller 2?")
    if valg_2A == "1" or valg_2A == "a":
        print("\n Han valgte løsning 1, situasjonen løses og prosjektet fortsetter som vanlig")
    elif valg_2A == "2" or valg_2A == "b":
        print("\n Han valgte løsning 2, situasjonen eskalerer og prototypen er ikke lenger klar før fristen")
    else: raise ValueError("Det er ikke et tilgjengelig valg.")

elif valg_2 == "b" or valg_2 == "2":
    print("\n Han velger konflikt B: Det har oppstått store uenigheter innenfor hvilket design som forventes å brukes innenfor den digitale medborgerportalen.")
    print("\n Velger Han å løse konflikten ved å:")
    print("\n 1. Ta det opp i plenum.")
    print("\n 2. Ta det opp privat med Silje og Sivert, hver for seg.")
    valg_2B = input("\n 1 eller 2?")
    if valg_2B == "1" or valg_2B == "a":
        print("\n Han valgte løsning 1, situasjonen løser seg, prosjektet fortsetter som normalt og kommunikasjonen i gruppa styrker seg.")
    elif valg_2B == "2" or valg_2B == "b":
        print("\n Han valgte løsning 2, kommunikasjonen i gruppa forverrer seg, og moral svekkes. Prototypen blir forsinket, og lederrollen din svekkes.")
    else: raise ValueError("Det er ikke et tilgjengelig valg.")

elif valg_2 == "c" or valg_2 == "3":
    print("\n Han velger konflikt C: Noa og Hallgeir er svært uenige om hvordan de skal løse situasjonene rundt innspill fra medborgere.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta en konfliktsløsningsøkt med alle i gruppa.")
    print("\n 2. Ta en rask, egen beslutning uten kommunikasjon med resten av gruppa.")
    valg_2C = input("1 eller 2?")
    if valg_2C == "1" or valg_2C == "a":
        print("\n Han valgte løsning 1, situasjonen løser seg, samarbeidsevnen og samholdet i gruppen styrker seg.")
    elif valg_2C == "2" or valg_2C == "b":
        print("\n Han valgte løsning 2, det blir lavere motivasjon og tillitt i gruppen, men prototypen blir fortsatt levert i tide.")
    else: raise ValueError("Det er ikke et tilgjengelig valg.")
else: raise ValueError("\n Det valget finnes ikke.")

# Valg 3
print("\n=================================================================================================")
valg_3 = None
if (valg_1 == "a" and valg_2 == "b") or (valg_1 == "b" and valg_2 == "a"):
    print("To av konfliktene har blitt håndtert")
    valg_3 = input("Han har ett valg igjen: (c) ")
elif (valg_1 == "a" and valg_2 == "c") or (valg_1 == "c" and valg_2 == "a"):
    print("To av konfliktene har blitt håndtert")
    valg_3 = input("Han har ett valg igjen: (b) ")
elif (valg_1 == "b" and valg_2 == "c") or (valg_1 == "c" and valg_2 == "b"):
    print("To av konfliktene har blitt håndtert")
    valg_3 = input("Han har ett valg igjen: (a) ")
print("\n --------------------------------------------------------------------------------------------------")

if valg_3 == valg_1 or valg_3 == valg_2:
    raise ValueError("Han har allerede gjennomgått dette valget. Prøv igjen.")
if valg_3 == "a" or valg_3 == "1":
    print("\n Han velger konflikt A: Uenighet har oppstått om med hva de klarer å gjøre før tidsfristen, og det har skapt stor spenning i hele teamet.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta det opp i plenum.")
    print("\n 2. Avvente situasjonen")
    valg_3A = input("\n 1 eller 2?")
    if valg_3A == "1" or valg_3A == "a":
        print("\n Han valgte løsning 1, situasjonen løses og prosjektet fortsetter som vanlig")
    elif valg_3A == "2" or valg_3A == "b":
        print("\n Han valgte løsning 2, situasjonen eskalerer og prototypen er ikke lenger klar før fristen")
    else: raise ValueError("Det er ikke et tilgjengelig valg. Uffda..")

elif valg_3 == "b" or valg_3 == "2":
    print("\n Han velger konflikt B: Det har oppstått store uenigheter innenfor hvilket design som forventes å brukes innenfor den digitale medborgerportalen.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta det opp i plenum.")
    print("\n 2. Ta det opp privat med Silje og Sivert, hver for seg.")
    valg_3B = input("\n 1 eller 2?")
    if valg_3B == "1" or valg_3B == "a":
        print("\n Han valgte løsning 1, situasjonen løser seg, prosjektet fortsetter som normalt og kommunikasjonen i gruppa styrker seg.")
    elif valg_3B == "2" or valg_3B == "b":
        print("\n Han valgte løsning 2, kommunikasjonen i gruppa forverrer seg, og moral svekkes. Prototypen blir forsinket, og lederrollen din svekkes.")
    else: raise ValueError("Det er ikke et tilgjengelig valg.")

elif valg_3 == "c" or valg_3 == "3":
    print("\n Han velger konflikt C: Noa og Hallgeir er svært uenige om hvordan de skal løse situasjonene rundt innspill fra medborgere.")
    print("\n Velger han å løse konflikten ved å:")
    print("\n 1. Ta en konfliktsløsningsøkt med alle i gruppa.")
    print("\n 2. Ta en rask, egen beslutning uten kommunikasjon med resten av gruppa.")
    valg_3C = input("1 eller 2?")
    if valg_3C == "1" or valg_3C == "a":
        print("\n Han valgte løsning 1, situasjonen løser seg, samarbeidsevnen og samholdet i gruppen styrker seg.")
    elif valg_3C == "2" or valg_3C == "b":
        print("\n Han valgte løsning 2, det blir lavere motivasjon og tillitt i gruppen, men prototypen blir fortsatt levert i tide.")
    else: raise ValueError("Det er ikke et tilgjengelig valg.")
else: raise ValueError("\n Det valget finnes ikke.")
print("\n---------------------------------------------------------------------------")

#slutt
print("=================== OPPSUMMERING =======================")
#Dersom du svarer "2" på c, men "1" på a og b:
if (((valg_1 == "c" and valg_1C == "2") or (valg_2 == "c" and valg_2C == "2") or (valg_3 == "c" and valg_3C == "2")) and
    (((valg_1 == "a" and valg_1A == "1") or (valg_2 == "a" and valg_2A == "1") or (valg_3 == "a" and valg_3A == "1")) and
     ((valg_1 == "b" and valg_1B == "1") or (valg_2 == "b" and valg_2B == "1") or (valg_3 == "b" and valg_3B == "1")))):
    print("Alle situasjonene har blitt håndtert, med noe negativt utfall.")
#Dersom du svarer "2" på a eller b, "2" på a og c, "2" på b og c, "2" på a, b og c:
elif (valg_1A == "2" or valg_1B == "2" or valg_1C == "2" or
      valg_2A == "2" or valg_2B == "2" or valg_2C == "2" or
      valg_3A == "2" or valg_3B == "2" or valg_3C == "2"):
    print("Alle situasjonene har blitt håndtert, men prosjektet har blitt forsinket...")
#Dersom du svarer "1" på a, b og c.
else: print("Alle situasjonene har blitt håndtert, og løste seg uten negative utfall.")
