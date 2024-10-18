from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try: 
        cursor = conn.cursor()

        # Updating book details
        new_price = 25.00
        new_genre = "Adventure"
        book_id = 5 # Example book ID

        # SQL query
        query = "UPDATE Books SET price = %s, genre = %s WHERE id = %s"

        # Executing the query
        cursor.execute(query, (new_price, new_genre, book_id))
        conn.commit()
        print("Book details updated successfully.")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()