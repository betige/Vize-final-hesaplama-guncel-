soru_1 = int(input ("vize notunu girer misin?"))
soru_2 = int(input ("final notunu girer misin?"))

geçme_notu = 57
vize = soru_1  * 0.4 
final = soru_2 * 0.6
toplam_puan = vize + final
print("Ortalaman: ", toplam_puan)


if toplam_puan >= 90 :
    print("AA")
elif toplam_puan >=85 :
    print("BA")
elif toplam_puan >= 80 :
    print("BB")
elif toplam_puan >= 75 :
    print("CB")
elif toplam_puan >= 70 :
    print("CC")
elif toplam_puan >= 60 :
    print("DC")
elif toplam_puan >= 55 :
    print("DD")
else :
    print("FF")
if toplam_puan >= geçme_notu :
  print("geçtin bravo")
  
else :
   print("üzülme diğer sefere düzeltirsin ")
   
   
print (soru_1)
print (soru_2)
print(geçme_notu)
