from django.shortcuts import render, redirect, HttpResponse
from .models import Travel
from ..user_app.models import User
from django.contrib import messages

def add_trip(request):
    if request.method == "POST":
        userID = request.session['id']
        trips= {
            "destination" : request.POST["destination"],
            "description" : request.POST["description"],
            "travel_date_from":request.POST['travel_date_from'],
            "travel_date_to" : request.POST["travel_date_to"],
            }
        response = Travel.objects.add_trip(trips, userID)
        print request.POST["destination"]
        print request.POST["travel_date_from"]


        if response['status'] ==False:
            for error in response['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect("/travels/add")
        else:
            print "YAYYYYYY"
            messages.add_message(request, messages.SUCCESS, "You have successfully added trip" )
            return redirect("/travels")

    else:
        messages.add_message(request, messages.ERROR, "login/register first")
        return redirect("/main")


def success(request):
    if not 'id' in request.session:
        messages.add_message(request, messages.ERROR, "Please login.")
        return redirect('/main')
    context = {
        'trips': Travel.objects.filter(your_plan = User.objects.get(id = request.session['id'])),
        'all_trips':Travel.objects.exclude(your_plan = User.objects.get(id = request.session['id']))
    }
    return render(request, 'travel_app/index.html', context)

def create(request):
    if not 'id' in request.session:
        messages.add_message(request, messages.ERROR, "Please login.")
        return redirect('/main')
    return render(request, 'travel_app/add.html')

def trip_detail(request, id):
    response = Travel.objects.trip_detail(id)
    context= {
        'trip_detail':response
        }
    return render(request, 'travel_app/detail.html', context)

def move_up(request, id):
    up = Travel.objects.get(id = id)
    person = User.objects.get(id = request.session['id'])
    up.your_plan.add(person)
    return redirect('/travels')


def home(request):
    return redirect("/travels")


def logout(request):
    request.session.clear()
    messages.add_message(request, messages.SUCCESS, "You have logged out!" )
    return redirect("/main")
