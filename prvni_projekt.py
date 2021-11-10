texts = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

oddelovac = "-" * 50

print(oddelovac)
print("WELCOME TO THE APP".center(len(oddelovac)))
print(oddelovac)

user = input("USER: ")
password = input("PASSWORD: ")

print(oddelovac)
# Ověření uživatele a hesla
if user == "bob" and password == "123":
    print(
        f"Welcome to the app, {user}.",
        "We have 3 texts to be analyzed",
        oddelovac,
        sep="\n"
    )
elif user == "ann" and password == "pass123":
    print(
        f"Welcome to the app, {user}.",
        "We have 3 texts to be analyzed",
        oddelovac,
        sep="\n"
    )
elif user == "mike" and password == "password123":
    print(
        f"Welcome to the app, {user}.",
        "We have 3 texts to be analyzed",
        oddelovac,
        sep="\n"
    )
elif user == "liz" and password == "pass123":
    print(
        f"Welcome to the app, {user}.",
        "We have 3 texts to be analyzed",
        oddelovac,
        sep="\n"
    )
else:
    print(
        "Wrong USER or PASSWORD, try again!",
        oddelovac,
        sep="\n"
    )
    quit()

text1 = str(texts[0])
text2 = str(texts[1])
text3 = str(texts[2])

text_number = input("Enter a number 1 to 3: ")
# Všechny úkoly pro text č. 1
if text_number == "1":
    print(oddelovac,
        "TEXT NUMBER 1: ",
        sep="\n"
    )
    # listy pro následné cykly
    slova_zvlast_1 = list()
    prvni_velke_1 = list()
    mala_pismena_1 = list()
    velka_pismena_1 = list()
    pocet_cisel_1 = list()
    suma_cisel_1 = list()

    # Počet slov celkem
    for slovo in text1.split():
        slova_zvlast_1.append(slovo)
    print("There are", len(slova_zvlast_1), "word in the selected text")

    # Počáteční velké písmeno
    for prvni_pismeno in text1.split():
        ciste_slovo = prvni_pismeno.istitle()
        if ciste_slovo == True:
            prvni_velke_1.append(ciste_slovo)
    print("There are", len(prvni_velke_1), "titlecase word")

    # Počet slov velými písmeny
    for velke in text1.split():
        ciste_slovo = velke.isupper()                               #Tady mi to bere i čísla (30N)
        if ciste_slovo == True:
            velka_pismena_1.append(ciste_slovo)
    print("There are", len(velka_pismena_1), "uppercase word")

    # Počet slov malými písmeny
    for male in text1.split():
        ciste_slovo = male.islower()
        if ciste_slovo == True:
            mala_pismena_1.append(ciste_slovo)
    print("There are", len(mala_pismena_1), "lowercase word")

    # Počet čísel
    for cislo in text1.split():
        cele_cislo = cislo.isnumeric()
        if cele_cislo == True:
            pocet_cisel_1.append(cele_cislo)
    print("There are", len(pocet_cisel_1), "numeric strings")

    # Suma všech čísel
    for cislo in text1.split():
        suma = cislo.isnumeric()
        if suma == True:
            suma_cisel_1.append(int(cislo))

    print(f"The sum of all the numbers {sum(suma_cisel_1)}")

    delka_slov_1 = dict()

    for slovo in text1.split():
        text = slovo.strip(".,")
        delka = len(text.lower())
        if delka not in delka_slov_1:
            delka_slov_1[delka] = 1
        else:
            delka_slov_1[delka] = delka_slov_1[delka] + 1

    print(oddelovac)

    print(f"{'LEN|': >5}",
          f"{'OCCURENCES': <15}",
          f"{'|NR.': <3}",
    )
    print(oddelovac)

    for pocet in sorted(delka_slov_1.keys()):
        hvezdy = '*' * delka_slov_1[pocet]

        print(f"{pocet: >4}|",
              f"{hvezdy: <15}",
              f"|{delka_slov_1[pocet]: <3}"
        )

