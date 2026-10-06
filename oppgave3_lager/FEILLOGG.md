+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Symptom                                              | Hvordan fant jeg den                 | Årsak                                | Rettelse                             |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| line 150, in main                                    | Kjørte koden for å se etter          | Feilen er at pc-en som er definert  | Måten eg rettet det på var å fikse  |
| print("Fant:", funnet[1])                            | feilmelding, fikk opp den            | i funnet variabelen med finn_utstyr | utstyrs_id                           |
|                    ~~~~~~^^^                         |                                      | funksjonen ikke er i lista lager    | I finn_utstyr funksjonen, løsningen |
| TypeError: 'NoneType' object is not subscriptable    |                                      |                                      | var å fikse slik at den hentet      |
|                                                      |                                      |                                      | verdiene ifra lager listen.          |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Feil utstyrs pris når den printes ut                 | Når jeg så på utskriften når jeg    | Feil er at i lista PRISLISTE er     | Løsningen er å gjøre strengen om    |
|                                                      | kjørte koden leste jeg gjennom og  | prisen satt som streng og ikke som  | til tall                              |
|                                                      | sammelignet med det som sto i      | int                                  |                                      |
|                                                      | koden og ser at det ikke stemmer   |                                      |                                      |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Feil med purrestatus                                 | Leste printen for purrestatus og   | Årsaken var feil rekkefølge i       | Løsningen var da å rette opp i       |
|                                                      | ser at det er feil for dager over  | logikken var satt feil. Første      | strukturen og flytte skjekken       |
|                                                      | 30                                   | kjekk var om det hadde godt mer en  | mellom 7 dager og 30 dager, slik at |
|                                                      |                                      | 7 dager skulle vi returnere         | 30 dager er første skjekk            |
|                                                      |                                      | purring. Men hvis jeg startet med  |                                      |
|                                                      |                                      | å skjekke om det hadde godt mer en  |                                      |
|                                                      |                                      | 30 dager så fungerte logikken      |                                      |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Manger utskrift av utlånt utsyr til Robin            | Ser ikke Robin i terminalen under   | Årsaken var at vi tok vekk 1 i for | Løsningen er å fjerne Fratrekke når |
|                                                      | lagerlista som blir krevet ut        | løkka. Når vi da henter ut lager    | loopen skal kjøre, da blir alle med |
|                                                      |                                      | lista blir ikke Robin med          |                                      |
|                                                      |                                      |                                    |                                      |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Feil ved utskrift av aktiverte lån. Det skal kunn    | Leste igjen priten i terminalen     | Åsaken kan være funksjonen som      | Jeg har ingen løsning på dette      |
| bli skrevet ut de som er aktive, men TAST-100 blir   | samtidig som jeg gikk gjennom       | skriver henter datan eller idet     | enda                                 |
| krevet ut og den er ikke utlånt til noen             | koden, da så jeg at TAST-100 som    | den blir printet ut i terminalen    |                                      |
|                                                      | ikke er utlånt blir skrevet ut.     |                                      |                                      |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Feil med utskrift av Snitt dager utlånt              | Syntes snittet var litt lavt o      | Her er feilen i kalkuleringen og    | Har ingen løsning enda               |
|                                                      | skjekket med å regne ut selv å fant | beregningen av snittet              |                                      |
|                                                      | ut at utregningen blir feil i       |                                      |                                      |
|                                                      | koden                                |                                      |                                      |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+

 

 