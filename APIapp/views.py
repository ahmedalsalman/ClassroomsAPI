from django.shortcuts import render
from rest_framework.generics import (
ListAPIView,
RetrieveAPIView,
RetrieveUpdateAPIView,
DestroyAPIView,
CreateAPIView
)
from classes.models import Classroom, Student
from .serializers import *

class APIList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer

class APIdetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"


class CreateClass(CreateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class UpdateClass(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"

class DeleteClass(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"
