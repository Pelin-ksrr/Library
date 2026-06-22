import sqlite3

def create_tables():
    conn=sqlite3.connect("library.db")
    cursor=conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL,
                   is_available INTEGER DEFAULT 1,
                   borrowed_by_member_id INTEGER DEFAULT NULL)""")
                    

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS members(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   member_type TEXT NOT NULL)""")
    
    conn.commit()
    conn.close()

if __name__=="__main__":
    create_tables()
    print("Tables created successfully!")