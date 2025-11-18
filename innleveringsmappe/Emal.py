# interaktive historie: Erling som prosjektleder
# IS-118 Innleveringoppgave 2 - del 2
# Laget av Emal Mir

print("Velkommen til prosjektet 'Medborgerskap'!")
print("Du er Erling, prosjektleder. Etter seks uker med innsats, står teamet ditt overfor flere utfordringer.")
print("Du må ta tre avgjørende valg som vil forme prosjektets videre utvikling.\n")

# Beslutning 1: Konflikt mellom Silje og Sivert
print("Beslutning 1: Silje og Sivert er i konflikt om teknologi og design.")
print("A) Ta det opp i plenum for å skape åpenhet og felles forståelse") 
print("B) Ha individuelle samtaler for å dempe tempraturen og forstå behovene")
valg1 = input("Hva velger du? (A/B): ")

# Beslutning 2: Spenning mellom Hamdi og Jabir
print("\nBeslutning 2: Hamdi og Jabir er uenige om hvordan digitale folkemøter skal organiseres.")
print("A) Kalle inn til felles møte for å avklare uenigheter og finne felles mål")
valg2= input("Hva velger du? (A/B): ")

# Beslutning 3: Bevare motivasjonen i teamet
print("\nBeslutning 3: Stemningen er spent. Hvordan beavarer du motivasjonen?")
print("A) Sette av tid til relasjonsbygging og sosiale aktiviteter for å styrke samholdet")
print("B) Prioritere fremdrift og leveranser for å holde fokus på resultatet")
valg3 = input("Hva velger du? (A/B): ")

# Evaluering av valg og utfall
print("\n--- Resultat ---")

if valg1 == "A" and valg2 == "A" and valg3 == "A": 
    print("Du har valgt åpenhet, samarbeid og relasjonsbygging. Temaet gjenoppretter tilit og går videre til norming-fasen.")
    print("Prosjektet leverer prototypen i tide, og engasjementet blant innbyggerne øker.")
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print("Du valgte å unngå direkte konfrontasjon og fokusere på leveranser.") 
    print("Prosjektet mister samhold, og flere teammedlemmer trekker seg. Prototypen blir forsinket.")
else:
    print("Du har forsøkt å balansere mellom relasjoner og fremdrift.")
    print("Konfliktene løses delvis, men noen sår gjenstår. Prosjektet går videre, men med redusert effektivitet.")

print("\nTakk for at du spilte gjennom historien, Erling!")