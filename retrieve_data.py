from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # SQL query
        query = """SELECT b.id, b.title, a.name, b.genre, b.price
        FROM Books b, Authors a
        WHERE b.author_id = a.id"""

        # Executing the query
        cursor.execute(query)

        # Fethching and displaying the results
        for book in cursor.fetchall():
            print(book)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()