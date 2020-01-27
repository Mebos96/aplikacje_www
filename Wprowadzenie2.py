#Zad1
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def funkcja(a_list, b_list):
    wynik=[]
    for i in range(0,len(a_list),2):
        wynik.append(i)
    for j in range(1,len(b_list),2):
        wynik.append(j)
    return wynik
# print(funkcja(list1,list2))

#Zad2
tekst2="Bartek jest super"
def funkcja2(data_text):
    letters=[]
    for i in data_text:
        letters.append(i)
    return {"length":len(data_text),"letters":letters,"big_letters":data_text.upper(),"small_letters":data_text.lower()}
# print(funkcja2(tekst2))

#Zad3
tekst3="Passat jest fajny"
letter3='s'
def funkcja3(text,letter):
    wynik=''
    for i in text:
        if i != letter:
            wynik+=i
    return wynik
# print(funkcja3(tekst3,letter3))

#Zad4
def funkcja4(temperature,temperature_type):
    types=["fahrenheit","rankine","kelvin"]