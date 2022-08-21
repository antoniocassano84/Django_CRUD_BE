from dataclasses import fields
from rest_framework import serializers
from mainApp.models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'Title', 'Description', 'Date', 'Completed')