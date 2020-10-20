from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'

urlpatterns = [
    path('', views.CoreView.as_view(), name='index'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('Add/', views.BlogCreateView.as_view(), name='blog'),
    path('posts-update/<int:pk>', views.CoreUpdateView.as_view(), name="posts_update"),
    path('posts-delete/<int:pk>', views.CoreDeleteView.as_view(), name="posts_delete"),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),

    path('project-forms', views.ProjectListView.as_view(), name="project"),
    path('project-add', views.ProjectCreateView.as_view(), name="project-add"),
    path('project-list', views.ProjectListView.as_view(), name="project-list"),
    path('project-detail/<int:pk>', views.ProjectDetailView.as_view(), name="project-detail"),
    path('project-update/<int:pk>', views.ProjectUpdateView.as_view(), name="project_update"),
    path('project-delete/<int:pk>', views.ProjectDeleteView.as_view(), name="project_delete"),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)