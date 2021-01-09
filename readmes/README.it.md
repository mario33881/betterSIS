# BETTERSIS

Bettersis, definito brevemente come "bsis", e' una **shell interattiva** 
che permette di **controllare SIS** (lo strumento per la sintesi e l'ottimizzazione di circuiti sequenziali)
piu' comodamente rispetto alla shell di default di SIS grazie alle sue nuove funzionalita' moderne come:

* **autocompletamento** dei comandi
* **storico** dei comandi
* **suggerimenti** dei comandi

> Read this README in: 
>
> |[English](../README.md)|[Italiano](README.it.md)|
> |-|-|

<br>
<p align="center">
    <img height="350px" alt="logo" src="../images/logo.svg">
</p>


<br>

<p align="center">
    <img height="350px" alt="esempio" src="../images/example.gif">
</p>

<br>

> **Attenzione:**
>
> Non sono affiliato con gli sviluppatori di SIS in alcun modo.
>
> L'obiettivo di questo software e' fornire una shell con funzionalita' moderne a SIS.
> 

## Indice
* [Descrizione](#descrizione)
* [Requisiti](#requisiti)
* [Installazione](#installazione)
* [Guida all'uso](#guida-alluso)
* [Changelog](#changelog)
* [Autore](#autore)

## Descrizione ![](https://i.imgur.com/wMdaLI0.png)
Questo software fornisce una nuova shell interattiva che 
**controlla SIS in background** utilizzando la libreria ```siswrapper```.
> Ho sviluppato la libreria ```siswrapper``` grazie alla libreria **pexpect**,
> una libreria per Python che puo' essere facilmente usata per controllare shell
> interattive creando e connettendosi al processo della shell.

La shell interattiva e' controllata da una istanza della classe ```Bettersis```
che usa la libreria ```prompt_toolkit``` per visualizzare il promt e
la toolbar in basso e fornisce l'autocompletamento e lo storico dei comandi.

[Torna all'indice](#indice)

## Requisiti ![](https://i.imgur.com/H3oBumq.png)
* Sistema operativo Unix-like
    > pexpect non possiede tutte le funzionalita' necessarie su Windows e SIS funziona meglio su sistemi linux
* SIS, con il percorso nella variabile d'ambiente "path" (richiamabile con il comando ```sis``` da terminale): lo strumento per la sintesi e l'ottimizzazione di circuiti sequenziali
    > Puoi [scaricarlo da questa pagina](https://jackhack96.github.io/logic-synthesis/sis.html)

### Requisiti per sviluppatori
* I requisiti indicati nella sezione precedente
* Python 3
* La libreria siswrapper per Python: permette di controllare SIS da Python
* (Pyinstaller per creare l'eseguibile)

[Torna all'indice](#indice)

## Installazione
Puoi:

* (soluzione piu' comoda e facile) Installare il software:

    Scarica il pacchetto .deb da [Github Release](https://github.com/mario33881/betterSIS/releases/latest) e
    installalo utilizzando il seguente comando:
    ```
    sudo dpkg -i <file>
    ```
    > Sostituire ```<file>``` con il percorso del file .deb
    
    > E' possibile rieseguire questo comando per aggiornare il programma.

    > E' necessario utilizzare super user per installare il programma
    > (il sistema richiedera' la password di root)

    > E' anche possibile effettuare doppio click sul file .deb e cliccare su "Installa"

    Vantaggi:
    * E' possibile eseguire la shell da qualunque cartella eseguendo il comando ```bsis``` da terminale.
    * Non e' necessario installare Python e le dipendenze 
      per eseguire ```bettersis.py```

    Puoi disinstallare la shell eseguendo il comando:
    ```
    dpkg --remove bettersis
    ```

* Usare l'eseguibile creato da Pyinstaller:
    
    Scaricare l'eseguibile creato da Pyinstaller dalla pagina [Github Release](https://github.com/mario33881/betterSIS/releases/latest)

    Puoi eseguire la shell eseguendo il file:
    ```
    ./bsis
    ```
    > Se il comando restituisce "Permission denied", e' necessario impostare il tipo di file come eseguibile usando il comando:
    > ```
    > chmod +x bsis
    > ```
    > Assicurarsi di essere nella stessa cartella del file prima di eseguire il comando.

    Vantaggi:
    * Non e' necessario installare il software
    * Non c'e' bisogno di installare Python e le dipendenze per eseguire ```bettersis.py```

    Svantaggi:
    * Difficile da usare a causa del percorso del file
        > Si puo' aggiungere il percorso alla variabile di ambiente "path",
        > altrimenti occorre richiamare il programma con il percorso completo oppure 
        > occorre leggere i file blif specificando il percorso completo

* Usare il codice sorgente:

    1. Scarica questo repository
    2. Installa le dipendenze (meglio se vengono installate in un ambiente virtuale per Python) utilizzando il seguente comando:
        ```
        pip3 install -r requirements.txt
        ```
        > Fare attenzione di eseguire il comando nella radice del repository
    3. Eseguire ```bettersis.py```:
        ```
        python3 bettersis.py
        ```
    
    Vantaggi:
    * E' l'unico modo per sviluppare miglioramenti di questo software

    Svantaggi:
    * Difficile da usare a causa del percorso del file
        > Si puo' aggiungere il percorso alla variabile di ambiente "path",
        > altrimenti occorre richiamare il programma con il percorso completo oppure 
        > occorre leggere i file blif specificando il percorso completo
    * Occorre installare Python e le dipendenze per sviluppatori

[Torna all'indice](#indice)

## Guida all'uso

Eseguire la shell interattiva di ```bettersis```.
>
> Utilizzare:
> * Python (si e' deciso di eseguire il codice sorgente) oppure
> * Il comando ```bsis``` (se ```bettersis``` e' stato installato dal file .deb)
> * Il comando ```./bsis``` (se si e' deciso di eseguire il file creato da Pyinstaller)

Adesso e' possibile utilizzare la shell come se fosse la normale shell di SIS:
iniziare a leggere file (ad esempio usando ```read_blif```), ottimizzare circuiti,
simularli, ...

E' possibile vedere nella GIF ad inizio documentazione
un esempio di utilizzo.

[Torna all'indice](#indice)

## Changelog ![](https://i.imgur.com/SDKHpak.png)

**2021-01-09 1.1.0:** <br>
### Funzionalita' aggiuntive:
* Aggiunti log a syslog per aiutare lo sviluppare a risolvere problemi (e il file ```/var/log/pybettersis.log``` per chi installa il pacchetto .deb)
* Un messaggio che dice "Un nuovo aggiornamento e' disponibile" appare all'avvio del programma quando una nuova Github Release e' online
* I file sono mostrati come parametri di alcuni comandi (per velocizzare il workflow)

### Fix:
* Il comando ```sim``` e' trattato come il comando ```simulate```
* ```siswrapper 1.1.1``` ora puo' gestire output delle FSM (fix: ```TypeError: 'NoneType' object is not subscriptable```)
* Le build vengono create su un sistema operativo piu' vecchio (Ubuntu 12.04) per aumentare il supporto ad altre versioni di altri sistemi operativi
> Questo dovrebbe sistemare il problema ```Error loading Python lib [...] GLIBC_2.29 not found```

**2020-11-14 1.0.0:** <br>
Primo commit

[Torna all'indice](#indice)

## Autore ![](https://i.imgur.com/ej4EVF6.png)
[Stefano Zenaro (mario33881)](https://github.com/mario33881)