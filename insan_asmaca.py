# Problem Set 2, insan_asmaca.py
# İsim: 
# Katkıda bulunanlar:
# Harcanan Zaman:

# İnsan Asmaca Oyunu
# -----------------------------------
# Yardımcı kod
# Bu yardımcı kodu anlamanıza gerek yok,
# fakat fonksiyonları nası kullanacağınız bilmeniz
# gerekiyor.
# (öğrenmek için fonksiyon dizelerini okuyun!)
import random
import string
import pandas as pd

KELIME_LISTESI_DOSYASI = "tdk_sozcukler2.csv"
TÜRKÇE_ALFABE = 'abcçdefgğhıijklmnoöprsştuüvyz'

def kelimeleri_yükle():
    """
    Geçerli kelimelerin bir listesini döndürür. 
    Kelimeler, küçük harflerden oluşan dizelerdir.
    
    Sözcük listesinin boyutuna bağlı olarak, bu işlevin 
    tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi okunuyor...")
    # dosyanın okunması
    dosya = pd.read_csv("tdk_sozcukler2.csv")
    # sözcüklerin küçük harfe çevrilmesi
    dosya['SOZCUKLER'] = dosya['SOZCUKLER'].str.lower() 
    # wordlist: list of strings
    kelime_listesi = dosya['SOZCUKLER'].tolist()
    print(f"{len(kelime_listesi)} kelimelik liste hazırlandı.")
    return kelime_listesi


def kelime_seç(kelime_listesi):
    """
    kelime_listesi (liste): kelimelerin listesi (dize)
    
    Kelime listesinde rastgele bir keliem döndürür.
    """
    return random.choice(kelime_listesi)

# yardımcı kodların sonu

# -----------------------------------

# Programın herhangi bir yerinden erişilebilmesi için kelime 
# listesini değişken kelime_listesine yükleyin
kelime_listesi = kelimeleri_yükle()


def kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: boolean, gizli_kelime'nin tüm harfleri tahmin_edilen_harfler içindeyse True; 
        aksi takdirde False
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass



def tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize, harflerden oluşur, alt çizgiler (_) ve gizli_kelime içindeki hangi harflerin 
        şimdiye kadar tahmin edildiğini temsil eden boşluklardan oluşur.
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass



def uygun_harfleri_al(tahmin_edilen_harfler, alfabe = TÜRKÇE_ALFABE):
    '''
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize (harfler), Henüz tahmin edilmemiş harfleri temsil 
        eden harflerden oluşur.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass
    
    

def insan_asmaca(gizli_kelime, alfabe = TÜRKÇE_ALFABE):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar

    Etkileşimli bir İnsan Asmaca oyunu başlatır.
    
     * Oyunun başında kullanıcıya gizli_kelime'nin kaç harf içerdiğini 
       ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin yaptğını ve henüz tahmin 
       etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin yapmasını isteyin. Kullanıcının 
       bir harf yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, tahminlerinin bilgisayarın kelimesinde görünüp görünmediğine 
       dair her tahminden hemen sonra geri bildirim almalıdır.

     * Her tahminden sonra, kullanıcıya o ana kadar kısmen tahmin edilen 
       kelimeyi göstermelisiniz.
    
    Problem yönergesinde detaylandırılan diğer sınırlamaları takip edin.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass



# insan_asmaca fonksiyonunuzu tamamladıktan sonra bu dosyanın en altına inin
# ve kodunuzu test etmek için ilk iki yorum satırının yorum işaretlerini kaldırın.
# (ipucu: kendi testinizi yaparken kendi gizli_kelimenizi'ünüzü seçmek 
# isteyebilirsiniz)


# -----------------------------------



def boşluklarla_eşleştir(benim_kelimem, diğer_kelime):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    diğer_kelime: dize, normal Türkçe kelime
    döndürdüğü: boolean, eğer benim_kelimem'in tüm gerçek harfleri 
       diğer_kelime'nin karşılık gelen harfleriyle eşleşiyorsa veya 
       harf özel sembol _ ise ve benim_kelimem ve diğer_kelim aynı 
       uzunluktaysa True; aksi takdirde False. 
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass



def olası_eşleşmeleri_göster(benim_kelimem):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    döndürdüğü: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen her kelimeyi 
             yazdırmalıdır. Ekranda bir harf tahmin edildiğinde, o harfin gizli kelimede 
             geçtiği tüm pozisyonların ortaya çıktığını unutmayın. Bu nedenle, 
             gizli harf (_) zaten açığa çıkmış kelimedeki harflerden biri olamaz.
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass



def ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    
    Etkileşimli bir İnsan Asmaca oyunu başlatır.
    
     * Oyunun başında kullanıcıya gizli_kelime'nin kaç harf içerdiğini 
       ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin yaptğını ve henüz tahmin 
       etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin yapmasını isteyin. Kullanıcının 
       bir harf yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, tahminlerinin bilgisayarın kelimesinde görünüp görünmediğine 
       dair her tahminden hemen sonra geri bildirim almalıdır.

     * Her tahminden sonra, kullanıcıya o ana kadar kısmen tahmin edilen 
       kelimeyi göstermelisiniz.
     
     * Tahmin, * sembolüyse, kelime listesindeki mevcut tahmin edilen kelimeyle 
       eşleşen tüm kelimeleri yazdırın.
    
    Problem yönergesinde detaylandırılan diğer sınırlamaları takip edin.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass


# ipuçlarıyla_insan_asmaca fonksiyonunu tamamladıktan sonra, yukarıdaki
# insan_asmaca fonksiyonundakine benzer şekilde iki yorum satırının yorum
# işaretlerini kaldırıp dosyayı çalıştırarak kodunuzu test edin.
# ipucu: kendi testinizi yaparken kendi gizli_kelimenizi'ünüzü seçmek 
# isteyebilirsiniz


if __name__ == "__main__":
    pass

    # Bölüm 2'yi test etmet için, yukarıdaki "pass" satırına yorum işaretini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.
    
    #gizli_kelime = kelime_seç(kelime_listesi)
    #insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines.
    # Bölüm 3'ü test etmek için yukarıdaki satırlara yeniden yorum işaretlerini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.
    
    #gizli_kelime = kelime_seç(kelime_listesi)
    #ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)