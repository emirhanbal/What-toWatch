import requests
from bs4 import BeautifulSoup
import random
#projede kullanacağımız modülleri import ediyoruz
imdburl = "https://www.imdb.com/chart/top"
#veriyi çekmek istediğimiz sitenin urlsini tanımladık
r = requests.get(imdburl)
soup = BeautifulSoup(r.content,"html.parser")
filmdata = soup.find_all("table",{"class" : "chart full-width"})
#ulaşmak istediğimiz veriler chart full-width classında bulunduğu için bu class'ı arattık.
filmlist=[]
#aldığımız verileri bir listede tutacağımız için boş bir liste oluşturduk.
# print(filmdata)
#aldığımız chart full-width classındaki tüm veriyi yazdırdık.
# print(len(filmdata))
#chart full-width class'ından 1 adet olduğu için 1 sonucunu verdi.
# print(filmdata[0].contents)
#listemiz 1 elemanlı olduğu için 0. elemanı aldık ve bunun alt başlıklarını gösterdi.
# print(len(filmdata[0].contents))
#\n gibi satır atlama komutlarını da eleman olarak algıladığı için fazla eleman çıktısı verdi.
filmtable = (filmdata[0].contents)[len(filmdata[0].contents)-2]
#ulaşmak istediğimiz tablo listenin sondan 2.elemanı olduğu için len-2 ile tablomuza ulaştık.
# print(filmtable)
#doğru sonuca ulaşabildik mi diye kontrol ediyoruz.
filmtable = filmtable.find_all("tr")
#almak istediğimiz filmler <tr> başlığının altında olduğu için tüm tr'leri bulduk.
for film in filmtable:
    #bunu bir for döngüsene sokarak filmlerin olduğu trlere tek tek ulaştık.
    filmtitle = film.find_all("td",{"class" : "titleColumn"})
    filmtitleimdb = film.find_all("td",{"class":"ratingColumn imdbRating"})
    #film isimleri td başlığının altındaki titlecolumn'da bulunduğu için buraya eriştik.
    #ulaşmak istediğimiz diğer veri IMDB puanı olduğu için aynı işlemi ratingColumn imdbRating için de yapıyoruz.
    # print(filmtitle)
    #böylece filmlerin isimlerini yazan paragrafa ulaşabildik.
    filmnames = filmtitle[0].text
    filmimdb = filmtitleimdb[0].text
    # print(filmimdb)
    # print(filmnames)
    #filmlerin direkt olarak isimlerini elde ettik.
    filmnames = filmnames.replace("\n","")
    filmimdb = filmimdb.replace("\n","")
    #\n gibi satır atlama komutlarını boşlukla değiştiriyoruz.
    #print(filmnames)
    filmlist.append(filmnames+ " " +filmimdb)
    #film isimlerini ve imdb puanlarını listemize birleştirip ekliyoruz.

def bringthemovie():
    randomfilms=random.choice(filmlist)
    print(randomfilms)
bringthemovie()
#kodumuzun çalışıp çalışmadığını görmek için bir fonksiyon oluşturuyoruz ve çalıştırıyoruz.
