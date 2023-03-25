class Book:
    pub_price=0
    def __init__(self, title, author, year, price):
        # public attributes
        self.title =  title
        self.author = author
        self.year = year
        # private attribute
        self.__price = price

    def __repr__(self):
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}"
      
    def priv_var(self):
      pub_price = self.__price
      return pub_price
      

# instantiating a new object
book1 = Book("Teller of secrets", "Bisi Adjapon", 2021, 5000)
book2 = Book("Stay with me", "Ayobami Adebayo", 2017, 4000)

print(book2.title)                    # Stay with me
print(book2.author)                   # Ayobami Adebayo
print(book2.year)
print(book2)                          # salida --> Book: Stay with me, Author: Ayobami Adebayo, Year: 2017
print(book2.priv_var())               # 4000  
#print(book2.__price)                 # Err var is attribute privated
