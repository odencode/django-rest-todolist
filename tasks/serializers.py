from rest_framework import serializers
from .models import Task
import django_filters

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta: 
        model = Task
        fields = {
            'title' : [],
            'completed' : ['exact']
        }

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)
