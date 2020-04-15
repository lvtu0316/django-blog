from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post.show'),
    path('archives/<int:year>/<int:month>', views.ArchiveView.as_view(), name='post.archive'),
    path('categories/<int:pk>', views.CategoryView.as_view(), name='post.category'),
    path('tags/<int:pk>', views.TagView.as_view(), name='post.tag'),
    path('mdeditor/', include('mdeditor.urls')),
    path('about/', views.about, name="about"),
    # path('search', views.search, name="search"),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
