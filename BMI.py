import tkinter
from tkinter import *
import string


window = Tk()
window.minsize(width=250,height=200)
window.title("BMI")

def hesapla():
    #fonksiyon içinde fonksiyon dışındaki bir değişkeni değiştirmek için global kullanmalıyız yoksa localde yani fonksiyon içinde sadece değişir.
    global text2
    global text1




    if my_entry1.get() == "" and my_entry2.get() == "":
        text2 = "değer girin"
        text1 ="!!"
    elif my_entry2.get() == "0" or my_entry1.get() == "0":
        text2 = "değer olarak 0 atamayın"
        text1 = "!!"
    elif my_entry1.get() == "":
        text2 = "boy girin"
        text1 = "!!"
    elif my_entry2.get() == "":
        text2 = "kilo girin"
        text1 = "!!"
    #elif any    (char     in    list_letters    for   char   in      my_entry1.get()):
    # any komutu ile içindekilerini kontrol eder
    #char bir değişkendir ne dediğiniz önemli değil a,b,c,ali,veli123 de diyebiliriz
    # in içinde olup olmadığını sorgulamak için gerken
    # list letters büyük v küçük harflerden oluşan listemiz string mödülü ile oluşturdum aşağıda değişkenlerde gözüküyor.
    #for list letter içinde dolaşamızı sağlıyor  ve char bu liste içindeki her bir eleman için atadığımız vekil değişken .
    #my_entry1-2.get() entryden aldığımız değer
    #for döngüsünü kullanıyoruz : char(vekil-geçici değişken istediğiniz harf ismi verebilirsiniz) -in list_letter(içindeki her elemana vekili ata)  for char in my_entry1-2.get() (ve şunu yap ,burdada eğer list_letter listesindeki herhangi bir eleman my_entryden gelenin içinde bulunuyorsa true bulunmuyorsa false)
    #eğer herhangi bir harf bulunuyorsa true bulunmuyorsa false döndürüyor true döndürürse hata mesajı çıkıyor chatgpt den yardım aldım fakat herhangi bir kutu içerisine sadece harf yazıp digerine sayı yazarsam sadece alabılıyorum harf hatasını birine harf birine boşluk birakınca olmuyor.

    elif any(letter in list_letters for letter in my_entry2.get()):
        text2 = "harf girmeyin"
        text1 = "!!"
    elif any(letter in list_letters for letter in my_entry1.get()):
        text2 = "harf girmeyin"
        text1 = "!!"





    elif my_entry2.get() != "" and my_entry1.get() != "" and my_entry1 not in (list_letters) and my_entry2 not in (list_letters):




        a = my_entry2.get()
        b = my_entry1.get()

        a = float(a)
        b = float(b)
        text1 = a / (b ** 2)




        if text1 < 18.5:
            text2 = "zayıf"
        elif text1 > 18.5 and text1 < 24.9:
            text2 = "normal"
        elif text1 > 25 and text1 < 29.9:
            text2 = "kilolu"
        elif text1 > 29.9 and text1 < 34.9:
            text2 = "obez"


    my_label3.config(text=f"{text1}\n{text2}")









#variables değişkenler
list_letters = list(string.ascii_letters)
list_specialcharacter = list(string.punctuation)
list_specialcharacter.remove(".")
text1 = 0
text2 = "a"

#labels satırlar
my_label1 = tkinter.Label(text="Boy metre cinsinden")
my_label2 = tkinter.Label(text="Kilo kg cinsinden")
my_label3 = tkinter.Label(text="Sonuç")

#entrys

my_entry1 = tkinter.Entry(width=25)
my_entry1.config()
my_entry2 = tkinter.Entry(width=25)
my_entry2.config()


#button
my_button = tkinter.Button(text="Hesapla",command=hesapla)

#locations
my_label1.pack(pady=10)
my_entry1.pack()
my_label2.pack(pady=10)
my_entry2.pack()
my_button.pack(pady=10)
my_label3.pack()









window.mainloop()