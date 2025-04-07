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



"""
MAIN.PY – Laiendatud Python Cheat Sheet
========================================

See fail koondab mitmesugused Python-i ülesanded ja kontseptsioonid.
Iga koodilõik on põhjalikult kommenteeritud, et eksamil oleks kiirelt leitav:
- Milliseid Python-i konstruktsioone kasutatakse (nt. muutujad, andmetüübid, tingimuslaused, tsüklid, funktsioonid, failide I/O, OOP)
- Selgitused iga rea kohta
- Märksõnad, mis aitavad teemat kiiresti meelde tuletada

Saad seda faili kasutada nii paberil kui ka arvutis kiireks kordamiseks.
========================================
"""

##############################
# SECTION 1: MUUTUJAD JA ANDMETÜÜBID
##############################

# KEYWORDS: muutuja, andmetüüp, string, int, float, bool, print

# Muutuja loomine: "nimi" on string-tüüpi muutuja, mis hoiab teksti
nimi = "Juku"  # string – tekst; väärtus "Juku"
# Selgitus: "nimi" hoiab kasutaja nime; kasutatakse tekstilise info salvestamiseks

# Täisarv – int; hoiab täisarvu
vanus = 25    # int – täisarv; väärtus 25
# Selgitus: "vanus" näitab inimese vanust

# Ujukomaarv – float; hoiab reaalarvu
hind = 19.99  # float – ujukomaarv; väärtus 19.99
# Selgitus: "hind" esindab näiteks toote hinda

# Loogiline väärtus – bool; võib olla True või False
aktiivne = True  # bool – loogiline; väärtus True (tõene)
# Märksõnad: boolean, True, False

# Väljundi väljastamine: print funktsioon
print("Tere, " + nimi)  # print: ühendab stringi "Tere, " ja muutuja "nimi" väärtuse
# Märksõnad: stringi ühendamine, print()

print("Vanus:", vanus)   # print: prindib sõna "Vanus:" ja täisarvu muutuja "vanus"
# Märksõnad: komadega eraldatud print, andmetüüpide väljund

##############################
# SECTION 2: TINGIMUSLAUSED
##############################

# KEYWORDS: if, elif, else, loogilised operaatorid (>, <, >=, <=, ==, !=), and, or, not

# Põhiline if-else struktuur:
a = 15  # määrame muutuja a väärtuseks 15
if a > 10:
    # Kui a on suurem kui 10 – tingimus True
    print("a on suurem kui 10")  # Käivitatakse, kui tingimus on tõene
else:
    # Kui a ei ole suurem kui 10 – tingimus False
    print("a ei ole suurem kui 10")
# Märksõnad: if, else, võrdlusoperaator (>)

# if-elif-else struktuur:
number = 0  # määrame number väärtuseks 0
if number > 0:
    print("Positiivne number")  # Käivitatakse, kui number on suurem kui 0
elif number == 0:
    # else if: kontrollib, kas number on täpselt 0
    print("Null")
else:
    print("Negatiivne number")
# Märksõnad: elif, võrdlusoperaator (==)

# Loogilised operaatorid: and, or, not
vanus = 20  # uuendame vanuse väärtuse
if vanus >= 18 and vanus < 65:
    # and: mõlemad tingimused peavad olema tõevad
    print("Täiskasvanu")
else:
    print("Kas laps või pensionär")
# Märksõnad: and, >=, <

# Pesastatud (nested) if-tingimus:
temperatuur = 25  # määrame temperatuur väärtuseks 25
if temperatuur > 0:
    # Esimene kontroll: temperatuur peab olema positiivne
    if temperatuur > 30:
        # Sisemine kontroll: kui temperatuur ületab 30, on see "väga soe"
        print("Väga soe")
    else:
        # Kui temperatuur on positiivne, kuid mitte üle 30
        print("Soe")
else:
    # Kui temperatuur pole positiivne (0 või madalam)
    print("Külm")
# Märksõnad: pesastatud if, loogiline struktuur

# Kombineeritud tingimused:
skoor = 85  # määrame skoori väärtuseks 85
if skoor >= 90:
    print("Suurepärane!")
elif skoor >= 75 and skoor < 90:
    print("Hea tulemus")
else:
    print("Vajab parandamist")
# Märksõnad: tingimuslaused, and, skooride hindamine

