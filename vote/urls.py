from django.urls import path
from . import views

urlpatterns = [
    path('', views.vote_dashboard, name='vote_dashboard'),  # Changed to the actual view    path('session/<int:session_id>/', views.session_detail, name='session_detail'),  # Session details page]
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),  # Health card details page
    path('vote/create/', views.create_vote, name='create_vote'),  # Create a new vote
    path('vote/update/<int:vote_id>/', views.update_vote, name='update_vote'),  # Update an existing vote
    path('summary/team/<int:team_id>/', views.team_summary, name='team_summary'),  # Summary for a specific team
    path('summary/department/<int:department_id>/', views.department_summary, name='department_summary'),  # Summary for a specific department
]