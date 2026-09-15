class User:
    def __init__(self, name:str):
        self._name = name

    def skip_ads(self):
        return False

class PremiumUser(User):
    def  __init__(self, name:str):
        User.__init__(self, name)

    def skip_ads(self):
        return True


user = User('Arthur')
premium_user = PremiumUser('Arthur')

print(user.skip_ads())
print(premium_user.skip_ads())