# Všechny úkoly pro text č. 2, ROZBOR TEXTU VE DVOU CYKLECH NE V ŠESTI
elif text_number == "2":
    print(oddelovac,
        "TEXT NUMBER 2: ",
        sep="\n"
    )

    slova_zvlast_2 = list()

    #Zvlášť cyklus pro rozdělení slov -> nevím jak vepsat do podmínek níže
    for slovo in text2.split():
        slova_zvlast_2.append(slovo)
    print("There are", len(slova_zvlast_2), "word in the selected text")

    prvni_velke_2 = list()
    mala_pismena_2 = list()
    velka_pismena_2 = list()
    pocet_cisel_2 = list()

    for slovo in text2.split():
        if slovo.istitle():
            prvni_velke_2.append(slovo)
        elif slovo.islower():
            mala_pismena_2.append(slovo)
        elif slovo.isupper():
            velka_pismena_2.append(slovo)
        elif slovo.isnumeric():
            pocet_cisel_2.append(int(slovo))

    print(f"There are {len(prvni_velke_2)} titlecase word",
          f"There are {len(mala_pismena_2)} lowercase word",
          f"There are {len(velka_pismena_2)} uppercase word",
          f"There are {len(pocet_cisel_2)} numeric strings",
          f"The sum of all the numbers {sum(pocet_cisel_2)}",
          oddelovac,
          sep="\n"
    )

    delka_slov_2 = dict()

    for slovo in text2.split():
        text = slovo.strip(".,")
        delka = len(text.lower())
        if delka not in delka_slov_2:
            delka_slov_2[delka] = 1
        else:
            delka_slov_2[delka] = delka_slov_2[delka] + 1

    print(oddelovac)

    print(f"{'LEN|': >5}",
          f"{'OCCURENCES': <15}",
          f"{'|NR.': <3}",
    )

    print(oddelovac)

    for pocet in sorted(delka_slov_2.keys()):
        hvezdy = '*' * delka_slov_2[pocet]

        print(f"{pocet: >4}|",
              f"{hvezdy: <15}",
              f"|{delka_slov_2[pocet]: <3}"
        )

# Všechny úkoly pro text č. 3
elif text_number == "3":
    print(oddelovac,
        "TEXT NUMBER 3: ",
        sep="\n"
    )
    slova_zvlast_3 = list()
    prvni_velke_3 = list()
    mala_pismena_3 = list()
    velka_pismena_3 = list()
    pocet_cisel_3 = list()

    # Ok přišel jsem na to :D nyní už jeden cyklus na vše
    for slovo in text3.split():
        slova_zvlast_3.append(slovo)
        if slovo.istitle():
            prvni_velke_3.append(slovo)
        elif slovo.islower():
            mala_pismena_3.append(slovo)
        elif slovo.isupper():
            velka_pismena_3.append(slovo)
        elif slovo.isnumeric():
            pocet_cisel_3.append(int(slovo))

    print(f"There are {len(slova_zvlast_3)} word in the selected text",
          f"There are {len(prvni_velke_3)} titlecase word",
          f"There are {len(mala_pismena_3)} lowercase word",
          f"There are {len(velka_pismena_3)} uppercase word",
          f"There are {len(pocet_cisel_3)} numeric strings",
          f"The sum of all the numbers {sum(pocet_cisel_3)}",
          oddelovac,
          sep="\n"
          )

    delka_slov_3 = dict()

    for slovo in text3.split():
        text = slovo.strip(".,")
        delka = len(text.lower())
        if delka not in delka_slov_3:
            delka_slov_3[delka] = 1
        else:
            delka_slov_3[delka] = delka_slov_3[delka] + 1

    print(oddelovac)

    print(f"{'LEN|': >5}",
          f"{'OCCURENCES': <15}",
          f"{'|NR.': <3}",
    )

    print(oddelovac)

    for pocet in sorted(delka_slov_3.keys()):
        hvezdy = '*' * delka_slov_3[pocet]

        print(f"{pocet: >4}|",
              f"{hvezdy: <15}",
              f"|{delka_slov_3[pocet]: <3}"
        )

# Špatně zadáno číslo textu, který chci analyzovat. Bye
else:
    print(oddelovac,
        "Wrong choice, the app will be terminated",
        sep="\n"
    )
    quit()




