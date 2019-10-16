# Asennusohje
Koneelle tulee olla asennettuna [Python](https://www.python.org/downloads/) (vähintään versio 3.5)
ja sen mukana oletuksena tuleva [pip](https://packaging.python.org/key_projects/#pip). 
Lisäksi [venv](https://docs.python.org/3/library/venv.html) -kirjasto tulee olla käytössä. Sovellus käyttää paikallisesti [SQLite](https://www.sqlite.org/index.html)-tietokantaa, joten myös se tulee olla asennettuna (versio 3), mikäli ei ennestään ole. 
Sovellusta on testattu vain Linux-ympäristössä.

Kun em. kohteet on asennettu voi repositorion ladata koneelle ja purkaa sopivaan kansioon. Konsolissa tulee siirtyä kansion sisälle
ja luoda sinne virtuaaliympäristö komennolla ```python3 -m venv venv```. Tämän jälkeen ympäristö käynnistetään komennolla 
```source venv/bin/activate```. Nyt voidaan ladata sovelluksen tarvitsemat riippuvuudet komennolla ```pip install -r requirements.txt```.
Tämän jälkeen sovellus voidaan käynnistää komennolla ```python run.py``` ja avata selaimella osoitteesta _http://localhost:5000/_.
Sovelluksen pitäisi nyt toimia paikallisesti. 
