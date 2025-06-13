from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Contrato
from .serializers import ContratoSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'cpf', 'data_emissao', 'estado']
    search_fields = ['cpf', 'estado']

@api_view(['GET'])
def resumo_contratos(request):
    cpf = request.GET.get('cpf')
    data_emissao = request.GET.get('data_emissao')
    estado = request.GET.get('estado')

    contratos = Contrato.objects.all()
    if cpf:
        contratos = contratos.filter(cpf=cpf)
    if data_emissao:
        contratos = contratos.filter(data_emissao__icontains=data_emissao)
    if estado:
        contratos = contratos.filter(estado=estado)

    total_receber = sum([
        sum(parcela.valor for parcela in contrato.parcelas.all())
        for contrato in contratos
    ])

    return Response({
        "valor_total_receber": total_receber,
        "valor_total_desembolsado": contratos.aggregate(Sum('valor_desembolsado'))['valor_desembolsado__sum'] or 0,
        "numero_total_contratos": contratos.count(),
        "taxa_media_contratos": contratos.aggregate(Avg('taxa'))['taxa__avg'] or 0,
    })
