
class BooksLibrery:
    def __init__(self, name_b, author_b, year_b, publisher_b):
        self.name_b = name_b
        self.author_b = author_b
        self.year_b = year_b
        self.publisher_b = publisher_b

    def give_b(self):
        return self.name_b, self.author_b, self.year_b, self.publisher_b

    def __str__(self):
        return ("Name book        : {:s},\n" 
        "Author book      : {:s},\n"
        "Year book        : {},\n"
        "Publisher book   : {}".format(self.name_b, self.author_b, self.year_b, self.publisher_b) )

        #print(" Name book        : {}\n".format(self.name_b),
        #      "Author book      : {}\n".format(self.author_b),
        #      "Year book        : {}\n".format(self.year_b),
        #      "Publisher book   : {}\n".format(self.publisher_b) )

    def __repr__(self):
        return ("Book:\n {:s},\n {:s},\n {:s},\n {:s} ".format(self.name_b, self.author_b, self.year_b, self.publisher_b))
       
    def __eq__(self, other):
        return ("This is equals:->  {}".format(self.name_b == other.name_b and
                                            self.author_b == other.author_b and
                                           self.year_b == other.year_b and
                                          self.publisher_b == other.publisher_b) )

    def __ne__(self, other):
        return ('This is not equals ->  {}'.format(self.name_b != other.name_b and
                                            self.author_b != other.author_b and
                                           self.year_b != other.year_b and
                                          self.publisher_b != other.publisher_b) )

    

book1 = BooksLibrery('To Kill a Mockingbird', 'Harper Lee', '1960', 'Lippincott & Co')
book2 = BooksLibrery('The Great Gatsby', 'Scott Fitzgerald', '1925', 'Lippincott & Co')
book3 = BooksLibrery('A Passage to India', 'E. M. Forster', '1924', 'Edward Arnold')
book4 = BooksLibrery('Invisible Man', 'Ralph Ellison', '1952', 'Random House')
book5 = BooksLibrery('To Kill a Mockingbird', 'Harper Lee', '1960', 'Lippincott & Co')

# print format: 'str' and 'repr'
# -----------------------------
##print(book1.give_b())
#print("'str - format'")
#print(book1)
#print()

#print("'repr - format'")
#print(repr(book1))
#print()
# -----------------------------



# check: '==' and '!='
# -----------------------------
b1 = book1
b2 = book3
print(b1 != b2)

