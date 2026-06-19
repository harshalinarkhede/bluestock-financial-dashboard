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
    profit_data = []
    eps_data = []

    for p in profits:

        years.append(str(p.year))

        try:
            sales_data.append(float(p.sales or 0))
        except:
            sales_data.append(0)

        try:
            profit_data.append(float(p.net_profit or 0))
        except:
            profit_data.append(0)

        try:
            eps_data.append(float(p.eps or 0))
        except:
            eps_data.append(0)

    html = f"""
    <html>

    <head>
        <title>{company.company_name}</title>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    </head>

    <body class="container mt-5">

        <a href="/companies/" class="btn btn-secondary mb-3">
            Back to Companies
        </a>

        <h1>{company.company_name}</h1>

        <p><b>Symbol:</b> {company.symbol}</p>
        <p><b>ROCE:</b> {company.roce_percentage}</p>
        <p><b>ROE:</b> {company.roe_percentage}</p>

        <hr>

        <h2>Sales Trend</h2>

        <canvas id="salesChart"></canvas>

        <br><br>

        <h2>Net Profit Trend</h2>

        <canvas id="profitChart"></canvas>

        <br><br>

        <h2>EPS Trend</h2>

        <canvas id="epsChart"></canvas>

        <br><br>

        <h2>Profit & Loss Data</h2>

        <table class="table table-bordered table-striped">

            <tr>
                <th>Year</th>
                <th>Sales</th>
                <th>Operating Profit</th>
                <th>Net Profit</th>
                <th>EPS</th>
            </tr>
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

        </table>

        <script>

        new Chart(document.getElementById('salesChart'), {{
            type: 'line',
            data: {{
                labels: {years},
                datasets: [{{
                    label: 'Sales',
                    data: {sales_data}
                }}]
            }}
        }});

        new Chart(document.getElementById('profitChart'), {{
            type: 'bar',
            data: {{
                labels: {years},
                datasets: [{{
                    label: 'Net Profit',
                    data: {profit_data}
                }}]
            }}
        }});

        new Chart(document.getElementById('epsChart'), {{
            type: 'line',
            data: {{
                labels: {years},
                datasets: [{{
                    label: 'EPS',
                    data: {eps_data}
                }}]
            }}
        }});

        </script>

    </body>
    </html>
    """

    return HttpResponse(html)

def screener_page(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Stock Screener</title>
    </head>
    <body style="padding:30px;font-family:Arial;">
        <h1>Stock Screener</h1>
        <p>Screener Working</p>
    </body>
    </html>
    """)


def compare_page(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Company Comparison</title>
    </head>
    <body style="padding:30px;font-family:Arial;">
        <h1>Company Comparison</h1>
        <p>Compare Page Working</p>
    </body>
    </html>
    """)


def sector_page(request, name):
    return HttpResponse(f"""
    <html>
    <head>
        <title>Sector Analysis</title>
    </head>
    <body style="padding:30px;font-family:Arial;">
        <h1>Sector Analysis</h1>
        <p>Selected Sector: <b>{name}</b></p>
    </body>
    </html>
    """)