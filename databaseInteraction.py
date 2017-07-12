import sqlite3
db = sqlite3.connect('database.db')

stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
]

c = db.cursor()
c.execute('create table portfolio1 (symbol text, shares integer, price real)')
db.commit()

c.executemany('insert into portfolio1 values (?,?,?)', stocks)

db.commit()

for row in db.execute('select * from portfolio1'):
    print(row)
