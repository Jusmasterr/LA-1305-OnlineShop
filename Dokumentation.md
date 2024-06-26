# LA-1305

### Beschreibung

Justus Meister & Fabian Meyer

Im Moment behandeln wir das Modul 165, das sich mit NoSql befasst. Aus diesem Grund haben wir uns entschieden, eine Datenbank für einen Onlineshop zu erstellen. Dabei möchten wir unsere Kenntnisse in Python vertiefen, indem wir ein Programm schreiben, das CREATE-, SELECT-, INSERT-, DELETE- und UPDATE-Befehle ausführen kann. Obwohl wir ursprünglich NoSql verwenden sollten, setzen wir stattdessen Sqlite3 ein.

### User Stories

| US-№ | Verbindlichkeit | Typ        | Beschreibung                                                                                                                                                  |
| ---- | --------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Muss            | Funktional | Als User möchte ich, dass die Tabellen automatisch erstellt werden, um Zeit zu sparen.                                                                       |
| 2    | Muss            | Funktional | Als User möchte ich, dass Hersteller, Kategorien und Produkte automatisch eingefügt werden.                                                                  |
| 3    | Muss            | Funktional | Als User möchte ich dass ein Datensatz gelöscht wird.                                                                                                           |
| 4    | Muss            | Funktional | Als User möchte ich dass ein Datensatz aktualisiert wird.                                                                                                        |


### Testfälle

| TC-№ | Ausgangslage                                 | Eingabe                                          | Erwartete Ausgabe                               |
| ---- | -------------------------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| 1.1  | Automatisches Erstellen von Tabellen           | -                                                | Tabellen werden automatisch erstellt.            |
| 2.1  | Automatisches Einfügen von Herstellern, Kategorien und Produkten | -                                              | Hersteller, Kategorien und Produkte werden automatisch in die Datenbank eingefügt. |
| 3.1  |  Automatisches Löschen eines Datensatzes                      | -                                                | Der ausgewählte Datensatz wird erfolgreich gelöscht. |
| 4.1  | Automatisches Aktualisieren eines Datensatzes                | -                                                | Der ausgewählte Datensatz wird erfolgreich aktualisiert. |



### Planen

| US-№ | Datum      | Arbeitspaket                            | Verantwortliche Person  |
| ---- | ---------- | --------------------------------------- | ----------------------- |
| 1    | 22.5.24    | Projekt Idee wählen                     | Fabian Meyer, Justus Meister |
| 2    | 22.5.24    | Userstories, Testfälle und Planung erstellen | Fabian Meyer            |
| 3    | 29.5.24      | Grundlegene Funktionen implementieren     | Fabian Meyer, Justus Meister |
| 4    | 29.5.24      | Implementierung spezifischer Funktionen   | Justus Meister          |
| 5    | 29.5.24      | Integration von Daten aus dem Dateisystem | Fabian Meyer           |
| 6    | 05.6.24      | Datenbankoperationen optimieren          | Fabian Meyer            |
| 7    | 05.6.24      | Automatisierung bestimmter Prozesse      | Fabian Meyer            |
| 8    | 05.6.24      | Testen und Testprotokoll ausfüllen       | Fabian Meyer            |
| 9    | 12.6.24      | Dokumentation fertigstellen      | Fabian Meyer, Justus Meister |

### Testprotokoll

| TC-№ | Datum   | Resultat | Tester         |
| ---- | ------- | -------- | -------------- |
| 1.1  | 05.6.24  | OK       | Justus Meister |
| 2.1  | 05.6.24  | OK       | Justus Meister |
| 3.1  | 05.6.24  | OK       | Justus Meister |
| 4.1  | 05.6.24  | OK       | Justus Meister |
| 5.1  | 05.6.24  | OK       | Justus Meister |


