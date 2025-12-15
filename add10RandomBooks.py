from faker import Faker
import requests
fake = Faker()

for _ in range(10):
    book = {
     "title": fake.sentence(nb_words=4),
     "author": fake.name(),
      "isbn": fake.isbn13()
            }
    print(book)
