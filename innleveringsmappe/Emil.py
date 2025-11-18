#Konfliktløsning - Erling

print("\nDet har oppstått noen konflikter innadd i teamet."
      "\nDet er tre konflikter Erling må løse: "
      "\n-----------------------"
      "\n1 - Hamdi og Jabir"
      "\n2 - Silje og Sivert"
      "\n3 - Noa og Halvgeir"   
      "\n-----------------------")

valg1 = input("Konflikt 1 - Hamdi og Jabir"
              "\nDet er uenighet med hva de klarer å gjøre før tidsfristen, og nå er det stor spenning innad i hele teamet."
              "\nHvordan skal Erling løse dette?"
              "\n1) - Kalle inn til et felles"
              "\n2) - Avvente og håpe det ordner seg"
              "\n")
if valg1 == "1":
    print("Erling valge å starte en åpen diskusjon for å løse problemet. Dette skaper åpenhet.")
elif valg1 == "2":
    print("Erling valgte å gå litt mer passivt, avvente og håper det order seg")
else:
    print("Dette er ikke et alternativ.")
    exit()

print("---------------------------------------------------------------------------------------------")

valg2 = input("Konflikt 2 - Silje og Sivert"
              "\nDe har funnet stor uenighet innenfor design og teknologivalget som forventes å brukes i den digitale medborgerportalen."
              "\nHvordan skal Erling løse dette?"
              "\n1) - Ta det opp i plenum"
              "\n2) - Ta individuelle samtaler"
              "\n")
if valg2 == "1":
    print("Erling velger å ta konflikten opp i forsamling, dette kan skape fellesskap")
elif valg2 == "2":
    print("Erling velger å ta individuelle samtaler med hver enkelt av dem, dette kan bli mer personlig.")
else:
    print("Dette er ikke et alternativ")
    exit()

print("---------------------------------------------------------------------------------------------")

valg3 = input("Konflikt 3 - Noa og Halvgeir"
              "\nNoa og Hallgeir er svært uenige om løsningen rundt innspill fra medborgerene."
              "\nHvordan skal Erling løse dette?"
              "\n1) - Aktiv konfliktmegling og finn en felles løsning"
              "\n2) - Autoritær beslutning og fokus på fremdrift?"
              "\n")
if valg3 == "1":
    print("Erling velger å kjøre en strukturert konfliktløsningsøkt. Samholdet kan økes.")
elif valg3 == "2":
    print("Erling velger å bruke makten sin og overkjører partene i håp om at dette funker.")
else:
    print("Dette er ikke et alternativ.")
    exit()
    
print("\n=====================================Resultatet=======================================")

slutt1 = "Etter å ha gått igjennom alle tre konfliktene styrkes samarbeidet mellom alle partene."
slutt2 = "Etter å ha gått igjennom alle tre konfliktene blir problemene delvis løst."
slutt3 = "Etter å ha gått igjennom alle tre konfliktene blir prosjektet forsinket."

#Bruker resultatene fra de tre konfliktene for å få et felles utfall
if valg1 == "1" and valg2 == "1" and valg3 == "1":
    print(slutt1)
elif valg1 == "2" and valg2 == "2" and valg3 == "2":
    print(slutt3)
elif valg1 == "1" and valg2 == "2" and valg3 == "2":
    print(slutt2)
elif valg1 == "1" and valg2 == "2" and valg3 == "1":
    print(slutt1)
elif valg1 == "2" and valg2 == "1" and valg3 == "1":
    print(slutt3)
elif valg1 == "2" and valg2 == "1" and valg3 == "2":
    print(slutt2)
elif valg1 == "2" and valg2 == "2" and valg3 == "1":
    print(slutt1)
elif valg1 == "1" and valg2 == "1" and valg3 == "2":
    print(slutt3)
else:
    print("Dette er ikke et alternativ.")

print("=======================================Slutt==========================================")