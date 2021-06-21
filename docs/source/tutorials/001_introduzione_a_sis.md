---
html_meta:
  "description lang=en": "SIS introduction. What is SIS? Should you use it? How to use it."
  "description lang=it": "Introduzione a SIS. Cosa e' SIS? Dovresti usare SIS? Come usarlo."
  "keywords": "betterSIS, SIS, BLIF"
  "property=og:locale": "it_IT"
---

# Introduzione a SIS

## Cosa e' SIS?

SIS, acronimo che sta per Sequential Interactive Synthesis, e' un software sviluppato negli anni novanta dalla Universita' della California situata a Berkeley.

Come dice il nome, SIS permette di sintetizzare (ed ottimizzare) circuiti sequenziali, circuiti dotati di memoria, 
ma anche circuiti combinatori attraverso una shell interattiva.

```{admonition} nota
Nei circuiti combinatori ad ogni combinazione di input 
corrisponde un output indipendente dagli ingressi passati.

I circuiti sequenziali sono dotati di memoria: l'output dipende dall'input
attuale e dagli input passati.
```

# Perche' usare SIS? Viene ancora usato?

Il programma "standalone" attualmente viene solo utilizzato per scopi didattici per capire come funzionano gli strumenti di sintesi automatica ma le sue funzionalita' interne e i suoi algoritmi sono alla base di strumenti piu' complessi e moderni che vengono utilizzati dalle aziende per progettare sistemi digitali.


## Utilizzi di SIS

La shell di SIS accetta diversi comandi che si occupano di:

* Leggere un file di descrizione di un circuito.
    ```{admonition} nota
    Tipicamente in formato ```.blif``` (Berkeley Logic Interchange Format).
    
    Un altro formato utile e' il formato ```.eqn```: descrive
    il circuito come insieme di equazioni di operazioni logiche.
    ```

* Ottimizzare/minimizzare il circuito per ridurre l'area e/o il ritardo di propagazione.

* Mappare il circuito su componenti disponibili sul mercato.

* Visualizzare le statistiche del circuito per verificare se l'ottimizzazione ha
effettivamente migliorato area/ritardo.

* Simulare il circuito per (cercare di) garantire il corretto funzionamento del circuito.

* Scrivere su file (o visualizzare) il risultato delle ottimizzazioni e/o mappatura.

<br>

<div align=center>

[🢠 Indice](./tutorials.md) &nbsp; | &nbsp; [Guida all'installazione di SIS 🢡](./002_installazione_sis.md)

[🗎 Torna all'indice](./tutorials.md)

</div>
