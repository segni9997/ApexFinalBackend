
from django.views.generic import  TemplateView
from django.urls import path,include, re_path
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
#    path('apexx/', include("users.urls")),
   path('apex/', include("apex.urls")),
   path('apexx/', include('djoser.urls')),
   path('apexx/', include('djoser.urls.jwt')),
   path('apexx/', include('djoser.urls.authtoken')),
   
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    
]

