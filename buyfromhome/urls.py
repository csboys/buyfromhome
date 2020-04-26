from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from user import views as user_view 
from django.contrib.auth import views as auth 
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('user.urls')),
    path('login/', include('login.urls')),
    path('form/', include('form.urls')),
   # path('user/', include('user.urls')),
    path('',views.index)
    

#	path('login/', user_view.Login, name ='login'), 
 #  	path('logout/', auth.LogoutView.as_view(template_name ='user / index.html'), name ='logout'), 
  #  path('register/', user_view.register, name ='register'),
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)