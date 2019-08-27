# Defines URl patterns for learning_logs

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'), # Home page
    path('topics/', views.topics, name='topics'), # Displays all topics
    path('topics/<int:topic_id>/', views.topic, name='topic'), # Displays detailed page for single topic
    path('new_topic/', views.new_topic, name='new_topic'), # New topic
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'), # New entry for a topic
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'), # Edit existing entry
]
