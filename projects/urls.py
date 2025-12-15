from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_project, name='generate_project'),
    path('project/<int:project_id>/', views.project_overview, name='project_overview'),
    path('project/<int:project_id>/start/', views.start_project, name='start_project'),
    path('session/<int:session_id>/', views.project_step, name='project_step'),
    path('session/<int:session_id>/complete-step/', views.complete_step, name='complete_step'),
    path('session/<int:session_id>/summary/', views.project_summary, name='project_summary'),
    path('session/<int:session_id>/submit/', views.submit_project, name='submit_project'),
    path('session/<int:session_id>/timer/', views.timer_status, name='timer_status'),
    path('resource/<int:resource_id>/download/', views.download_resource, name='download_resource'),
    # Onboarding flow
    path('onboarding/', views.onboarding_start, name='onboarding_start'),
    path('onboarding/technologies/', views.onboarding_technologies, name='onboarding_technologies'),
    path('onboarding/tracks/', views.onboarding_tracks, name='onboarding_tracks'),
    path('onboarding/interests/', views.onboarding_interests, name='onboarding_interests'),
    path('onboarding/complete/', views.onboarding_complete, name='onboarding_complete'),
]

