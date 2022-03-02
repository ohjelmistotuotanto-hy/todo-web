# todo-web

Esimerkkiprojekti web-pohjaiselle Python-sovellukselle. Projektin web-palvelin on toteutettu [Flask](https://flask.palletsprojects.com/en/2.0.x/)-kirjaston avulla. Tietokantana on [PostgreSQL](https://www.postgresql.org/), jota käytetään [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)-kirjaston avulla.

## Asennus

1. Asenna PostgreSQL. Tässä voit hyödyntää esimerkiksi Tietokantasovellus-kurssin [ohjetta](https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen), tai PostgreSQL:n oman dokumentaation [ohjetta](https://www.postgresql.org/download/).
1. Asenna riippuvuudet komennolla `poetry install`
2. Luo projektin juurihakemistoon tiedosto `.env` ja kopioi siihen `.env.template`-tiedoston sisältö. Aseta `DATABASE_URL`-ympäristömuuttujan arvo siten, että se on muotoa `DATABASE_URL=postgres://...`. Kokeile ennen tätä, että yhteyden muodostus onnistuu komentoriviltä komennolla `psql <url>`, jossa `<url>` on tietokantayhteyden URL.
3. Alusta tietokanta komennolla `poetry run python3 initialize_database.py`.
4. Käynnistä sovellus komennolla `poetry run flask run`

## Tietokannan skeeman ylläpitäminen

Tietokannan taulut alustetaan [src/initialize_database.py](initialize_database.py)-tiedostossa. Jos haluat tehdä muutoksia tietokannan skeemaan, tee muutokset tähän tiedostoon ja suorita muutosten jälkeen komento `poetry run python3 src/initialize_database.py`.

## Testaaminen

Testejä varten kannattaa luoda oma tietokanta. Ota yhteys tietokantaan `psql`-komennon avulla ja suorita siellä seuraava komento:

```sql
CREATE DATABASE todotest
```

Korvaa tietokannan nimi haluamallasi nimellä.

Luo seuraavaksi projektin juurihakemistoon tiedosto `.env.test` ja kopioi siihen `.env.template`-tiedoston sisältö. Aseta `DATABASE_URL`-ympäristömuuttujan arvo siten, että yhteys muodostetaan testitietokantaan. Esimerkiksi jos sovelluksen URI on `postgresql://localhost/tododev`, on testitietokannan URL `postgresql://localhost/todotest`.

Testit suoritetaan [pytestin](https://docs.pytest.org/) avulla. Testien suorituksessa käytettävät ympäristömuuttujat ladataan `.env.test`-tiedostosta [pytest.ini](pytest.ini)-tiedoston konfiguraation mukaisesti. Jokainen testiajo alustaa tietokannan uudelleen [src/tests/conftest.py](tests/conftest.py)-tiedoston mukaisesti.

Testien suorittaminen onnistuu komennolla `poetry run pytest src`.

## Tuotantoonvienti

Luo sovellusta varten Heroku-sovellus komennolla `heroku apps:create ohtu-todo-web` (korvaa sovelluksen nimi haluamallasi nimellä). Ota tämän jälkeen tuotantoympäristön tietokantaa varteen käyttöön [Herokun PostgreSQL-tietokanta](https://elements.heroku.com/addons/heroku-postgresql) komennolla `heroku addons:create heroku-postgresql`. Herokun pitäisi asettaa ympäristömuuttujan `DATABASE_URL` arvo Heroku sovelluksessa oikein. Tarkista tämä vielä komennolla `heroku config`.

Ennen tuotantoonvientiä Herokuun, tulee `requirements.txt`-tiedosto muodostaa riippuvuuksien perusteella. Tämä onnistuu komennolla `poetry export -f requirements.txt --output requirements.txt`.
