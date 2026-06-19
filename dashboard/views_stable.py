from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Bluestock Dashboard</title>
    </head>
    <body style="font-family: Arial; padding: 40px;">
        <h1>Bluestock Nifty Financial Intelligence Platform</h1>
        <p>Django Web Application connected with PostgreSQL database.</p>

        <h2>Pages</h2>
        <ul>
            <li><a href="/companies/">Companies Page</a></li>
            <li><a href="/admin/">Admin Panel</a></li>
        </ul>

        <h2>API Endpoints</h2>
        <ul>
            <li><a href="/api/companies/">Companies API</a></li>
            <li><a href="/api/profitandloss/">Profit and Loss API</a></li>
            <li><a href="/api/balancesheet/">Balance Sheet API</a></li>
            <li><a href="/api/cashflow/">Cash Flow API</a></li>
            <li><a href="/api/analysis/">Analysis API</a></li>
            <li><a href="/api/company/ABB/">Company Detail API - ABB</a></li>
        </ul>
    </body>
    </html>
    """)