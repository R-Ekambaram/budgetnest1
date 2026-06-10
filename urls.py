from django.urls import path

from family import views

urlpatterns = [
    path('addmember/',views.addmember,name='addmember'),
path('familydata/',views.familydata,name='familydata'),
path('update_member/<int:id>',views.update_member,name='update_member'),
path('delete_member/<int:id>',views.delete_member,name='delete_member'),
path('addexpenses/',views.addexpenses,name='addexpenses'),
path('viewexpenses/',views.viewexpenses,name='viewexpenses'),
path('update_expenses/<int:id>',views.updateexpenses,name='updateexpenses'),
path('delete_expenses/<int:id>',views.deleteexpenses,name='deleteexpenses'),
path('monthly/',views.monthly,name='monthly'),
path('yearly/',views.yearly,name='yearly'),
path('total/',views.total,name='total'),

]