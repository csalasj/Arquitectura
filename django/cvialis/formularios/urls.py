from django.urls import path, include
from rest_framework import routers, serializers, viewsets, filters
from .models import ContratoEmpresas
from .models import ContratoProyectos
from django_filters.rest_framework import DjangoFilterBackend

class ContratoEmpresasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContratoEmpresas
        fields = ['nomempresa', 'rut', 'direccion', 'telefono', 'nombre_representante',
        'email', 'fechainicio', 'fechatermino', 'valormensual']

class ContratoEmpresasViewSet(viewsets.ModelViewSet):
    queryset = ContratoEmpresas.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nomempresa', 'rut']
    search_fields = ['nomempresa', 'rut']
    serializer_class = ContratoEmpresasSerializer

router = routers.DefaultRouter()
router.register(r'ContratoEmpresas', ContratoEmpresasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

class ContratoProyectosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContratoProyectos
        fields = ['nomempresa', 'rut', 'direccion', 'telefono', 'nombre_representante',
        'email', 'fechainicio', 'fechatermino', 'nombre_proyecto', 'tipo_proyecto',
        'valor_proyecto', 'observaciones']

class ContratoProyectosViewSet(viewsets.ModelViewSet):
    queryset = ContratoProyectos.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nomempresa', 'rut']
    search_fields = ['nomempresa', 'rut']
    serializer_class = ContratoProyectosSerializer

router = routers.DefaultRouter()
router.register(r'ContratoProyectos', ContratoProyectosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
