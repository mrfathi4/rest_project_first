from rest_framework import serializers

from lib_app.models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate_name(self, value):
        if value.isdigit():
            raise serializers.ValidationError('name could not be digit')
        return value

    # def validate(self, attrs):
    #     if str(attrs['name']).isdigit():
    #         raise serializers.ValidationError({'name': 'name could not be digit'})
    #
    #     return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookReadSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        exclude = ('file', 'cover_image')


class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('file', 'cover_image')
