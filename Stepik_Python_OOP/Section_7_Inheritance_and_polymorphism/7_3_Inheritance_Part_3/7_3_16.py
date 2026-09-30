
class TitledText(str):
    '''класс TitledText, наследник класса str, который описывает текст, имеющий заголовок'''
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance


    def title(self):
        return self.text_title



headlines = ['Как полностью изменить...', 'Где найти …', 'Быстрый способ...', 'Ошибки, которые приведут тебя к ...',
             'Как быстро...']
contents = ['Нужно всего лишь...', 'Обратитесь к нам, и мы всё расскажем', 'Для этого Вы должны', 'Не делай их',
            'Ну это вообще просто']

for heading, content in zip(headlines, contents):
    titledtext = TitledText(content, heading)
    print(titledtext.title(), titledtext)