# BETTERSIS

[![Unit Tests](https://github.com/mario33881/betterSIS/actions/workflows/unittests.yml/badge.svg)](https://github.com/mario33881/betterSIS/actions/workflows/unittests.yml)
![Linter](https://github.com/mario33881/betterSIS/workflows/Linter/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/bettersis/badge/?version=latest)](https://bettersis.readthedocs.io/en/latest/?badge=latest)
[![bettersis](https://snapcraft.io/bettersis/badge.svg)](https://snapcraft.io/bettersis)

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
    * [Requisiti per sviluppatori](#requisiti-per-sviluppatori)
* [Installazione](#installazione)
* [Guida all'uso](#guida-alluso)
    * [Storico permanente dei comandi tra piu' sessioni](#storico-permanente-dei-comandi-tra-piu-sessioni)
* [Trovato qualche problema?](#trovato-qualche-problema)
* [Changelog](#changelog)
* [Autore](#autore)

## Descrizione ![](https://i.imgur.com/wMdaLI0.png)
Questo software fornisce una nuova shell interattiva che 
**controlla SIS in background** utilizzando la libreria ```siswrapper```.
> Ho sviluppato la libreria ```siswrapper``` grazie alla libreria **pexpect**,
> una libreria per Python che puo' essere facilmente usata per controllare shell
> interattive creando e connettendosi al processo della shell.

La shell interattiva e' controllata da una istanza della classe ```Bettersis```
che usa la libreria ```prompt_toolkit``` per visualizzare il prompt e
la toolbar in basso e fornisce l'autocompletamento e lo storico dei comandi.

Puoi leggere piu' informazioni riguardo al codice di betterSIS su readthedocs [cliccando qui](https://bettersis.readthedocs.io/en/latest/readme.html)

[Torna all'indice](#indice)

## Requisiti ![](https://i.imgur.com/H3oBumq.png)
* Sistema operativo Unix-like
    > pexpect non possiede tutte le funzionalita' necessarie su Windows e SIS funziona meglio su sistemi linux
* SIS, con il percorso nella variabile d'ambiente "path" (richiamabile con il comando ```sis``` da terminale): lo strumento per la sintesi e l'ottimizzazione di circuiti sequenziali
    > Puoi [scaricarlo da questa pagina](https://jackhack96.github.io/logic-synthesis/sis.html)

    > Non e' necessario installare SIS per la versione dello Snap store

* (snap SOLO per installare la versione dello Snap store)

### Requisiti per sviluppatori
* I requisiti indicati nella sezione precedente
* Python 3 (versione >= 3.6)
    > La libreria prompt-toolkit non supporta le versioni piu' vecchie di Python 3
* La libreria siswrapper per Python: permette di controllare SIS da Python
* La libreria prompt-toolkit per Python: gestisce la shell di betterSIS e le sue funzionalita'
* (Pyinstaller - solo per creare l'eseguibile)
    > Il sistema operativo su cui si crea l'eseguibile dovrebbe essere il piu' vecchio possibile
    > per supportare i sistemi operativi piu' moderni
    > (Le build non sono retrocompatibili)
* La libreria certifi: gestisce cerificati SSL/TLS. E' necessaria per collegarsi a Github Release per verificare presenza di aggiornamenti.
    > Questo e' necessario solo per i sistemi operativi piu' vecchi che non hanno certificati aggiornati

[Torna all'indice](#indice)

## Installazione

> Puoi vedere un riassunto delle [differenze tra i vari metodi di installazione qui](https://github.com/mario33881/betterSIS/wiki/Differenza-tra-metodi-di-installazione).
>
> Dopo aver guardato il riassunto e' possibile leggere maggiori dettagli su come installare betterSIS con il metodo desiderato e sui vantaggi e svantaggi qui sotto.

Puoi:

* (soluzione piu' comoda e facile) Installare il software dallo Snap store:
    
    Dal terminale eseguire questo comando:
    ```
    sudo snap install bettersis
    ```
    > E' necessario avere snap installato. Puoi installarlo [seguendo le istruzioni qui](https://snapcraft.io/docs/installing-snapd). 
    >
    > Nota che probabilmente snap e' gia' installato sul tuo computer. (specialmente se si sta utilizzando una versione recente di una distro basata su Ubuntu)

    Dall'interfaccia grafica:
    1. Clicca questo pulsante:

        [![Scarica dallo Snap Store](https://snapcraft.io/static/images/badges/it/snap-store-black.svg)](https://snapcraft.io/bettersis)


    2. Poi clicca sul pulsante "Install" (installa) in alto a destra della pagina
    3. Clicca su "View in Desktop Store" (visualizza nello store sul desktop) e "Choose an app" (scegli una app)
    4. Scegli "Ubuntu software" OPPURE "Handler for snap:// URIs" OPPURE "Snap Store"
        > Queste opzioni sono scritte in ordine di preferenza: se la prima opzione non e' disponibile scegliere la seconda, ecc... Se non c'e' nessuna delle opzioni allora e' consigliato installare betterSIS con il comando scritto sopra
    5. Clicca sul pulsante "Install" / "Installa"
    6. (Opzionale) Se vuoi puoi modificare i permessi cliccando sul pulsante "Permissions" / "Permessi"
        > Consiglio di abilitare/disabilitare solo la opzione "read/write permissions on removable media" (lettura/scrittura su dispositivi rimovibili) che serve per permettere la lettura/scrittura dei file BLIF nelle USB oppure nelle cartelle in ```/mnt/``` (come le cartelle condivise di Virtualbox).
        >
        > Gli altri permessi sono necessari per accedere ai file BLIF all'interno della cartella home e per controllare se ci sono aggiornamenti disponibili (Cambiare questi permessi potrebbe impedire alla applicazione di funzionare completamente e/o correttamente finche' non si ri-abilitano i permessi)
    
    Vantaggi rispetto alle altre soluzioni:
    * E' possibile eseguire la shell da qualunque cartella eseguendo il comando ```bettersis``` da terminale.
    * Non e' necessario installare Python e le altre dipendenze
    * SIS e' incluso all'interno dello snap insieme a betterSIS: non e' necessario installarlo manualmente
        > Nota: non succede niente se si decide di installare sia lo snap con sis incluso sia sis,
        NON vanno in conflitto
    * Aggiornamenti automatici: quando un nuovo aggiornamento e' disponibile verra' scaricato e installato automaticamente.
        > Questo permette di avere sempre tutte le nuove funzionalita' e bug fix.
    * Compatibile con tutti i sistemi operativi che supportano snap.
    
    Svantaggi:
    * Potrebbe usare (leggermente) piu' risorse delle altre installazioni
    * SIS e' incluso: occupa piu' spazio disco (circa 3.08 MB in piu')
    * Aggiornamenti completamente automatici: non c'e' modo di poter [disabilitare e ri-abilitare comodamente gli aggiornamenti automatici](https://forum.snapcraft.io/t/snap-method-to-remove-auto-updates/21199)
    * snap e' necessario per l'installazione
        > Molte distro basate su Ubuntu ma anche altre hanno [snap installato di fabbrica](https://snapcraft.io/docs/installing-snapd)
    
    Vantaggio/Svantaggio:
    * Le Snap sono molto limitate in termini di permessi. Questo significa che e' facile incontrare errori "Permission Error" se si cerca di aprire file in cartelle in cui si ha il permesso di entrare/modificare file come utente.
        > Suggerisco di aprire e usare betterSIS in una cartella che e' da qualche parte all'interno della cartella home (Un esempio di cartella valida ```/home/mioutente/Documenti/imieiprogetti/progetti_sis```) e di NON usare sudo per aprire betterSIS.
        >
        > Potresti anche dare i permessi per aprire ed utilizzare betterSIS in dispositivi rimovibili
        > seguendo il passo numero 6 descritto sopra a "Vantaggi rispetto alle altre soluzioni"

    Puoi disinstallare betterSIS aprendo la pagina sull'Ubuntu Store/Snap store e cliccando sul pulsante rimuovi/disinstalla.
    > Puoi seguire gli stessi passaggi svolti per installare betterSIS e poi nel passaggio 5 cliccare su rimuovi/disinstalla invece di "installa"

    Puoi anche disinstallarlo eseguendo questo comando:
    ```
    snap remove bettersis
    ```

* Usare l'eseguibile AppImage:

    Scaricare il file .AppImage dalla [pagina Github Release qui](https://github.com/mario33881/betterSIS/releases/latest).
    > Ignora il file ```.AppImage.zsync```: e' usato dalla AppImage per trovare aggiornamenti e NON e' necessario scaricarlo

    E' possibile eseguire betterSIS con questo comando:
    ```
    ./Bettersis-<version>-x86_64.AppImage
    ```
    > Sostituire ```<version>``` con il numero di versione (come ```1.2.1```)

    > Se il terminale visualizza "Permesso negato", e' necessario impostare come eseguibile il file:
    > ```
    > chmod +x Bettersis-<version>-x86_64.AppImage
    > ```
    > Assicurarsi di essere nella stessa cartella del file prima di eseguire il comando
    
    Vantaggi:
    * Non e' necessario installare betterSIS
    * Non e' necessario installare Python e le sue dipendenze
    * E' possibile aggiornare la AppImage utilizzando il comando ```bsis_update``` dalla shell di betterSIS

    Svantaggi:
    * Difficile da usare a causa del percorso del file
        > Si puo' aggiungere il percorso alla variabile di ambiente "path",
        > altrimenti occorre richiamare il programma con il percorso completo oppure 
        > occorre leggere i file blif specificando il percorso completo
    
    > Su molte distribuzioni e' possibile scaricare l'eseguibile nella cartella ```bin``` della cartella home (```$HOME```): questo permette di eseguire il comando ```bsis``` da qualsiasi cartella come se betterSIS fosse installato

    Per "disinstallarlo" e' sufficiente cancellare il file.

* Installare il software con il pacchetto DEB:

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

    Svantaggi:
    * Potrebbe non essere al 100% compatibile con tutti i sistemi operativi / versioni dei sistemi operativi
        > Sicuramente NON e' compatibile con i sistemi NON basati su debian
    * Niente aggiornamenti automatici: occorre scaricare e installare manualmente il pacchetto DEB package.

    Puoi disinstallare la shell eseguendo il comando:
    ```
    dpkg --remove bettersis
    ```

* Usare l'eseguibile creato da PyInstaller:
    
    Scaricare l'eseguibile creato da PyInstaller dalla pagina [Github Release](https://github.com/mario33881/betterSIS/releases/latest) (e' il file chiamato "bsis" senza estensione file)

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
    * Niente aggiornamenti automatici: occorre installare manualmente la nuova versione e sostituire la versione vecchia
    
    > Su molte distro e' possibile scaricare l'eseguibile nella cartella ```bin``` della cartella home (```$HOME```): questo permette di eseguire il comando ```bsis``` da qualsiasi cartella come se betterSIS fosse installato

    Per "disinstallarlo" e' sufficiente cancellare il file.

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

* (esiste anche una [versione PyPI](https://pypi.org/project/bettersis/) ma non dovresti utilizzarla. L'ho creata per registrare il nome e per evitare possibili confusioni da parte dell'utente)
    > Potrebbe tornarmi comoda anche per creare futuri metodi di installazione

[Torna all'indice](#indice)

## Guida all'uso

Eseguire la shell interattiva di ```bettersis```.

Per eseguire la shell utilizzare:
* Python (si e' deciso di eseguire il codice sorgente) oppure
* Il comando ```bsis``` (se ```bettersis``` e' stato installato dal file .deb)
* Il comando ```./bsis``` (se si e' deciso di eseguire il file creato da Pyinstaller)
    > Se il percorso dell'eseguibile e' nella variabile d'ambiente ```$PATH``` e' sufficiente eseguire il comando ```bsis```
* Il comando ```bettersis``` (se si e' installata la versione snap)

Adesso e' possibile utilizzare la shell come se fosse la normale shell di SIS:
iniziare a leggere file (ad esempio usando ```read_blif```), ottimizzare circuiti,
simularli, ...

E' possibile vedere nella GIF ad inizio documentazione
un esempio di utilizzo.

Utilizzare il comando ```help``` per vedere sia i comandi di SIS sia i nuovi comandi forniti da betterSIS.
> Se la descrizione non e' sufficiente probabilmente su questa pagina sono presenti maggiori dettagli. Per ulteriori informazioni creare una issue.

Sono stati scritti dei tutorial su readthedocs (in italiano): [clicca qui per vedere i tutorial](https://bettersis.readthedocs.io/en/latest/tutorials/tutorials.html)

---

### Storico permanente dei comandi tra piu' sessioni

Questa funzionalita' permette di eseguire comandi SIS, chiudere betterSIS e poi riaprirlo in futuro e avere memorizzati i comandi eseguiti in passato utilizzando i pulsanti freccia su/giu'.

Questa funzionalita' e' disabilitata di default perche' betterSIS necessita' di scrivere il file ```~/.bsis_history``` per salvare i vecchi comandi e l'utente potrebbe non volere questo comportamento dal programma.

Per abilitare questa funzionalita' occorre impostare la variabile d'ambiente "```BSIS_HISTORY_ENABLED```" a "true".

> Per impostare la variabile d'ambiente modificare il file ```~/.bashrc``` file (o l'equivalente della shell di default del sistema operativo) e
> aggiungere questa riga ```export BSIS_HISTORY_ENABLED=true``` a fine file.

Di default il limite della dimensione dello storico e' di 100 KB ma e' possibile modificarlo impostando la variabile d'ambiente "```BSIS_HISTORY_SIZELIMIT```" (il valore minimo e' 1000 bytes)
> Per modificare questa dimensione aggiungere al file ```~/.bashrc``` (o equivalente) la seguente riga: ```export BSIS_HISTORY_SIZELIMIT=10000```.
>
> Sostituire "10000" con il numero di byte massimo desiderato.

Chiudere e riaprire la shell per attuare le modifiche.

[Torna all'indice](#indice)

## Trovato qualche problema?

Per favore crea una "issue" con tutti i dettagli qui: https://github.com/mario33881/betterSIS/issues

Se hai usato:
* la versione snap: esegui il seguente comando per creare un file di log e poi copia il contenuto nella issue.

        cat /var/log/syslog | grep \"bettersis\" > pybettersis.log

* la versione PyInstaller: esegui il seguente comando per creare un file di log e poi copia il contenuto nella issue.

        cat /var/log/syslog | grep \"bettersis\" > pybettersis.log

* il pacchetto DEB: copia il contenuto del file ```/var/log/pybettersis/pybettersis.log``` nella issue

[Torna all'indice](#indice)

## Changelog ![](https://i.imgur.com/SDKHpak.png)

**WIP 1.2.1:** <br>
### Modifiche:
* Adesso l'output originale e' mantenuto completamente intatto (inclusi i warning) e alla fine dell'esecuzione del comando vengono visualizzati i warning una seconda volta.
    > I warning erano nascosti perche' erano considerati duplicati (scelta dello sviluppatore) ma avere uno "storico" completo dell'output
    > e poi un breve riassunto con gli errori e/o warning ha molto piu' senso.

### Funzionalita' aggiuntive:
* Aggiunto storico permanente dei comandi tra piu' sessioni. Vengono salvati all'interno del file ```~/.bsis_history```. Questa funzionalita' e' disabilitata di default.

  Impostare la variabile d'ambiente "```BSIS_HISTORY_ENABLED```" a "true" per abilitare questa funzione (e' necessario chiudere e poi riaprire la shell).
  Leggere la documentazione per i dettagli su come abilitare questa funzionalita' e come modificare il limite della dimensione dello storico.
* Aggiunto il comando ```bsis_tutorials```: apre il browser alla [pagina dei tutorial SIS](https://bettersis.readthedocs.io/en/latest/tutorials/tutorials.html)
* Aggiunto il comando ```bsis_documentation```: apre il browser alla [pagina della documentazione di betterSIS](https://bettersis.readthedocs.io/en/latest/readme.html)
* Aggiunto il comando ```bsis_releases```: apre il browser alla [pagina per scaricare l'ultima versione di betterSIS](https://github.com/mario33881/betterSIS/releases/latest)
* Aggiunto il comando ```bsis_checkblif```: utilizza la libreria blifparser come un semplice tool di verifica per validare i file BLIF
* Adesso il comando ```help``` visualizza anche i comandi di betterSIS
* Nuovo metodo di installazione attraverso lo Snap store. E' possibile installare betterSIS con il comando ```snap install bettersis``` oppure utilizzando l'interfaccia grafica dello Snap store.
* Nuovo metodo di installazione: AppImage. E' paragonabile alla versione PyInstaller ma e' aggiornabile automaticamente.
    > Utilizzare il comando ```bsis_update``` per aggiornare la AppImage quando e' disponibile un nuovo aggiornamento
* Aggiunti due parametri a betterSIS: la flag ```--debug``` usata per scrivere piu' informazioni sul file di log e la flag ```--verbosedebug``` che visualizza le informazioni di debug nella shell.
    > ```--verbosedebug``` necessita di essere utilizzato insieme a ```--debug```

### Fix:
* Adesso il programma riesce a verificare la presenza di aggiornamenti
* Risolto l'errore ```UnicodeEncodeError: 'ascii' codec can't encode character in position 0: ordinal not in range(128)```
    > Questo errore appariva quando veniva visualizzato il titolo "BETTERSIS" come "ASCII art": 
    > il terminale deve essere configurato per usare una lingua con encoding UTF-8 con la variabile d'ambiente ```$LANG``` per poter visualizzare quei caratteri ASCII.
    >
    > Ora la "ASCII art" non viene visualizzata quando il terminale non e' configurato con encoding UTF-8.
* (siswrapper) Risolti errori di timeout per i comandi con l'output suddiviso in pagine (come, ad esempio, il comando ```help read_blif```).

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