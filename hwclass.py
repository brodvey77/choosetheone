class BlogPost:
    def __init__(self,user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

    def change_number_of_likes(self, number_of_dislakes):
        self.number_of_likes = number_of_dislakes

post_about_history = BlogPost('Pistrushka', 'world war', 125)
post_about_humor = BlogPost('Brodvey77', 'cumedy club', 259)

print(post_about_history.number_of_likes)
print(post_about_humor.number_of_likes)
post_about_history.change_number_of_likes(1520)
print(post_about_history.number_of_likes)
post_about_humor.number_of_likes = 2000
print(post_about_humor.number_of_likes)



