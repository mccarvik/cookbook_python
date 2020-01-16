from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)
# Users dont have a natural comparison functiio
# print(sorted(users))
# can pass it callable function
print(sorted(users, key=lambda u: u.user_id))

# Can use attrgetter function instead
print(sorted(users, key=attrgetter('user_id')))

# Can use with max and min as well
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
