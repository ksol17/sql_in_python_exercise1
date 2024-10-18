from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Book ID to be deleted
        book_id = 1 # Example of book ID

        # First, check if the book exists in the database
        check_query = "SELECT id from Books WHERE id = %s"
        cursor.execute(check_query, (book_id,))
        book = cursor.fetchone()

        if book:
            # If the book exists, proceed to delete
            delete_query = "DELETE FROM Books WHERE id = %s"
            cursor.execute(delete_query, (book_id,))
            conn.commit()
            print("Book deleted successfully.")
        else:
            # If the book doesn't exist, inform the user
            print(f"No book found with ID {book_id}.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()