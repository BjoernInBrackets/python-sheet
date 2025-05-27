class Sportlane:
    def __init__(self, nimi, kaal):
        # Konstruktor: seadistab sportlase nime ja kaalu
        self.nimi = nimi             
        self.kaal = kaal
        
    def __str__(self):
        # Tagastab objekti tekstilise kujutise printimiseks
        return "Nimi: " + self.nimi + ", kaal: " + str(self.kaal) + " kg"


class Maadleja(Sportlane):
    def __init__(self, nimi, kaal):
        # Kutsub baasklassi konstruktorit, et seadistada nimi ja kaal
        super().__init__(nimi, kaal)
        # Määrame automaatselt kaalukategooria kaalu alusel
        if   kaal <= 55:
            self.kaalukategooria = "kärbsekaal"
        elif kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        else:
            self.kaalukategooria = "raskekaal"
        
    def muuda_kaalu(self, uus_kaal):
        # Uuendab maadleja kaalu ja arvutab kategooria uuesti
        self.kaal = uus_kaal
        
        if   uus_kaal <= 55:
            self.kaalukategooria = "kärbsekaal"
        elif uus_kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif uus_kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif uus_kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        else:
            self.kaalukategooria = "raskekaal"
        
    def __str__(self):
        # Laiendab stringiesitust ka kaalukategooriaga
        return (
            "Nimi: " + self.nimi +
            ", kaal: " + str(self.kaal) + " kg, " +
            "kaalukategooria: " + self.kaalukategooria
        )
    

# Näide klasside kasutamisest:

sportlane = Sportlane("Indrek", 105)
print(sportlane)  
# Väljastab: Nimi: Indrek, kaal: 105 kg

maadleja1 = Maadleja("Georg", 83)
print(maadleja1)  
# Väljastab: Nimi: Georg, kaal: 83 kg, kaalukategooria: keskkaal

maadleja2 = Maadleja("Kristjan", 115)
print(maadleja2)  
# Väljastab: Nimi: Kristjan, kaal: 115 kg, kaalukategooria: raskekaal

# Muudame Kristjani kaalu ja arvutame kategooria uuesti
maadleja2.muuda_kaalu(95)
print()          
print(maadleja2)  
# Nüüd: Nimi: Kristjan, kaal: 95 kg, kaalukategooria: poolraskekaal






class Tont:
    def __init__(self, nimi, vanus, elukoht):
        # Konstruktor, mis seab iga uue Tont-objekti põhiväljad
        self.nimi = nimi               # Tont’i nimi
        self.vanus = vanus             # Tont’i vanus
        self.elukoht = elukoht         # Tont’i elukoht
        
    def kummita(self):
        # Meetod, mis tagastab sõnumi: kes kummitab ja kus
        return self.nimi + " kummitab elukohas " + self.elukoht + "!"

    def __str__(self):
        # Eriline meetod, mis määrab objekti tekstilise esituse printimisel
        return (
            "Nimi: " + self.nimi +
            ", Vanus: " + str(self.vanus) +
            ", Elukoht: " + self.elukoht
        )
    

class Võlur(Tont):
    def __init__(self, nimi, vanus, elukoht, nõiu):
        # Kutsub baasklassi Tont konstruktorit, et initsialiseerida
        # nimi, vanus ja elukoht
        super().__init__(nimi, vanus, elukoht)
        self.nõiu = nõiu             # Täiendav väli: kellele nõidus tehti
        
    def nõidus(self):
        # Meetod, mis kirjeldab nõiduse kasutamist
        return (
            self.nimi + " pani nõiduse, millega sai pihta " +
            self.nõiu + "!"
        )
        
        
# Näited klasside kasutamisest:

tont = Tont("Norbert", 31, "Tartu")
print(tont)             # Printerdatakse __str__ meetodi tagastus
print(tont.kummita())   # Printerdame kummitusteate

võlur1 = Võlur("Harry", 17, "Tartu", "Snape")
võlur2 = Võlur("Snape", 35, "Tartu", "")

print(võlur1)           # Võluvägi esineb ka __str__ meetodis
print(võlur2)
print(võlur1.nõidus()) # Näitab, kuidas Võlur kasutab nõidust





def loe_failist(fail):
    # Määran tühja listi, kuhu salvestan iga rea alusel autoandmed
    autod = []
    # Avan faili lugemiseks UTF-8 kodeeringus
    with open(fail, "r", encoding="utf-8") as f:
        for rida in f:
            # Eemaldan reavahetuse ja tühikud rea algusest ja lõpust
            rida = rida.strip()
            # Jagaan rea semikoolonite alusel osadeks: mark ja kuluväärtused
            osad = rida.split(";")
            # Esimene osa on autobränd
            automark = osad[0]
            # Ülejäänud osad teisendan float-väärtusteks kütusekulu jaoks
            kütusekulu = [float(x) for x in osad[1:]]
            # Lisan koos marki ja kütusekuludega ühe kirje listi
            autod.append([automark] + kütusekulu)
        # Tagastan valminud kahemõõtmelise listi autode andmetega
        return autod
            
            

