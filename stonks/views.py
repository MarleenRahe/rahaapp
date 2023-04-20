from django.shortcuts import render, redirect
from .forms import NewUserForm, NewDeptForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .data_methods import data, save_data


# Create your views here.
def homepage(request):
    labels = []
    values = []
    for name in data:
        if data[name] != 0:
            labels.append(name)
            values.append(data[name])
    context = {
        "labels": labels,
        "values": values,
    }
    return render(request, "index.html", context)


def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/stonks")
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/stonks")
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/stonks")


@login_required(login_url="login")
def add_dept_page(request):
    form = NewDeptForm()
    if request.method == "POST":
        form = NewDeptForm(request.POST)
        if form.is_valid():
            username = request.user.username
            name = form.cleaned_data.get('name')
            amount = form.cleaned_data.get('amount')
            if username not in data:
                data[username] = 0
            if name not in data:
                data[name] = 0
            data[name] += amount
            data[username] -= amount
            save_data()
            messages.info(request, f"Võlg kasutajale {name} suuruses {amount}€ lisatud.")
    return render(request, "adddept.html", context={"dept_form": form})