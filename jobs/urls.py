from django.urls import path
from .views import JobListCreateView, JobRetriveUpdateDestroyView

urlpatterns = [
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path(
        'jobs/<int:pk>/',
        JobRetriveUpdateDestroyView.as_view(),
        name='job-retrieve-update-destroy'
    ),
]
