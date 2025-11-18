#Eivind Bentsen 

#Intro til oppgaven
print("\nHei, Erling trenger din hjelp med å ta enkelte beslutninger for å løse ulike situasjoner som oppstår under han sin ledelse, nærmere bestemt konflikthåndteringer. Dette trenger han og teamet for å fullføre prosjektet der de skal ferdigstille en prototype innen en tidsfrist. ")

#Variabler for løsning A og B
løsning1 = "a"
løsning2 = "b"
utfallsPoeng = 0

#Første situasjon
print("\n---------Situasjon 1---------")
print("Det har oppstått konflikter innad i teamet til Erling mellom Hamdi og Jabir. I tillegg ser det ut som at prototypen ikke er klar innen fristen. ")
print("Hva skal Erlig gjøre for å løse dette problemet? ")
print("\nDet står mellom to løsninger: ")
print("\n---A---: Kalle inn til et felles møte med hele teamet hvor alle deler sine problemer." ,
    "Deretter diskutere og analysere hva man kan gjøre for å finne en løsning som er god for alle parter. ")
print("---B---: Avvente dette møte, og håpe på at de klarer å finne ut av situasjonen. ")

#Her kan brukeren skrive enten A eller B, ettersom hvilken løsning som bruker tror er best. 
valg1 = input("\nSkriv A dersom du tenker at løsning A er best, eller skriv B dersom du tenker at løsning B er mest optimal: ").lower()

#Hvis valget til brukeren tilsvarer "løsning1" eller "løsning2" vil bruker få en tilbakemelding på valget. Dersom det står noe annet enn A (a) eller B (b) så vil svaret være ugyldig.
print("\n-------Tilbakemelding-------")
if valg1 == løsning1:
    print("Flott! Det ser ut til at Hamdi og Jabir har kommet til en enighet, slik at problemet er løst, og prototypen er klar innenfor fristen. ")
    utfallsPoeng += 1
elif valg1 == løsning2:
    print("Huff! Denne løsningen ser ikke ut til å funke. Stemningen innad i teamet er ikke god, og prototypen er ikke klar innenfor fristen. ")
else:
    print("Ditt svar er ugyldig. Det du skrev inn tilsvarer verken løsning A eller B. ")

#Andre situasjon
print("\n---------Situasjon 2---------")
print("En ny konflikt har oppståt i teamet, men nå mellom IT-rådgiver Sivert og UX-designer Silje. De er uenige angående bruk av design og teknologivalg i den digitale medborgerportalen. ", 
      "Silje er motivert til å drive kreative løsninger med et dynamisk design, mens Sivert mener det kan bli for komplekst og risikabelt med tanke på kostnad og teknisk stabilitet . ")
print("Hva skal Erlig gjøre for å forhindre at samarbeidet mellom dem går i oppløsning? ")
print("\nDet står mellom to løsninger: ")
print("\n---A---: Erling tar opp konflikten i åpen forsamling slik at flere fra prosjektgruppen kan dele sine formeninger fra sitt faglige ståsted. ",
       "Slik får gruppen en mer helhetelig forståelse til å ta en beslutning. ")
print("---B---: Erling diskuterer dette med Silje og Sivert via individuelle samtaler. Med forståelse fra demmes standpunkt forsøker han å endre arbeidsplanen for å balansere mellom begge sine syn. ",
      "Han går ikke i detaljer om konflikten i plenum, og gir bare beskjed om at konflikten er håndtert. ")

#Her kan brukeren skrive enten A eller B, ettersom hvilken løsning som bruker tror er best. 
valg2 = input("\nSkriv A dersom du tenker at løsning A er best, eller skriv B dersom du tenker at løsning B er mest optimal: ").lower()

#Hvis valget til brukeren tilsvarer "løsning1" eller "løsning2" vil bruker få en tilbakemelding på valget. Dersom det står noe annet enn A (a) eller B (b) så vil svaret være ugyldig.
print("\n-------Tilbakemelding-------")
if valg2 == løsning1:
    print("Godt valg! Løsningen førte til et kompromiss mellom Silje og Sivert hvor ingen fikk sin fulle vlije, men konflikten er løst og prosjektet fortsetter. ")
    utfallsPoeng += 1
