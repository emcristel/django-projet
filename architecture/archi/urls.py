from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('ajout/',views.ajout, name="Ajout"),
    path('traitement/',views.traitement),
    path('affiche/<int:id>/',views.affiche, name="Affiche"),
    path('update/<int:id>/',views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path('delete/<int:id>/', views.delete),
    path('tous',views.tous, name="Tous"),

   # path('ajout_architecte', views.ajout_architecte),
    path('liste_architecte', views.liste_architecte, name="Architecte"),
   # path('update_architecte/<architecte_id>', views.update_architecte),
   # path('delete_architecte/<architecte_id>,', views.delete_architecte),

]