# Kasutades or operaatorit:
päev = "laupäev"
if päev == "laupäev" or päev == "pühapäev":
    print("Puhkepäev!")  # Kui päev on kas laupäev või pühapäev, siis on see puhkeaeg
else:
    print("Tööpäev")
# Märksõnad: or, võrdlus

# Kasutades not operaatorit:
kas_sul_on_kodu = False
if not kas_sul_on_kodu:
    print("Sul pole kodu, otsi varjupaika!")
else:
    print("Kodune turvalisus")
# Märksõnad: not, loogiline negatsioon

##############################
# SECTION 3: TSÜKELID
##############################

# KEYWORDS: for, while, range(), enumerate(), pesastatud tsüklid

# For-tsükkel kasutades range():
for i in range(1, 6):  
    # range(1, 6) genereerib jada arvudest 1 kuni 5
    print("Arv:", i)  # Prindib iga tsükli iteratsiooni väärtuse
# Märksõnad: range(), for-loop, loendamine

# For-tsükkel listi elementide üle:
puuviljad = ["õun", "pirn", "banaan"]
for puuvili in puuviljad:
    # Itereerib läbi iga elemendi listis "puuviljad"
    print("Puuvili:", puuvili)
# Märksõnad: list, itereerimine

# For-tsükkel sõne (string) tähtede kaupa:
tekst = "Python"
for täht in tekst:
    # Iga tähe puhul sõnes "Python" käivitatakse tsükkel
    print("Täht:", täht)
# Märksõnad: string, itereerimine, for-loop

# enumerate() funktsiooni kasutamine:
for indeks, element in enumerate(puuviljad):
    # enumerate() annab nii indeksi kui ka väärtuse iga iteratsiooni jaoks
    print("Indeks:", indeks, "väärtus:", element)
# Märksõnad: enumerate(), indeksid

# While-tsükkel:
loendur = 1  # Algväärtus 1
while loendur <= 5:
    # Tsükkel töötab seni, kuni loendur on 5 või vähem
    print("Loendur:", loendur)
    loendur += 1  # Suurendab loendurit ühe võrra; sama mis loendi inkrementeerimine
# Märksõnad: while-loop, inkrementeerimine

# While-tsükkel kasutaja sisendi kontrollimiseks:
parool = ""
while parool != "salajane":
    # Tsükkel töötab seni, kuni kasutaja sisestab õige parooli "salajane"
    parool = input("Sisesta parool: ")  # Küsib kasutajalt parooli
    if parool != "salajane":
        print("Vale parool, proovi uuesti!")
print("Õige parool, tere tulemast!")
# Märksõnad: while-loop, kasutaja sisend, stringi võrdlus

# Pesastatud (nested) tsüklid 2D-massiivi jaoks:
maatriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for rida in maatriks:
    # Itereerime läbi iga rea maatriksis (iga rida on list)
    for element in rida:
        # Itereerime läbi iga elemendi reas
        print(element, end=" ")  # end=" " prindib elemendid samal real tühikutega eraldatult
    print()  # Prindib reavahetuse, et järgmine rida alustaks uuel real
# Märksõnad: nested loop, 2D list, pesastatud tsüklid

##############################
# SECTION 4: LISTID JA SÕNED
##############################

# KEYWORDS: list, slicing, append(), pop(), remove(), extend(), sort(), reverse(), string, lower(), upper(), split(), join(), replace()

# Listi loomine:
puuviljad = ["õun", "pirn", "banaan"]  # Loome listi, mis sisaldab puuviljade nimesid
print(puuviljad)  # Prindib kogu listi

# Listi elementide lisamine:
puuviljad.append("kiivi")  # append() lisab elemendi listi lõppu
print(puuviljad)  # Kontrollime, et "kiivi" on lisatud

# Elemendi indekseerimine:
esimene = puuviljad[0]  # Võtame esimese elemendi (indeks 0)
print("Esimene puuvili:", esimene)

# Listi viilimine (slicing):
alam_list = puuviljad[0:2]  # Võtab alam-listi esimese kahe elemendi jaoks (indeksid 0 ja 1)
print("Alam-list:", alam_list)

# Listi elementide muutmine:
puuviljad[1] = "maasikas"  # Muudame teise elemendi väärtust; asendame "pirni" "maasikaga"
print("Muudetud list:", puuviljad)

