#Zad1
lorem="Lorem Ipsum jest tekstem " \
      "stosowanym jako przykładowy wypełniacz" \
      " w przemyśle poligraficznym. Został po " \
      "raz pierwszy użyty w XV w. przez nieznanego" \
      " drukarza do wypełnienia tekstem próbnej książki." \
      " Pięć wieków później zaczął być używany przemyśle " \
      "elektronicznym, pozostając praktycznie niezmienionym. " \
      "Spopularyzował się w latach 60. XX w. wraz z publikacją " \
      "arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a" \
      " ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem" \
      " przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

#Zad2
imie="Bartosz"
nazwisko="Adamczuk"
litera_1=imie[2]
litera_2=nazwisko[3]
liczba_liter1=lorem.count(litera_1)
liczba_liter2=lorem.count(litera_2)
# print("W tekście jest %i liter %s oraz %i liter %s" %(liczba_liter1,litera_1,liczba_liter2,litera_2))

#Zad4
# print(dir(lorem))
# help(lorem.upper())

#Zad5
# print(nazwisko[::-1].capitalize(),imie[::-1].capitalize())

#Zad6
lista1 = list(range(1,11))
lista2 = lista1[5:10]
lista1=lista1[0:5]

#Zad7
lista3=lista1+lista2
lista3.insert(0,0)
lista4=lista3.copy()
# print(sorted(lista4,reverse=True))

#Zad8
krotka=(
    ((1234),("Adam Małysz ")),
    ((567),("Mateusz Włucznikowski ")),
    ((12345),("Andrzej Duda")),
)

#Zad9
slownik={1234:"Adam Małysz",567:"Mateusz Włucznikowski",12345:"Andrzej Duda"}
# print(slownik)

#Zad10
lista=[123,123,345]
s=set(lista)

#Zad11
# for i in range(1,10):
#     print(i)

#Zad12
# for j in reversed(range(20,100,5)) :
#     print(j)

#Zad13
listaa=[{1234:"Adam Małysz"},{567:"Mateusz Włucznikowski"},{12345:"Andrzej Duda"}]
index=0
for i in listaa:
    print(index,":",i)
    index+=1
