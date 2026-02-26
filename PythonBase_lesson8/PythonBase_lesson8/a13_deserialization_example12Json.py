import json

#with open('data/example12.json') as data:
#    users = json.load(data)

#print(users)


class User(object):
    def __init__(self, name, email):
        self.username = name
        self.email = email

    def to_json(self):
        return {'username': self.username, 'email': self.email}

    @classmethod
    def from_json(cls, js_object):
        return cls(js_object['username'], js_object['email'])

    def __repr__(self):
        return 'User({!r}, {!r})'.format(self.username, self.email)

with open('data/example12.json') as data:
    users = json.load(data, object_hook=User.from_json)

print(users)