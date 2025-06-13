from rest_framework import serializers
from .models import Contrato, Parcela

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = ['numero', 'valor', 'data_vencimento']

class ContratoSerializer(serializers.ModelSerializer):
    parcelas = ParcelaSerializer(many=True)

    class Meta:
        model = Contrato
        fields = '__all__'

    def create(self, validated_data):
        parcelas_data = validated_data.pop('parcelas')
        contrato = Contrato.objects.create(**validated_data)
        for parcela in parcelas_data:
            Parcela.objects.create(contrato=contrato, **parcela)
        return contrato
