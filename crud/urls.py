from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [    

    path('admin/', admin.site.urls),
    path('new/', blog.views.new, name="new"),
    path('', blog.views.home, name="home"),
    path('post/<int:index>/', blog.views.post_detail, name="post_detail"), 
    path('post/<int:index>/edit/', blog.views.post_edit, name="post_edit"),
    path('post/<int:index>/delete/', blog.views.post_delete, name="post_delete"),     
    path('comment/<int:index>/delete/<int:cindex>/',blog.views.comment_delete, name="comment_delete"),
    path('comment/<int:index>/edit/<int:cindex>/',blog.views.comment_edit, name="comment_edit"),
    
]