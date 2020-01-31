from django.urls import path
from main.views import index, movies , login ,signup ,success ,board,profile , write, boardlist, popup
from django.conf.urls import url
from django.conf.urls.static import static
from main import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('movies/',movies),
	path('popup/', popup),
    path('login/',views.login, name="login"),
    path('write/',views.write, name="write"),
    path('signup/',views.signup, name="signup"),
    path('logout/',views.logout, name="loginout"),
    path('board/',views.board, name="board"),
    path('profile/',views.profile, name="profile"),
    path('board/<int:pk>', boardlist),
	path('board/<int:pk>/delete',views.delete , name='delete'),
	path('board/<int:pk>/edit',views.edit , name='edit'),
    path('success/',success),
    path('useredit/', views.useredit, name='useredit'),
    path('movies/search_restful/', views.search_restful, name='search_restful'),
]
