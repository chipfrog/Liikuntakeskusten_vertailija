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
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?);
```
* Sisäänkirjautuminen: haetaan käyttäjä tietokannasta
```
SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.email AS account_email, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.id = ?;
```
## Arvostelut
* Uuden arvostelun lisääminen
```
INSERT INTO review (date_created, date_modified, grade, review, account_id, club_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?);
```
* Käyttäjän kaikkien arvostelujen listaaminen
```
SELECT review.id AS review_id, review.grade, review.review, review.club_id, club.name, club.city 
FROM review LEFT JOIN club ON review.club_id = club.id 
WHERE review.account_id = ?;
```
* Arvostelun hakeminen tietokannasta muokkaamista tai poistamista varten
```
SELECT review.id AS review_id, review.date_created AS review_date_created, review.date_modified AS review_date_modified, review.grade AS review_grade, review.review AS review_review, review.account_id AS review_account_id, review.club_id AS review_club_id 
FROM review 
WHERE review.id = ?;
```
* Arvostelun muokkaaminen; muutosten tallentaminen tietokantaan
```
UPDATE review SET date_modified=CURRENT_TIMESTAMP, grade=?, review=? WHERE review.id = ?;
```
* Arvostelun poistaminen tietokannasta
```
DELETE FROM review WHERE review.id = ?;
```
## Urheiluseurat
* Uuden seuran luominen, tarkistetaan aluksi ettei samannimistä seuraa ole olemassa.
```
SELECT club.id AS club_id, club.date_created AS club_date_created, club.date_modified AS club_date_modified, club.name AS club_name, club.city AS club_city, club.address AS club_address, club.email AS club_email, club.tel AS club_tel, club.price AS club_price, club.account_id AS club_account_id 
FROM club 
WHERE club.name = ?;
```
Lisätään uusi seura tietokantaan.
```
INSERT INTO club (date_created, date_modified, name, city, address, email, tel, price, account_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?);
```
* Seuran tietojen päivittäminen (tässä tapauksessa kaksi kohtaa, voi olla useampiakin)
```
UPDATE club SET date_modified=CURRENT_TIMESTAMP, city=?, tel=? WHERE club.id = ?;
```
* Seuran poistaminen tietokannasta; poistetaan aluksi liitostaulusta sports kaikki seuraan liittyvät rivit, eli kytkökset poistettavan seuran ja urheilulajien välillä
```
DELETE FROM sports WHERE sports.sport_id = ? AND sports.club_id = ?;
```
Haetaan seuraan liittyvät poistettavat arvostelut
```
SELECT review.id AS review_id, review.date_created AS review_date_created, review.date_modified AS review_date_modified, review.grade AS review_grade, review.review AS review_review, review.account_id AS review_account_id, review.club_id AS review_club_id 
FROM review 
WHERE ? = review.club_id;
```
Poistetaan lopuksi seura
```
DELETE FROM club WHERE club.id = ?;
```
* Kaikkien seurojen järjestäminen yhden kriteerin perusteella (esimerkissä kaupugin mukaan aakkosjärjestyksessä)
```
SELECT club.id AS club_id, club.name, club.city, club.price, 
COUNT(review.grade) AS reviews, 
ROUND(AVG(review.grade), 2) AS average FROM club 
LEFT JOIN review ON review.club_id = club.id 
GROUP BY club.id 
ORDER BY club.city ASC;
```
* Seurojen hakeminen useiden kriteerien (kaupunki, hinta (min, max), keskiarvo, liikuntalaji) perusteella
```
SELECT club.id AS club_id, club.name, club.city, club.price, 
COUNT(DISTINCT review.grade) as reviews, 
ROUND(AVG(review.grade), 2) AS average FROM club 
LEFT JOIN review ON review.club_id = club.id 
LEFT JOIN sports ON sports.club_id = club.id 
LEFT JOIN sport ON sport.id = sports.sport_id 
WHERE (? = '' OR club.city = ?) AND (? = '' OR sport.name = ?) AND (? IS NULL OR club.price >= ?) AND (? IS NULL OR club.price <= ?) 
GROUP BY club.id 
HAVING ? IS NULL OR ROUND(AVG(review.grade), 2) >= ? 
ORDER BY (CASE WHEN ROUND(AVG(review.grade), 2) is NULL THEN 1 ELSE 0 END), average DESC;
```
* Yhden seuran koottujen tietojen hakeminen (perustietojen lisäksi arvostelujen määrä, saatavilla olevat liikuntamuodot jne.)
```
SELECT club.id AS club_id, club.name AS club_name, club.city, club.address, club.email, club.tel, club.price, 
COUNT(DISTINCT review.grade) as reviews, 
ROUND(AVG(review.grade), 2) AS average, 
COUNT(DISTINCT sports.sport_id) AS sportscount FROM club 
LEFT JOIN review ON review.club_id = club.id 
LEFT JOIN sports ON sports.club_id = club.id 
WHERE club.id = ? 
GROUP BY club.id;
```
## Urheilulajit
* Uuden lajin lisääminen

Tarkistetaan löytyykö samannimistä lajia ennestään
```
SELECT sport.id AS sport_id, sport.date_created AS sport_date_created, sport.date_modified AS sport_date_modified, sport.name AS sport_name 
FROM sport 
WHERE sport.name = ?;
```
Lisätään uusi laji sport-tauluun ja sports-liitostauluun
```
INSERT INTO sport (date_created, date_modified, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?);

INSERT INTO sports (sport_id, club_id) VALUES (?, ?);
```
* Lajin poistaminen seuran tarjonnasta
```
DELETE FROM sports WHERE sports.sport_id = ? AND sports.club_id = ?;
```
* Kaikkien seuran lajien hakeminen aakkosjärjestyksessä
```
SELECT name, id FROM sports 
LEFT JOIN sport ON sport.id = sports.sport_id 
WHERE sports.club_id = ? 
ORDER BY name ASC;
```




