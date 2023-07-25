from django.shortcuts import render

# Create your views here.


def index(requests):
    ctx = {

    }
    return render(requests, "index.html", ctx)

def about(requests):
    ctx = {

    }
    return render(requests, "about.html", ctx)

def contact(requests):
    ctx = {

    }
    return render(requests, "contact.html", ctx)

def food(requests):
    ctx = {

    }
    return render(requests, "food.html", ctx)

