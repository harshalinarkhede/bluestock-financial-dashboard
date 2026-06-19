from django.contrib import admin
from django.urls import path, include
from dashboard.views import home
from companies.views import companies_page, company_detail_page, screener_page, compare_page, sector_page
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', home),

    path('companies/', companies_page),
    path('company/<str:symbol>/', company_detail_page),

    path('', include('accounts.urls')),

    path('admin/', admin.site.urls),
    path('api/', include('companies.urls')),

   path('screener/', screener_page),

   path('compare/', compare_page),

   path('sector/<str:name>/', sector_page),

   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]