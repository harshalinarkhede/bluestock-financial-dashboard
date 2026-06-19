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

    html = f"""
    <html>
    <head>
        <title>{company.company_name}</title>
    </head>
    <body style="font-family: Arial; padding: 30px;">
        <a href="/companies/">Back to Companies</a>

        <h1>{company.company_name}</h1>
        <p><b>Symbol:</b> {company.symbol}</p>
        <p><b>ROCE:</b> {company.roce_percentage}</p>
        <p><b>ROE:</b> {company.roe_percentage}</p>

        <h2>Profit and Loss Data</h2>

        <table border="1" cellpadding="8" cellspacing="0">
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

    html += """
        </table>
    </body>
    </html>
    """

    return HttpResponse(html)
def screener_page(request):

    min_roe = request.GET.get("roe", "")
    max_de = request.GET.get("de", "")

    companies = Companies.objects.all()

    html = f"""
    <html>
    <head>
        <title>Stock Screener</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body class="container mt-5">

        <h1>Stock Screener</h1>

        <form method="get">

            <div class="mb-3">
                <label>Minimum ROE</label>
                <input
                    type="number"
                    step="0.1"
                    name="roe"
                    value="{min_roe}"
                    class="form-control">
            </div>

            <div class="mb-3">
                <label>Maximum Debt/Equity</label>
                <input
                    type="number"
                    step="0.1"
                    name="de"
                    value="{max_de}"
                    class="form-control">
            </div>

            <button class="btn btn-primary">
                Run Screener
            </button>

        </form>

        <hr>

        <table class="table table-bordered">

            <tr>
                <th>Symbol</th>
                <th>Company Name</th>
                <th>ROE</th>
                <th>ROCE</th>
                <th>D/E</th>
            </tr>
    """

    for company in companies:

        try:

            balance = Balancesheet.objects.filter(
                company_id=company.symbol
            ).first()

            de_ratio = 0

            if balance:
                borrowings = float(balance.borrowings or 0)
                equity = float(balance.equity_share_capital or 0)
                reserves = float(balance.reserves or 0)

                total_equity = equity + reserves

                if total_equity > 0:
                    de_ratio = round(borrowings / total_equity, 2)

            if max_de and de_ratio > float(max_de):
                continue

            roe = float(company.roe_percentage or 0)

            if min_roe and roe < float(min_roe):
                continue

        except:
            continue

        html += f"""
        <tr>
            <td>{company.symbol}</td>
            <td>{company.company_name}</td>
            <td>{company.roe_percentage}</td>
            <td>{company.roce_percentage}</td>
            <td>{de_ratio}</td>
        </tr>
        """

    html += """
        </table>

    </body>
    </html>
    """

    return HttpResponse(html)

def compare_page(request):

    company1_symbol = request.GET.get("c1", "")
    company2_symbol = request.GET.get("c2", "")

    html = """
    <html>
    <head>
        <title>Company Comparison</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body class="container mt-5">

        <h1>Company Comparison</h1>

        <form method="get" class="row g-3">

            <div class="col-md-5">
                <input class="form-control"
                       name="c1"
                       placeholder="Company 1 Symbol (ABB)">
            </div>

            <div class="col-md-5">
                <input class="form-control"
                       name="c2"
                       placeholder="Company 2 Symbol (INFY)">
            </div>

            <div class="col-md-2">
                <button class="btn btn-primary w-100">
                    Compare
                </button>
            </div>

        </form>

        <hr>
    """

    if company1_symbol and company2_symbol:

        c1 = Companies.objects.filter(symbol=company1_symbol).first()
        c2 = Companies.objects.filter(symbol=company2_symbol).first()

        if c1 and c2:

            html += f"""
            <table class="table table-bordered">

                <tr>
                    <th>Metric</th>
                    <th>{c1.symbol}</th>
                    <th>{c2.symbol}</th>
                </tr>

                <tr>
                    <td>Company Name</td>
                    <td>{c1.company_name}</td>
                    <td>{c2.company_name}</td>
                </tr>

                <tr>
                    <td>ROE</td>
                    <td>{c1.roe_percentage}</td>
                    <td>{c2.roe_percentage}</td>
                </tr>

                <tr>
                    <td>ROCE</td>
                    <td>{c1.roce_percentage}</td>
                    <td>{c2.roce_percentage}</td>
                </tr>

            </table>
            """

        else:

            html += """
            <div class="alert alert-danger">
                Company symbol not found.
            </div>
            """

    html += """
    </body>
    </html>
    """

    return HttpResponse(html)