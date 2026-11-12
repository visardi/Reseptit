### Sovelluksen testaaminen###
- aja komentorivillä komento git clone https://github.com/visardi/Reseptit.git
- varmista että olet Reseptit -kansiossa minkä juuri kloonasit!
- aja komento python3 "-m venv venv" luodaksesi virtuaaliympäristö
- aja komento source "venv/bin/activate"
- aja komento "pip install flask" ladataksesi flaskin samaan kansioon
- aja komento "sqlite3 database.db < schema.sql" alustaaksesi tietokannan
- aja komento "flask run" avataksesi web-sovelluksen paikallisesti omalla koneella
- kopio saamasi osoite komentoriviltä ja liitä se selaimeen
- testaa sovellusta




# Reseptit

- Sovelluksessa käyttäjät pystyvät jakamaan ruokareseptejään.
- Reseptissä lukee tarvittavat ainekset ja valmistusohje.
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään reseptejä ja muokkaamaan ja poistamaan niitä.
- Käyttäjä näkee sovellukseen lisätyt reseptit.
- Käyttäjä pystyy etsimään reseptejä hakusanalla.
- Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt ja listan käyttäjän lisäämistä resepteistä.
- Käyttäjä pystyy valitsemaan esimerkiksi seuraavia luokitteluja:
    - Ruoan tyyppi: alkuruoka, pääruoka tai jälkiruoka
    - Ruokavalio: laktoositon, gluteeniton tai vegaaninen
- Käyttäjä pystyy antamaan reseptille kommentin ja arvosanan. Reseptistä näytetään kommentit ja keskimääräinen arvosana.
