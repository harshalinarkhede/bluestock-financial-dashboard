from django.urls import path
from .views import (
    companies_list,
    profitandloss_list,
    balancesheet_list,
    cashflow_list,
    analysis_list,
    company_detail
)

urlpatterns = [
    path('companies/', companies_list),
    path('profitandloss/', profitandloss_list),
    path('balancesheet/', balancesheet_list),
    path('cashflow/', cashflow_list),
    path('analysis/', analysis_list),
    path('company/<str:symbol>/', company_detail),
]