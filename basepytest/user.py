"""用户的类"""
class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        userdata = self.last_name + ' ' + self.first_name + ' Age: ' + str(self.age) + ' sex: ' + self.sex
        print(userdata.title())

    def greet_user(self):
        print("Hi,"+str(self.first_name)+',welcome!')

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0