def arvuta_keskmine(autod, automark):
    # Läbin iga auto kirje listis
    for auto in autod:
        # Kui marki vastav kirje on leitud
        if auto[0] == automark:
            # Võtan välja ainult kütusekulude listi
            kulud = auto[1:]
            # Kui kulude list on tühi, tagastan 0.0
            if not kulud:
                return 0.0
            # Arvutan keskmise summa jagatuna arvude arvuga
            return sum(kulud) / len(kulud)
    # Kui automarki ei leidu, tagastan 0.0
    return 0.0
          

def main():
    # Küsin kasutajalt faili nime
    failinimi = input("Sisesta faili nimi: ")
    # Loe failist autode andmed
    autod = loe_failist(failinimi)
    # Küsin keskmise künnise väärtuse float-na
    lävend = float(input("Sisesta kütusekulu lävend: "))
    
    # Prindi autod, mille keskmine kütusekulu on vähemalt lävend
    print("Lävendi ületanud autod:")
    for auto in autod:
        automark = auto[0]
        keskmine = arvuta_keskmine(autod, automark)
        if keskmine >= lävend:
            print(f"{automark}: {keskmine:.2f}")
    
    # Leia auto, millel on väikseim keskmine kütusekulu
    v_am = None          # hoiab automarki
    v_kk = float('inf')  # hoiab väikseimat keskmist, algul lõpmatu
    for auto in autod:
        automark = auto[0]
        keskmine = arvuta_keskmine(autod, automark)
        # Kui leitud keskmine on väiksem kui seni leitud
        if keskmine < v_kk:
            v_kk = keskmine
            v_am = automark
    # Kui vähemalt üks auto oli listis
    if v_am is not None:        
        print(f"Vähima keskmise kütusekuluga auto on {v_am}: {v_kk:.2f} liitrit 100 km kohta.")
    

if __name__ == "__main__":
    # Käivitan main-funktsiooni, kui skript on otse käivitatud
    main()







def juurdekasv(rida, a_juurdekasv):
    # Funktsioon arvutab metsapinna juurdekasvu põhinedes
    # rea väärtusel (aakrite arv) ja aastasel juurdekasvul
    # teisendab aakrid hektariteks (1 aakr ≈ 0.4047 ha),
    # korrutab aastase juurdekasvu hektari kohta
    # ning ümardab tulemuse kahe komakohani.
    answer = round(rida * 0.4047 * a_juurdekasv, 2)
    return answer  # Tagastame arvutatud väärtuse

