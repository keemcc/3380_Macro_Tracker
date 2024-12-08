from prettytable import PrettyTable

def visualizeData(cursor):
    tables = ['USER_T', 'BRAND', 'FOOD', 'SERVING', 'LOG', 'FITNESS_GOAL']
    
    for table_name in tables:
        print(f"\nData in {table_name} table:")
        
        cursor.execute(f"SELECT * FROM {table_name};")
        
        table = PrettyTable()
        
        columns = [desc[0] for desc in cursor.description]
        table.field_names = columns
        
        rows = cursor.fetchall()
        for row in rows:
            table.add_row(row)
        
        print(table)

def visualizeStructure(cursor):
    cursor.execute("SHOW TABLES;")
    tables = [table[0] for table in cursor.fetchall()]

    if not tables:
        print("No tables found in the schema.")
        return

    for table_name in tables:
        cursor.execute(f"DESCRIBE {table_name};")
        print(f"\nStructure of {table_name} table:")
        
        table = PrettyTable(["Field", "Type", "Null", "Key", "Default", "Extra"])
        for row in cursor.fetchall():
            table.add_row(row)
        
        print(table)