from rest_framework import serializers
from classes.models import Classroom, Student


class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'subject', 'year', 'teacher']

class ClassroomDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'subject', 'year', 'id', 'teacher']

class ClassroomCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'subject', 'year']
