

class BooksLibrery:
    def __init__(self, name_b, author_b, year_b, publisher_b, review_b):
        self.name_b = name_b
        self.author_b = author_b
        self.year_b = year_b
        self.publisher_b = publisher_b
        self.review_b = review_b

    def give_b(self):
        return self.name_b, self.author_b, self.year_b, self.publisher_b

    def __str__(self):
        return ("Name book        : {:s},\n" 
        "Author book      : {:s},\n"
        "Year book        : {},\n"
        "Publisher book   : {},\n"
        "Review           :\n {}".format(self.name_b, self.author_b, self.year_b, self.publisher_b, self.review_b) )

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

    
review = ['To Kill a Mocking bird is an intriguing book about justice and judging.\n'
'It is set in a small town in America. A young girl named Scout is playing in her\n'
'front garden with her older brother, Jem, when she meets a young boy called Dill,\n'
'who they befriend.',

'Parents need to know that THE GREAT GATSBY is at once a romantic and cynical novel\n'
":about the wealth and habits of a group of New Yorkers during the Jazz Age. Fitzgerald's\n"
'writing is unassailably magnificent, as he paints a grim portrait of shallow characters who\n'
'maneuver themselves into complex situations. This classic American novel is required reading\n'
'for a lot of high school students, and it can definitely be appreciated and understood on \n'
'some levels by teenagers.',

"When Adela Quested and her elderly companion Mrs Moore arrive in the Indian town of \n"
"Chandrapore, they quickly feel trapped by its insular and prejudiced 'Anglo-Indian' community.\n"
"Determined to escape the parochial English enclave and explore the 'real India', they seek the\n"
"guidance of the charming and mercurial Dr Aziz, a cultivated Indian Muslim.",

"I really liked the writing in The Invisible Man, but I thought the storytelling was awful. \n"
"H. G. Wells has a way with words and I really enjoyed his turn of phrase.  Phrases like ",

'To Kill a Mocking bird is an intriguing book about justice and judging.\n'
'It is set in a small town in America. A young girl named Scout is playing in her\n'
'front garden with her older brother, Jem, when she meets a young boy called Dill,\n'
'who they befriend.'  ]

book1 = BooksLibrery('To Kill a Mockingbird', 'Harper Lee', '1960', 'Lippincott & Co', review[0])
book2 = BooksLibrery('The Great Gatsby', 'Scott Fitzgerald', '1925', 'Lippincott & Co', review[1])
book3 = BooksLibrery('A Passage to India', 'E. M. Forster', '1924', 'Edward Arnold', review[2])
book4 = BooksLibrery('Invisible Man', 'Ralph Ellison', '1952', 'Random House', review[3])
book5 = BooksLibrery('To Kill a Mockingbird', 'Harper Lee', '1960', 'Lippincott & Co', review[4])

# print format: 'str' and 'repr'
# -----------------------------
##print(book1.give_b())
print("'str - format'")
print(book1)
print()

#print("'repr - format'")
#print(repr(book1))
#print()
# -----------------------------



# check: '==' and '!='
# -----------------------------
#b1 = book1
#b2 = book3
#print(b1 != b2)
#print(b1 == b2)

