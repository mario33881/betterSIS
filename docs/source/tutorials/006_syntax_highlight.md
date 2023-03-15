---
myst:
  html_meta:
    "description lang=en": "syntax highlighting for BLIF (SIS) files. Extensions for Visual Studio Code, Sublime Text, Notepad++ and Vim."
    "description lang=it": "syntax highlight per i file BLIF (SIS). Estensioni per Visual Studio Code, Sublime Text, Notepad++ e Vim."
    "keywords": "betterSIS, SIS, BLIF, syntax highlight, Visual Studio Code extension, Sublime Text package, Notepad++, Vim"
    "property=og:locale": "it_IT"
---

# Syntax Highlighting per file BLIF

Questa pagina elenca delle estensioni che permettono al
vostro editor di testo di riconoscere il formato
BLIF e colorare le parole chiave. (piu' altre funzionalita' ugualmente utili)

## vscode-blif: estensione per Visual Studio Code

<p align="center">
<img height="150px" src="https://raw.githubusercontent.com/mario33881/vscode-blif/9c1c9abb292ec0ed749e85ead7f2fdea4b80dbfc/images/icon.png" />
<br>
<img src="https://github.com/mario33881/vscode-blif/blob/9c1c9abb292ec0ed749e85ead7f2fdea4b80dbfc/images/presentation.gif?raw=true" />
</p>

Gli editor di testo, come Visual Studio Code, non riconoscono il formato BLIF e quindi non possono aiutare con:

* Highlight della sintassi

* auto completamento delle parole chiave

* descrizione delle parole chiave

* template standard (iniziare a scrivere il punto esclamativo "!", selezionare uno dei template e premere il tasto tab)

Ho realizzato una estensione per Visual Studio Code per aggiungere queste funzionalita'.

L'estensione si chiama ["BLIF (SIS)" sul marketplace](https://marketplace.visualstudio.com/items?itemName=mario33881.vscode-blif) di Visual Studio Code o [vscode-blif su Github](https://github.com/mario33881/vscode-blif).

### Installare l'estensione

Per installare l'estensione e' possibile scegliere UNO dei seguenti metodi:

* Accedere con il browser al [marketplace ufficiale di Visual Studio Code cliccando qui](https://marketplace.visualstudio.com/items?itemName=mario33881.vscode-blif) e cliccare sul pulsante verde "Install". A questo punto, dopo aver dato il consenso, il browser aprira' Visual Studio Code per installare l'estensione.

* Cercare "BLIF (SIS)" sul marketplace delle estensioni di Visual Studio Code mediante l'editor stesso e installarla cliccando sul pulsante "Install".

* Se si apre un file con estensione ```.blif``` Visual Studio Code vi dira' con una notifica in basso a destra 
che esistono estensioni nel marketplace per questo formato: cliccare il pulsante che vi fa accedere al marketplace.

    A sinistra verranno elencate le estensioni per i file BLIF (attualmente solo una): cliccare su "BLIF (SIS)" (di "mario33881") e poi cliccare sul pulsante "Install" per installarla

Per ulteriori informazioni su questi ed altri metodi di installazione accedere al repository Github [cliccando qui](https://github.com/mario33881/vscode-blif)

```{note}
Per chi fosse interessato il repository contiene anche il codice sorgente della estensione.
```

---

## SISvim: estensione per VIM

Per chi utilizza vim esiste una estensione simile a quella che ho creato per Visual Studio Code: si chiama SISvim.

Lo sviluppatore si chiama [Dapizz01 su Github](https://github.com/Dapizz01)

[E' possibile scaricare l'estensione per vim da qui](https://github.com/Dapizz01/SISvim)

---

## sublime-blif_sis: l'estensione per Sublime Text

<p align="center">

<img alt="GIF che mostra syntax highlight" src="https://raw.githubusercontent.com/mario33881/sublime-blif_sis/6d12b011ab479341949a42bd9f5175391fedc0ea/assets/presentation.gif"/>
</p>

Simile alla estensione vscode-blif, questa estensione permette di avere Syntax Highlighting,
autocompletamento e template base per l'editor di testo Sublime Text.

L'estensione e' stata approvata e aggiunta a Package Control, il package manager ufficiale dei pacchetti(/estensioni) per Sublime Text, quindi
e' possibile installarla direttamente da Sublime Text.

Ecco i passi per installarla:

* Installa il [package manager "package control" seguendo questa guida](https://packagecontrol.io/installation) su Sublime Text
* Da Sublime Text nella toolbar in alto andare su ```Tools```, poi cliccare ```Command Palette```.
* Digitare "Install Package": dovrebbe apparire l'opzione ```Package Control: Install Package```, cliccare quella opzione per selezionarla
* Cercare "blif" oppure "sis" oppure "blif_sis".
* Cliccare sul pacchetto chiamato "blif_sis" per installarlo.

```{note}
Assicurarsi prima che l'URL del repository (indicato sotto al nome del pacchetto) sia https://github.com/mario33881/sublime-blif_sis
```

* Chiudere e riaprire Sublime Text.
* Verificare che sia presente il syntax highlight aprendo un file BLIF con Sublime Text. Se funziona l'estensione e' stata installata correttamente.

Se non funziona provare ad aprire un file .blif e POI (mentre il file BLIF e' aperto) dalla Command Palette eseguire il comando:
```{note}
Set Syntax: blif
```
Questo dice a Sublime Text che i file .blif hanno la sintassi "blif", descritta nella estensione.

[Per ulteriori informazioni, ad esempio per vedere il codice corgente, clicca qui](https://github.com/mario33881/sublime-blif_sis)

---
## notepadpp-blif_sis: L'estensione per Notepad++
<p align="center">

<img alt="GIF che mostra syntax highlight" src="https://raw.githubusercontent.com/mario33881/notepadpp-blif_sis/6f7d5ee4613695e3654fb94b4b59b66dd0798f77/assets/syntax_highlight.png"/>
</p>

La "estensione" per Notepad++ e' [scaricabile da qui](https://github.com/mario33881/notepadpp-blif_sis)

Le funzionalita' incluse sono:
* syntax highlighting
* 2 macro per creare i file BLIF template

<div align=center>

[🢠 siswrapper: il wrapper per automatizzare SIS con Python](./005_siswrapper.md) &nbsp; | &nbsp; [Errori e Warning in SIS 🢡](./007_errori_e_warning.md)

[🗎 Torna all'indice](./tutorials.md)

</div>