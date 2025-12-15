from django.contrib import admin
from .models import Project, ProjectStep, ProjectResource, UserSession, UserProfile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'track', 'created_at']
    list_filter = ['difficulty', 'track']
    search_fields = ['title', 'description']


@admin.register(ProjectStep)
class ProjectStepAdmin(admin.ModelAdmin):
    list_display = ['project', 'step_number', 'title', 'timeframe', 'estimated_time']
    list_filter = ['timeframe', 'project']
    search_fields = ['title', 'description']


@admin.register(ProjectResource)
class ProjectResourceAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'resource_type', 'order']
    list_filter = ['resource_type', 'project']
    search_fields = ['name', 'description']


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'project', 'selected_timeframe', 'current_step', 'completed', 'start_time']
    list_filter = ['completed', 'selected_timeframe', 'project']
    readonly_fields = ['start_time', 'completed_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'experience_level', 'onboarding_completed', 'created_at', 'updated_at']
    list_filter = ['experience_level', 'onboarding_completed', 'preferred_difficulty']
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ['session_id']

