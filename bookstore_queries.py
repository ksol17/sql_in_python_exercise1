from connect_mysql import connect_database

def list_distinct_genres(cursor):
    query = "SELECT DISTINCT genre FROM Books"
    cursor.execute(query)
    print("Distinct Genres:")
    for genre in cursor.fetchall():
        print(genre[0])


def find_books_with_similar_titles(cursor, keyword):
    query = "SELECT id, title, genre, publication_date, price FROM Books WHERE title LIKE %s"
    cursor.execute(query, ('%' + keyword + '%',))
    print("Books with similar titles:")
    for book in cursor.fetchall():
        print(book)

def select_books_by_authors(cursor, authors):
    # Prepare a string with placeholders for the authors tuple
    placeholders = ', '.join(['%s'] * len(authors))
    print(placeholders)
    query = f"""
    SELECT B.id, B.title, B.genre, B.publication_date, B.price, A.name AS AuthorName
    FROM Books B, Authors A
    WHERE B.author_id = A.id AND A.name IN ({placeholders})
    """
    cursor.execute(query, authors)
    print("Books by specific authors:")
    for book in cursor.fetchall():
        print(book)

def books_published_in_period(cursor, start_date, end_date):
    query = "SELECT id, title, genre, publication_date, price FROM Books WHERE publication_date BETWEEN %s AND %s"
    cursor.execute(query, (start_date, end_date))
    print(f"Books published between {start_date} and {end_date}:")
    for book in cursor.fetchall():
        print(book)


def main():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            print("1: List Distinct Genres")
            print("2: Find Books with Similar Titles")
            print("3: Select Books by Specific Authors")
            print("4: Books Published in a Specific Period")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                list_distinct_genres(cursor)
            elif choice == '2':
                keyword = input("enter a keyword for the title: ")
                find_books_with_similar_titles(cursor, keyword)
            elif choice == '3':
                authors = tuple(input("Enter author names separated by comma: ").split(", "))
                select_books_by_authors(cursor, keyword)
            elif choice == '4':
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                books_published_in_period(cursor, start_date, end_date)
            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")

        finally: 
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()