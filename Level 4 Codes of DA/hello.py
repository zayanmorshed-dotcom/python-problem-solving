class Book:
    title = ""
    author = ""
    price = ""
    def set_book_info(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

book1 = Book()
book1.set_book_info("1984", "Mr. X", 250)
book1.display_info()

