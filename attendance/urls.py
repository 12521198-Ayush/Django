from django.urls import path
from attendance import views

urlpatterns = [
    path('students/', views.StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-retrieve-update-destroy'),
    path('parents/', views.ParentListCreateAPIView.as_view(), name='parent-list-create'),
    path('parents/<int:pk>/', views.ParentRetrieveUpdateDestroyAPIView.as_view(), name='parent-retrieve-update-destroy'),
    path('teachers/', views.TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', views.TeacherRetrieveUpdateDestroyAPIView.as_view(), name='teacher-retrieve-update-destroy'),
]
