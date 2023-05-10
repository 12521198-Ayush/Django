from rest_framework import generics
from .models import Student, Teacher, Parent
from .serializers import StudentSerializer, TeacherSerializer, ParentSerializer

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            return Student.objects.all()
        elif user.is_parent:
            return user.parent.students.all()
        else:
            return Student.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_teacher:
            serializer.save()
        elif user.is_parent:
            serializer.save(parents=[user.parent])

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            return Student.objects.all()
        elif user.is_parent:
            return user.parent.students.all()
        else:
            return Student.objects.none()

class ParentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            return Parent.objects.all()
        elif user.is_parent:
            return Parent.objects.filter(pk=user.parent.pk)
        else:
            return Parent.objects.none()

class ParentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            return Parent.objects.all()
        elif user.is_parent:
            return Parent.objects.filter(pk=user.parent.pk)
        else:
            return Parent.objects.none()

class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
