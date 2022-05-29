from rest_framework import serializers
from .models import Building, Category,Product




class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    tenantsRN=serializers.StringRelatedField(many=True)# gets self.fname+self.lname+" tenant"
    tenantsRN = serializers.SlugRelatedField(
                many=True,
                read_only=True,
                slug_field='fname')
    class Meta:
        model=Building
        fields = ('id', 'address', 'zipcode', 'city','tenantsRN')

class CrudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "__all__"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "__all__"
        )