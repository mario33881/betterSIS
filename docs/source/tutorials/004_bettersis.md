---
html_meta:
  "description lang=en": "betterSIS: the modern shell for SIS. What is betterSIS? How to install betterSIS."
  "description lang=it": "betterSIS: la shell moderna per SIS. Cosa e' betterSIS? Come installare betterSIS."
  "keywords": "betterSIS, SIS, BLIF, install betterSIS"
  "property=og:locale": "it_IT"
---

# betterSIS: la shell moderna per SIS

<p align="center">
<img style="height: 350px;" height="350px" src="https://raw.githubusercontent.com/mario33881/betterSIS/69a1208e0bcb21236b9daf3318763ed793cada8d/images/logo.svg" />
</p>
<p align="center">
<img height="450px" src="https://raw.githubusercontent.com/mario33881/betterSIS/69a1208e0bcb21236b9daf3318763ed793cada8d/images/example.gif" />
</p>

SIS non ha alcune funzionalita' che ci si possono aspettare da una shell moderna come, ad esempio, l'autocompletamento dei comandi con il tasto tab, storico dei comandi con cui si puo' interagire utilizzando i pulsanti freccia verso l'alto e verso il basso, modifica dei comandi gia' scritti spostando il cursore a destra e a sinistra con i relativi tasti freccia...

Ho programmato il software betterSIS per aggiungere queste ed altre funzionalita' aggiuntive per migliorare la user experience di SIS.

betterSIS e' una shell interattiva che utilizza siswrapper, una libreria per Python che ho realizzato per controllare SIS attraverso il linguaggio di programmazione Python, per controllare SIS.

betterSIS dovrebbe essere compatibile con tutte le versioni di SIS: la libreria e' stata pensata per essere un wrapper completo: 

* Se un comando viene riconosciuto dalla libreria il programma esegue operazioni sull'output del comando per verificare se ci sono stati errori.

* Se il comando non viene riconosciuto il programma restituisce semplicemente l'output del comando.

E' possibile scaricare betterSIS (o il suo codice sorgente) da Github [cliccando qui](https://github.com/mario33881/betterSIS)

#### Installare betterSIS

Per installare betterSIS scaricare dalla pagina [Github releases di betterSIS](https://github.com/mario33881/betterSIS/releases/latest) il pacchetto ```.deb``` e installarlo eseguendo il comando:

```
sudo dpkg -i bettersis.deb
```

```{note}
Verra' chiesta la password del "super user" (equivalente dell'account amministratore per Windows): inserirla e premere invio.

NOTA: la password per sicurezza non viene visualizzata sul terminale (NEMMENO nascosta tra asterischi "*")
```

```{note}
Se il file scaricato si chiama in maniera diversa modificare nel comando `bettersis.deb` con il nome del file.
```

Per maggiori dettagli su questo ed altri metodi di installazione accedere al repository Github [cliccando qui](https://github.com/mario33881/betterSIS)

<div align=center>

[🢠 Guida iniziale SIS](./003_guida_iniziale_sis.md) &nbsp; | &nbsp; [siswrapper: il wrapper per automatizzare SIS con Python 🢡](./005_siswrapper.md)

[🗎 Torna all'indice](./tutorials.md)

</div>