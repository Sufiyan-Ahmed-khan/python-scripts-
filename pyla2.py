# Function to read inventory data from file
def read_inventory(file_name):
    inventory = []
    with open(file_name, 'r') as file:
        book_info = {}
        for line in file:
            if line.strip():
                key, value = line.strip().split(': ')
                book_info[key] = value
            else:
                inventory.append(book_info)
                book_info = {}
    return inventory

# Function to filter books by price
def filter_books_by_price(books_list, max_price):
    return list(filter(lambda book: int(book['Price']) <= max_price, books_list))

# Function to calculate total quantity of books
def calculate_total_quantity(books_list):
    return sum(map(lambda book: int(book['Quantity']), books_list))

# Function for searching a book by title (using recursion)
def search_book_by_title(title, books_list):
    if not books_list:
        return None
    else:
        current_book = books_list[0]
        if current_book['Title'] == title:
            return current_book
        else:
            return search_book_by_title(title, books_list[1:])

# Main program
file_name = "books_inventory.txt"
inventory_data = read_inventory(file_name)
print("Inventory Data:", inventory_data)

# Filter books priced $30 or less
filtered_books = filter_books_by_price(inventory_data, 30)
print("Books priced $30 or less:", filtered_books)

# Calculate total quantity of books
total_quantity = calculate_total_quantity(inventory_data)
print("Total Quantity of Books:", total_quantity)

# Search for a book by title
searched_book_title = "Python Crash Course"
searched_book = search_book_by_title(searched_book_title, inventory_data)
if searched_book:
    print(f"Book '{searched_book_title}' Found:", searched_book)
else:
    print(f"Book '{searched_book_title}' not found.")
