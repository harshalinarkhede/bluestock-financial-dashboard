from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return HttpResponse("""
            <h3>Username already exists.</h3>
            <a href="/register/">Try another username</a><br>
            <a href="/login/">Already have an account? Login</a>
            """)

        User.objects.create_user(username=username, password=password)
        return redirect("/login/")

    return HttpResponse("""
    <html>
    <head>
        <title>Register</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <h2>Register</h2>
        <form method="post">
            <input class="form-control mb-2" type="text" name="username" placeholder="Username">
            <input class="form-control mb-2" type="password" name="password" placeholder="Password">
            <button class="btn btn-primary" type="submit">Register</button>
        </form>
        <br>
        <a href="/login/">Already have an account? Login</a>
    </body>
    </html>
    """)


@csrf_exempt
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/companies/")
        else:
            return HttpResponse("""
            <h3>Invalid username or password.</h3>
            <a href="/login/">Try again</a>
            """)

    return HttpResponse("""
    <html>
    <head>
        <title>Login</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <h2>Login</h2>
        <form method="post">
            <input class="form-control mb-2" type="text" name="username" placeholder="Username">
            <input class="form-control mb-2" type="password" name="password" placeholder="Password">
            <button class="btn btn-success" type="submit">Login</button>
        </form>
        <br>
        <a href="/register/">Create new account</a>
    </body>
    </html>
    """)


def logout_page(request):
    logout(request)
    return redirect("/login/")