from django.contrib import admin

from .models import (
    Analysis,
    Balancesheet,
    Cashflow,
    Companies,
    Documents,
    Profitandloss,
    Prosandcons,
    ProfitDashboard
)

admin.site.register(Analysis)
admin.site.register(Balancesheet)
admin.site.register(Cashflow)
admin.site.register(Companies)
admin.site.register(Documents)
admin.site.register(Profitandloss)
admin.site.register(Prosandcons)
admin.site.register(ProfitDashboard)