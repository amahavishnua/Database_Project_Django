
from django.urls import path,include
from . import views
from .admin import *
urlpatterns = [
    #path('',views.home,name='WDS-home'),
    path('login/',views.login,name='WDS-login'),
    path('signup/',views.customercreate,name='WDS-Signup'),
    path('elogin/',views.emplogindefault,name='WDS-emplogin'),
    path('about/',views.about,name='WDS-about'),
    
    path('driver/',views.drivercreate,name='WDS-Driver'),
    path('homepre/',views.hpcreate,name='WDS-HomePremium'),
    path('invoice/',views.invoicecreate,name='WDS-Invoice'),
    path('payment/',views.paymentcreate,name='WDS-Payment'),
    path('vehicle/',views.vehiclecreate,name='WDS-Vehicle'),
    path('house/',views.housecreate,name='WDS-House'),
    path('policy/',views.policycreate,name='WDS-Policy'),
    path('',views.boochio,name='WDS-Home'),
        



    #path('entity-admin/', admin.site.urls),
    path('WDSadmin/', wds_admin_site.urls,name='WDS-Admin'),

]