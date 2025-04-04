# Generative AI - Projektbeskrivelser
Dette repository indeholder en _standard case_ for generative AI. Du finder data der er relevant til at løse opgaven, behovs- og procesbeskrivelse samt en Python applikation som du kan bygge din løsning ind i. 

# Baggrund
Du er af ledelsen blevet bedt om at udvikle en generative AI løsning der kan understøtte projektlederne i din organisation. Det drejer sig særligt om projektbeskrivelser som er mangelfulde, eller som ikke lever op til din organisations krav til projektbeskrivelser. Kvaliteten afhænger meget af projektlederen selv og for nogle projektledere bruges der væsentligt tid på at formulere og udfylde projektbeskrivelser som bedre kunne bruges på at drive og lede projekter.

## Behovsafdækning
Igennem behovsafdækning er du, sammen med interessenterne på dette projekt, blevet enige om følgende formål:

>	_For at effektivisere projektbeskrivelsesprocessen skal løsningen bidrage projektlederne i at oprette nye projektbeskrivelser, baseret på deres notater, skitser og andre relevante dokumenter._

Ydermere har I arbejdet sammen på at lave en template over hvilke overskrifter der skal inkluderes i en projektbeskrivelse. I har defineret følgende overskrifter:

1. Projektbeskrivelse
2. Tidsplan
3. Budget
4. Risici
5. Milepæle

## Data
I samarbejde med projektlederne i din organisation har du fået udleveret følgende data:
- `data/noter_og_dokumenter`: Denne mappe indeholder noter, dokumenter og billeder der kan være relevante for opgaven.
- `data/eksempler`: Indeholder færdige og godkendte projektbeskrivelser fra tidligere projekter.
- `data/skabelon`: Denne mappe indeholder en skabelon for projektbeskrivelserne.

# Basisapplikation
Udover projektbeskrivelsen er der også lavet en basisapplikation som du kan bruge til at løse casen med. Den finder du under `app` hvor der både ligger en datamodel for projektstrukturen som du kan benytte, samt en simpel frontend applikation. 

## Lokal udvikling
1. Download en kopi, eller opret en fork af repository
2. Installer [`uv`](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2) (**Der anbefales at standalone installeren downloades**)
3. Åben mappen med projektet og kør: `uv sync`
4. Der skulle nu oprettes en lokal .venv mappe som indeholder et Python miljø med de rigtige dependencies.
5. For at starte applikationen kan du køre: `uv run uvicorn app.main:app --port 8000 --reload`
