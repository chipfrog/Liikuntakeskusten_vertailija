# TIetokannan rakenne
## Tietokantakaavio
![Tietokantakaavio](https://github.com/chipfrog/Liikuntakeskusten_vertailija/blob/master/documentation/Tietokantakaavio.png)
## CREATE TABLE-lauseet
```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(40) NOT NULL, 
	email VARCHAR(40) NOT NULL, 
	username VARCHAR(20) NOT NULL, 
	password VARCHAR(400) NOT NULL, 
	role VARCHAR(10) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (username)
)
CREATE TABLE sport (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id)
)
CREATE TABLE club (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(40) NOT NULL, 
	city VARCHAR(40) NOT NULL, 
	address VARCHAR(40), 
	email VARCHAR(40), 
	tel VARCHAR(40), 
	price INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
CREATE TABLE review (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	grade INTEGER NOT NULL, 
	review VARCHAR(500) NOT NULL, 
	account_id INTEGER NOT NULL, 
	club_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(club_id) REFERENCES club (id)
)
CREATE TABLE sports (
	sport_id INTEGER NOT NULL, 
	club_id INTEGER NOT NULL, 
	PRIMARY KEY (sport_id, club_id), 
	FOREIGN KEY(sport_id) REFERENCES sport (id), 
	FOREIGN KEY(club_id) REFERENCES club (id)
)

