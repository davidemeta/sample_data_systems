# Sistema a dati campionati
Repository per l'implementazione in Python di sistemi di dati campionati per tesi su "Controlli Automatici".

Questo progetto analizza la trasformazione di sistemi a tempo continuo nel dominio discreto utilizzando un mantenitore di ordine zero. L'obiettivo è studiare il comportamento della risposta al gradino al variare dei parametri del sistema, con particolare attenzione alla stabilità e ai fenomeni di fase non minima (undershoot) introdotti dagli zeri nel semipiano destro.

## 1) File
Il repository è organizzato come segue:

* **`main.py`**: Script Python principale. Contiene l'implementazione delle funzioni di trasferimento discrete $P_d(z)$ derivate dai modelli continui $P(s)$. Esegue la simulazione temporale della risposta al gradino per i tre casi di studio e genera i grafici comparativi.
* **`requirements.txt`**: Elenco delle dipendenze necessarie per replicare l'ambiente di sviluppo e garantire la corretta esecuzione del codice.
* **`discrete_systems_analysis.png`**: Immagine di output generata dallo script, che mostra visivamente il confronto tra le risposte dei sistemi.

## 2) Prima dell'esecuzione
Per garantire il corretto funzionamento del codice, è necessario installare le seguenti librerie Python:

* **Numpy**: Utilizzata per operazioni vettoriali, gestione degli array temporali e calcolo dei termini esponenziali ($e^{-aT}$) nelle formule di discretizzazione.
* **Scipy**: Fondamentale per il modulo `signal`, utilizzato per definire le funzioni di trasferimento discrete (`dstep`) e simularne la risposta nel tempo.
* **Matplotlib**: Utilizzata per la visualizzazione dei risultati tramite grafici a scalini (step plot).

Tutte le dipendenze possono essere installate tramite **pip** eseguendo il seguente comando nel terminale:

```bash
pip install numpy scipy matplotlib
```

## 3) Istruzioni di Esecuzione

Una volta installate le librerie descritte sopra, il progetto è pronto per essere eseguito.

**Esecuzione Main**:
Aprire il terminale nella cartella del progetto (assicurandosi che il `venv` sia attivo) ed eseguire il file principale digitando:

```bash
python3 main.py
```
