import sqlite3

conn = sqlite3.connect("data/conocimiento.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conocimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modulo TEXT,
    titulo TEXT,
    descripcion TEXT,
    codigo TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Base de datos creada correctamente")