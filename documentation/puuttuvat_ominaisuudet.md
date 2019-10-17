# Ongelmat ja puuttuvat ominaisuudet

## Puuttuvat ominaisuudet
* Sivutus on käytössä ainoastaan käyttäjän omien arvostelujen listauksessa. Liikuntaseuroja hakiessa hakutuloksen kokoa voi kuitenkin rajata pienemmäksi _Search_ -ikkunan filtteröinin avulla. 
* Käyttäjä ei voi muokata omia tietojaan, eikä poistaa tiliään.

## Toteutuksen puutteet
* HTML-koodissa hieman copypastea jäljellä, josta pääsisi eroon perittävillä luokilla
* SQL-kyselyiden tehokkuuden optimointia voisi parantaa. Esim. liikuntaseurojen listauksessa sovellus hakee kaikki tietokannann seurat ellei niitä rajaa erikseen hakuikkunan kautta erilaisin filtterein. Ongelmasta pääsisi eroon sivutuksen avulla. 
* Sport-tauluun periytyvät date_created ja date_modified -sarakkeet sovelluksen käytön kannalta turhia. 
* Jatkoa ajatellen liikuntakeskuksen jäsenmaksu olisi ollut hyvä eriyttää omaksi taulukseen, sillä seuroilla voi olla erilaisia jäsenyysvaihtoehtoja. Tällöin tosin myös saatavilla olevat liikunntalajit saattaisivat olla riippuvaisia jäsenyystasosta (hinnasta) ja tietokanta vaatisi lisämuokkausta.




