print("\nDet har oppstått noen spenninger innad i prosjektgruppen."
      "\nErling står overfor tre konflikter som må håndteres: "
      "\n1 - Hamdi og Jabir"
      "\n2 - Silje og Sivert"
      "\n3 - Noa og Halvgeir" 
      "\n")

valg = input("Konflikt 1 - Hamdi og Jabir"
              "\nDe er uenige om hvor mye som faktisk kan ferdigstilles før tidsfristen, og stemningen i teamet er anspent."
              "\nHvordan bør Erling håndtere dette? (a) Kalle inn til et felles møte eller (b) Vente og se om situasjonen roer seg selv?"
              "\n")

if valg == "a":
    print("Erling bestemmer seg for å samle alle til en åpen samtale for å finne en løsning. Dette bidrar til mer åpenhet.")
elif valg == "b":
    print("Erling velger en mer tilbakelent tilnærming og håper at konflikten løser seg naturlig.\n")
else:
    print("Dette er ikke et gyldig alternativ.\n")



valg2 = input("Konflikt 2 - Silje og Sivert"
              "\nDe har sterke meninger om hvilket design og hvilke teknologier som skal brukes i medborgerportalen.\n"
              "\nHvordan bør Erling gripe dette an? (a) Ta det opp med hele gruppen eller (b) Ha én-til-én-samtaler med partene?\n"
              "\n")

if valg2 == "a":
    print("Erling velger å ta opp uenigheten i plenum for å styrke fellesskapet.\n")
elif valg2 == "b":
    print("Erling velger å snakke med hver enkelt individuelt for å forstå deres perspektiver bedre.\n")
else:
    print("Dette er ikke et gyldig alternativ.\n")


valg3 = input("Konflikt 3 - Noa og Halvgeir\n"
              "\nDe er sterkt uenige om hvordan innspill fra medborgerne skal implementeres.\n"
              "\nHva gjør Erling? (a) Gå inn som aktiv megler og finne en felles løsning eller (b) Ta en tydelig lederbeslutning for å sikre fremdrift?\n"
              "\n")

if valg3 == "a":
    print("Erling velger å megle aktivt mellom partene i håp om å skape bedre samhold.\n")
elif valg3 == "b":
    print("Erling tar en autoritær beslutning og overstyrer partene for å få prosjektet videre.\n")
else:
    print("Dette er ikke et gyldig alternativ.\n")

valg = [valg, valg2, valg3]
kombinasjon = "".join(valg)


if kombinasjon == "aaa":
    print("Erling valgte kun gode løsninger. Resultatet er et sterkt team og et prosjekt som blomstrer.")
elif kombinasjon in ["baa", "aba", "aab"]:
    print("Erling håndterte konfliktene godt, men noen konflikter oppstår")
elif kombinasjon in ["abb", "bba", "bab"]:
    print("Erling forsøkte å fikse opp i konfliktene men på grunn av dårlige valg gjenstår konfliktene")
elif kombinasjon == "bbb":
    print("Erling valgte å overse eller overstyre konfliktene. Tilliten i teamet svekkes, og prosjektet blir forsinket.")
else:
    print("Det ser ut til at et ugyldig valg ble gjort underveis.")
