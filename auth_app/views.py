from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from django.contrib.auth.decorators import login_required

# Create your views here.

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# logorusr = 'login/sign'












# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GeoLog

@csrf_exempt
def save_location(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        GeoLog.objects.create(
            method=data.get("method"),
            ip=data.get("ip"),
            city=data.get("city"),
            region=data.get("region"),
            country=data.get("country"),
            lat=data.get("lat"),
            lng=data.get("lng"),
            accuracy=data.get("accuracy")
        )

        return JsonResponse({"status": "saved"}, status=200)

    return JsonResponse({"error": "invalid"}, status=400)




# payments/views.py
import hashlib
import time
from django.shortcuts import render
from django.conf import settings

def initiate_payment(request):
    order_id = str(int(time.time()))
    amount = "3"  # PKR

    hash_string = (
        settings.EASYPAISA_STORE_ID +
        order_id +
        amount +
        settings.EASYPAISA_CALLBACK_URL +
        settings.EASYPAISA_HASH_KEY
    )

    secure_hash = hashlib.sha256(hash_string.encode()).hexdigest()

    context = {
        "payment_url": settings.EASYPAISA_PAYMENT_URL,
        "store_id": settings.EASYPAISA_STORE_ID,
        "order_id": order_id,
        "amount": amount,
        "callback_url": settings.EASYPAISA_CALLBACK_URL,
        "hash": secure_hash,
    }

    return render(request, "payments/easypaisa_form.html", context)


# payments/views.py
from django.http import HttpResponse

def payment_callback(request):
    status = request.GET.get("paymentStatus")
    order_id = request.GET.get("orderRefNum")

    if status == "SUCCESS":
        # Mark order as paid
        return HttpResponse("Payment Successful")
    else:
        return HttpResponse("Payment Failed")
