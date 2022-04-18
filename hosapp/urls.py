from django.urls import path
from hosapp import views

urlpatterns = [
path('',views.index),
path('about/',views.about),
path('contact/',views.contact),
path('services/',views.services),
path('patient/',views.patient),
path('patientlogin/',views.patientlogin),
path('logout/',views.logout),
path('doctors/',views.doctors),
path('drlogin/',views.drlogin),
path('booking/',views.booking),
path('view/',views.view),
path('viewajas/',views.viewajas),










]