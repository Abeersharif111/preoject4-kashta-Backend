# data/user_data.py

from models.user import UserModel

def create_test_users():
    user1 = UserModel(username="Abeer",role="admin")
    user1.set_password("111")
    user2 = UserModel(username="AAA",role="customer")
    user2.set_password("securepassword2")
    user3 = UserModel(username="BBB",role="customer")
    user3.set_password("securepassword3")
    user4 = UserModel(username="lucas_silva",role="customer")
    user4.set_password("securepassword4")
   

    return [user1, user2, user3, user4]

user_list = create_test_users()