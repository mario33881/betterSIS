---
myst:
  html_meta:
    "description lang=en": "SIS documentation: what I've found online."
    "description lang=it": "Documentazioni SIS: cosa ho trovato online."
    "keywords": "betterSIS, SIS, BLIF, SIS documentation"
    "property=og:locale": "it_IT"
---

# Documentazione SIS online

Questa pagina contiene documentazioni/presentazioni riguardanti SIS che ho trovato online:

* [https://course.ece.cmu.edu/~ee760/760docs/blif.pdf](https://course.ece.cmu.edu/~ee760/760docs/blif.pdf)
  
  ```{note}
  Una delle informazioni che per me e' stata piu' utile contenuta in questo pdf e' una frase a pagina 4: 
   
  "All feedback loops in a model must go through a generic-latch. Purely combinational-logic cycles are not allowed."
   
  Per correggere l'errore di cycle dovuto a loop/cicli nei circuiti (che possono avvenire ad esempio quando si sviluppa una FSMD interfacciando un datapath ad una FSM) occorre aggiungere un latch per "interrompere" il loop.
  ```

* [https://www.di.univr.it/documenti/OccorrenzaIns/matdid/matdid882703.pdf](https://www.di.univr.it/documenti/OccorrenzaIns/matdid/matdid882703.pdf)

* [https://www.researchgate.net/publication/2624520_SIS_A_System_for_Sequential_Circuit_Synthesis](https://www.researchgate.net/publication/2624520_SIS_A_System_for_Sequential_Circuit_Synthesis)

* [http://www.diit.unict.it/users/mpalesi/COURSES/CE_08-09/DOWNLOAD/16_introduzione_sis.pdf](http://www.diit.unict.it/users/mpalesi/COURSES/CE_08-09/DOWNLOAD/16_introduzione_sis.pdf)

<div align=center>

[🢠 Errori e Warning in SIS](./007_errori_e_warning.md) &nbsp; | &nbsp; [Automazione semplice in SIS 🢡](./009_automazione_semplice.md)

[🗎 Torna all'indice](./tutorials.md)

</div>