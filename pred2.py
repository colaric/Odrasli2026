# spremenjivke

starost = 30
password = "ejk9012ej1209j"
resnica = True # /False

# print()
print(starost, password)

# seznami / list

# povprecje višin dijakov v razredu

visine = [180, 210, 160, 170, 194, 170] # seznam celih števil / integer list
print(visine)
# dostop do indeksev seznama
print(visine[0])
print(visine[len(visine)-1])
print(len(visine))
print(max(visine))
print(sum(visine))

# povprecje višin dijakov v razredu

visine = [180, 210, 160, 170, 194, 170]
povprecje = sum(visine) / len(visine)
print(povprecje)

ime = "Aleksander Veliki€"
print(ime[0])
print(ime[-1])
ime = ['A', 'l', 'e', 'k', 's', 'a', 'n', 'd', 'e', 'r', ' ', 'V', 'e', 'l', 'i', 'k', 'i']
print(ime[0])
print(ime[-1])
ime[0] = "B"
print(ime)


# If statement; pogojni/vejitveni stavki

# izpiši, če je oseba polnoletna ali ni


# starost = input("Vnesi svojo starost")

# if pogoj:
#   koda1
#   koda2
#koda3
starost = 18
if starost >= 18:
    print("Oseba je polnoletna")
else:
    print("Oseba ni polnoletna")
    print("Dober dan")
#

ocena = 100
if ocena >= 90:
    print("Odlično")
elif ocena >= 80:
    print("Prav dobro")
elif ocena >= 70:
    print("Dobro")
else:
    print("Nezadostno")


# gnezdeni if stavki

temperatura = 25
vlaznost = 60
veter = 40
if temperatura > 20:
    if vlaznost > 50:
        print("Toplo in mokro")
    else:
        print("Toplo in suho")
else:
    print("Hladno")

# logični način
temperatura = 25
vlaznost = 50

if temperatura >= 25 and vlaznost <= 50:
    print("Toplo in suho")
elif temperatura >= 25 and vlaznost >= 50:
    pass

else:
    print("Hladno")