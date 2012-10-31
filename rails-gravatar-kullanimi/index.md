# Rails'te Gravatar Kullanımı

.fx: first

ecylmz `<ecylmz@bil.omu.edu.tr>`

[http://ecylmz.com/](http://ecylmz.com/)

Kasım 2012

---

##  Gem'i Yükle

-   Gemfile'a aşağıdaki satırı ekle:

        !ruby
        gem 'gravtastic'

-   Yükle ve aktif et:

        !sh
        # proje dizini içerisindeyken
        $ bundle install

---

##  Modeli Düzenle

        !ruby
        class User < ActiveRecord::Base
          include Gravtastic
          gravtastic
        end

##  Kullanım

-   Örnek 1: default değerlerle kullanımı

        !ruby
        <%= image_tag @user.gravatar_url %>

-   Örnek 2: https ile kullanımı

        !ruby
        <%= image_tag @user.gravatar_url(:secure => true) %>

##  Default Değerleri Değiştir

User modeli içerisinde:

        !ruby
        gravtastic secure:   true,
                   filetype: :jpg,
                   size:     120,
                   default:  "identicon"

##  Kaynak

[https://github.com/chrislloyd/gravtastic/blob/master/README.md](https://github.com/chrislloyd/gravtastic/blob/master/README.md)
