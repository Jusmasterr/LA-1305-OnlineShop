# LA-1305

### Beschreibung

Justus Meister & Fabian Meyer

Im Moment behandeln wir das Modul 165, das sich mit NoSql befasst. Aus diesem Grund haben wir uns entschieden, eine Datenbank für einen Onlineshop zu erstellen. Dabei möchten wir unsere Kenntnisse in Python vertiefen, indem wir ein Programm schreiben, das CREATE-, SELECT-, INSERT-, DELETE- und UPDATE-Befehle ausführen kann. Obwohl wir ursprünglich NoSql verwenden sollten, setzen wir stattdessen Sqlite3 ein.

### User Stories

| US-№ | Verbindlichkeit | Typ        | Beschreibung                                                                                                                                                  |
| ---- | --------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Muss            | Funktional | Als User möchte ich, dass die Tabellen automatisch erstellt werden, um Zeit zu sparen.                                                                       |
| 2    | Muss            | Funktional | Als User möchte ich selbst einen Hersteller, eine Kategorie oder ein Produkt zur Datenbank hinzufügen können.                                                  |
| 3    | Muss            | Funktional | Als User möchte ich, dass Hersteller, Kategorien und Produkte automatisch eingefügt werden.                                                                  |
| 4    | Muss            | Funktional | Als User möchte ich einen Datensatz löschen können.                                                                                                           |
| 5    | Muss            | Funktional | Als User möchte ich einen Datensatz aktualisieren können.                                                                                                      |


### Testfälle

| TC-№ | Ausgangslage                                 | Eingabe                                          | Erwartete Ausgabe                               |
| ---- | -------------------------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| 1.1  | Automatisches Erstellen von Tabellen           | -                                                | Tabellen werden automatisch erstellt.            |
| 2.1  | Hinzufügen eines Herstellers, einer Kategorie oder eines Produkts | -                                              | Der Hersteller, die Kategorie oder das Produkt wird zur Datenbank hinzugefügt. |
| 3.1  | Automatisches Einfügen von Herstellern, Kategorien und Produkten | -                                              | Hersteller, Kategorien und Produkte werden automatisch in die Datenbank eingefügt. |
| 4.1  | Löschen eines Datensatzes                      | -                                                | Der ausgewählte Datensatz wird erfolgreich gelöscht. |
| 5.1  | Aktualisieren eines Datensatzes                | -                                                | Der ausgewählte Datensatz wird erfolgreich aktualisiert. |



### Planen

| US-№ | Datum      | Arbeitspaket                            | Verantwortliche Person  |
| ---- | ---------- | --------------------------------------- | ----------------------- |
| -    | 21.6.24    | Projekt Idee wählen                     | Fabian Meyer, Justus Meister |
| -    | 21.6.24    | Userstories, Testfälle und Planung erstellen | Fabian Meyer            |
| 1    | Datum      | Grundlegene Funktionen implementieren     | Fabian Meyer, Justus Meister |
| 2    | Datum      | Implementierung spezifischer Funktionen   | Justus Meister          |
| 3    | Datum      | Integration von Daten aus dem Dateisystem | Fabian Meyer           |
| 4    | Datum      | Einleitung über das Datenbankprojekt     | Elias Spycher           |
| 5    | Datum      | Datenbankoperationen optimieren          | Fabian Meyer            |
| 6    | Datum      | Automatisierung bestimmter Prozesse      | Fabian Meyer            |
| 7    | Datum      | Testen und Testprotokoll ausfüllen       | Fabian Meyer            |
| 8    | Datum      | Dokumentation und Bericht erstellen      | Fabian Meyer, Justus Meister |

### Testprotokoll

| TC-№ | Datum   | Resultat | Tester         |
| ---- | ------- | -------- | -------------- |
| 1.1  | 21.6.24 | OK       | Justus Meister |
| 2.1  | 21.6.24 | OK       | Justus Meister |
| 3.1  | 21.6.24 | OK       | Justus Meister |
| 4.1  | 21.6.24 | OK       | Justus Meister |
| 5.1  | 21.6.24 | OK       | Justus Meister |

### Testfälle

