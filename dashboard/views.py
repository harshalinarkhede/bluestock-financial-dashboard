from django.http import HttpResponse

def home(request):

    total_companies = 50
    total_profit = 500
    total_balance = 500
    total_cashflow = 500

    return HttpResponse(f"""
    <html>
    <body>
        <h1>Bluestock Dashboard</h1>
        <h2>Total Companies: {total_companies}</h2>
        <h2>Profit Records: {total_profit}</h2>
        <h2>Balance Records: {total_balance}</h2>
        <h2>Cashflow Records: {total_cashflow}</h2>
    </body>
    </html>
    """)