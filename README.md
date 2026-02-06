# Sistema a Dati Campionati

Repository per l'implementazione in Python di sistemi di dati campionati per tesi su "Controlli Automatici".

Questo progetto analizza la trasformazione di sistemi a tempo continuo nel dominio discreto utilizzando un mantenitore di ordine zero. L'obiettivo è studiare il comportamento della risposta al gradino al variare dei parametri del sistema, con particolare attenzione alla stabilità e ai fenomeni di fase non minima (undershoot) introdotti dagli zeri nel semipiano destro.

## 1) Esecuzione Immediata (Google Colab)
Se non desideri configurare un ambiente di sviluppo locale, puoi eseguire il codice direttamente nel browser utilizzando il notebook predisposto:

* **`Simulazione_Controllo_Digitale.ipynb`**: [Apri in Google Colab](https://colab.research.google.com/drive/1oqKPVfyog_sogelR3DbToiNwmy9wjoLn?usp=sharing).

Il notebook contiene tutto il codice sorgente unificato ed è pronto per l'esecuzione immediata.

## 2) Struttura del Repository
Il repository è organizzato come segue:

* **`main.py`**: Script Python principale. Contiene l'implementazione modulare che richiama le funzioni dalla cartella `src`. Esegue la simulazione temporale e genera i grafici comparativi.
* **`Simulazione_Controllo_Digitale.ipynb`**: Notebook Jupyter completo. Contiene l'intera logica del progetto in un unico file. È identico alla versione Colab ed è presente in locale per essere eseguito comodamente su **Visual Studio Code**.
* **`src/`**: Cartella contenente i moduli sorgente (utilizzati dallo script `main.py`):
    * `pd_z.py`: Funzioni per la discretizzazione dei modelli continui $P(s)$ in $P_d(z)$.
    * `cd_z.py`: Algoritmi per il calcolo dei controllori stabilizzanti.
    * `utils.py`: Funzioni di utilità per operazioni polinomiali e formattazione dell'output.
* **`requirements.txt`**: Elenco delle dipendenze necessarie per replicare l'ambiente di sviluppo.
* **`discrete_systems_analysis.png`**: Immagine di output generata dallo script, che mostra visivamente il confronto tra le risposte dei sistemi.

## 3) Installazione Locale
Per garantire il corretto funzionamento del codice sul proprio computer, è necessario installare le librerie Python richieste (Numpy, Scipy, Matplotlib).

Tutte le dipendenze possono essere installate automaticamente tramite **pip**. Aprire il terminale nella cartella del progetto ed eseguire:

```bash
pip install -r requirements.txt
```

## 4) Istruzioni di Esecuzione

Il progetto può essere eseguito in due modalità, a seconda delle preferenze:

### Opzione A: Esecuzione Script (Terminale)
Questa è la modalità standard per eseguire la simulazione completa in un solo passaggio. Assicurarsi di essere nella cartella principale del progetto ed eseguire:

```bash
python3 main.py
```
Lo script calcolerà le funzioni di trasferimento, stamperà a video i polinomi risultanti e salverà il grafico della risposta al gradino nel file `discrete_systems_analysis.png`.

### Opzione B: Esecuzione Notebook
Se si possiede una copia locale del notebook (es. `Simulazione_Controllo_Digitale.ipynb`), è possibile aprirlo ed eseguirlo direttamente nell'editor Visual Studio Code.

1. Aprire la cartella del progetto in Visual Studio Code.
2. Fare doppio clic sul file `Simulazione_Controllo_Digitale.ipynb` dal pannello laterale.
3. Assicurarsi di aver selezionato il kernel Python corretto in alto a destra (lo stesso ambiente dove sono state installate le dipendenze).
4. Premere il tasto "Esegui tutto" (o "Run All") nella barra superiore del notebook per eseguire tutte le celle in sequenza e visualizzare i grafici interattivi.