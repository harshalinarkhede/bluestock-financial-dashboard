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
        <title>Bluestock Financial Dashboard</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    </head>

    <body class="bg-light">

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">

        <a class="navbar-brand" href="/">
            Bluestock Dashboard
        </a>

        <div>

            <a href="/" class="btn btn-outline-light me-2">
                Home
            </a>

            <a href="/companies/" class="btn btn-outline-light me-2">
                Companies
            </a>

            <a href="/logout/" class="btn btn-danger">
                Logout
            </a>

        </div>

    </div>
</nav>

        <div class="container mt-5">
<div class="alert alert-primary mt-3">

    <h4>Welcome to Bluestock Financial Intelligence Platform</h4>
<div class="mb-4">

    <a href="/companies/" class="btn btn-primary me-2">
        Browse Companies
    </a>

    <a href="/api/companies/" class="btn btn-success me-2">
        Companies API
    </a>

    <a href="/api/profitandloss/" class="btn btn-warning me-2">
        Profit & Loss API
    </a>

</div>

    <p>
        Analyze companies, profit records, balance sheets and cash flow data
        through an interactive dashboard.
    </p>

</div>

            <h1 class="mb-4">
                Bluestock Financial Intelligence Platform
            </h1>

            <div class="row">

                <div class="col-md-3">
                    <div class="card shadow text-center">
                        <div class="card-body">
                            <h2>{total_companies}</h2>
                            <p>Total Companies</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3">
                    <div class="card shadow text-center">
                        <div class="card-body">
                            <h2>{total_profit}</h2>
                            <p>Profit Records</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3">
                    <div class="card shadow text-center">
                        <div class="card-body">
                            <h2>{total_balance}</h2>
                            <p>Balance Sheet Records</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3">
                    <div class="card shadow text-center">
                        <div class="card-body">
                            <h2>{total_cashflow}</h2>
                            <p>Cash Flow Records</p>
                        </div>
                    </div>
                </div>

            </div>

            <div class="mt-4">
                <a href="/companies/" class="btn btn-primary">
                    Browse Companies
                </a>

                <a href="/compare/" class="btn btn-success ms-2">
                    Compare Companies
                </a>

                <a href="/logout/" class="btn btn-danger ms-2">
                    Logout
                </a>
            </div>

        </div>
<hr class="mt-5">

<footer class="text-center text-muted mb-4">

    <p>
        Bluestock Financial Intelligence Platform
    </p>

    <p>
        Developed using Django, PostgreSQL, Bootstrap and DRF
    </p>

    <p>
        Version 1.0
    </p>

</footer>
    </body>
    </html>
    """)