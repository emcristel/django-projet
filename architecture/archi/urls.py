from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('ajout/',views.ajout),
    path('traitement/',views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/',views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path('delete/<int:id>/', views.delete),
    path('tous',views.tous),

   # path('ajout_architecte', views.ajout_architecte),
   # path('liste_architecte', views.liste_architecte),
   # path('update_architecte/<architecte_id>', views.update_architecte),
   # path('delete_architecte/<architecte_id>,', views.delete_architecte),

]