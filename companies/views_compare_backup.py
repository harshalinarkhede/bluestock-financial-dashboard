from django.http import JsonResponse, HttpResponse
from .models import Companies, Profitandloss, Balancesheet, Cashflow, Analysis

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompaniesSerializer, ProfitandlossSerializer

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
    </head>
    <body style="font-family: Arial; padding: 30px;">
        <h1>Top Companies</h1>

        <form method="get">
            <input type="text" name="q" value="{query}" placeholder="Search Company" style="padding:8px; width:300px;">
            <button type="submit" style="padding:8px;">Search</button>
        </form>

        <br>

        <table border="1" cellpadding="8" cellspacing="0">
        <tr>
            <th>Symbol</th>
            <th>Company Name</th>
        </tr>
    """

    for company in companies:
        html += f"""
        <tr>
            <td>{company.symbol}</td>
            <td>
                <a href="/company/{company.symbol}/">{company.company_name}</a>
            </td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return HttpResponse(html)

def company_detail_page(request, symbol):
    company = Companies.objects.filter(symbol=symbol).first()
    profits = Profitandloss.objects.filter(company_id=symbol)

    if not company:
        return HttpResponse("<h1>Company not found</h1>")

    years = []
    sales_data = []
    net_profit_data = []

    for p in profits:
        years.append(str(p.year))
        sales_data.append(float(p.sales or 0))
        net_profit_data.append(float(p.net_profit or 0))

    html = f"""
    <html>
    <head>
        <title>{company.company_name}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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

            <div class="card shadow-sm mb-4">
                <div class="card-body">
                    <h3>Sales and Net Profit Trend</h3>
                    <canvas id="profitChart" height="100"></canvas>
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

    html += f"""
                </tbody>
            </table>
        </div>

        <script>
            const ctx = document.getElementById('profitChart');

            new Chart(ctx, {{
                type: 'line',
                data: {{
                    labels: {years},
                    datasets: [
                        {{
                            label: 'Sales',
                            data: {sales_data},
                            borderWidth: 2
                        }},
                        {{
                            label: 'Net Profit',
                            data: {net_profit_data},
                            borderWidth: 2
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    scales: {{
                        y: {{
                            beginAtZero: true
                        }}
                    }}
                }}
            }});
        </script>
    </body>
    </html>
    """

    return HttpResponse(html)

def compare_page(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Company Comparison</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body class="container mt-5">

        <h1>Company Comparison</h1>

        <form>
            <input class="form-control mb-2" placeholder="Company 1 (ABB)">
            <input class="form-control mb-2" placeholder="Company 2 (INFY)">
            <input class="form-control mb-2" placeholder="Company 3 (TCS)">
            <button class="btn btn-primary">Compare</button>
        </form>

        <hr>

        <h3>Comparison Result Area</h3>

        <p>Coming Soon...</p>

    </body>
    </html>
    """)