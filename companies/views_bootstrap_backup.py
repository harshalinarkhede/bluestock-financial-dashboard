from django.http import JsonResponse, HttpResponse
from .models import Companies, Profitandloss, Balancesheet, Cashflow, Analysis


def companies_list(request):
    data = list(Companies.objects.values()[:10])
    return JsonResponse(data, safe=False)


def profitandloss_list(request):
    data = list(Profitandloss.objects.values()[:10])
    return JsonResponse(data, safe=False)


def balancesheet_list(request):
    data = list(Balancesheet.objects.values()[:10])
    return JsonResponse(data, safe=False)


def cashflow_list(request):
    data = list(Cashflow.objects.values()[:10])
    return JsonResponse(data, safe=False)


def analysis_list(request):
    data = list(Analysis.objects.values()[:10])
    return JsonResponse(data, safe=False)


def company_detail(request, symbol):
    company = list(Companies.objects.filter(symbol=symbol).values())
    profit = list(Profitandloss.objects.filter(company_id=symbol).values())
    balance = list(Balancesheet.objects.filter(company_id=symbol).values())
    cashflow = list(Cashflow.objects.filter(company_id=symbol).values())
    analysis = list(Analysis.objects.filter(company_id=symbol).values())

    data = {
        "company": company,
        "profitandloss": profit,
        "balancesheet": balance,
        "cashflow": cashflow,
        "analysis": analysis
    }

    return JsonResponse(data)


def companies_page(request):
    query = request.GET.get('q', '')

    if query:
        companies = Companies.objects.filter(company_name__icontains=query)[:50]
    else:
        companies = Companies.objects.all()[:50]

    html = f"""
    <html>
    <head>
        <title>Companies List</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <nav class="navbar navbar-dark bg-primary mb-4">
            <div class="container">
                <a class="navbar-brand" href="/">Bluestock Nifty Dashboard</a>
            </div>
        </nav>

        <div class="container">
            <div class="card shadow-sm mb-4">
                <div class="card-body">
                    <h2 class="card-title">Companies List</h2>
                    <p class="text-muted">Search and view company financial details.</p>

                    <form method="get" class="d-flex">
                        <input class="form-control me-2" type="text" name="q" value="{query}" placeholder="Search Company">
                        <button class="btn btn-primary" type="submit">Search</button>
                    </form>
                </div>
            </div>

            <table class="table table-striped table-bordered bg-white shadow-sm">
                <thead class="table-primary">
                    <tr>
                        <th>Symbol</th>
                        <th>Company Name</th>
                    </tr>
                </thead>
                <tbody>
    """

    for company in companies:
        html += f"""
                    <tr>
                        <td><b>{company.symbol}</b></td>
                        <td><a href="/company/{company.symbol}/">{company.company_name}</a></td>
                    </tr>
        """

    html += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


def company_detail_page(request, symbol):
    company = Companies.objects.filter(symbol=symbol).first()
    profits = Profitandloss.objects.filter(company_id=symbol)

    if not company:
        return HttpResponse("<h1>Company not found</h1>")

    html = f"""
    <html>
    <head>
        <title>{company.company_name}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <nav class="navbar navbar-dark bg-primary mb-4">
            <div class="container">
                <a class="navbar-brand" href="/">Bluestock Nifty Dashboard</a>
            </div>
        </nav>

        <div class="container">
            <a href="/companies/" class="btn btn-secondary mb-3">Back to Companies</a>

            <div class="card shadow-sm mb-4">
                <div class="card-body">
                    <h2>{company.company_name}</h2>
                    <p><b>Symbol:</b> {company.symbol}</p>
                    <p><b>ROCE:</b> {company.roce_percentage}</p>
                    <p><b>ROE:</b> {company.roe_percentage}</p>
                    <p><b>About:</b> {company.website}</p>
                </div>
            </div>

            <h3>Profit and Loss Data</h3>

            <table class="table table-bordered table-striped bg-white shadow-sm">
                <thead class="table-success">
                    <tr>
                        <th>Year</th>
                        <th>Sales</th>
                        <th>Operating Profit</th>
                        <th>Net Profit</th>
                        <th>EPS</th>
                    </tr>
                </thead>
                <tbody>
    """

    for p in profits:
        html += f"""
                    <tr>
                        <td>{p.year}</td>
                        <td>{p.sales}</td>
                        <td>{p.operating_profit}</td>
                        <td>{p.net_profit}</td>
                        <td>{p.eps}</td>
                    </tr>
        """

    html += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)