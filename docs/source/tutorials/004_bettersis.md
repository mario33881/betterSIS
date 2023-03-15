---
myst:
  html_meta:
    "description lang=en": "betterSIS: the modern shell for SIS. What is betterSIS? How to install betterSIS."
    "description lang=it": "betterSIS: la shell moderna per SIS. Cosa e' betterSIS? Come installare betterSIS."
    "keywords": "betterSIS, SIS, BLIF, install betterSIS"
    "property=og:locale": "it_IT"
---

# betterSIS: la shell moderna per SIS

<p align="center">
<img style="height: 350px;" height="350px" src="https://raw.githubusercontent.com/mario33881/betterSIS/e541aea3c849503b4c16c22d586cc98aa7732039/_static/images/logo.svg" />
</p>
<script style="height: 350px; width: 100%;" height="350px" id="asciicast-02RkuwG4vNtsVb3LvxukxV34z" src="https://asciinema.org/a/02RkuwG4vNtsVb3LvxukxV34z.js" async data-autoplay="true"></script>

SIS non ha alcune funzionalita' che ci si possono aspettare da una shell moderna come, ad esempio, l'autocompletamento dei comandi con il tasto tab, storico dei comandi con cui si puo' interagire utilizzando i pulsanti freccia verso l'alto e verso il basso, modifica dei comandi gia' scritti spostando il cursore a destra e a sinistra con i relativi tasti freccia...

Ho programmato il software betterSIS per aggiungere queste ed altre funzionalita' aggiuntive per migliorare la user experience di SIS.

betterSIS e' una shell interattiva che utilizza siswrapper, una libreria per Python che ho realizzato per controllare SIS attraverso il linguaggio di programmazione Python, per controllare SIS.

betterSIS dovrebbe essere compatibile con tutte le versioni di SIS: la libreria e' stata pensata per essere un wrapper completo: 

* Se un comando viene riconosciuto dalla libreria il programma esegue operazioni sull'output del comando per verificare se ci sono stati errori.

* Se il comando non viene riconosciuto il programma restituisce semplicemente l'output del comando.

E' possibile scaricare betterSIS (o il suo codice sorgente) da Github [cliccando qui](https://github.com/mario33881/betterSIS)

## Installare betterSIS

Esistono [diversi metodi di installazione](https://github.com/mario33881/betterSIS/wiki/Differenza-tra-metodi-di-installazione). 
```{note}
Dopo aver capito quale versione fa al caso nostro e' possibile seguire le [istruzioni per installarla da qui](https://github.com/mario33881/betterSIS)
```

Il metodo consigliato perche' e' il piu' semplice e permette di ricevere automaticamente gli ultimi aggiornamenti e' installare la versione Snap.

E' possibile installare betterSIS da terminale con il seguente comando:
```
sudo snap install bettersis
```

E' anche possibile installarlo da interfaccia grafica seguendo queste istruzioni:
1. Clicca questo pulsante:

    [![Scarica dallo Snap Store](https://snapcraft.io/static/images/badges/it/snap-store-black.svg)](https://snapcraft.io/bettersis)

2. Poi clicca sul pulsante "Install" (installa) in alto a destra della pagina
3. Clicca su "View in Desktop Store" (visualizza nello store sul desktop) e "Choose an app" (scegli una app)
4. Scegli "Ubuntu software" OPPURE "Handler for snap:// URIs" OPPURE "Snap Store"
    ```{note}
    Queste opzioni sono scritte in ordine di preferenza: se la prima opzione non e' disponibile scegliere la seconda, ecc... Se non c'e' nessuna delle opzioni allora e' consigliato installare betterSIS con il comando scritto sopra
    ```
5. Clicca sul pulsante "Install" / "Installa"
6. (Opzionale) Se vuoi puoi modificare i permessi cliccando sul pulsante "Permissions" / "Permessi"
    ```{note}
    Consiglio di abilitare/disabilitare solo la opzione "read/write permissions on removable media" (lettura/scrittura su dispositivi rimovibili) che serve per permettere la lettura/scrittura dei file BLIF nelle USB oppure nelle cartelle in ```/mnt/``` (come le cartelle condivise di Virtualbox).
    
    Gli altri permessi sono necessari per accedere ai file BLIF all'interno della cartella home e per controllare se ci sono aggiornamenti disponibili (Cambiare questi permessi potrebbe impedire alla applicazione di funzionare completamente e/o correttamente finche' non si ri-abilitano i permessi)
    ```

Dopo aver installato betterSIS e' possibile eseguirlo da terminale con il comando ```bettersis```.

Per maggiori dettagli su questo ed altri metodi di installazione accedere al repository Github [cliccando qui](https://github.com/mario33881/betterSIS)

<div align=center>

```{only} html
[🢠 Guida iniziale SIS](./003_guida_iniziale_sis.md) &nbsp; | &nbsp; [siswrapper: il wrapper per automatizzare SIS con Python 🢡](./005_siswrapper.md)

[🗎 Torna all'indice](./tutorials.md)
```

</div>