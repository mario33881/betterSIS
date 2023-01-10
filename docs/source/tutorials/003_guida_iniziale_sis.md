---
myst:
  html_meta:
    "description lang=en": "SIS starting guide. Workflow, the and logic gate."
    "description lang=it": "Guida iniziale SIS. Workflow tipico e la porta logica and."
    "keywords": "betterSIS, SIS, BLIF, SIS workflow, and logic gate"
    "property=og:locale": "it_IT"
---

# Guida iniziale SIS

## Workflow tipico

Tipicamente la procedura per la progettazione di circuiti combinatori segue questi passi:

1. Viene scritto con un editor di testo il file che descrive il comportamento del circuito (insieme di porte logiche descritte da tabella/e di verita')

2. Si legge su SIS il file con uno dei comandi appositi

3. Si simula il circuito

4. Si ottimizza il circuito
   > E si simula di nuovo il circuito...

5. Si scrive su file il risultato della ottimizzazione

6. Se necessario si mappa il circuito per poterlo realizzare fisicamente con componenti disponibili in commercio

Questi passaggi vengono eseguiti per creare:
* porte logiche
* multiplexer
* demultiplexer
* shifter
* sommatori
* sottrattori
* comparatori (uguaglianza, maggiore, minore, maggiore uguale, minore uguale, diverso)
* registri
* datapath (insieme di unita' di calcolo in cascata: operazioni logico-matematiche e registri)

<br>

Per progettare circuiti sequenziali (ad esempio macchine a stati finiti, o FSM) invece:

1. Viene scritto con un editor di testo il file che descrive il comportamento del circuito (si specifica la tabella degli stati)

2. Si legge su SIS il file con uno dei comandi appositi

3. Si simula il circuito

4. Si minimizzano e si codificano gli stati (solo se la codifica non e' stata specificata manualmente nel file)

5. Si ottimizzano le funzioni di stato prossimo e di uscita
    > E si simula di nuovo il circuito...

6. Si scrive su file il risultato della ottimizzazione

7. Se necessario si mappa il circuito per poterlo realizzare fisicamente con componenti disponibili in commercio

<br>

E' possibile anche realizzare circuiti che includono circuiti sequenziali e circuiti combinatori.
(FSMD: FSM + Datapath)

```{warning}
ATTENZIONE: prima di includere circuiti sequenziali (FSM) in altri circuiti occorre codificare gli stati. 

Il file con le codifiche puo' poi essere incluso in altri circuiti. Se non si codificano gli stati il circuito non dara' i risultati attesi. (anche se il file blif con la FSM funziona senza problemi)
```

## Primo circuito: porta logica AND

Come primo esercizio proviamo a creare una porta logica AND.

Una porta AND ha:
* due input: chiamiamoli ```A``` e ```B```
* un output: chiamiamolo ```O```
* l'output vale 1 quando i due input valgono 1, altrimenti vale zero.

    |A|B|O|
    |-|-|-|
    |0|0|0|
    |0|1|0|
    |1|0|0|
    |1|1|1|

Per descrivere a SIS come funziona una porta logica AND
dobbiamo creare un file ```.blif```. Chiamiamolo con un nome che ha senso, come ```and.blif```.

Scrivere nel file:
```
.model and
.inputs A B
.outputs O

.names A B O
11 1

.end

```

```{admonition} nota
Notare l'ultima riga vuota: e' consigliato crearla in tutti i file BLIF
per evitare problemi.
```

<br>

Proviamo a simulare il circuito:
1. Aprire SIS con il comando ```sis``` nella cartella in cui si e' creato il file.
2. Eseguire il comando ```read_blif and.blif``` per leggere il file BLIF chiamato ```and.blif```
3. Simulare il circuito con il comando ```simulate <input 1> <input 2>``` dove ```<input 1>``` e ```<input 2>``` sono i due input e devono essere sostituiti con "```0```" e/o "```1```".

    ```{admonition} nota
    Ci sono due input perche' in questo caso il circuito ha 2 input: in un altro circuito potrebbe essere necessario indicare piu' o meno valori in input in base al numero di input del circuito stesso.
    ```

    Ad esempio, per simulare il circuito con ```A=0``` e ```B=0```, eseguire:
    ```
    simulate 0 0
    ```
    L'output atteso dovrebbe essere "```0```"

    Ora, per simulare il circuito con ```A=1``` e ```B=1```, eseguire:
    ```
    simulate 1 1
    ```
    L'output atteso dovrebbe essere "```1```"

    E' possibile eseguire la simulazione sulle altre due combinazioni. (```0 1``` e ```1 0```), per ```A=1``` e ```B=0```:
    ```
    simulate 1 0
    ```
    E per ```A=0``` e ```B=1```:
    ```
    simulate 0 1
    ```

    L'output in entrambe i casi dovrebbe essere "```0```"

<br>

Analizziamo il file BLIF:
```
.model and
```
La keyword ```.model``` specifica il nome del circuito/componente.

E' utile quando si desidera usare piu' componenti che svolgono la stessa funzione (anche descritti su piu' file diversi).

```{admonition} nota
Ad esempio un sommatore da 4 bit puo' essere creato definendo cosa e' un sommatore a 1 bit
e poi metterne 4 collegati "in cascata".
```

Non e' necessario dargli lo stesso nome del file ma personalmente lo consiglio. (evita il rischio di dimenticarsi quale file contiene quale componente)

```
.inputs A B
```
La keyword ```.inputs``` indica "i seguenti elementi, separati da uno spazio, sono i nomi degli input"

```{admonition} nota
Notare la ```s``` in ```.inputs```
```

```
.outputs O
```
La keyword ```.outputs``` indica "i seguenti elementi, separati da uno spazio, sono i nomi degli output"

```{admonition} nota
Notare la ```s``` in ```.outputs```
```

```
.names A B O
11 1
```
La keyword ```.names``` indica "i seguenti elementi descrivono una funzione booleana: gli elementi, separati da uno spazio, sono i nomi degli input; l'ultimo elemento e' il nome dell'output"

```{admonition} nota
Notare la ```s``` in ```.names```
```

```{admonition} nota
Non e' per forza necessario che il ```.names``` abbia gli input specificati in ```.inputs``` e gli output in ```.outputs```:

Ad esempio e' possibile dare un nome arbitrario (ovviamente diverso dagli altri) all'output
di un ```.names``` e creare un nuovo ```.names``` piu' avanti che riceve in input l'output del ```.names``` precedente in modo da suddividere la funzione
booleana in sotto-funzioni piu' semplici.

Esempio:

    
    .model mycircuit
    .inputs a b
    .outputs o
        
    .names a example
    1 0

    .names example a b o
    101 1
    111 1

    .end
    

In questo circuito:
* ```a``` e' input sia del circuito sia di due funzioni booleane.
* ```example``` e' output della prima funzione booleana e input della seconda.
* ```b``` e' input sia del circuito sia della seconda funzione booleana.
* ```o``` e' output sia del circuito sia della seconda funzione booleana.

```

Sotto la keyword ```.names``` segue la tabella di verita' della funzione booleana:

```11 1``` indica "quando il primo elemento di .names, ovvero A, vale 1 e il secondo elemento (B) vale 1 allora l'output (separato da uno spazio dagli input, in questo caso O) vale 1.

```{warning}
ATTENZIONE: uno dei primi errori "del principiante" e' inserire l'intera
tabella di verita' sotto a ```.names```: SIS dara' l'errore "```must give F or R, but not both```".

SIS si aspetta o i mintermini (output uguale a uno) o i maxtermini (output uguale a zero), NON entrambi.
```

```
.end
```
La keyword ```.end``` indica la fine del componente definito a partire dalla keyword ```.model```.


<div align=center>

[🢠 Installazione SIS](./002_installazione_sis.md) &nbsp; | &nbsp; [betterSIS: la shell moderna per SIS 🢡](./004_bettersis.md)

[🗎 Torna all'indice](./tutorials.md)

</div>