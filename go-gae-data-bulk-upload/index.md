#   Go Gae Data Bulk Upload

.fx: first

ecylmz `<ecylmz@bil.omu.edu.tr>`

http://ecylmz.com/

Aralık 2012

---

##  Remote Api

-   Toplu halde yükleme yapmak için `remote api` etkinliştirmek gereklidir.

-   Uygulama dizininde bulunan `app.yaml` dosyasına aşağıdaki satırlar eklenir:

        !yaml
        - url: /remote_api
          script: $PYTHON_LIB/google/appengine/ext/remote_api/handler.py

---

##  Model Dosyası

-   Uygulama dizininde `models.py` adında dosya oluşturulur.

    Person Modeli İçin:

    .code: code/models.py

    CSV'deki sütunların sırası buradakiyle aynı olmalıdır.

---

##  Yükleyici Sınıfı

-   Uygulama dizininde `person_loader.py` adında dosya oluşturulur.

    Örnek Yükleyici Sınıfı:

    .code: code/person_loader.py

---

##  Örnek CSV

-   CSV sütunları kodda tanımlanan sırada olmalı:

    .code: code/person.csv

---

##  Yükleme Komutu

- Yukarıdaki adımlar tamam ise aşağıdaki komut uygulanır:

        !sh
        $ appcfg.py upload_data --config_file=person_loader.py \
        --filename=person.csv --kind=Person \
        http://your_app_id.appspot.com/remote_api

---

##  Kaynak

- [https://developers.google.com/appengine/docs/python/tools/uploadingdata](https://developers.google.com/appengine/docs/python/tools/uploadingdata)
