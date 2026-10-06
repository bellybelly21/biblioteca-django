from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutorViewSet, sincronizar_offline
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.listar_libros, name='catalogo'),
    path('catalogo/disponibles/', views.disponibles, name='disponibles'),
    path('catalogo/nuevo/', views.agregar_libro, name='agregar_libro'),
    path('catalogo/editar/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('catalogo/eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/nuevo/', views.agregar_autor, name='agregar_autor'),
    path('api/sync/', sincronizar_offline, name='sincronizar_offline'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]