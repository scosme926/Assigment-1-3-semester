from django.db import models

# "artist" (CharField)
# * "title" (CharField)

class Artist(models.Model): # This is called a "table" in a database. In django it's called a "model".
    value = models.CharField()  # This is called the "column" in a database. In django it's called a "field".

class Title(models.Model):
    text = models.CharField()
