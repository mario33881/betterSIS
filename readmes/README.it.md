# BETTERSIS

[![Unit Tests](https://github.com/mario33881/betterSIS/actions/workflows/unittests.yml/badge.svg)](https://github.com/mario33881/betterSIS/actions/workflows/unittests.yml)
![Linter](https://github.com/mario33881/betterSIS/workflows/Linter/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/bettersis/badge/?version=latest)](https://bettersis.readthedocs.io/en/latest/?badge=latest)

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
    <img height="350px" alt="logo" src="../_static/images/logo.svg">
</p>


<br>

<p align="center">
    <img height="350px" alt="esempio" src="../_static/images/example.gif">
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

Puoi leggere piu' informazioni riguardo al codice di betterSIS su readthedocs [cliccando qui](https://bettersis.readthedocs.io/en/latest/readme.html)

[Torna all'indice](#indice)

## Requisiti ![](https://i.imgur.com/H3oBumq.png)
* Sistema operativo Unix-like
    > pexpect non possiede tutte le funzionalita' necessarie su Windows e SIS funziona meglio su sistemi linux
* SIS, con il percorso nella variabile d'ambiente "path" (richiamabile con il comando ```sis``` da terminale): lo strumento per la sintesi e l'ottimizzazione di circuiti sequenziali
    > Puoi [scaricarlo da questa pagina](https://jackhack96.github.io/logic-synthesis/sis.html)

### Requisiti per sviluppatori
* I requisiti indicati nella sezione precedente
* Python 3 (versione >= 3.6)
    > La libreria prompt-toolkit non supporta le versioni piu' vecchie di Python 3
* La libreria siswrapper per Python: permette di controllare SIS da Python
* La libreria prompt-toolkit per Python: gestisce la shell di betterSIS e le sue funzionalita'
* (Pyinstaller per creare l'eseguibile)
    > Il sistema operativo su cui si crea l'eseguibile dovrebbe essere il piu' vecchio possibile
    > per supportare i sistemi operativi piu' moderni
    > (Le build non sono retrocompatibili)
* La libreria certifi: gestisce cerificati SSL/TLS. E' necessaria per collegarsi a Github Release per verificare presenza di aggiornamenti.

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

Sono stati scritti dei tutorial su readthedocs (in italiano): [clicca qui per vedere i tutorial](https://bettersis.readthedocs.io/en/latest/tutorials/tutorials.html)

[Torna all'indice](#indice)

## Changelog ![](https://i.imgur.com/SDKHpak.png)

**WIP 1.2.1:** <br>
### Funzionalita' aggiuntive:
* Aggiunto storico permanente dei comandi tra piu' sessioni (vengono salvati all'interno del file ```~/.bsis_history```):
  impostare la variabile d'ambiente "```BSIS_HISTORY_ENABLED```" a "true" per abilitare questa funzione (e' necessario chiudere e poi riaprire la shell)
    > Il limite della dimensione del file di default e' di 100 KB ma e' possibile cambiarlo impostando la variabile d'ambiente "```BSIS_HISTORY_SIZELIMIT```" (la dimensione minima consentita e' di 1000 byte)

    > Per impostare le variabili d'ambiente modificare il file ```~/.bashrc``` (o l'equivalente della shell di default del sistema operativo)
    > aggiungendo la riga ```export BSIS_HISTORY_ENABLED=true``` in fondo al file.
    >
    > Per il limite della dimensione del file ```.bsis_history``` aggiungere la seguente riga: ```export BSIS_HISTORY_SIZELIMIT=10000``` (sostituire "10000" con il numero di byte desiderato)
* Aggiunto il comando ```bsis_tutorials```: apre il browser alla [pagina dei tutorial SIS](https://bettersis.readthedocs.io/en/latest/tutorials/tutorials.html)
* Aggiunto il comando ```bsis_documentation```: apre il browser alla [pagina della documentazione di betterSIS](https://bettersis.readthedocs.io/en/latest/readme.html)
* Aggiunto il comando ```bsis_releases```: apre il browser alla [pagina per scaricare l'ultima versione di betterSIS](https://github.com/mario33881/betterSIS/releases/latest)

### Fix:
* Adesso il programma riesce a verificare la presenza di aggiornamenti

**2021-03-17 1.2.0:** <br>
### Funzionalita' aggiuntive:
* Aggiunto il comando ```ls```: mostra i file e le cartelle di una cartella data come parametro/della cartella corrente
* Aggiunto il comando ```cd```: permette di navigare le cartelle direttamente da betterSIS (senza necessita' di chiudere e riaprire il programma)
* Aggiunto il comando ```edit```: apre il file specificato come parametro con un semplice editor di testo
    > funzionalita' dell'editor di testo: syntax highlighting, funzionalita' base per modificare/salvare il file, tasto tab per scrivere/completare le keyword
* (feature siswrapper) Aggiunto il comando ```bsis_script``` command. I suoi parametri sono:
    * ```fsm_autoencoding_area```, utile per le FSM: minimizza gli stati, assegna automaticamente la codifica degli stati, ottimizza l'area e mappa il circuito per area (libreria synch)
        > Esegue ```state_minimize stamina```, ```state_assign jedi```, ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```fsm_autoencoding_delay```, utile per le FSM: minimizza gli stati, assegna automaticamente la codifica degli stati, ottimizza il ritardo e mappa il circuito per ritardo (libreria synch)
        > Esegue ```state_minimize stamina```, ```state_assign jedi```, ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```
    * ```fsm_area```, utile per le FSM: minimizza gli stati, usa la codifica manuale degli stati, ottimizza l'area e mappa il circuito per area (libreria synch)
        > Esegue ```state_minimize stamina```, ```stg_to_network```, ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```fsm_delay```, utile per le FSM: minimizza gli stati, usa la codifica manuale degli stati, ottimizza il ritardo e mappa il circuito per ritardo (libreria synch)
        > Esegue ```state_minimize stamina```, ```stg_to_network```, ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```
    * ```lgate_area_mcnc```, utile per i circuiti combinatori: ottimizza l'area e mappa il circuito per area (libreria mcnc)
        > Esegue ```source script.rugged```, ```read_library mcnc.genlib```, ```map -m 0 -W -s```
    * ```lgate_delay_mcnc```, utile per i circuiti combinatori: ottimizza il ritardo e mappa il circuito per ritardo (libreria mcnc)
        > Esegue ```reduce_depth```, ```source script.rugged```, ```read_library mcnc.genlib```, ```map -n 1 -W -s```
    * ```lgate_area_synch```, utile per i circuiti combinatori: ottimizza l'area e mappa il circuito per area (libreria synch)
        > Esegue ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```lgate_delay_synch```, utile per i circuiti combinatori: ottimizza il ritardo e mappa il circuito per ritardo (libreria synch)
        > Esegue ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```
    * ```fsmd_area```, utile per le FSMD (circuiti che includono datapath e FSM): ottimizza l'area e mappa il circuito per area (libreria synch)
        > Esegue ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```fsmd_delay```, utile per le FSMD (circuiti che includono datapath e FSM): ottimizza il ritardo e mappa il circuito per ritardo (libreria synch)
        > Esegue ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```

    > Il comando visualizza anche i comandi eseguiti e le statistiche dopo i comandi che eseguono modifiche importanti ai circuiti

    > I risultati parziali e completi dei comandi vengono scritti su nuovi file BLIF.

    > ATTENZIONE! L'esecuzione di questi comandi in questo ordine non garantisce il risultato migliore: la minimizzazione multilivello non e' esatta!
    > per ottenere risultati migliori si e' invitati ad eseguire manualmente i comandi in ordine sparso (ed eventualmente eseguire gli stessi comandi piu' volte)
* (feature siswrapper) Adesso questa libreria verifica se il comando ```stg_to_network``` ha successo

### Fix
* (fix siswrapper) Adesso il metodo ```write_eqn``` viene eseguito quando il comando ```write_eqn``` viene passato al metodo ```parsed_output()```.
    > Prima veniva eseguito il metodo ```write_blif```
* (fix siswrapper) Richiamando il metodo ```write_eqn``` e ```write_blif``` senza parametri non restituisce piu' il comando nell'output.
* (fix siswrapper) Quando SIS non e' installato sul computer il messaggio di errore mostra esattamente quale e' il problema
* (fix siswrapper) Non e' possibile eseguire lo script rugged se non sono stati letti file con un comando read
* (fix siswrapper) Quando si esegue un comando read, viene richiamato il metodo ```reset``` per terminare la sessione di SIS attuale e avviarne
  una nuova all'interno della cartella del file in input
    > In questo modo si "risolve" l'errore ".search x file not found" quando si cerca di leggere un file che si trova in un'altra cartella e che usa la keyword .search.
    >
    > Questo errore era normale ma non intuitivo (perche' il file era presente nella cartella del file in input ma non nella cartella corrente).
    > Era il comportamento di SIS.
* (fix siswrapper) L'output del comando ```print_stats``` non veniva interpretato correttamente quando i letterali/stati erano superiori a 10000
    > L'output era corretto ma il programma considerava l'output come un errore

### bug conosciuti:
* La versione eseguibile di betterSIS (sia il pacchetto deb sia l'eseguibile di PyInstaller) non riescono a connettersi correttamente a Github Release per controllare la presenza di aggiornamenti (dovuto ad un errore di verifica del certificato SSL)
    > Questo problema sara' risolto nella prossima versione(per ora e' necessario controllare manualmente se un aggiornamento e' disponibile

**2021-01-09 1.1.0:** <br>
### Funzionalita' aggiuntive:
* Aggiunti log a syslog per aiutare lo sviluppare a risolvere problemi (e il file ```/var/log/pybettersis/pybettersis.log``` per chi installa il pacchetto .deb)
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