import sqlite3

class Product:

    def __init__(self):
        self.con = sqlite3.connect("quotes.db")
        self.cur = self.con.cursor()
        self.create_table()
        
    def create_table(self):
        # self.cur.execute("""DROP TABLE products""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS quotes(
            id INT PRIMARY KEY,
            quote TEXT,
            )""")
       
      
