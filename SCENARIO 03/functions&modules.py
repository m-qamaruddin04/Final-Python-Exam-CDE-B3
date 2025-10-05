import math

# -------------------------------
# 📘 Inventory Management Section
# -------------------------------

inventory = []  # List of dictionaries to store book info
borrowed_books = {}  # { 'Book Title': days_borrowed }

def add_book(title, author):
    book = {'title': title, 'author': author, 'available': True}
    inventory.append(book)
    print(f"✅ Book added: {title} by {author}")

def remove_book(title):
    global inventory
    inventory = [book for book in inventory if book['title'].lower() != title.lower()]
    print(f"❌ Book removed: {title}")

def display_inventory():
    print("\n📚 Current Inventory:")
    if not inventory:
        print("No books available.")
    else:
        for book in inventory:
            status = "Available" if book['available'] else "Borrowed"
            print(f" - {book['title']} by {book['author']} ({status})")

# ---------------------------------------
# 📘 Borrowing, Returning, and Fine Logic
# ---------------------------------------

def borrow_book(title):
    for book in inventory:
        if book['title'].lower() == title.lower() and book['available']:
            book['available'] = False
            borrowed_books[title] = 0  # start tracking days borrowed
            print(f"📖 '{title}' has been borrowed.")
            return
    print(f"⚠️ '{title}' is not available for borrowing.")

def return_book(title, days_late=0):
    for book in inventory:
        if book['title'].lower() == title.lower() and not book['available']:
            book['available'] = True
            borrowed_books.pop(title, None)
            if days_late > 0:
                fine = calculate_fine(days_late)
                print(f"💰 '{title}' returned {days_late} days late. Fine: Rs {fine}")
            else:
                print(f"✅ '{title}' returned on time.")
            return
    print(f"⚠️ '{title}' was not borrowed or does not exist.")

def calculate_fine(days_late):
    """Calculate fine using math module."""
    return round(2 * math.sqrt(days_late), 2)  # fine formula


# ---------------------------------------
# 📘 Main Demonstration Section
# ---------------------------------------

def main():
    # Add books to inventory
    add_book("Python Programming", "John Doe")
    add_book("Data Structures", "Jane Smith")
    add_book("Machine Learning", "Andrew Ng")

    display_inventory()

    # Borrow and return books
    borrow_book("Python Programming")
    borrow_book("Data Structures")
    display_inventory()

    # Return one book late
    return_book("Python Programming", days_late=9)
    display_inventory()

    # 🔍 Lambda: filter overdue books (simulate)
    borrowed_books_with_days = {
        "Data Structures": 5,
        "Machine Learning": 12,
        "Python Programming": 2
    }
    overdue_books = list(filter(lambda item: item[1] > 7, borrowed_books_with_days.items()))
    print("\n📅 Overdue Books (using lambda):")
    for title, days in overdue_books:
        print(f" - {title}: {days} days overdue")

    # 🧾 List Comprehension: borrowed book report
    borrowed_report = [f"{title} ({days} days borrowed)" for title, days in borrowed_books_with_days.items()]
    print("\n📋 Borrowed Books Report (using list comprehension):")
    for entry in borrowed_report:
        print(" -", entry)

    # Remove a book
    remove_book("Machine Learning")
    display_inventory()


# Run program
if __name__ == "__main__":
    main()