# Listi meetodid:
viimane = puuviljad.pop()  # pop() eemaldab ja tagastab viimase elemendi
print("Eemaldatud element:", viimane)
print("Pärast pop():", puuviljad)

puuviljad.remove("õun")  # remove() eemaldab esimese leitud "õuna"
print("Pärast 'õun' eemaldamist:", puuviljad)

rohkem_puuvilju = ["mango", "ananass"]
puuviljad.extend(rohkem_puuvilju)  # extend() lisab teise listi elemendid "puuviljad" lõppu
print("Pärast extend():", puuviljad)

puuviljad.sort()  # sort() järjestab listi vaikimisi kasvavas järjekorras
print("Järjestatud list:", puuviljad)

puuviljad.reverse()  # reverse() muudab listi elemendid vastupidiseks järjekorras
print("Pööratud list:", puuviljad)

# Sõnede töötlemine:
tekst = "Python on võimas keel"  # Sõne loomine
print("Algne tekst:", tekst)

esimene_täht = tekst[0]  # Sõne esimene täht (indeks 0)
print("Esimene täht:", esimene_täht)

# Sõne viilimine: võtame alamsõna "võimas"
voimas = tekst[11:17]  # Märkus: indeksid määravad, kust alates ja kuni milleni sõna võetakse
print("Viilitud sõna:", voimas)

print("Väiksed tähtedega:", tekst.lower())  # lower() muudab kõik tähed väikesteks
print("Suurtähtedega:", tekst.upper())      # upper() muudab kõik tähed suurteks

sõnad = tekst.split()  # split() jagab sõne listiks, kasutades vaikimisi tühikut eraldajana
print("Sõnade list:", sõnad)

tekst_uuesti = " ".join(sõnad)  # join() liidab listi elemendid üheks sõneks, eraldades need tühikutega
print("Ühendatud tekst:", tekst_uuesti)

asendatud = tekst.replace("võimas", "tõhus")  # replace() asendab kindla alamsõne uuega
print("Asendatud tekst:", asendatud)

# Iteratsioon sõnade listi üle:
for sõna in sõnad:
    # Prindib iga sõna ja selle pikkuse, kasutades len() funktsiooni
    print("Sõna:", sõna, "| Pikkus:", len(sõna))
    
##############################
# SECTION 5: FUNKTSIOONID
##############################

# KEYWORDS: def, return, parameters, arguments, lambda, default parameters, recursion

# Lihtne funktsioon, mis tagastab tervitussõnumi:
def tervita(nimi):
    # Funktsioon, mis võtab parameetriks "nimi" ja tagastab tervitussõnumi
    # Märksõnad: funktsioonide definitsioon, return
    return "Tere, " + nimi + "!"

print(tervita("Mari"))  # Väljakutse: prindib "Tere, Mari!"

# Funktsioon kahe arvu summamiseks:
def summa(a, b):
    # Liidab kaks argumenti a ja b ning tagastab tulemuse
    # Märksõnad: aritmeetika, return
    return a + b

print(summa(5, 3))  # Prindib 8

# Funktsioon, mis prindib ilma return'ita:
def tervita_ilma_returnita(nimi):
    # Prindib sõnumi otse; tagastab vaikimisi None
    print("Tere, " + nimi + "!")

tervita_ilma_returnita("Juku")  # Prindib "Tere, Juku!"

# Funktsioon vaikimisi väärtustega:
def võitlus(punktid, bonus=10):
    # Funktsioon, kus "bonus" omab vaikimisi väärtust 10
    # Märksõnad: default parameters
    return punktid + bonus

print(võitlus(50))      # Kasutab vaikimisi bonusena 10; prindib 60
print(võitlus(50, 20))  # Kasutab antud bonus 20; prindib 70

# Funktsioon, mis tagastab hinnangu vastavalt punktidele:
def hinnang(skoor):
    # Kasutab if-elif-else struktuuri, et määrata hinnang skoori alusel
    if skoor >= 90:
        return "Suurepärane!"
    elif skoor >= 75:
        return "Hea tulemus"
    else:
        return "Vajab parandamist"

print(hinnang(85))  # Prindib "Hea tulemus"

