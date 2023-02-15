#importovanie modulu
import random

#zadeklarovanie zoznamov
slova = []
pismenka = []
ano_nie = [0,1]
novy_subor = []
novy_riadok = []
nove_slovo = []

#random rozhodnutie o prehadzovani riadkov
prehadzovanie_riadkov = random.choice(ano_nie)

#otvorenie suboru
subor = open("virus.txt","r")

#vypisanie suboru
for riadok in subor:
    print(riadok)
print("\n")

#zatvorenie suboru
subor.close()

#otvorenie suboru
subor1 = open("virus.txt","r")

#podmienka na poprehadzovanie
if prehadzovanie_riadkov == 0:
    print("Riadky prehadzovať nebudem\n")

    for riadok1 in subor1: #cyklus pre riadok v subore
        riadocek = riadok1.strip()
        riadocek1 = riadok1.split()

        #random rozhodnutie o prehadzovani slov
        prehadzovanie_slov = random.choice(ano_nie)
        
        for slovo in riadocek1: #cyklus pre slovo v riadku
            #random rozhodnutie o prehadzovani pismen
            prehadzovanie_pismen = random.choice(ano_nie)

            #podmienka na prehadzanie pismen opacne
            if prehadzovanie_pismen == 1:
                nove_slovo = slovo[::-1]
                novy_riadok.append(nove_slovo)
            else:
                novy_riadok.append(slovo)

        #podmienka na prehadzanie slov
        if prehadzovanie_slov == 1:
            random.shuffle(novy_riadok)
            riadocek2 = " ".join(novy_riadok)
            
        else:
            riadocek2 = " ".join(novy_riadok)

        #vlozenie do noveho suboru
        novy_subor.append(str(riadocek2)+"\n")

        #vyprazdenie zoznamu
        novy_riadok.clear()
    
else:
    print("Budem prehadzovať riadky\n")
    for riadok1 in subor1: #cyklus pre riadok v subore
        riadocek = riadok1.strip()
        riadocek1 = riadok1.split()

        #random rozhodnutie o prehadzovani slov
        prehadzovanie_slov = random.choice(ano_nie)
        
        for slovo in riadocek1: #cyklus pre slovo v riadku
            #random rozhodnutie o prehadzovani pismen
            prehadzovanie_pismen = random.choice(ano_nie)

            #podmienka na prehadzanie pismen opacne
            if prehadzovanie_pismen == 1:
                nove_slovo = slovo[::-1]
                novy_riadok.append(nove_slovo)
            else:
                novy_riadok.append(slovo)

        #podmienka na prehadzanie slov
        if prehadzovanie_slov == 1:
            random.shuffle(novy_riadok)
            riadocek2 = " ".join(novy_riadok)
            
        else:
            riadocek2 = " ".join(novy_riadok)

        #vlozenie do noveho suboru
        novy_subor.append(str(riadocek2)+"\n")

        #vyprazdenie zoznamu
        novy_riadok.clear()

    #zamiesanie suboru    
    random.shuffle(novy_subor)

#vypisanie finalneho vysledku
print("".join(novy_subor))

#zatvorenie suboru   
subor1.close()
