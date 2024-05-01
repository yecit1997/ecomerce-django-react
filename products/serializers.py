from rest_framework import serializers
from .models import Product, Reviews


class ReviewSerializer(serializers.ModelSerializer):
    '''Declaramos una variable en la que vamos a guardar el avatar del usuario que se encuentra logueado,
    La cual obtenemos con la propiedad del serializer que se muestra acontinuación, luego le pasalos el odjeto
    que se encuentra en el modelo usuario, el cual contiene esta información.'''
    avatar = serializers.SerializerMethodField(source='user.avatar.url')
    
    '''Declaramos una variable en la cuel vamos a almacenar el nombre del usuario que se encuentra logueado
    en el sitio, para poder mostrarlo en pantalla'''
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Reviews
        fields = "__all__"

    def get_avatar(self, obj):
        return obj.user.avatar.url
    

class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = "__all__"

    def get_reviews(self, obj):
        reviews = obj.reviews_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data