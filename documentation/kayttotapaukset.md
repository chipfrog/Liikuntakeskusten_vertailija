# Käyttötapaukset
Alla kuvatuissa käyttötapauksissa puhutaan harrastajista ja omistajista. Harrastajalla tarkoitetaan "tavallista" käyttäjää, joka voi kirjoittaa arvosteluja ja hakea liikuntakeskuksia tietokannasta.
Omistajalla puolestaan tarkoitetaan käyttäjää, esim. liikuntakeskuksen henkilökuntaan kuuluvaa henkilöä, jolla on oikeus muokata "omistamansa" liikuntakeskuksen tietoja. Käyttäjällä tarkoitetaan mihin tahansa käyttäjäryhmään kuuluvaa henkilöä.

### Kirjautuminen ja käyttäjät
* Käyttäjänä pääsen luomaan itselleni sovellukseen profiilin, johon kuuluu käyttäjärooli (harrastaja tai omistaja), sekä uniikki käyttäjätunnus. Profiilin luomisen jälkeen pääsen käyttämään sovelluksen muita toimintoja kirjautumalla sisään.   
* Harrastajana voin kirjautua sivulle henkilökohtaisella käyttäjätunnuksellani. Sovelluksen normaalin toiminnallisuuden lisäksi (arvostelujen antaminen, liikuntakeskusten haku) pääsen käsiksi personoituun näkymään, josta näen kaikki antamani arvostelut ja voin muokata omia tietojani. 
* Omistajana voin kirjautua sivulle henkilökohtaisella käyttäjätunnuksellani. Liikuntakeskusten haun ja arvostelujen tarkastelun lisäksi pääsen näkymään, jossa voin muokata hallinnoimani liikuntakeskuksen tietoja.

### Liikuntakeskusten hakeminen
* Käyttäjänä voin hakea liikuntakeskuksia eri kriteerien perusteella. Hakunäkymässä on omat kenttänsä liikuntakeskuksen nimelle, lajeille ja kuukausimaksulle. Mitä useamman kentän täytän, sitä tarkemmin rajattuja tuloksia saan. Voin esimerkiksi etsiä liikuntakeskusta, jonka kuukausimaksu on maksimissaan 60€, ja jossa voi harrastaa nyrkkeilyä. Sovellus listaa kaikki ehdot täyttävät keskukset tai kertoo ettei sellaisia löytynyt.

### Liikuntakeskusten listaaminen
* Käyttäjän voin listata kaikki tietokannassa olevat liikuntaseurat. Seurat järjestää voi nimen, kaupungin, hinnan ja arvosanojen keskiarvon mukaan.

### Arvostelut
* Harrastajana voin kirjoittaa testaamalleni liikuntakeskukselle julkisen arvostelun, 
johon sisältyy numeroarvosana, sekä sanallinen osio. Liikuntakeskus saa toiminnastaan tärkeää palautetta ja toiset harrastajat
voivat lukea mielipiteeni etsiessään itselleen sopivaa keskusta.
* Harrastajana pääsen tarkastelemaan jo antamiani arvosteluja omasta profiilistani ja voin tarvittaessa muokata niitä, jos mielipiteeni
arvostellusta liikuntakeskuksesta on muuttunut. Voin myös halutessani poistaa antamani arvostelun.
* Käyttäjänä voin katsoa tarkastelemani liikuntakeskuksen keskiarvon, joka perustuu keskukselle annettuihin arvosanoihin.
Keskiarvosta ja annettujen arvostelujen määrästä (ilmoitetaan keskiarvon alapuolella) voin nopeasti päätellä harrastajien yleisen 
tyytyväisyyden keskukseen.

### Liikuntakeskuksen hallinnointi
* Omistajana voin lisätä liikuntakeskuksen tietokantaan. Lisäämisen yhteydessä annan keskuksen yleiset tiedot, kuten nimen osoitteen, yhteystiedot jne. Voin myös päivittää tietoja myöhemmin, jos ne muuttuvat. 
* Omistajana voin lisätä lajeja, joita hallinnoimassani liikuntakeskuksessa on tarjolla, jotta mahdolliset asiakkaat saavat tarkempaa ja ajantasaista tietoa keskuksesta. Jos jokin laji poistuu keskuksen tarjonnasta, voin myös poistaa sen.
* Omistajana voin poistaa hallinnoimani liikuntakeskuksen, jos se lopettaa toimintansa. Poistamisen yhteydessä poistuvat myös keskukseen liittyvät arvostelut.

# SQL-kyselyt
## Käyttäjäprofiilit
* Uuden käyttäjän lisääminen tietokantaan
```
INSERT INTO account (date_created, date_modified, name, email, username, password, role) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)
```
* Sisäänkirjautuminen: tarkistetaan aluksi, että syötetyllä nimimerkillä ja salasanalla löytyy käyttäjä tietokannasta
```
SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.email AS account_email, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.username = ? AND account.password = ?
```