elif valg2 == løsning2:
    print("Offf! Dette ledet til usikkerhet i gruppen. Etter en stund føler Silje og Sivert at frustrasjonen til deres konflikt har bygget seg opp igjen. Ingen ble tatt på alvor. ",
          "Prosjektet er nå forsinket grunnet dårligere arbeidsmoral og Erling sin autoritet er svekket som følge av kommunikasjonsproblemer. ")
else:
    print("Ditt svar er ugyldig. Det du skrev inn tilsvarer verken løsning A eller B. ")

#Tredje situasjon
print("\n---------Situasjon 3---------")
print("Nå begynner individene i gruppen å føle på tidspress. Innen tre uker skal prototypen være ferdigstilt. Utenkelig nok har det oppstått en ny konflikt oppi det hele. ", 
      "Denne gangen er det Noa og Hallgeir som er uenig om hvordan innspill fra medborgerene skal håndteres. Hallgeir ønsker å ha åpenhet og tilgjengelighet, mens Noa er bekymret for personvernet og datasikkerheten. ")
print("Hvordan burde Erling håndtere denne konflikten? ")
print("\nDet står mellom to løsninger: ")
print("\n---A---: Erling setter opp et konfliktløsningsmøte, og alle i teamet er pliktig til å delta. Noa og Hallgeir får muligheten til å legge frem sine prespektiver på saken, og gruppen finner en kompromissløsning. ")
print("---B---: Erling er sterkt resulatfokusert og lei av diskusjoner i gruppen, slik at han nedtoner konflikten uten videre diskusjon og fokuserer på å ferdigstille produktet. ",
      "Han gir videre beskjed til Noa om å tilpasse sikkerhetsløsningen mot Hallgeirs ønske, noe Noa er svært uenig i. ")

#Her kan brukeren skrive enten A eller B, ettersom hvilken løsning som bruker tror er best. 
valg3 = input("Skriv A dersom du tenker at løsning A er best, eller skriv B dersom du tenker at løsning B er mest optimal: ").lower()

#Hvis valget til brukeren tilsvarer "løsning1" eller "løsning2" vil bruker få en tilbakemelding på valget. Dersom det står noe annet enn A (a) eller B (b) så vil svaret være ugyldig.
print("\n-------Tilbakemelding-------")
if valg3 == løsning1:
    print("Hurra! Nå har produktiviteten økt, samholdet har blitt styrket og gruppen har lært å håndtere uenigheter på en konstruktiv måte. ", 
          "Ikke minst har prototypen blitt utivklet nå med en balasnert løsning som tar inkluderer både personvern og åpenhet. ")
    utfallsPoeng += 1
elif valg3 == løsning2:
    print("Buuu! Selv om Erling sin dominans til å ta en slik brutal sjefsavgjørelse førte til at framdriften var god nok til å levere prototypen på tide, kom det etiske og jurudiske utfordringer etter leveransen. ")
else:
    print("Ditt svar er ugyldig. Det du skrev inn tilsvarer verken løsning A eller B. ")

print("\n----------Resultat----------")

#Her får brukeren vite hvordan prosjektet gikk helhetlig
if utfallsPoeng == 1:
    print("Prosjektet ble gjennomført, men med store utfordringer. Prosjektgruppen leverte en prototype, men på bekostning av at gruppen mistet motivasjon og tillit til hverandre og Erling blir nå uglesett av medlemene. Han har lært at tidlig konflikthåndtering er avgjørende. ")
elif utfallsPoeng == 2:
    print("Prosjektet ble levert med godkjent resultat. Selv om en av konfliktene påvirket fremdriften, klarte Erling å håndtere de fleste utfordringene. Teamet har fått verdifull erfaring i samarbeid og konflikthåndtering. ")
elif utfallsPoeng == 3:
    print("Gratulerer! Prosjektet ble gjennomført med suksess. Prototypen ble levert før fristen, teamet jobbet effektivt sammen, og Erling har styrket sin rolle som en trygg og inkluderende leder. ")
else:
    print("Beklager! Prosjektet kom ikke i mål da prototypen ikke ble levert før fristen. Samarbeidet var preget av konflikt og lav trivsel. Erling endte opp med å miste sin rolle som leder.")