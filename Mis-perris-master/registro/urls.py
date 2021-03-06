

from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.conf.urls import url, include
from django.conf import settings 
from rest_framework import routers
from registro.quickstart import api_views

router = routers.DefaultRouter()
router.register(r'personas', api_views.PersonaViewSet)
router.register(r'mascotas', api_views.MascotaViewSet)


urlpatterns = [
    path('', views.index, name="index"),
    path('registro/crear',views.crear,name="crear"),
    path('registro/eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('registro/editar',views.editar,name="editar"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('administrar/',views.administrar, name="administrar"),
    path('administrar/registPerro',views.registPerro, name='registPerro'),
    path('administrar/editPerro',views.editPerro, name='editPerro'),
    url(r'^api/', include(router.urls)),
    path('manifest.json', views.manifest, name="manifest"),
    path('galeria', views.galeria, name='galeria'),
    path('shell_sworker', views.shell_sworker, name='shell_sworker'),
    path('shell_admin', views.shell_admin, name='shell_admin'),
    path('shell_galeria', views.shell_galeria, name='shell_galeria'),
    path('shell_log', views.shell_log, name='shell_log'),
    url(r'^sw(.*.js)$', views.sw, name='sw'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
