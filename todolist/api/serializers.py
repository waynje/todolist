from rest_framework import serializers

from tasks.models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description',
                  'category', 'execution_date',
                  'complete')