# Rekursiivne funktsioon faktoriaali arvutamiseks:
def faktoriaal(n):
    # Kui n on 0 või 1, on faktoriaal 1 (baasjuhtum)
    if n <= 1:
        return 1
    else:
        # Rekursiivne kõne: n * faktoriaal(n - 1)
        return n * faktoriaal(n - 1)

print(faktoriaal(5))  # Prindib 120, sest 5*4*3*2*1 = 120

# Lambda funktsioon – lühifunktsioon ühele reale:
topeldu = lambda x: x * 2  # lambda funktsioon, mis korrutab sisendi kahega
print(topeldu(7))  # Prindib 14

##############################
# SECTION 6: FAILIDE TÜÖTLEMINE
##############################

# KEYWORDS: open, with, read, write, append, encoding, file I/O

# Failist lugemine rida-haaval:
with open("failinimi.txt", "r", encoding="utf-8") as file:
    # 'with' plokk tagab, et fail sulgub automaatselt pärast kasutamist
    for rida in file:
        # Iga rida loetakse ja liigsed tühikud eemaldatakse strip() abil
        print(rida.strip())

# Faili lugemine kogu sisuna:
with open("failinimi.txt", "r", encoding="utf-8") as file:
    sisu = file.read()  # Loeb kogu faili sisu ühte stringi
    print(sisu)

# Faili kirjutamine:
tekst = "See on kirjutatud tekst, mida salvestatakse faili."
with open("tulemus.txt", "w", encoding="utf-8") as file:
    # "w" režiim kirjutab faili üle või loob uue faili, kui see ei eksisteeri
    file.write(tekst)

# Faili lisamine (appending):
lisa_tekst = "\nSee on lisatud uus rida faili lõppu."
with open("tulemus.txt", "a", encoding="utf-8") as file:
    # "a" režiim lisab teksti olemasolevale failile ilma eelmist sisu kustutamata
    file.write(lisa_tekst)

# Faili avamine ilma "with" plokita – tuleb käsitsi sulgeda:
fail = open("failinimi.txt", "r", encoding="utf-8")
# Teostada vajalikud operatsioonid failiga
fail.close()  # Sulgeb faili; oluline ressurside vabastamiseks

##############################
# SECTION 7: OBJEKTORIENTEERITUD PROGRAMMEERIMINE (OOP)
##############################

# KEYWORDS: class, __init__, self, inheritance, super(), __str__

# Klasside loomine ja konstruktor (__init__)
class Inimene:
    def __init__(self, nimi, vanus):
        # Konstruktor: käivitatakse iga kord, kui uus objekt luuakse
        self.nimi = nimi      # self.nimi – objekti atribuut, hoiab inimese nime
        self.vanus = vanus    # self.vanus – objekti atribuut, hoiab inimese vanust

    def tervita(self):
        # Meetod, mis tagastab tervitussõnumi, kasutades objekti andmeid
        return "Tere, minu nimi on " + self.nimi + " ja ma olen " + str(self.vanus) + " aastat vana."

    def __str__(self):
        # __str__ meetod määrab, kuidas objekt prinditakse, kui kasutatakse print()
        return "Nimi: " + self.nimi + ", Vanus: " + str(self.vanus)

# Objekti loomine ja meetodi väljakutse
inimene1 = Inimene("Juku", 25)
print(inimene1.tervita())  # Väljastab tervitussõnumi, kasutades objekti andmeid
print(inimene1)            # Prindib objekti info __str__ meetodi abil

# Pärimine – alamklasside loomine
class Õpilane(Inimene):
    def __init__(self, nimi, vanus, kool):
        # Kasutab baasklassi Inimene konstruktorit via super()
        super().__init__(nimi, vanus)
        self.kool = kool  # Lisab uue atribuudi "kool"
    
    def info(self):
        # Lisab kooli teabe põhisõnumile
        return self.tervita() + " Ma õpin " + self.kool + " koolis."
    
    def __str__(self):
        # Ülekirjutab __str__ meetodi, et lisada kooli info
        return "Nimi: " + self.nimi + ", Vanus: " + str(self.vanus) + ", Kool: " + self.kool

õpilane1 = Õpilane("Mari", 17, "Tallinna Gümnaasium")
print(õpilane1.info())  # Väljastab täiendatud info koos kooli andmetega
print(õpilane1)         # Prindib objekti kasutades uuendatud __str__ meetodit














