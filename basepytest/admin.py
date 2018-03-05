"""用户的子类"""

from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = ["can add post", 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)