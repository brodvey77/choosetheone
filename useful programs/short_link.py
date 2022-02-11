import pyshorteners

link = input('Введите ссылку, которую нужно сократить: ')
s = pyshorteners.Shortener()
print(s.tinyurl.short(link))


