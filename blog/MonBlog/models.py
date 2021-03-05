from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=50)

class Post(models.Model):
    titre = models.CharField(max_length=50)
    imageUrl = models.URLField()
    descriptionCourte = models.CharField(max_length=100)
    descriptionLongue = models.CharField(max_length=250)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    dateParution = models.DateField(auto_now_add=True)

class Commentaire(models.Model):
    commentaire = models.CharField(max_length=250)
    post = models.ForeignKey(Post, null = True , on_delete=models.CASCADE)