# Go - Google App Engine

.fx: first

Emre Can Yılmaz `<ecylmz@bil.omu.edu.tr>`

[http://ecylmz.com/](http://ecylmz.com)

Ekim 2012

---

##  Geliştirme Ortamı

-   Go Software Development Kit (SDK), App Engine platformunun bir kopyasını
  bilgisayarınızda kurmanızı sağlar

-   Go SDK indirilir:

           https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Go

-   İndirilen zip dosyayı `/opt` altına çıkar:

        !sh
        # Önce /opt için izinleri ayarla
        $ sudo chgrp $USER /opt
        $ sudo chmod g+w /opt

        # Unzip ile zip dosyasını aç
        $ cd /opt/ && unzip go_appengine*

---

##  Path'i Ayarla

App Engine betiklerini çalıştırmak için path ayarlanır

-   `$HOME/.bashrc` dosyasının içine

        !sh
        export PATH=/opt/google_appengine:$PATH

-   [19/x](https://github.com/00010011/x) kullanıcılar ise `$HOME/etc/init/270-local` dosyasının içine

        !sh
        export PATH=/opt/google_appengine:$PATH

---

##  Yapılandırma Dosyası

Yapılandırma dosyası uygulama dizinin içerisinde bulunur

Örnek:

        !text
        application: kavak
        version: 1
        runtime: go
        api_version: go1

        handlers:
        - url: /favicon\.ico
          static_files: favicon.ico
          upload: favicon\.ico

        - url: /.*
          script: _go_app

---

##  Uygulamayı Çalıştır

-   Uygulama dizini içerisindeyken:

        !sh
        $ dev_appserver.py .

-   Web tarayıcısında [http://localhost:8080](http://localhost:8080]) açılır

---

##  Tekrarlı Geliştirme

-   Kaynak kodda değişiklik olduğunda uygulamayı yeniden başlatmaya gerek yok

-   [http://localhost:8080](http://localhost:8080]) yeniden yüklemek yeterli

---

##  Yükleme Öncesi

-   Uygulamayı [https://appengine.google.com/](https://appengine.google.com/) adresinden kaydettir

-   `app.yaml` içini `application: uygulama_adı` olacak şekilde ayarla

---

##  Karşıya Yükleme

-   Uygulama dizini içerisindeyken

        !sh
        $ appcfg.py update .
