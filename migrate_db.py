import sqlite3
import os

db_path = 'instance/maasadguru.db'

if not os.path.exists(db_path):
    print(f"Database not found at {db_path}. No migration needed.")
    exit()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Check if 'type' column already exists in 'photo' table
    cursor.execute("PRAGMA table_info(photo)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'type' not in columns:
        print("Adding 'type' column to 'photo' table...")
        cursor.execute("ALTER TABLE photo ADD COLUMN type VARCHAR(20) DEFAULT 'image'")
        conn.commit()
        print("Migration successful.")
    else:
        print("Column 'type' already exists in 'photo' table.")
except Exception as e:
    print(f"Migration failed: {e}")
finally:
    conn.close()
