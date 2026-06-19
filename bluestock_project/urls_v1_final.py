from django.contrib import admin
from django.urls import path, include
from dashboard.views import home
from companies.views import companies_page, company_detail_page
urlpatterns = [
    path('', home),

    path('companies/', companies_page),
    path('company/<str:symbol>/', company_detail_page),

    path('', include('accounts.urls')),

    path('admin/', admin.site.urls),
    path('api/', include('companies.urls')),
]