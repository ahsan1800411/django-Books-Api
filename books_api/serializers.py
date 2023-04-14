from rest_framework import serializers
from .models import Book


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField();
#     quantity = serializers.IntegerField()
#     publish_date = serializers.DateTimeField()

#     def create(self, data):
#         return Book.objects.create(**data)
    

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.number_of_pages = validated_data.get('number_of_pages',instance.number_of_pages)
#         instance.quantity = validated_data.get('quantity',instance.quantity)
#         instance.publish_date = validated_data.get('publish_date',instance.publish_date)
#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'