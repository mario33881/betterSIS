# Automazione avanzata di SIS

Dopo aver automatizzato il processo di esecuzione
dei comandi SIS ed aver ottenuto su file l'output
l'ultimo passo per automatizzare completamente tutti i test
e' verificare che l'output dei circuiti sia l'output atteso.

* [Verifica semplice con diff](#verifica-semplice-con-diff)
* [Verifica avanzata con Python](#verifica-avanzata-con-python)
* [Workflow e test completamente automatici CI/CD](#workflow-e-test-completamente-automatici-ci-cd)

## Verifica semplice con diff

```diff``` e' un comando disponibile dalla
shell di molti (quasi tutti) sistemi Linux che permette di
controllare se due file sono identici.

Dopo aver creato il file di output atteso e aver
eseguito lo script per creare il file output dei comandi SIS
e' possibile eseguire il comando:

```
diff <file_output_atteso.txt> <file_output.txt>
```

diff:
* visualizzera' le differenze tra i due file
* restituira' al sistema operativo un exit code che indica se i file sono identici oppure no

E' possibile visualizzare manualmente il exit code dell'ultimo comando eseguito con il comando:

```
echo $?
```

A questo punto e' possibile creare un programma bash
simile a questo:

```bash
./testa_blif.sh  # contiene "sis -t pla -f scriptfantastico.script -x" 
                 # che esegue scriptfantastico.script con sis

# scriptfantastico.script contiene "set sisout output_sis.txt"
# che indica a sis di scrivere l'output nel file output_sis.txt
# e in fondo allo script "quit" che dice a sis di chiudersi a fine script

# abbiamo scritto un file output_atteso.txt
# con l'esatto output che ci aspettiamo da sis
diff output_sis.txt output_atteso.txt

if [ "$?" = "0" ] ; then
    echo "TEST PASSATO: SIS ha restituito l'output atteso"
else
    echo "TEST FALLITO: output diverso da quello atteso"
fi
```

```{note}
Personalmente non ho testato questo codice
ma dovrebbe funzionare correttamente.

NOTARE: gli spazi sono tutti necessari
(tra "```[```" e  "```$?```" e "```=```" e ...)
```

## Verifica avanzata con Python

Utilizzando un linguaggio di programmazione, come Python,
e' possibile creare delle test suite complesse.

Ad esempio e' possibile:
* Creare una cartella con i file di simulazione piu' frequenti
* Creare file di configurazione per specificare cosa testare e per quale circuito
* Eseguire comandi di set up e di tear down rispettivamente all'inizio e alla fine di ogni test
* Estrarre file di test di grandi dimensioni da file compressi

Ecc...

Il programma [blif_tester](https://github.com/arc6-202021/lib_componenti_sis/blob/main/blif_tester.py) che ho realizzato per l'elaborato di Architettura degli elaboratori permette di fare questo.

```{note}
Potete usare tranquillamente questo programma per testare il vostro elaborato.

Per capire come funziona e' possibile leggere la documentazione
del repository dell'elaborato qui: [https://github.com/arc6-202021/lib_componenti_sis](https://github.com/arc6-202021/lib_componenti_sis).

Una breve descrizione del programma e' presente alla fine della prossima sezione.
```

## Workflow e test completamente automatici CI/CD

```{note}
Questa sezione descrive il ragionamento che c'e' dietro alla configurazione di un sistema CI/CD:

E' possibile semplicemente leggere e capire come funziona e poi copiare da [https://github.com/arc6-202021/lib_componenti_sis](https://github.com/arc6-202021/lib_componenti_sis) la cartella ```.github``.
```

Questo e' un uso "molto avanzato" di SIS: e' possibile
utilizzare un sistema automatico CI/CD per, ad esempio, testare automaticamente
ad ogni ```git push``` i file BLIF (ovvero i file di descrizione dei circuiti per SIS) per garantirne il funzionamento.

Ci sono diversi sistemi CI/CD, ecco una lista breve di alcuni dei piu' noti:
* [Github actions](https://github.com/features/actions) (integrato in Github)
* [Travis CI](https://www.travis-ci.com/)
* [Circle CI](https://circleci.com/)
* [Gitlab CI](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/) per chi
preferisce Gitlab a Github
* molti altri... 

Ogni sistema deve essere configurato con un file di configurazione (tipicamente scritto in YAML, file ```.yml```) e la struttura del file varia da sistema a sistema: cerchero' di
essere il piu' generico possibile nella prossima parte...

Il processo di installazione concettualmente e' molto simile
a quello di una macchina Debian-based:

* scarichiamo il deb package (file ```.deb``` dell'installazione)
* installiamo il deb package

L'unica differenza e' che dobbiamo automatizzare questo processo: tutto
deve essere eseguito con pochi comandi da terminale.

I passi che dobbiamo seguire sono:

* Copiare l'url che e' "puntato" dal pulsante "Scarica" della sezione "Installazione su Debian o simili" (e' possibile cliccare con il tasto destro sul pulsante e poi cliccare su "Copia indirizzo link")

* Aggiungere il comando ```wget``` davanti all'url per automatizzare il processo di download.
    ```{note}
    ```wget``` e' un programma/comando che permette di scaricare file (sia di testo sia binari) da Internet via terminale.
    ```
    Il risultato dovrebbe essere simile/uguale al seguente (nota: se il link non cambia in futuro potete copiare questo):

    ```
    wget https://github.com/JackHack96/logic-synthesis/releases/download/1.3.6/sis_1.3.6-1_amd64.deb
    ```
    Senza specificare altri parametri il file verra' salvato nella cartella corrente
    con il suo nome originale (in questo caso ```sis_1.3.6-1_amd64.deb```)

* L'installazione e' esattamente come quando si installa il deb package su una macchina Debian-based...

    Si esegue il comando:
    ```
    sudo dpkg -i sis_1.3.6-1-amd64.deb
    ```
    ```{note}
    Eventualmente cambiare ```sis_1.3.6-1_amd64.deb``` con il nome del file ```.deb```
    ```

Per eseguire i comandi in un'unica riga basta aggiungere ```&&``` tra i due comandi:

```
wget https://github.com/JackHack96/logic-synthesis/releases/download/1.3.6/sis_1.3.6-1_amd64.deb && sudo dpkg -i sis_1.3.6-1_amd64.deb
```

Questo comando (opportunamente modificato se necessario) scarica ed installa SIS e deve essere inserito nel file di configurazione del sistema CI/CD.

D'ora in poi il resto della guida andra' avanti parlando nello specifico di Github Actions perche'
e' fortemente integrato in Github e perche' l'ho scelto per l'elaborato di Architettura degli elaboratori.

Ecco uno dei file YAML di test di file BLIF che ho utilizzato:
```{warning}
Attenzione alle indentazioni: sono molto importanti in YAML tanto quanto lo sono in Python.

Se si desidera replicare questa soluzione copiare il contenuto del file [registri_tester.yml cliccando qui](https://github.com/arc6-202021/lib_componenti_sis/blob/main/.github/workflows/registri_tester.yml)
```

```{eval-rst}
.. code-block:: yaml

    on:
        push

    name: Tester registri

    jobs:
        build:
            name: Tester registri
            runs-on: ubuntu-18.04
            steps:
            - name: Checkout code
                uses: actions/checkout@v2
            - name: Install Python
                uses: actions/setup-python@v2.2.1
                with:
                python-version: 3.8.5
            - name: Install SIS
                run: wget https://github.com/JackHack96/logic-synthesis/releases/download/1.3.6/sis_1.3.6-1_amd64.deb && sudo dpkg -i sis_1.3.6-1_amd64.deb
            - name: Check Python and SIS version
                run: echo -e "\n[PYTHON VERSION]\n" && python3 --version && echo -e "\n\n[SIS VERSION]\n" && (sis -v || true)
            - name: Execute tests
                run: python3 blif_tester.py registri
```

Anche se spieghero' brevemente come funziona qui sotto questa configurazione consiglio di cercare tutorial online ed imparare ad usare un sistema CI/CD (anche diverso da Github Actions) perche' e' molto comodo automatizzare test (o perfino deploy completi) di parte e/o di tutto il codice che si scrive.

Sapere nei dettagli come funziona vi permette anche di espandere i test possibili
e fare troubleshooting quando ci sono problemi.

Ecco come funziona il file di configurazione:
```{eval-rst}
.. code-block:: yaml

    on:
        push
```
Dice che quando il programmatore esegue un ```git push``` il "workflow" del file di configurazione viene eseguito.

```{eval-rst}
.. code-block:: yaml
    
    name: Tester registri
```
E' il nome del workflow: appare su Github con quel nome e se si crea un badge (come questo: ![Badge tester registri](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20registri/badge.svg)) verra' visualizzato come nome del badge.

```{note}
Se c'e' scritto "passing" con sfondo verde il workflow e' terminato con successo. (codice di uscita uguale a 0 in tutti i comandi)

Se c'e' scritto "failed" con sfondo rosso il workflow e' fallito in uno dei suoi comandi (codice di uscita diverso da 0 in uno dei comandi)
```

```{eval-rst}
.. code-block:: yaml

    jobs:
        build:
            name: Tester registri
            runs-on: ubuntu-18.04
```
In questa sezione viene indicato che il file di configurazione contiene un "Job" (di tipo build),
con nome "Tester registri", eseguito su macchina virtuale in cui e' installato Ubuntu 18.04.

```{eval-rst}
.. code-block:: yaml

    steps:
      - name: Checkout code
        uses: actions/checkout@v2
```
Vengono elencati gli step da eseguire nel job.

Il primo step, chiamato "Checkout code" scarica il repository (detto semplicemente e' la cartella root, principale, del progetto).

```{eval-rst}
.. code-block:: yaml

    - name: Install Python
        uses: actions/setup-python@v2.2.1
        with:
          python-version: 3.8.5
```
Questo step "Install Python" installa Python (versione 3.8.5).

```{note}
Se si desidera e' possibile cambiare linguaggio di programmazione.

Io ho scelto di utilizzare Python per testare i file BLIF.

NOTA: se si sceglie di usare Python potete usare il mio script, altrimenti
vi tocca scrivere codice "da zero" che fa piu' o meno la stessa cosa.
```

```{eval-rst}
.. code-block:: yaml

    - name: Install SIS
        run: wget https://github.com/JackHack96/logic-synthesis/releases/download/1.3.6/sis_1.3.6-1_amd64.deb && sudo dpkg -i sis_1.3.6-1_amd64.deb
```
Questo step "Install SIS" esegue il comando per scaricare e installare SIS versione 1.3.6.

```{eval-rst}
.. code-block:: yaml

    - name: Check Python and SIS version
        run: echo -e "\n[PYTHON VERSION]\n" && python3 --version && echo -e "\n\n[SIS VERSION]\n" && (sis -v || true)
```
Questo step puo' essere considerato "inutile" perche' visualizza semplicemente la versione
di Python e di SIS installati.

L'ho creato per essere sicuro che il workflow abbia avuto effettivamente successo fino a questo punto
e che SIS sia eseguibile tramite il comando ```sis```.

Alcuni di voi avranno notato qualcosa di strano nel comando: "```(sis -v || true)```".

Questa parte esegue sis con il parametro "-v" e se non ha successo esegue "true", ovvero
vero, che restituisce sempre 0, successo... Quella porzione di comando tra parentesi tonde non fallira' mai...

Come mai, in un sistema CI/CD che deve dirmi se e quali comandi hanno avuto successo o meno, ho deciso di eseguire questa porzione di comando che si conclude sempre con successo? Per necessita'... 

SIS non possiede il parametro "-v" e non ha flag alternative per visualizzare un help senza dargli parametri che non riconosce... Quindi non c'e' un modo di fare cio' che voglio fare senza che SIS
consideri il comando come "fallito".

```{note}
Magari l'opzione esiste ma non l'ho trovata tra le varie (e poche) documentazioni del programma...
```

Questo "successo incondizionato" crea problemi nel workflow? No.

Non crea problemi perche' il prossimo step che esegue SIS per testare i file BLIF
non ha "stratagemmi" per ottenere sempre esito positivo.

```{eval-rst}
.. code-block:: yaml

    - name: Execute tests
        run: python3 blif_tester.py registri
```
Questo e' il cuore del test: esegue con Python il mio script chiamato "blif_tester" passando
come parametro "registri". Lo script si occupera' di trovare i file BLIF e eseguirli con SIS.

```{note}
Per chi e' interessato: "registri" e' il nome della cartella che contiene i file BLIF con i registri.

Ho deciso di far funzionare il mio script in questo modo: se non vengono passati parametri
vengono testati tutti i file BLIF nelle sottocartelle, altrimenti vengono testati solo
i file blif nella cartella specificata nel parametro.

Questo mi permette di parallelizzare su piu' workflow i vari test. (o eseguire solo parte dei test)

E' possibile vedere come funzionano tutti i workflow guardando [questo repository (clicca qui)](https://github.com/arc6-202021/lib_componenti_sis) che contiene l'elaborato di architettura degli elaboratori del mio gruppo. 

In particolare controllare la cartella ```".github/workflows"```, lo script ```blif_tester.py``` e il file ```README.md```.

Potete usare il mio script per il vostro progetto senza problemi.
```

Lo script esce con codice 0 (successo) quando gli output dei file BLIF sono identici agli output attesi/desiderati.

Negli altri casi il comando ha esito negativo e il workflow verra' considerato come "failed":
apparira' una X rossa su Github e i badge indicheranno il fallimento con il colore rosso (oltre alla scritta "failed").

<br>

Grazie ai workflow e' possibile automatizzare i test dei file BLIF, fare ottimizzazioni (io ho automatizzato l'ottimizzazione della fsm), 
inviare notifiche via mail / discord (tramite webhook) / altro e in generale 
eseguire tutti i comandi che si possono eseguire manualmente da terminale.



<div align=center>

[🢠 Semplice automazione in SIS](./009_automazione_semplice.md)

[🗎 Torna all'indice](./tutorials.md)

</div>