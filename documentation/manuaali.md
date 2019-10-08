# Käyttöohjeet

## Kirjautumaton käyttäjä
Kirjautumaton käyttäjä voi tarkastella tietokannassa olevia urheiluseuroja, rajata niitä eri hakukriteerein ja katsoa muiden käyttäjien kirjoittamia arvosteluja. 

### Seurojen listaaminen ja järjestäminen
Kaikkien urheiluseurojen listaaminen onnistuu yläpalkin _List sport clubs_ -painikkeella.
Napista aukeaa näkymä, joka listaa tietokannan kaikki seurat parhaimmat arvosanat saaneista huonompiin ja arvostelemattomiin. Yläreunassa on palkki, jossa olevilla napeilla seuroja voi järjestää eri tavoin. _Name_ ja _City_ järjestävät seurat aakkosjärjestykseen seuran nimen tai kaupungin mukaan. _Price_-napista voi järjestää seurat hinnan perusteella pienimmästä suurimpaan tai toisinpäin. _Score_-taas palauttaa alkuperäisen arvosteluihin perustuvan järjestyksen.

### Seurojen hakeminen hakukriteerein
Liikuntaseurojen tarkempaan hakuun päästään yläpalkin painikkeella _Search_. Aukeavaan lomakkeeseen voidaan täyttää halutut kohdat, joiden mukaan hakutuloksia halutaan rajata. Esimerkiksi Tampereella sijaitsevat urheiluseurat, joissa voi harrastaa nyrkkeilyä haetaan kirjoittamalla kohtaan _City_ "Tampere" ja kohtaan _Available sport_ "Nyrkkeily". Kenttiä voi jättää tyhjäksi.

### Seuran tarkempien tietojen tarkastelu
Seurojen listaaminen ja haku tuottaa joukon kortteja, jotka sisältävät joitakin tietoja seurasta, kuten nimen ja paikkakunnan. Tarkempia tietoja pääsee tarkastelemaan klikkaamalla kortin alareunassa olevaa _Info_-painiketta. Aukeaa näkymä, jossa näkyy aiempien tietojen lisäksi saatavilla olevien liikuntamuotojen määrä. Napista _Available sports_ tulevat seuran kaikki liikuntamuodot näkyviin ja napista _Contact information_ seuran yhteystiedot.

### Seuran arvostelujen tarkastelu
Kortin alareunassa on _Info_-painikkeen lisäksi _Show reviews_ painike, josta avautuu lista kaikista seuran arvosteluista. Uusin tai viimeksi editoitu arvostelu näkyy ensimmäisenä. Arvostelussa näkyy arvostelijan nimimerkki, arvosana, sanallinen arvio ja kirjoitusajankohta.  

### Uuden käyttäjän luominen
Yläpalkin oikeasta reunasta painetaan _Login_-painiketta, josta päästään kirjautumissivulle. Sivulla painetaan kohtaa _New User_, josta aukeaa lomakesivu uuden käyttäjän luontiin. Kaikki kentät ovat pakollisia. Nimimerkin ja sähköpostin tulee olla uniikkeja ja sovellus ilmoittaa jos ne löytyvät jo tietokannasta. Sovellus ilmoittaa myös, jos syötetyt merkkijonot ovat liian pitkiä. Tässä kohtaa myös valitaan käyttärooli. Roolilla _User_ käyttäjä voi kirjoittaa arvosteluja liikuntaseuroista, sekä tarvittaessa editoida ja poistaa näitä. Roolilla _Owner_ käyttäjä voi luoda uusia liikuntakeskuksia, editoida näiden yhteystietoja ja saatavilla olevia liikuntamuotoja. Arvostelujen tekeminen ei onnistu.

### Sisäänkirjautuminen
Käyttäjän luomisen jälkeen avautuu kirjautumissivu suoraan. Tähän kirjoitetaan nimimerkki ja salasana ja painetaan _Login_ -painiketta. Jos nimimerkki ja salasana löytyvät tietokannasta ja täsmäävät, pääsee käyttäjä kirjautumaan sisään. Kirjautumisikkunaan pääsee myös suoraan oikean yläreunan _Login_ -painikkeella.

