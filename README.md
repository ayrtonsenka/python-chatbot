# LangChain ReAct Agent

Ovo je interaktivni AI asistent (chatbot) za terminal, napisan u Python-u. Koristi LangChain i LangGraph biblioteke kako bi kreirao agenta sposobnog da koristi eksterne alate za precizno odgovaranje na korisnička pitanja.

## Funkcionalnosti

**Interaktivni chat**
Razgovor sa AI botom odvija se direktno iz komandne linije. Petlja traje sve dok korisnik ne unese komandu `q` za izlaz.

**Korišćenje alata (Tool Calling)**
Agent ima pristup prilagođenom kalkulatoru. Ako mu postaviš matematički zadatak, samostalno prepoznaje da treba da pozove alat umesto da nagađa rezultat.

**LangGraph arhitektura**
Aplikacija koristi `create_react_agent` za stabilno izvršavanje logičkih koraka, prateći tok: razmišljanje, akcija, pa odgovor.

## Korišćene tehnologije

Projekat je razvijen u **Python** programskom jeziku. 
Od radnih okvira implementirani su **LangChain** i **LangGraph**. 
Za generisanje odgovora koristi se **OpenAI API** (ChatOpenAI model). 
Lokalno okruženje se oslanja na **python-dotenv** za bezbedno upravljanje API ključevima.

## Instalacija i pokretanje

Za lokalno pokretanje projekta, potrebno je ispratiti sledeće korake.

1. Kloniraj repozitorijum:
```bash
git clone [https://github.com/TvojUsername/ime-repozitorijuma.git](https://github.com/TvojUsername/ime-repozitorijuma.git)
cd ime-repozitorijuma