def main():
    # Küsi kasutajalt faili nime, kust lugeda aakrite andmed
    fail = str(input("Sisesta failinimi: "))
    # Loendur, mis hakkab lugema, mitu metsatükki arvesse võetakse
    arvesse = 0
    # Küsi kasutajalt aastane juurdekasv hektari kohta (tihumeetrites)
    a_juurdekasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
    # Küsi piirväärtus: ainult suuremad metsatükid kui antud aakripiir arvesse võtta
    piir = int(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

    # Ava fail lugemiseks UTF-8 kodeeringus
    with open(fail, "r", encoding="utf-8") as file:
    
        # Itereerime läbi iga rea failis
        for rida in file:
            # Eemalda reavahetus ja üleliigsed tühikud
            rida = rida.strip()
            # Konverteeri rida stringist ujukomaarvuks
            rida = float(rida)
            if rida > piir:
                # Arvuta juurdekasv ja prindi tulemus
                print(juurdekasv(rida, a_juurdekasv))
                # Suurenda arvesse-võetud tükkide loendurit
                arvesse += 1
            else:
                print("Metsatükki ei võeta arvesse")
        
    print(f"Võeti arvesse {arvesse} metsatükki")
                
if __name__ == "__main__":
    main()


```python
def lugemise_aeg(lk_arv, kirjasuurus):
    """
    Arvutab lugemiseks kuluva aja sekundites antud
    lehekülgede arvu ja kirjastiili suuruse põhjal.
    """
    if kirjasuurus == "väike":
        # Väikese kirjastiili puhul kulub 40 sekundit lehekülje lugemiseks
        return lk_arv * 40
    elif kirjasuurus == "keskmine":
        # Keskmise kirjastiili puhul kulub 30 sekundit lehekülje lugemiseks
        return lk_arv * 30
    elif kirjasuurus == "suur":
        # Suure kirjastiili puhul kulub 20 sekundit lehekülje lugemiseks
        return lk_arv * 20
    else:
        # Kui sisend ei vasta ühelegi eeldatud kirjastiili suurusele,
        # tagastame 0 (või võiks tõsta erandi)
        return 0


def main():
    # Küsi kasutajalt faili nime, kus on reas üks raamatu lehekülgede arv
    fail = input("Sisesta faili nimi: ")
    kokku = 0  # Muutuja lugemisele kuluvate sekundite summaks

    # Avame faili ja tagame, et see suletakse automaatselt pärast lugemist
    with open(fail, "r", encoding="utf-8") as f:
        for rida in f:
            # Eemaldame rea algusest ja lõpust tühikud ning reavahetuse
            rida = rida.strip()
            if not rida:
                # Jätame tühjad read vahele
                continue

            # Teisendame loetud rea täisarvuks (lehekülgede arv)
            lk_arv = int(rida)

            # Küsimus kasutajalt, millise suurusega on raamatu kirjasuurus
            kirjasuurus = input(f"Raamat on {lk_arv} lk. Kui suur on kirjastiil (väike/keskmine/suur)? ")

            # Lisame selle raamatu lugemisele kuluva aja koguajale
            kokku += lugemise_aeg(lk_arv, kirjasuurus)

    # Arvutame koguse sekunditest ümber tundideks, minutiteks ja sekunditeks
    total_seconds = kokku
    tunnid = total_seconds // 3600
    ülejäänud = total_seconds % 3600
    minutid = ülejäänud // 60
    sekundid = ülejäänud % 60

    # Väljastame kokkuvõtte lugemisajast
    print(f"Kokku kulub raamatute lugemiseks {tunnid} tundi, {minutid} minutit ja {sekundid} sekundit.")


if __name__ == "__main__":
    main()
```

def loe_seis(fail):
    """
    Loeb faili, kus iga reas on: Nimi p1 p2 p3 …
    Tagastab sõnastiku kujul {nimi: [p1, p2, p3, …], …}.
    """
    seis = {}
    with open(fail, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()           # eemalda tühikud ja reavahetus
            if not rida:
                continue                  # jäta tühjad read vahele

            osad = rida.split()           # jagame nimeks ja punktideks
            nimi = osad[0]                # esimene osa = mängija nimi
            # ülejäänud osad teisendame täisarvudeks ja salvestame listi
            punktid = [int(x) for x in osad[1:]]  
            seis[nimi] = punktid          # lisa sõnastikku
    return seis


def lisa_tulemus(nimi, seis, tulemus):
    """
    Lisab mängijale `nimi` sõnastikus `seis` uue punktisumma `tulemus`.
    """
    if nimi in seis:
        seis[nimi].append(tulemus)     # lisa listi lõppu
        print(f"Tulemus lisatud: {nimi} → {seis[nimi]}")
    else:
        print("Sellist mängijat ei ole sõnastikus!")


def leia_keskmine(nimi, seis):
    """
    Arvutab ja tagastab mängija `nimi` keskmise skoori sõnastikus `seis`.
    """
    punktid = seis.get(nimi)
    if not punktid:
        print("Mängijat pole!")        # turvalisus, kui nimi puudub
        return None
    # Keskmine = punktide summa jagatud arvu elementidega
    return sum(punktid) / len(punktid)


def leia_parim(seis):
    """
    Leiab ja väljastab mängija, kellel on suurim keskmine skoor.
    """
    if not seis:
        print("Andmed puuduvad.")
        return

    parim_nimi = None
    parim_keskmine = -1.0

    # Käime üle kõik mängijad ja arvutame nende keskmise
    for nimi in seis:
        km = leia_keskmine(nimi, seis)
        if km is not None and km > parim_keskmine:
            parim_keskmine = km
            parim_nimi = nimi

    # Väljastame tulemuse ühe komakohaga
    print(f"Parim keskmine on {parim_nimi} → {parim_keskmine:.1f}")


def main():
    fail = "punktid.txt"
    # 1) Loeme algandmed faili coroutine loe_seis abil
    seis = loe_seis(fail)

    while True:
        # 2) Kuvame kasutajale lihtsa menüü
        print("\n=== Menüü ===")
        print("1 - Kuvan punktitabeli")
        print("2 - Lisa tulemus")
        print("3 - Leia mängija keskmine")
        print("4 - Leia parim mängija")
        print("5 - Salvesta ja lõpeta")
        valik = input("Vali tegevus: ").strip()

        if valik == "1":
            # näitame kõiki mängijaid ja nende punktid riduena
            for nimi, punktid in seis.items():
                print(nimi, *punktid)

        elif valik == "2":
            # küsime nime ja uue punktili
            nimi = input("Sisesta nimi: ").strip()
            tulemus = int(input("Sisesta uus tulemus: ").strip())
            lisa_tulemus(nimi, seis, tulemus)

        elif valik == "3":
            # küsime nime ja arvutame tema keskmise
            nimi = input("Sisesta nimi: ").strip()
            km = leia_keskmine(nimi, seis)
            if km is not None:
                print(f"{nimi} keskmine skoor on {km:.1f}")

        elif valik == "4":
            # leiame parima keskmise
            leia_parim(seis)

        elif valik == "5":
            # 3) Salvesta muudetud tabel tagasi faili
            with open(fail, "w", encoding="utf-8") as f:
                for nimi, punktid in seis.items():
                    # liidame nime ja punktid üheks realoendi stringiks
                    rida = nimi + " " + " ".join(str(x) for x in punktid)
                    f.write(rida + "\n")
            print("Andmed salvestatud. Programm lõpetab töö.")
            break

        else:
            print("Tundmatu valik, proovi uuesti.")


if __name__ == "__main__":
    main()


1. Muutujad ja Andmetüübid

# Muutuja loomine ja andmetüübid

nimi = "Juku"           # String: salvestab teksti, näiteks kasutaja nime
vanus = 25              # Int: salvestab täisarvu, näiteks kasutaja vanust
hind = 19.99            # Float: salvestab ujukomaarvu, näiteks toote hinda
aktiivne = True         # Bool: salvestab loogilise väärtuse (True/False)

# Väljund: print funktsioon prindib väärtused ekraanile
print("Tere, " + nimi)  # Ühendab teksti ja muutujat, et kuvada tervitus
print("Vanus:", vanus)   # Kuvab teksti ja täisarvu

2. Tingimuslaused

# Tingimuslause näide: kontrollib kasutaja vanust

# Tingimuslaused – Cheat Sheet

# 1. Põhiline if-else struktuur
# Kontrollib, kas muutuja 'a' väärtus ületab 10.
a = 15  # Määrame 'a' väärtuseks 15
if a > 10:
    # Kui 'a' on suurem kui 10 (tingimus on True), käivitatakse see plokk.
    print("a on suurem kui 10")
else:
    # Kui tingimus on False, käivitatakse see plokk.
    print("a ei ole suurem kui 10")

# 2. if-elif-else struktuur
# Kontrollib, kas 'number' on positiivne, null või negatiivne.
number = 0  # Näiteks number väärtuseks 0
if number > 0:
    print("Positiivne number")
elif number == 0:
    # 'elif' kontrollib, kas number on täpselt 0.
    print("Null")
else:
    print("Negatiivne number")

# 3. Loogilised operaatorid: and, or, not
# Kontrollib, kas isik on täiskasvanu (vanus 18 kuni 64)
vanus = 20
if vanus >= 18 and vanus < 65:
    # Mõlemad tingimused peavad olema tõevad (and)
    print("Täiskasvanu")
else:
    print("Kas laps või pensionär")

# FOR-TSÜKELID

# 1. Lihtne for-tsükkel loendamiseks kasutades range() funktsiooni
# range(1, 6) loob jada arvudest 1 kuni 5
for i in range(1, 6):
    print("Arv:", i)    # Prindib iga tsükli iteratsiooni väärtuse

# 2. For-tsükkel, mis itereerib listi elementide üle
puuviljad = ["õun", "pirn", "banaan"]
for puuvili in puuviljad:
    print("Puuvili:", puuvili)   # Iga iteratsiooni käigus prindib ühe puuvilja

# 3. For-tsükkel sõne (stringi) tähtede kaupa läbimiseks
tekst = "Python"
for täht in tekst:
    print("Täht:", täht)   # Prindib iga tähe eraldi reale

# 4. Kasutades enumerate() funktsiooni, et saada nii indeks kui ka väärtus
for indeks, element in enumerate(puuviljad):
    print("Indeks:", indeks, "väärtus:", element)


# WHILE-TSÜKELID

# 5. Lihtne while-tsükkel loenduri suurendamiseks
loendur = 1               # Algväärtus
while loendur <= 5:        # Tsükkel töötab kuni loendur jõuab 5-ni
    print("Loendur:", loendur)
    loendur += 1         # Loendurit suurendatakse iga iteratsiooni jooksul ühe võrra

# 6. While-tsükkel, mis töötab seni, kuni kasutaja sisestab õige väärtuse
parool = ""
while parool != "salajane":
    parool = input("Sisesta parool: ")   # Küsib kasutajalt parooli
    if parool != "salajane":
        print("Vale parool, proovi uuesti!")
print("Õige parool, tere tulemast!")


# PESASTATUD (NESTED) TSÜKELID

# 7. Pesastatud tsükkel 2D-massiivi (maatriksi) läbimiseks
maatriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for rida in maatriks:
    for element in rida:
        print(element, end=" ")  # Prindib elemendi samal real, eraldatuna tühikuga
    print()  # Prindib uue rea, kui üks rida on lõppenud

# 8. Näide pesastatud tsüklist: reaalarvude summade arvutamine iga rea kohta
for rida in maatriks:
    summa = 0
    for element in rida:
        summa += element     # Liidab iga rea elemendid kokku
    print("Rea summa:", summa)


# 4. Pesastatud (nested) if-tingimus
# Kontrollib temperatuuri taset: kui temperatuur on üle 0 ja üle 30.
temperatuur = 25
if temperatuur > 0:
    # Esimene kontroll: kas temperatuur on positiivne.
    if temperatuur > 30:
        # Sisemine if kontrollib, kas temperatuur on üle 30
        print("Väga soe")
    else:
        # Kui temperatuur on positiivne, kuid mitte üle 30.
        print("Soe")
else:
    # Kui temperatuur pole positiivne (on 0 või madalam)
    print("Külm")

# 5. Kombineeritud tingimused mitme väärtuse kontrollimiseks
# Näiteks: hindame skoori vastavalt punktidele.
skoor = 85
if skoor >= 90:
    print("Suurepärane!")
elif skoor >= 75 and skoor < 90:
    # Kontrollib, kas skoor jääb vahemikku 75 kuni 89
    print("Hea tulemus")
else:
    print("Vajab parandamist")

# 6. Kasutades 'or' operaatorit
# Kui üks tingimustest peab olema tõene, et väljund prinditaks.
päev = "laupäev"
if päev == "laupäev" or päev == "pühapäev":
    print("Puhkepäev!")
else:
    print("Tööpäev")
    
# 7. Kasutades 'not' operaatorit
# Tagastab vastupidise väärtuse antud tingimusele.
kas_sul_on_kodu = False
if not kas_sul_on_kodu:
    print("Sul pole kodu, otsi varjupaika!")
else:
    print("Kodune turvalisus")


3. Tsüklid
3.1. For-tsükkel

# For-tsükkel loendab alates 1 kuni 5

for i in range(1, 6):                   # range(1, 6) loob loenduse 1 kuni 5
    print("Arv:", i)                    # Prindib iga tsükli väärtuse

3.2. While-tsükkel

# While-tsükkel, mis jätkab seni, kuni tingimus muutub vääraks

loendur = 1                            # Algväärtus
while loendur <= 5:                     # Tsükkel töötab, kuni loendur on 5 või vähem
    print("Loendur:", loendur)           # Kuvab hetkelise loenduri väärtuse
    loendur += 1                        # Suurendab loendurit ühe võrra

4. Listid ja Sõned
4.1. Listide kasutamine

# List: andmestruktuur, mis sisaldab mitut väärtust

numbrid = [1, 2, 3, 4, 5]              # Loob listi numbritest
print(numbrid[0])                      # Kuvab esimese elemendi (indeks 0)
numbrid.append(6)                      # Lisab lõppu uue elemendi (6)
print(numbrid)                         # Prindib uuendatud listi

4.2. Sõnede töötlemine

# Sõned on tegelikult loetavad jadad

tekst = "Python on võimas keel"        # Määrab sõne
print(tekst.lower())                   # Muudab kõik tähed väikesteks
print(tekst.upper())                   # Muudab kõik tähed suurteks
print(tekst.split())                   # Jagab sõne tühikute alusel sõnedeks listi

# LISTID JA SÕNED – CHEAT SHEET

# 1. Listi loomine ja elementide lisamine
# Loome nimekirja puuviljadest
puuviljad = ["õun", "pirn", "banaan"]  # List, mis sisaldab kolme stringi
print(puuviljad)  # Prindib kogu listi

# Lisame uue elemendi lõppu
puuviljad.append("kiivi")  # append() lisab elemendi listi lõppu
print(puuviljad)  # Kontrollib, et element on lisatud

# 2. Elemendi indekseerimine ja viilimine (slicing)
# Võtame listist esimese elemendi (indeks 0)
esimene = puuviljad[0]  # "õun"
print("Esimene puuvili:", esimene)

# Võtame alam-listi: esimene ja teine element
alam_list = puuviljad[0:2]  # viilimine alustades indeksist 0 kuni enne indeksit 2
print("Alam-list:", alam_list)

# 3. Listi elementide muutmine
# Muudame teise elemendi väärtust
puuviljad[1] = "maasikas"  # Asendab indeksi 1 väärtuse
print("Muudetud list:", puuviljad)

# 4. Listi meetodid: pop, remove, extend, sort ja reverse
# pop() eemaldab ja tagastab viimase elemendi (või antud indeksi elemendi)
viimane = puuviljad.pop()  
print("Eemaldatud element:", viimane)
print("Pärast pop():", puuviljad)

# remove() eemaldab esimese leitud vastavuse
puuviljad.remove("õun")
print("Pärast 'õun' eemaldamist:", puuviljad)

# extend() lisab ühe listi elemendid teise listi lõppu
rohkem_puuvilju = ["mango", "ananass"]
puuviljad.extend(rohkem_puuvilju)
print("Pärast extend():", puuviljad)

# sort() järjestab listi (kasutatakse vaikimisi kasvavas järjekorras)
puuviljad.sort()
print("Järjestatud list:", puuviljad)

# reverse() muudab listi elementide järjekorra vastupidiseks
puuviljad.reverse()
print("Pööratud list:", puuviljad)

# 5. Sõnede töötlemine

# Sõne loomine
tekst = "Python on võimas keel"
print("Algne tekst:", tekst)

# Sõne indeksimine: esimene täht
esimene_täht = tekst[0]  # esimene täht on 'P'
print("Esimene täht:", esimene_täht)

# Sõne viilimine: võtame sõna "võimas" (eeldades, et positsioonid on teada)
# Näiteks kui "võimas" algab indeksist 11 ja lõpeb enne indeksit 17:
voimas = tekst[11:17]
print("Viilitud sõna:", voimas)

# Muudatused: kõik tähed väikesteks või suurteks
print("Väiksed tähtedega:", tekst.lower())
print("Suurtähtedega:", tekst.upper())

# split() – jagab sõne listiks, kasutades vaikimisi tühikut eraldajana
sõnad = tekst.split()
print("Sõnade list:", sõnad)

# join() – liidab listi elemendid üheks sõneks, kasutades eraldajat
tekst_uuesti = " ".join(sõnad)
print("Ühendatud tekst:", tekst_uuesti)

# replace() – asendab sõnes kindla alamsõne uuega
asendatud = tekst.replace("võimas", "tõhus")
print("Asendatud tekst:", asendatud)

# 6. Kombineerimine – iteratsioon listi elementide üle, kasutades sõnede meetodeid
for sõna in sõnad:
    # Prindib iga sõna ja selle pikkuse
    print("Sõna:", sõna, "| Pikkus:", len(sõna))


5. Funktsioonid

# Funktsioon: korduvkasutatav koodiplokk, mis täidab kindlat ülesannet

def tervita(nimi):                     # Funktsiooni definitsioon, võtab parameetriks 'nimi'
    # Funktsioon prindib tervitussõnumi koos antud nimega
    return "Tere, " + nimi + "!"

# Funktsiooni väljakutse ja tagastatud väärtuse prindimine
print(tervita("Juku"))                 # Kuvab: "Tere, Juku!"

# 1. Lihtne funktsioon – Tervitussõnum
def tervita(nimi):              # Funktsiooni definitsioon: võtab ühe parameetri 'nimi'
    # Tagastab tervitussõnumi, ühendades sõned
    return "Tere, " + nimi + "!"

# Funktsiooni väljakutse
print(tervita("Mari"))          # Prindib: Tere, Mari!


# 2. Funktsioon kahe arvu summamiseks
def summa(a, b):
    # Liidab kaks argumenti ja tagastab tulemuse
    return a + b

print(summa(5, 3))              # Prindib: 8


# 3. Funktsioon ilma return'ita – prindib väärtuse otse
def tervita_ilma_returnita(nimi):
    # Prindib sõnumi, kuid ei tagasta väärtust (tagastab vaikeselt None)
    print("Tere, " + nimi + "!")

tervita_ilma_returnita("Juku")  # Prindib: Tere, Juku!


# 4. Funktsioon vaikimisi väärtustega (default parameters)
def võitlus(punktid, bonus=10):
    # Tagastab tulemuse, kus lisatakse vaikimisi bonus (10) või kasutaja poolt määratud bonus
    return punktid + bonus

print(võitlus(50))             # Kasutab vaikimisi bonusi: prindib 60
print(võitlus(50, 20))         # Kasutab antud bonusi (20): prindib 70


# 5. Funktsioon if-elif-else lausetega – tagastab hinnangu
def hinnang(skoor):
    # Tagastab erineva sõnumi sõltuvalt punktide arvust
    if skoor >= 90:
        return "Suurepärane!"
    elif skoor >= 75:
        return "Hea tulemus"
    else:
        return "Vajab parandamist"

print(hinnang(85))             # Prindib: Hea tulemus


# 6. Rekursiivne funktsioon – Faktoriaali arvutamine
def faktoriaal(n):
    # Kui n on 0 või 1, tagastab 1 (baasjuhtum)
    if n <= 1:
        return 1
    else:
        # Rekursiivne kõne: n * faktoriaal(n - 1)
        return n * faktoriaal(n - 1)

print(faktoriaal(5))           # Prindib: 120, sest 5*4*3*2*1 = 120


# 7. Lambda funktsioon – lühifunktsioon ühe rea koodiga
# Defineerime anonüümse funktsiooni, mis korrutab sisendi 2-ga
topeldu = lambda x: x * 2
print(topeldu(7))             # Prindib: 14



6. Failide Töötlemine
6.1. Failist lugemine

# Faili lugemine: avab faili ja prindib kõik read

with open("andmed.txt", "r", encoding="utf-8") as f:
    # 'with' tagab faili korrektse sulgemise pärast lugemist
    for rida in f:                   # Iteratsioon iga rea üle failis
        print(rida.strip())           # .strip() eemaldab liigsed tühikud ja reavahetused

6.2. Faili kirjutamine

# Faili kirjutamine: loob või kirjutab faili uue sisu

tekst = "See on salvestatud tekst"
with open("tulemus.txt", "w", encoding="utf-8") as f:
    f.write(tekst)                     # Kirjutab tekstimuutuja sisu faili

# FAILIDE TÜÖTLEMINE – CHEAT SHEET

# 1. Failist lugemine rida-haaval:
# 'with' plokk tagab, et fail suletakse automaatselt pärast kasutamist.
with open("failinimi.txt", "r", encoding="utf-8") as file:
    # Itereerime iga rea üle failis
    for rida in file:
        print(rida.strip())   # .strip() eemaldab liigsed tühikud ja reavahetused

# 2. Faili lugemine kogu sisuna:
with open("failinimi.txt", "r", encoding="utf-8") as file:
    sisu = file.read()        # Loeb kogu faili sisu ühte stringi
    print(sisu)

# 3. Faili kirjutamine:
tekst = "See on kirjutatud tekst, mida salvestatakse faili."
# Avame faili kirjutamise režiimis ('w' – kirjutab üle olemasoleva sisu või loob uue faili)
with open("tulemus.txt", "w", encoding="utf-8") as file:
    file.write(tekst)         # Kirjutab muutujas 'tekst' oleva sisu faili

# 4. Faili lisamine (appending):
lisa_tekst = "\nSee on lisatud uus rida faili lõppu."
# Avame faili lisamise režiimis ('a' – lisab teksti olemasolevale sisule)
with open("tulemus.txt", "a", encoding="utf-8") as file:
    file.write(lisa_tekst)    # Lisab 'lisa_tekst' faili lõppu ilma eelmist sisu kustutamata

# 5. Faili avamine ilma 'with' plokita (mida tuleb käsitsi sulgeda):
fail = open("failinimi.txt", "r", encoding="utf-8")
# Tee siin vajalikke operatsioone faili andmetega
fail.close()                  # Sulgeb faili käsitsi – oluline, et ressursid vabastuksid



7. Objektorienteeritud Programmeerimine (OOP)
7.1. Klass ja objekt

# Klass defineerib andmete ja käitumise koos
class Inimene:
    def __init__(self, nimi, vanus):    # Konstruktor, mis käivitub objekti loomisel
        self.nimi = nimi               # Määrab isendivälja 'nimi'
        self.vanus = vanus             # Määrab isendivälja 'vanus'
    
    def tervita(self):                 # Meetod, mis prindib tervitussõnumi
        # Kasutab objekti atribuute, et moodustada sõnum
        return "Tere, minu nimi on " + self.nimi + " ja ma olen " + str(self.vanus) + " aastat vana."

# Objekti loomine
inimene1 = Inimene("Juku", 25)
print(inimene1.tervita())              # Kutsub välja meetodi ja prindib sõnumi

7.2. Pärimine

# Pärimine võimaldab luua alamklasse, mis kasutavad baasklassi omadusi

class Õpilane(Inimene):                 # Õpilane pärib klassi Inimene
    def __init__(self, nimi, vanus, kool):  # Laiendab __init__ konstruktorit uue atribuudiga 'kool'
        super().__init__(nimi, vanus)      # Kutsub välja Inimene konstruktorit
        self.kool = kool                   # Määrab uue atribuudina kooli nime
    
    def info(self):                      # Uus meetod, mis lisab infot kooli kohta
        return self.tervita() + " Ma õpin " + self.kool + " koolis."

õpilane1 = Õpilane("Mari", 17, "Tallinna")
print(õpilane1.info())                  # Prindib täiustatud tervitussõnumi koos kooli infoga

# OOP – CLASSID, OBJEKTID JA PÄRIMINE

# 1. Klasside loomine ja konstruktor (__init__)
class Inimene:
    def __init__(self, nimi, vanus):
        # Konstruktor – käivitatakse iga kord, kui objekt luuakse
        # Määrab isendiväljad 'nimi' ja 'vanus'
        self.nimi = nimi
        self.vanus = vanus

    def tervita(self):
        # Meetod, mis tagastab tervitussõnumi, kasutades objekti andmeid
        return "Tere, minu nimi on " + self.nimi + " ja ma olen " + str(self.vanus) + " aastat vana."

    def __str__(self):
        # __str__ meetod – määrab, kuidas objekt ekraanile prinditakse
        return "Nimi: " + self.nimi + ", Vanus: " + str(self.vanus)

# 2. Objekti loomine ja meetodi väljakutsed
inimene1 = Inimene("Juku", 30)  # Loome Inimene klassi objekti
print(inimene1.tervita())       # Kutsub välja meetodi, mis tagastab tervitussõnumi
print(inimene1)                 # Prindib objekti kasutades __str__ meetodit


# 3. Pärimine – alamklasside loomine
class Õpilane(Inimene):
    def __init__(self, nimi, vanus, kool):
        # Kutsub välja baasklassi konstruktorit, et määrata 'nimi' ja 'vanus'
        super().__init__(nimi, vanus)
        # Lisab uue isendivälja 'kool'
        self.kool = kool

    def info(self):
        # Lisame lisainfot – kasutame nii baasklassi meetodit kui ka uut atribuuti
        return self.tervita() + " Ma õpin " + self.kool + " koolis."

    def __str__(self):
        # Ülekirjutame __str__ meetodi, et lisada kooli teave
        return "Nimi: " + self.nimi + ", Vanus: " + str(self.vanus) + ", Kool: " + self.kool

# Loome Õpilane klassi objekti
õpilane1 = Õpilane("Mari", 17, "Tallinna Gümnaasium")
print(õpilane1.info())  # Prindib täiustatud info koos kooli nimega
print(õpilane1)        # Prindib objekti info __str__ meetodi abil

**4.3. Sõnastikud (dictionaries)**

```python
# Näide: võtme–väärtuse paaride kogum
õpilased = {
    "Mari": 19,
    "Juku": 21,
    "Kaidi": 18
}

# 1) Elemendi lisamine või muutmine
õpilased["Malle"] = 20        # lisame uue kirje
õpilased["Juku"] = 22         # muudame olemasolevat

# 2) Väärtuse lugemine
vanus = õpilased["Mari"]      # 19
# turvaline lugemine get()-iga, et vältida KeyError’it
surname = õpilased.get("Peeter", "Pole andmeid")

# 3) Elemendi eemaldamine
õpilased.pop("Kaidi")         # eemaldab võtme "Kaidi" ja tagastab tema vanuse

# 4) Iteratsioon võtmete ja väärtuste üle
for nimi, vanus in õpilased.items():
    print(nimi, "on", vanus, "aastat vana")

# 5) Võtmete / väärtuste nimekirjad
võtmed = list(õpilased.keys())
väärtused = list(õpilased.values())

# 6) Dictionary comprehension
ruut = {i: i * i for i in range(1, 6)}
print(ruut)  # {1:1, 2:4, 3:9, 4:16, 5:25}
```

# Sõnastikud – CHEAT SHEET

1. **Sõnastiku loomine**

   ```python
   tühisõnastik = {}
   andmed = {"võti1": "väärtus1", "võti2": 42}
   ```
2. **Elemendi lisamine / muutmine**

   ```python
   andmed["uus_võti"] = "uus_väärtus"
   ```
3. **Väärtuse lugemine**

   ```python
   x = andmed["võti1"]
   y = andmed.get("puudub", None)
   ```
4. **Elemendi eemaldamine**

   ```python
   väärtus = andmed.pop("võti2", "vaikimisi")
   ```
5. **Itereerimine**

   ```python
   for võti in andmed:
       print(võti, andmed[võti])
   for võti, väärtus in andmed.items():
       …
   ```
6. **Põhilised meetodid**

   * `keys()`, `values()`, `items()`
   * `get(võti[, vaikimisi])`
   * `update( teine_sõnastik )`
   * `clear()`
7. **Comprehension**

   ```python
   uus = {x: f(x) for x in algne_list if tingimus(x)}
   ```

# Sõnastik, kus iga mängija nime all on tema voorude tulemuste list
tulemused = {
    'Mari':  [2,  4,  5,  '-', 1, 4],
    'Juku':  [1,  3,  2,   7,  8, '-'],
    'Malle': ['-', 2,  '-', 3,  2, 5],
    'Kalle': [4,  6,  '-', '-', 2, '-']
}

# 1) Lihtne läbikäik sõnastiku ja listide sees
for nimi, voorud in tulemused.items():
    print(nimi, "tulemused on", voorud)

# Väljund:
# Mari tulemused on [2, 4, 5, '-', 1, 4]
# Juku tulemused on [1, 3, 2, 7, 8, '-']
# ...

# 2) Täpne ligipääs: antud mängija antud voor
mängija = 'Malle'
vooru_nr = 3   # tähele: indeks 0 = esimene voor
vaartus = tulemused[mängija][vooru_nr]
print(f"{mängija}, voor {vooru_nr+1} tulemus:", vaartus)
# Malle, voor 4 tulemus: 3

# 3) „Maatriksina“: võtame sõnastiku väärtuste listid ja paneme need uude listi
maatriks = list(tulemused.values())
# nüüd maatriks on:
# [
#   [2, 4, 5, '-', 1, 4],
#   [1, 3, 2, 7, 8, '-'],
#   ['-', 2, '-', 3, 2, 5],
#   [4, 6, '-', '-', 2, '-']
# ]

# 4) Läbikäik maatriksina (pesastatud tsüklid)
for rida in maatriks:
    for el in rida:
        print(el, end=" ")
    print()
# Väljatrükk ridadena, kus iga rida kuulub erinevale mängijale

# 5) Transponeerimine: et saada voorude kaupa ridad
transponeeritud = [
    [rida[i] for rida in maatriks]
    for i in range(len(maatriks[0]))
]
# transposeeritud[0] = [2,1,'-',4]  → 1. voor kõigi mängijate tulemused

# 6) Võtme järgi matrixi muutmine või uue maatriksi salvestamine
# Näiteks muuta puudunud voorud („-“) väärtuseks 0:
puhastatud = {
    nimi: [0 if t == '-' else t for t in voorud]
    for nimi, voorud in tulemused.items()
}


---

**4.4. Kahemõõtmeline loend (maatriks)**

```python
# Maatriks – loendide loend (3×3 näide)
maatriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1) Ligipääs elemendile [rida][veerg]
print(maatriks[1][2])   # 6

# 2) Läbikäik pesastatud tsüklitega
for rida in maatriks:
    for element in rida:
        print(element, end=" ")
    print()

# 3) Indeksitega läbikäik (vajalik transponeerimiseks)
for i in range(len(maatriks)):
    for j in range(len(maatriks[0])):
        print(f"({i},{j}) =", maatriks[i][j])

# 4) Transponeerimine list-comprehension’iga
transp = [
    [maatriks[r][c] for r in range(len(maatriks))]
    for c in range(len(maatriks[0]))
]
print(transp)  # [[1,4,7],[2,5,8],[3,6,9]]
```

# Maatriks – CHEAT SHEET

1. **Maatriksi loomine**

   ```python
   m = [
       [a11, a12, …, a1n],
       …,
       [am1, am2, …, amn]
   ]
   ```
2. **Elemendi ligipääs**

   ```python
   väärtus = m[rida][veerg]
   ```
3. **Pesastatud tsüklid**

   ```python
   for rida in m:
       for x in rida:
           …
   ```
4. **Indeksitega tsüklid**

   ```python
   for i in range(len(m)):
       for j in range(len(m[0])):
           …
   ```
5. **Transponeerimine**

   ```python
   T = [[m[r][c] for r in range(ridade_aru)] for c in range(veergude_aru)]
   ```
6. **Maatriksi initsialiseerimine**

   ```python
   # nt 5×5 null-matriks
   nullm = [[0 for _ in range(5)] for _ in range(5)]
   ```
7. **Tabeli väljatrükk**

   ```python
   for rida in m:
       print(*rida)
   ```

