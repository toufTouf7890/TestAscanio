from rest_framework.serializers import ModelSerializer

from .models import Company

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('titre','imageUrl','descriptionCourte','descriptionLongue','categorie','dateParution')