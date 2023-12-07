from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path("", views.vue, name="index"),
    path("connexion/<str:formType>", views.connection, name ="connexion"),
    path("logout", views.logoutPage, name ="logout"),
    path("faq",views.faq, name = "faq"),
    path("contact",views.contact, name = "contact"),
    path("profileIndex", views.profileIndex, name ="profileIndex"),
    path("commande", views.commande, name ="commande"),
    path("postRaspberry", views.postRaspberry, name="postRaspberry"),

    path('add_cat/', views.add_cat, name='add_cat'),
    path('get_cats/', views.get_cats, name='get_cats'),
    path('get_cat_details/<str:catId>/', views.get_cat_details, name='get_cat_details'),
    path('delete_cat/<str:catId>/', views.delete_cat, name='delete_cat'),
    path('modify_cat/<str:catId>/', views.modify_cat, name='modify_cat'),
    path("forgotpassword/", views.forgotpassword, name ="forgotpassword"),
    path("newpassword/", views.newpassword, name="newpassword"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('mail_sent',views.mail_sent,name="mail_sent"),
    path('reset_done', views.reset_done, name="reset_done"),
    path("postRaspberry", views.postRaspberry, name="postRaspberry"),
    path("profileNoDevice", views.profileNoDevice, name ="profileNoDevice" )


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)