import random
def sakums():
    sveiciens = [
        'Laipni lūdzam karātavās! Nejauši tiks izvelets vards,',
        'un Tev ir jāuzmin šis vārds pareizi burts pa burtam',
        'pirms beidzas meginajumi. Veiksmi!'
    ]

    for rinda in sveiciens:
        print(rinda, sep='\n')

    spelet_velreiz = True

    while spelet_velreiz:
        vardi = [
            "akmens", "putns", "zieds", "draugs", "skola", "suns", "zivs", "karte", 
            "durvis", "ledus", "pavasaris", "vasara", "rudens", "ziema", "galds", "krusts", "pele", "datums", "spogulis", "dziesma", "deja", "raksts", "parkets", "zeme", "debesis", "līgava", "kāzas", "jubileja", 
            "klase", "skolotājs", "students", "birojs", "krēsls", "gulta", "skapis", "spainis", "balons", "pulkstenis", 
            "maize", "piens", "sviests", "kafija", "tēja", "cukurs", "sāls", "pipars", "biete", "burkāns", 
            "kartupelis", "kāposts", "paprika", "gurķis", "saule", "mēness", "zvaigzne", "pludmale", "ūdens", "upe", 
            "ezers", "jūra", "kalns", "mežs", "pils", "tilts", "automašīna", "velosipēds", "skrejritenis", "lidmašīna", 
            "vilciens", "autobuss", "tramvajs", "kuģis", "laiva", "māja", "dzīvoklis", "ofiss", "veikals", "parks", 
            "stadions", "baseins", "teātris", "kinoteātris", "mūzika", "grupa", "albums", "dziedātājs", "spēle", "zīmējums", 
             "programmatūra", "spēles", "vēsture", "literatūra", "zinātne", "tehnoloģija", "sports", "medicīna"

        ]

        izveletais_vards = random.choice(vardi).lower()
        speletaja_minejums = None
        uzminetie_burti = []
        vards_uzminets = []
        for burts in izveletais_vards:
            vards_uzminets.append("-")
        varda_progress = None

        STATUSS = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print(STATUSS[0])
        meginajumi = len(STATUSS) - 1

        while (meginajumi != 0 and "-" in vards_uzminets):
            print(("\nTev ir atlikuši {} mēģinājumi").format(meginajumi))
            varda_progress = "".join(vards_uzminets)
            print(varda_progress)

            try:
                speletaja_minejums = str(input("\nLūdzu, izvēlies burtu no A-Z" + "\n> ")).lower()
            except:
                print("Lūdzu, meģini vēlreiz. Šis simbols nav derīgs")
                continue                
            else: 
                if not speletaja_minejums.isalpha():
                    print("Tas nav burts. Lūdzu, meģini vēlreiz.")
                    continue
                elif len(speletaja_minejums) > 1:
                    print("Tie ir vairāk nekā viens burts. Lūdzu, meģini vēlreiz.")
                    continue
                elif speletaja_minejums in uzminetie_burti:
                    print("Tu jau mineji šo burtu. Lūdzu, meģini vēlreiz.")
                    continue
                else:
                    pass

            uzminetie_burti.append(speletaja_minejums)

            for burts in range(len(izveletais_vards)):
                if speletaja_minejums == izveletais_vards[burts]:
                    vards_uzminets[burts] = speletaja_minejums

            if speletaja_minejums not in izveletais_vards:
                meginajumi -= 1
                print(STATUSS[(len(STATUSS) - 1) - meginajumi])

        if "-" not in vards_uzminets:
            print(("\nApsveicu! {} bija īstais vārds").format(izveletais_vards))
        else:
            print(("\nNepaveicas! Vards, kuru Tev vajadzēja uzminēt, bija {}.").format(izveletais_vards))

        print("\nVai vēlies spēlēt vēlreiz?")

        atbilde = input("> ").lower()
        if atbilde not in ("jā", "j", "ja"):
            spelet_velreiz = False


sakums()