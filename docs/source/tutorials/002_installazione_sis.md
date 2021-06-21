---
html_meta:
  "description lang=en": "SIS installation. How to install SIS."
  "description lang=it": "Installazione SIS. Come installare SIS."
  "keywords": "betterSIS, SIS, BLIF, install SIS"
  "property=og:locale": "it_IT"
---

# Installazione SIS

## Premessa
Attualmente (anno 2020-2021), e' consigliato installare la versione 1.3.6 di SIS su un sistema operativo basato su Debian (come, ad esempio, Ubuntu).

**E' SCONSIGLIATO:**

* Installare la versione 1.4 di SIS: alcuni comandi non funzionano correttamente.

* Installare SIS su Mac OS o, peggio ancora, su Windows: il programma puo' dare diversi errori che non sono presenti su sistemi GNU/Linux
  
  ```{admonition} nota
  Se si desidera comunque installare SIS su Windows provare ad utilizzarlo su [WSL](https://docs.microsoft.com/it-it/windows/wsl/about) (permette di eseguire comandi e applicazioni GNU/Linux in un sottosistema, o "container", su Windows). 
   
  Per installare SIS su WSL procedere come se si avesse un sistema basato su Debian.
   
  Altri metodi sono sconsigliati.
  ```

Personalmente ho testato SIS 1.3.6 su Ubuntu 18.04 e Ubuntu 20.
```{admonition} nota
Sono a conoscenza del fatto che altre persone abbiano utilizzato Debian 10 per il proprio elaborato di Architettura degli Elaboratori.

Non avendo sufficientemente testato di persona SIS con altri sistemi operativi diversi da Ubuntu non posso confermare con certezza che SIS non gli abbia creato problemi.
```

## Installazione su Debian o derivati

1. [Cliccare qui](https://jackhack96.github.io/logic-synthesis/sis.html) per accedere alla pagina da cui e' possibile scaricare SIS

2. Scorrere la pagina fino alla sezione "Downloads" e scaricare il pacchetto ```.deb``` cliccando sul pulsante "Download Debian package" della versione 1.3 (che sarebbe la versione 1.3.6)
   
   ![Download](https://i.imgur.com/qwQco9W.png)

3. Aprire il terminale nella cartella del file appena scaricato (o navigare all'interno di quella cartella utilizzando il comando ```cd```) e installare il file eseguendo il comando:
   
   ```
   sudo dpkg -i sis_1.3.6-1-amd64.deb
   ```

```{admonition} nota
Verra' chiesta la password del "super user" (possiamo definirlo per semplicita' come l'equivalente dell'account amministratore per Windows): inserirla e premere invio.
 
**NOTA**: la password per sicurezza non viene visualizzata sul terminale (NEMMENO nascosta da asterischi "\*")
```

```{admonition} nota
Se il file scaricato si chiama in maniera diversa modificare nel comando ```sis_1.3.6-1-amd64.deb``` con il nome del file.
```

## Verifica l'installazione

Per prima cosa assicurarsi che la installazione abbia avuto successo eseguendo SIS da terminale con il comando:

```
sis
```

Se il sistema operativo dice "Command not found" (comando non riconosciuto), provare a chiudere e riaprire il terminale e a ri-eseguire il comando.

Se non va provare a riavviare il computer.

Se non va ancora provare a modificare il file ```.bashrc``` (file presente nella home dell'utente, la cartella rappresentata dalla tilde ```~```) aggiungendo la seguente riga in fondo al file:

```
PATH="/usr/local/sis-1.3.6/bin/:$PATH"
```

```{admonition} nota
Dove ```/usr/local/sis-1.3.6/bin``` e' il percorso di installazione di SIS.
 
Questa operazione indica al sistema operativo che quella cartella contiene eseguibili che devono essere disponibili ed eseguibili da qualsiasi percorso del sistema.
```

Chiudere e riaprire la shell. Adesso con il comando ```sis``` sara' possibile eseguire SIS su terminale da qualsiasi cartella.

Per uscire dalla shell di SIS eseguire il comando ```exit``` o ```quit```.

Ora e' possibile iniziare a progettare sistemi digitali utilizzando SIS.

<div align=center>

[🢠 Introduzione a SIS](./001_introduzione_a_sis.md) &nbsp; | &nbsp; [Guida iniziale SIS 🢡](./003_guida_iniziale_sis.md)

[🗎 Torna all'indice](./tutorials.md)

</div>