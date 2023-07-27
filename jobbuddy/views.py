from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Job
import json

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'jobbuddy/index.html')

def login_view(request):
    if request.method == 'POST':
        # try to sign user in

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # check if authentication is successful

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'jobbuddy/login.html', {'message': 'Invalid username and/or password.'})
    else:
        return render(request, 'jobbuddy/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # ensures passwords match
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, 'jobbuddy/register.html', {'message': 'Passwords must match.'})

        # try to create user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'jobbuddy/register.html',{'message': 'Username already taken.'})
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, 'jobbuddy/register.html')

@csrf_exempt
@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            job = Job(
                title=data.get("title"), 
                company=data.get("company"), 
                location=data.get("location"), 
                url=data.get("url"), 
                description=data.get("description"), 
                color=data.get("color"), 
                user=request.user, 
                posting_date=data.get("posting_date"), 
                level=data.get("level"),
                mode=data.get("mode"),
                stage=data.get("stage"),
                )
            job.save()
            return JsonResponse({"message": "success"}, status=201)
        except:
            return JsonResponse({"error", "bad request"}, status=400)
    else:
        return render(request, 'jobbuddy/add.html')

@login_required(login_url='login')
def jobs(request):
    # jobs = Job.objects.all()
    jobs = Job.objects.filter(user=request.user)
    jobs = [job.serialize() for job in jobs]

    return JsonResponse(jobs, safe=False)

@csrf_exempt
@login_required(login_url='login')
def update(request, id):
    try:
        job = Job.objects.get(user=request.user, pk=id)
    except Job.DoesNotExist:
        return JsonResponse({"error": "Job not found."}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        if data.get("stage") is not None:
            job.stage = data["stage"]
        if data.get("archived") is not None:
            job.archived = data["archived"]
        job.save()
        return HttpResponse(status=204)

    elif request.method == 'DELETE':
        job.delete()
        return HttpResponse(status=204)
    # elif request.method == 'GET':
    #     return JsonResponse(job.serialize(), safe=False)

@login_required(login_url='login')
def details(request, id):
    try:
        job = Job.objects.get(user=request.user, pk=id)
    except Job.DoesNotExist:
        return render(request, 'jobbuddy/details.html', {
            "message": "Job Not Found"
        })

    return render(request, 'jobbuddy/details.html', {
        "job": job.serialize()
    })
