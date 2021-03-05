from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Post

class PostResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'post_titre': 'titre',
        'post_imageUrl': 'imageUrl',
        'post_postdescriptionCourte': 'descriptionCourte',
        'post_descriptionLongue' : 'descriptionLongue',
        'post_categorie' : 'categorie.nom',
        'post_dateParution' : 'dateParution'
    })

    def getCategories(self, nom):
    	posts = Post.Objects.all()
    	categories = [post.categorie.nom for post in posts]

    	return categories
      

from django.conf.urls import include, url
from .api import PostResource

urlpatterns = [
    url(r'^post/', include(PostResource.urls())),
]