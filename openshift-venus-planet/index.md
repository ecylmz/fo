#   OpenShift Venus Planet

.fx: first

ecylmz `<ecylmz@bil.omu.edu.tr>`

http://ecylmz.com/

Nisan 2013

---

#   Venus Nedir?

- Harika bir blog birleştiricisidir
- Yeni girdileri tek sayfa halinde size sunan bir sistemdir
- Daha fazla bilgi: [http://intertwingly.net/code/venus/docs/index.html](http://intertwingly.net/code/venus/docs/index.html)

---

#   OpenShift'te Çalıştırma

**PHP uygulaması oluştur:**

        !sh
        $ rhc app create -a gezegen -t php-5.3

**Cron desteği ekle:**

        !sh
        $ rhc app cartridge add -a gezegen -c cron-1.4

---

**Ana depoyu ekle:**

        !sh
        cd gezegen
        rm -f php/index.php
        git remote add upstream -m master
        git://github.com/jasonbrooks/venus-openshift-quickstart.git
        git pull -s recursive -X theirs upstream master

---

#   Özelleştir

        !sh
        $ $EDITOR libs/planet.ini

---

#   Aktifleştir

Yapılandırmaları komitle:

        !sh
        $ git commit -a -m "customized planet config"

OpenShift'e gönder:

        !sh
        $ git push

---

#   Sonuç

**Gezegen hazır:** http://gezegen-$yournamespace.rhcloud.com

**Alias Ekle:**

        !sh
        $ rhc alias add gezegen gezegen.example.com

Alan adınızın DNS ayarlarına değeri `http://gezegen-$yournamespace.rhcloud.com`
  olan CNAME kaydını girmeyi unutmayın!

---

#   Kaynaklar

-   [https://github.com/jasonbrooks/venus-openshift-quickstart](https://github.com/jasonbrooks/venus-openshift-quickstart)
-   [http://intertwingly.net/code/venus/docs/index.html](http://intertwingly.net/code/venus/docs/index.html)