### Uloskirjautuminen
Kun käyttäjä on kirjautunut sisään, oikeaan yläreunaan ilmestyy _Logout_ -painike. Tätä painamalla käyttäjä kirjautuu ulos.

## Kirjautuneet käyttäjät
Kirjautuneella käyttäjällä on käytössä kaikki samat toiminnot kuin kirjautumattomallakin ja lisäksi joitain ekstratoimintoja käyttäjäroolista riippuen.

## User-rooli
### Arvostelun kirjoittaminen
Aluksi haetaan haluttu urheiluseura joko aiemmin mainitun _List sport clubs_ - tai _Search_ - painikkeen kautta. Korttinäkymään on nyt ilmestynyt _Show reviews_- ja _Info_ -painikkeiden lisäksi _Review_ -nappi. Napista aukeaa lomakesivu, jolle arvostelu voidaan kirjoittaa. Kohtaan _Grade_ annetaan arvosana kokonaislukuna väliltä 1-5 ja kohtaan _Review_ kirjoitetaan sanallinen arvostelu. Vain _Grade_ on pakko täyttää. Arvostelu lähetetään _Submit_-napista.

### Arvostelujen tarkastelu, editointi ja poistaminen
Yläpalkin _List my reviews_ listaa nimensä mukaisesti käyttäjän kaikki arvostelut. Jokaisen arvostelun kohdassa on painike _Edit_, josta pääsee muokkaamaan arvostelua (arvosanaa ja sanallista osuutta). Muutos tallennetaan _Submit_ -painikkeella. Arvostelun voi poistaa tietokannasta _Submit_ -painikkeen alla olevasta _Delete_ -napista. Kumpikin nappi palauttaa takaisin omien arvostelujen listaukseen.

## Owner-rooli
### Seuran luominen
Uuden seuran luomiseen päästään yläpalkin painikkeesta _Create a new sports club_. Seuralle täytyy antaa nimi, kapunki ja kuukausimaksu. Muut kentät ovat vapaaehtoisia. Seuran nimen tulee olla uniikki. Pakollisten kenttien täyttämisen jälkeen painetaan _Submit_ -nappia.

### Omien seurojen tarkastelu
Omien seurojen tarkasteluun päästään suoraan uuden seuran luomisen jälkeen ja yläpalkin napista _My Clubs_. Sivu listaa kaikki käyttäjän luomat seurat korteittain. Korteissa on joitain seuran perustietoja, sekä painikkeita jatkotoiminnoille.

### Liikuntalajien lisääminen ja poistaminen
Kun omat seurat on listattu _My Clubs_ -painikkeen kautta, voidaan mille tahansa käyttäjän omistamalle seuralle lisätä liikuntalajeja painamalla seuran kortin _Add Sport_-painiketta. Painike listaa seuralle jo lisätyt lajit ja antaa kentän johon voi kirjoittaa lisättävän lajin nimen. Tämän jälkeen painetaan _Add_-painiketta ja lisätty laji ilmestyy seuran lajien joukkoon, mikäli sitä ei siellä jo ennestään ole (isot ja pienet kirjaimet vaikuttavat). Jokaisen lisätyn lajin vieressä on _Delete_-nappi, jota painamalla lajin voi poistaa kyseisen seuran tarjonnasta.

### Seuran tietojen editointi ja seuran poistaminen
_My Clubs_ -näkymästä valitaan haluttu seura painamalla _Edit_ -painiketta. Aukeaa sama lomake, jolla seura luotiin, mutta se sisältää jo lisätyt tiedot. Tietoja voidaan vapaasti muokata ja lisätä. Muutokset tallennetaan _Save changes_ -painikkeella. Jos seura halutaan poistaa tietokannasta, painetaan _Save changes_ -napin alla olevaa _Delete_ -painiketta. Seuran lisäksi poistuvat myös kaikki seuraan liittyvät arvostelut. 

### Seuran arvostelujen tarkastelu
_My Clubs_ -näkymästä valitaan haluttu seura ja painetaan _Reviews_ -painiketta. Kaikki seuran saamat arvostelut listataan uusimmasta vanhimpaan. 







