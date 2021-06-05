# Semplice automazione in SIS

E' possibile automatizzare in vari modi l'esecuzione delle
simulazioni (e di altri comandi) in SIS.

In questa pagina vengono elencati i metodi piu' semplici:
* [Script e il comando source](#script-e-il-comando-source)
* [Script e parametro -f](#script-e-parametro--f)
* [Automazione avanzata](#automazione-avanzata)

## Script e il comando source

Questo e' il primo (e il piu' semplice) metodo di automazione
per poter eseguire piu' comandi in SIS.

Per farlo basta:
1. creare un file di testo (io come "standard personale" ho scelto di mettere l'estensione ```.script```)

2. scrivere i comandi che si vorrebbero normalmente eseguire su SIS.

    Esempio di un file chiamato "```scriptfantastico.script```":
    ```
    echo Leggo il file blif
    read_blif miocircuito.blif

    echo Simulo: 0 0 0 0 1 0 1 0 1 0 1
    simulate 0 0 0 0 1 0 1 0 1 0 1

    echo Simulo: 0 0 0 0 1 0 1 0 1 0 1
    simulate 0 0 0 0 1 0 1 0 1 0 1

    echo Simulo: 0 1 0 0 1 0 1 1 1 0 1
    simulate 0 1 0 0 1 0 1 1 1 0 1

    echo Simulo: 0 0 1 0 1 1 1 0 1 0 1
    simulate 0 0 1 0 1 1 1 0 1 0 1

    echo Statistiche prima di rugged:
    print_stats

    echo Adesso eseguo lo script rugged
    source script.rugged

    echo Statistiche dopo rugged:
    print_stats
    ```

    ```{note}
    Ho inserito comandi "a caso" ma plausibili
    ```

3. Eseguire normalmente SIS con il comando ```sis``` e poi usare il comando ```source```.

    Procedendo con l'esempio di prima e supponendo che nella cartella
    in cui ho eseguito SIS si trova lo script ```scriptfantastico.script``` e il file blif ```miocircuito.blif```, eseguo il comando:

    ```
    source scriptfantastico.script
    ```
    Dopo aver eseguito questo comando tutte le istruzioni inserite
    nello script verranno eseguite e gli output verranno visualizzati
    come se avessimo eseguito manualmente quei comandi.

    A questo punto e' possibile analizzare "a mano" l'output e vedere
    se tutto ha funzionato come doveva.

4. Uscire da SIS con il comando ```quit``` quando si e' finito di usarlo.

## Script e parametro -f

SIS dispone di un parametro, ```-f <file_script>```, che gli permette
di eseguire i comandi contenuti all'interno di un file.
```{note}
Non c'e' bisogno neanche di eseguire sis e fare il source dello script
```

Ecco cosa bisogna fare:
1. creare un file di testo (io come "standard personale" ho scelto di mettere l'estensione ```.script```)

2. scrivere i comandi che si vorrebbero normalmente eseguire su SIS.

    Esempio di un file chiamato "```scriptfantastico.script```":
    ```
    echo Leggo il file blif
    read_blif miocircuito.blif

    echo Simulo: 0 0 0 0 1 0 1 0 1 0 1
    simulate 0 0 0 0 1 0 1 0 1 0 1

    echo Simulo: 0 0 0 0 1 0 1 0 1 0 1
    simulate 0 0 0 0 1 0 1 0 1 0 1

    echo Simulo: 0 1 0 0 1 0 1 1 1 0 1
    simulate 0 1 0 0 1 0 1 1 1 0 1

    echo Simulo: 0 0 1 0 1 1 1 0 1 0 1
    simulate 0 0 1 0 1 1 1 0 1 0 1

    echo Statistiche prima di rugged:
    print_stats

    echo Adesso eseguo lo script rugged
    source script.rugged

    echo Statistiche dopo rugged:
    print_stats
    ```

    ```{note}
    Ho inserito comandi "a caso" ma plausibili
    ```

3. Eseguire da terminale il comando:

        sis -t pla -f scriptfantastico.script -x

4. Uscire da SIS con il comando ```quit``` quando si e' finito di usarlo.

<br>

---

<br>

All'apparenza non cambia nulla dall'altro sistema...
Ma il semplice fatto che questo metodo non richiede di inserire
neanche un comando sulla shell di SIS permette di automatizzare
veramente molte piu' operazioni! E questo permette anche di velocizzare il workflow e di ridurre le nostre possibilita' di errore.

Supponiamo che non vogliamo neanche uscire manualmente da SIS...

Basta aggiungere a fine script ```quit``` e il gioco e' fatto.
```{note}
Si poteva fare anche prima in realta'...
```

Supponiamo ora che non vogliamo neppure vedere il risultato su terminale
perche' vogliamo avere gli output permanenti su un file per una possibile analisi automatica...

Basta aggiungere come prima riga dello script:

    set sisout <file_output>

```{note}
Questo e' un comando in sis. ```<file_output>``` e' il nome del file di output.
```

Adesso abbiamo gli input a portata di un comando e l'output
scritto su file: possiamo creare uno script bash, ad esempio ```testa_blif.sh```, per
eseguire il comando SIS e a questo punto basta eseguire lo script da terminale
e aprire il file al termine.

```
./testa_blif.sh
```

```{note}
Da notare il ```./``` a inizio comando
```

Un solo comando facilmente ricordabile (e un editor che riconosce in tempo reale la modifica del file di output)
e potete immediatamente vedere e scorrere gli output di tutti i comandi!

## Automazione avanzata

Il passo successivo e "finale" dell'automazione e' il controllo
automatico dell'output.

Sappiamo gia' il risultato che ci attendiamo da una simulazione:
basta confrontare il risultato ottenuto dalla simulazione e l'output
che desideriamo e capiamo subito se il nostro file BLIF funziona o no.

```{note}
Esempio: se si esegue ```simulate 0 1``` su un file BLIF che definisce
una porta AND e il risultato e' ```Outputs: 1``` c'e' qualcosa di sbagliato...
```

Nella prossima pagina della wiki trattero' questo passaggio.

<div align=center>

[🢠 Documentazione SIS online](./008_documentazione_sis.md) &nbsp; | &nbsp; [Automazione avanzata in SIS 🢡](./010_automazione_avanzata.md)

[🗎 Torna all'indice](./tutorials.md)

</div>