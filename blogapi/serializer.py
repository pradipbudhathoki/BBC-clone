from rest_framework import serializers
from news.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['name','created_at']   # also it can be used
