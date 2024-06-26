import sqlite3

def connect_to_database(db_path):
    
    connection = sqlite3.connect(db_path)
    print("Datenbank-Verbindung hergestellt.")
    return connection
    

# CREATE
def add_tables_to_database(connection):
    
    cursor = connection.cursor()

    table_definitions = {
        'Kategorie': """
            CREATE TABLE IF NOT EXISTS Kategorie (
                KategorieID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name STRING NOT NULL
            );
        """,
        'Hersteller': """
            CREATE TABLE IF NOT EXISTS Hersteller (
                HerstellerID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name STRING NOT NULL
            );
        """,
        'Produkt': """
            CREATE TABLE IF NOT EXISTS Produkt (
                ProduktID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name STRING NOT NULL,
                Preis INT NOT NULL,
                KategorieID INTEGER,
                HerstellerID INTEGER,
                FOREIGN KEY (KategorieID) REFERENCES Kategorie(KategorieID),
                FOREIGN KEY (HerstellerID) REFERENCES Hersteller(HerstellerID)
            );
        """
    }
    
    for table_name, create_table_sql in table_definitions.items():
        try:
            cursor.execute(create_table_sql)
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table '{table_name}': {e}")
    
    connection.commit()


# INSERT
def insert_data(connection):
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO Kategorie (Name) VALUES ('Handys');")
    cursor.execute(f"INSERT INTO Hersteller (Name) VALUES ('Apple');")
    cursor.execute(f"INSERT INTO Hersteller (Name) VALUES ('Samsung');")

    cursor.execute(f"INSERT INTO Produkt (Name, Preis, KategorieID, HerstellerID) VALUES ('Iphone 69', 420, 1, 1)")
    cursor.execute(f"INSERT INTO Produkt (Name, Preis, KategorieID, HerstellerID) VALUES ('S420', 999, 1, 2)")
    connection.commit()

# SELECT
def select_data(connection):
    cursor = connection.cursor()

    cursor.execute(f"SELECT Preis, Name FROM Produkt WHERE ProduktID = 1;")
    result = cursor.fetchone()
    print(result)


# UPDATE
def update_data(connection):
    cursor = connection.cursor()

    cursor.execute(f"UPDATE Produkt SET Preis = 42069 WHERE ProduktID = 1;")
    connection.commit()


# DELETE
def delete_data(connection):
    cursor = connection.cursor()

    cursor.execute(f"DELETE from Produkt WHERE ProduktID = 2")
    connection.commit()


def main():
    db_path = r'C:\DB\OSDB.db'
    
    connection = connect_to_database(db_path)
    
    if connection:

        # Abgragen
        add_tables_to_database(connection)
        insert_data(connection)
        select_data(connection)
        update_data(connection)
        delete_data(connection)
        
        connection.close()
        print("Datenbank-Verbindung geschlossen.")


if __name__ == '__main__':
    main()
