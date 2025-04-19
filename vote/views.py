from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Vote

# This function checks if the user is either an engineer or a team leader
def is_engineer_or_team_leader(user):
    return user.is_engineer or user.is_team_leader

@user_passes_test(is_engineer_or_team_leader)
def create_vote(request):
    # Logic for creating a vote
    return render(request, 'voting.html')

@user_passes_test(is_engineer_or_team_leader)
def update_vote(request, vote_id):
    # Logic for updating a vote
    return render(request, 'vote/update_vote.html')
def vote_dashboard(request):
    # Logic for the vote dashboard
    return render(request, 'vote_dashboard.html')
def card_detail(request, card_id):
    # Your logic for displaying card details
    return render(request, 'vote/card_detail.html', {'card_id': card_id})

# Define the 'team_summary' view
def team_summary(request, team_id):
    # Logic for fetching and displaying the team summary by its ID
    return render(request, 'vote/team_summary.html', {'team_id': team_id})
def department_summary(request, department_id):
    # Logic for fetching and displaying the department summary by its ID
    return render(request, 'vote/department_summary.html', {'department_id': department_id})