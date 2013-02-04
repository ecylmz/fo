#   BigBlueButton Kurulumu

.fx: first

ecylmz `<ecylmz@bil.omu.edu.tr>`

http://ecylmz.com/

Şubat 2013

---

#   Kuruluma Başlamadan Önce

Kurulum için Ubuntu 10.04 32-bit veya 64 bit gerekli

**Sistem Gereksinimleri**

-   2 GB RAM(4 GB İdealdir)
-   Dual-core 2.6 GHZ CPU
-   80, 1935, 9123 portları ulaşılabilir olmalı.
-   Port 80 diğer uygulamalar tarafından kullanılmamalı
-   50 GB boş alan

Ek olarak ortam dili `en_US.UTF-8` olmalıdır.

---

#   Sunucuyu Güncelle

        !sh
        # BigBlueButton anahtarını ekle
        $ wget http://ubuntu.bigbluebutton.org/bigbluebutton.asc -O- | sudo apt-key add -

        # BigBlueButton deposunu ekle
        $ echo "deb http://ubuntu.bigbluebutton.org/lucid_dev_08/ bigbluebutton-lucid main" | sudo tee /etc/apt/sources.list.d/bigbluebutton.list

        # Güncelleştirme başlasın
        $ sudo apt-get update
        $ sudo apt-get dist-upgrade

---

#   Gerekli Paketleri Yükle

Ruby kurmak için gerekli paketleri Yükle:

        !sh
        $ sudo apt-get install zlib1g-dev libssl-dev libreadline5-dev libyaml-dev\
        build-essential bison checkinstall libffi5 gcc checkinstall libreadline5 libyaml-0-2

---

#   Ruby Kur

install-ruby.sh adında dosya oluşturup aşağıdaki kodları yazın:

.code: code/install-ruby.sh

---

#   Ruby Kur

Betiği çalıştır:

        !sh
        $ chmod +x install-ruby.sh
        $ ./install-ruby.sh

---

#   BigBlueButton Kur

        !sh
        $ sudo apt-get install bigbluebutton

---

#   API Demolarını Kur

Bu sadece test içindir, kurma zorunluluğu yok

        !sh
        $ sudo apt-get install bbb-demo

Kaldırmak isterseniz:

        !sh
        $ sudo apt-get purge bbb-demo

---

#   Yeniden Başlat

BigBlueButton'ın sorunsuz şekilde başlatıldığından emin olmak için:

        !sh
        $ sudo bbb-conf --clean
        $ sudo bbb-conf --check

---

#   Kaynak

- [http://code.google.com/p/bigbluebutton/wiki/InstallationUbuntu#Installation_of_BigBlueButton_0.80](http://code.google.com/p/bigbluebutton/wiki/InstallationUbuntu#Installation_of_BigBlueButton_0.80)
