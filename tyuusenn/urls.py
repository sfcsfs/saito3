from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name = 'tyuusenn'
urlpatterns = [
    path('', views.Login, name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('home', views.index, name='index'),
    path('i_ajax/',views.i_ajax,name='i_ajax'),
    #path('y',views.Yosouhe.as_view(),name="yosouhe"),
    path('yosou',views.yosouhee,name="yosouhe1"),
    path('sousuhe',views.sousuhe,name="sousuhe"),
    path('gurahu',views.Index2.as_view(),name='Index2'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
