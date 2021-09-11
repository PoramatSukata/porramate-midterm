from django.urls import path
from web.views import index, patient , physician 


urlpatterns = [
    path('', index, name='index'),
    path('patient/', patient, name='patient'),
    path('physician/', physician, name='physician'),
]