from rest_framework import serializers
from .models import Companies, Profitandloss, Balancesheet, Cashflow, Analysis


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'


class ProfitandlossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profitandloss
        fields = '__all__'


class BalancesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balancesheet
        fields = '__all__'


class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = '__all__'


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'