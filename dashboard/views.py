from django.http import HttpResponse
from companies.models import Companies, Profitandloss, Balancesheet, Cashflow

def home(request):

    total_companies = Companies.objects.count()
    total_profit = Profitandloss.objects.count()
    total_balance = Balancesheet.objects.count()
    total_cashflow = Cashflow.objects.count()

    return HttpResponse(f"""
    <html>
    <head>
        <title>Bluestock Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body class="bg-light">

        <div class="container mt-5">

            <h1>Bluestock Dashboard</h1>

            <h3>Total Companies: {total_companies}</h3>
            <h3>Profit Records: {total_profit}</h3>
            <h3>Balance Records: {total_balance}</h3>
            <h3>Cashflow Records: {total_cashflow}</h3>

        </div>

    </body>
    </html>
    """)