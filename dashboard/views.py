from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Bluestock Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body style="background-color:#f5f6fa; font-family:Arial;">

        <div style="text-align:center; padding:50px;">

            <h1 style="color:#2c3e50;">📊 Bluestock Financial Dashboard</h1>

            <div style="display:flex; justify-content:center; gap:20px; margin-top:40px; flex-wrap:wrap;">

                <div style="background:white; padding:20px; width:200px; border-radius:10px; box-shadow:0 0 10px #ddd;">
                    <h2>✔ LIVE</h2>
                    <p>System Status</p>
                </div>

                <div style="background:white; padding:20px; width:200px; border-radius:10px; box-shadow:0 0 10px #ddd;">
                    <h2>OK</h2>
                    <p>Deployment</p>
                </div>

                <div style="background:white; padding:20px; width:200px; border-radius:10px; box-shadow:0 0 10px #ddd;">
                    <h2>RUNNING</h2>
                    <p>Django Server</p>
                </div>

            </div>

            <h3 style="margin-top:50px; color:green;">
                Submission Ready ✔
            </h3>

        </div>

    </body>
    </html>
    """)