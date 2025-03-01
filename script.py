from src.randomVerse import getRandomVerse 
from src.allBooks import books
from src.sendMessage import sendMessage
from src.data import phone1, phone2, phone3

versos, libro, rango = getRandomVerse(books=books)
versiculos = ''

for i in versos:
    versiculos += i

versiculos += f'\n{libro} [{rango}]'
sendMessage(phone1, versiculos)
sendMessage(phone2, versiculos)
sendMessage(phone3, versiculos)