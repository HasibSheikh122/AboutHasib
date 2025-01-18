from django.urls import path
from core import views
from .views import (
    MemberListView,
    MemberCreateView,
    MemberUpdateView,
    MemberDeleteView
)




urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('projects/<int:pk>/', views.ProjectView.as_view(), name='project_detail'),
    path('contact', views.ContactView.as_view(), name='contact'),
    
    path('members/', MemberListView.as_view(), name='view_members'),  # or use view_members for FBVs
    path('member/add/', MemberCreateView.as_view(), name='add_member'),  # or use add_member for FBVs
    path('member/update/<int:pk>/', MemberUpdateView.as_view(), name='update_member'),  # or use update_member for FBVs
    path('member/delete/<int:pk>/', MemberDeleteView.as_view(), name='delete_member'),
]
