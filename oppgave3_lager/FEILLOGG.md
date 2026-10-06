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
|                                                      | kjørte koden leste jeg gjennom og  | prisen satt som streng og ikke som   | til tall                              |
|                                                      | sammelignet med det som sto i      | int                                  |                                      |
|                                                      | koden og ser at det ikke stemmer   |                                      |                                      |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Feil med purrestatus                                 |                                      |                                      |                                      |
+------------------------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+