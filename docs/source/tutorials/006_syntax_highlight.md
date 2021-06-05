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

Gli editor di testo, come Visual Studio Code, non riconoscono il formato e quindi non possono aiutare con:

* Highlight della sintassi

* auto completamento delle parole chiave

* descrizione delle parole chiave

* template standard

Ho realizzato una estensione per Visual Studio Code per aggiungere queste funzionalita'.

L'estensione si chiama ["BLIF (SIS)" sul marketplace](https://marketplace.visualstudio.com/items?itemName=mario33881.vscode-blif) di Visual Studio Code o [vscode-blif su Github](https://github.com/mario33881/vscode-blif).

#### Installare l'estensione

Per installare l'estensione e' possibile:

* Accedere con il browser al [marketplace di Visual Studio Code cliccando qui](https://marketplace.visualstudio.com/items?itemName=mario33881.vscode-blif) e cliccare sul pulsante verde "Install". A questo punto, dando il consenso, il browser aprira' Visual Studio Code per installare l'estensione.

* Cercare "BLIF (SIS)" sul marketplace delle estensioni di Visual Studio Code mediante l'editor stesso e installarla cliccando sul pulsante "Install".

* Se si apre un file con estensione ```.blif``` Visual Studio Code vi dira' con una notifica in basso a destra 
che esistono estensioni nel marketplace per questo formato: cliccare il pulsante che vi fa accedere al marketplace.

    A sinistra verranno elencate le varie estensioni (attualmente solo una): cliccare su "BLIF (SIS)" e poi cliccare sul pulsante "Install" per installarla

Per ulteriori informazioni su questi ed altri metodi di installazione accedere al repository Github [cliccando qui](https://github.com/mario33881/vscode-blif)

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

L'estensione, attualmente, non e' stata aggiunta al Package Control Channel quindi
non e' possibile installarla direttamente da Sublime Text.

[E' possibile scaricare l'estensione per Sublime Text da qui](https://github.com/mario33881/sublime-blif_sis)
```{note}
E' stata ufficialmente verificata ed e' possibile installarla dal package manager di Sublime Text chiamato "package control".
```

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