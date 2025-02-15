# Girilen en az üç basamaklı bir tamsayının tüm bölenlerini hesaplayan kod
# Sınırlılıklar:
# 1) Öncelikle, girilen değerin bir tamsayı olup olmadığının kontrolü
# 2) Eğer tamsayı değeri girilmişse bu tamsayının en az 3 basamaklı bir
# tamsayı olup olmadığının kontrolü

sayi = input("Lütfen bir tamsayı giriniz: ")

try:
    if sayi.lstrip('-').isdigit():#girilen sayının tamsayı olup olmadığını kontrol ediyoruz
        my_num = int(sayi) # girilen değeri int tipine dönüştürdük
        if my_num>100:
            bolenler = []
            sayac = 0
            for i in range(1,my_num):
                if my_num%i==0:
                    sayac = sayac + 1
                    #sayac+=1
                    bolenler.append(i)
            print(f"{sayi} sayısının {sayac} adet böleni bulundu")
            for sayilar in bolenler:
                print(sayilar)
        else:
            print("Lütfen 100'den büyük bir tamsayı giriniz")

except Exception as e:
    print(f"Hata = {e}")

# Lütfen bir tamsayı giriniz
#------------------------------------------------------




# Bir Türkçe cümledeki Türkçe karakterleri İngilizcedeki karşılıkları ile
# değiştiren kod

# Yöntem-1 (replace ile)
my_sentence = "Orta Çağ Dönemi, KİLİSE'nin aşırı despot ve katı tutumuyla insanları yaşadığına pişman eden, üzen karanlık bir dönemdir"

print(f"Cümlenin Orijinal Hali\n{my_sentence}")

my_sentence = my_sentence.replace("Ç","C").replace("ö","o")

print("*"*50)
print(f"\nCümlenin İşlenmiş Hali\n = {my_sentence}")
#------------------------------------------------------



#Yöntem-2 (Dictionary veri yapısı ile)

my_sentence = "Orta Çağ Dönemi, KİLİSE'nin aşırı despot ve katı tutumuyla insanları yaşadığına pişman eden, üzen karanlık bir dönemdir"

print(f"Cümlenin Orijinal Hali\n{my_sentence}")


translate_turkish_to_english = {
    'Ç':'C', 'ç':'c', 'İ':'I', 'ı':'i', 'Ğ':'G','ğ':'g',
    'Ö':'O', 'ö':'o', 'Ü':'U', 'ü':'u', 'Ş':'S', 'ş':'s'
}

print("*"*50)

for turkish_character, english_character in translate_turkish_to_english.items():
    my_sentence = my_sentence.replace(turkish_character, english_character)

print(f"\nCümlenin İşlenmiş Hali\n = {my_sentence}")

#--------------------------------------------------------



calisanlar = {"maas":[100000,55250,38960,205450,75893,45632]}

# maas sütünundaki değerleri bir değişkene atıyoruz
salary_values = calisanlar["maas"]

zamli_maas = []

for orijinal_maas in salary_values:
    zamli_maas.append(orijinal_maas*1.4)

print(f"Çalışanların İlk maaşları = {salary_values}")
print(f"Çalışanların Zamlı maaşları = {zamli_maas}")