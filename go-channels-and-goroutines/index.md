#   Go - Channels ve Goroutines

.fx: first

ecylmz `<ecylmz@bil.omu.edu.tr>`

http://ecylmz.com/

Şubat 2013

---

##  Goroutines

-   Program içinde bağımsız thread'lerin çalışmasıdır
-   Arkaplanda iş yapılmak istenildiğinde kullanılır
-   Fonksiyonun başına `go` anahtar kelimesi getirilerek kullanılır

---

##  Channels

-   Channel veri yapısının iki ana işlevi: "okuma ve yazma"
-   Channel haberleşmede kullanılır
-   Birinin channel'dan okuma yapması için, birinin de channel'a yazması
    gereklidir (buffer kullanılmamışsa)
-   Channel'dan okuma yapmak istenirse, yazar işini bitirene kadar uygulama
    bekler.

---

##  Örnek

**Amaç:** Verilen `count`(N) sayıyı `start` değerinden başlayarak ekrana yazdırma

---

##  Klasik Çözüm

        !go

        package main

        import "fmt"

        func printNumbers(start, count int) {
                for i := 0; i < count; i++ {
                        fmt.Printf("%d\n", start+i)
                }
        }

        func main() {
                printNumbers(3, 5)
        }

---

#   Goroutines ve Channels ile

---

##  Sayı Üretici

        !go

        package main

        import "fmt"

        func numberGen(start, count int, out chan<- int) {
                for i := 0; i < count; i++ {
                        out <- start + i
                }
                close(out)
        }

---

##  Sayı Üretici

`numberGen` fonksiyonu 3 argüman almakta:

`start`: Üretilmeye başlanacak ilk sayı
`count`: Üretilecek sayı adeti
`out`: Channel'a verilecek sayı

-   Numaraları doğrudan basmak yerine, çıkışı `<-` ile out channel'ına veriyor
-   Birisi `out` channel'ını okuyana kadar döngü devam etmez
-   `out` channel'ı okunduktan sonra kalınan yerden devam edilir
-   `close(out)` ile channel kapatılır
-   Eğer `out` channel'ı kapatılmasaydı, bütün goroutine'leri uykuya geçebilirdi(deadlock)

---

##  Sayı Tüketici

        !go

        func printNumbers(in <-chan int, done chan<- bool) {
                for num := range in {
                        fmt.Printf("%d\n", num)
                }
                done <- true
        }

---

##  Sayı Tüketici

`printNumbers` fonksiyonu 2 argüman almakta:

`in`: Channel'a girilen sayı
`done`: fonksiyonun dönüş değeri için boolean değer

-   Fonksiyonun tek işlevi `in` channel'ındaki sayıyı ekrana basmak
-   Döngüdeki `in` channel'ı kapanırsa döngü sonlanır
-   `done` channel'ı bütün işler bittiğinde ana programı sonlandırmak içindir

---

##  Main

        !go

        func main() {
                numberChan := make(chan int)
                done := make(chan bool)
                go numberGen(1, 10, numberChan)
                go printNumbers(numberChan, done)

                <-done
        }

---

##  Main

-   `make` fonksiyonu kullanılarak gerekli channel'lar ilklenir
-   goroutine'leri go anahtar kelimesiyle ardı ardına başlatılır
-   Eğer `done` channel'ı olmazsa bütün sayıların ekrana basılacağı garanti edilemezdi

---

##  Kurcala

-   Aşağıdaki linkten kodu inceleyip, kurcalayıp, çalıştırabilirsin:

[http://play.golang.org/p/v-FsYAxohb](http://play.golang.org/p/v-FsYAxohb)

---

##  Kaynak

[http://jnwhiteh.net/posts/2010/09/go-examples-1-channels-and-goroutines.html](http://jnwhiteh.net/posts/2010/09/go-examples-1-channels-and-goroutines.html)

