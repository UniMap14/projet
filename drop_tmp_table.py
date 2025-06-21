import sqlite3

# Remplace par le chemin exact de ta base SQLite
db_path = 'path/to/your/database.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS _alembic_tmp_users;")
    print("Table _alembic_tmp_users supprimée (si elle existait).")
except Exception as e:
    print("Erreur :", e)
finally:
    conn.commit()
    conn.close()
