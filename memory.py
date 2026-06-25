import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    query TEXT,
    response TEXT
)
""")

conn.commit()


def save_memory(customer_name, query, response):
    cursor.execute(
        "INSERT INTO memory(customer_name, query, response) VALUES(?,?,?)",
        (customer_name, query, response)
    )
    conn.commit()


def get_memory(customer_name):
    cursor.execute(
        "SELECT query, response FROM memory WHERE customer_name=? ORDER BY id DESC LIMIT 3",
        (customer_name,)
    )

    rows = cursor.fetchall()

    if not rows:
        return "No previous conversation."

    text = ""

    for q, r in rows:
        text += f"Query: {q}\nResponse: {r}\n\n"

    return text