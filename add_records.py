from connect_mysql import connect_database


def add_author(name, birth_year, nationality):
    query = "INSERT INTO Authors (name, birth_year, nationality) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, birth_year, nationality))

def add_book(title, genre, price, publication_date, author_id):
    query = "INSERT INTO Books (title, genre, price, publication_date, author_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (title, genre, price, publication_date, author_id))

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Add author
        add_author("J.K. Rowling", 1965, "British")

        # Add book
        add_book("Harry Potter and the Philosopher's Stone", "Fantasy", 20.00, "1997-06-26", cursor.lastrowid)

        conn.commit()
        print("Author and book added successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()              
