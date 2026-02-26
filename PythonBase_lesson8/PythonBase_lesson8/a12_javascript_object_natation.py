
import json

users = [
      {
          'username':'john',
          'email':'john@hotmail.com'
          },
          {
          'username':'linda',
          'email':'linda@hotmail.com'
          },
          {
          'username':'mario',
          'email':'mario@hotmail.com'
          },
   
        ]

#print(users)

#with open('data/example12.json', 'w') as file:
#    json.dump(users, file, indent=2)

class User(object):
    def __init__(self, name, email):
        self.username = name
        self.email = email

    def to_json(self):
        return {'username': self.username, 'email': self.email}

users = [User('john', 'jsad@gmail.com'), User('mario', 'mar@mar@gmail.com')]

with open('data/example12.json', 'w') as file:
    json.dump(users, file, indent=2, default=User.to_json)