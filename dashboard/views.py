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

            <h1 class="mb-4">📊 Bluestock Financial Dashboard</h1>

            <div class="row">

                <div class="col-md-3">
                    <div class="card text-center shadow">
                        <div class="card-body">
                            <h2>{total_companies}</h2>
                            <p>Total Companies</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3">
                    <div class="card text-center shadow">
                        <div class="card-body">
                            <h2>{total_profit}</h2>
                            <p>Profit Records</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3">
                    <div class="card text-center shadow">
                        <div class="card-body">
                            <h2>{total_balance}</h2>
                            <p>Balance Sheet Records</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3">
                    <div class="card text-center shadow">
                        <div class="card-body">
                            <h2>{total_cashflow}</h2>
                            <p>Cash Flow Records</p>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </body>
    </html>
    """)