from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import logging
from datetime import datetime, timedelta
from .logging_handlers import get_logs
from .analytics_handlers import logs_analytics_api

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

@login_required(login_url='login')
def logs_page_view(request):
    """Display logs page"""
    logger = logging.getLogger(__name__)
    logger.info(f"User {request.user.username} accessed logs page")
    return render(request, 'logs_pages/log_pages.html')


@login_required(login_url='login')
def logs_analytics_page_view(request):
    """Display logs analytics dashboard"""
    logger = logging.getLogger(__name__)
    logger.info(f"User {request.user.username} accessed logs analytics")
    return render(request, 'logs_pages/analytics_dashboard.html')

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

    # Easypaisa hash format (without pipes): storeIdorderRefNumamountpostBackURLhashKey
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
    """Handle Easypaisa payment callback"""
    status = request.GET.get("paymentStatus")
    order_id = request.GET.get("orderRefNum")
    amount = request.GET.get("amount")
    hash_received = request.GET.get("hash")
    
    # Verify hash for security (without pipes)
    hash_string = (
        settings.EASYPAISA_STORE_ID +
        order_id +
        amount +
        settings.EASYPAISA_HASH_KEY
    )
    hash_calculated = hashlib.sha256(hash_string.encode()).hexdigest()
    
    if hash_received != hash_calculated:
        return HttpResponse("Hash Verification Failed", status=400)

    if status == "0":  # 0 = SUCCESS in Easypaisa
        # Mark order as paid in your database
        return redirect(settings.EASYPAISA_SUCCESS_URL)
    else:
        return redirect(settings.EASYPAISA_FAILURE_URL)


# ===================== LOGS MANAGEMENT =====================

@require_http_methods(["GET"])
def logs_api(request):
    """API endpoint to fetch logs"""
    try:
        logs_list = get_logs()
        
        return JsonResponse({
            'status': 'success',
            'logs': logs_list,
            'count': len(logs_list),
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
            'logs': []
        }, status=500)


@require_http_methods(["GET"])
def logs_status_api(request):
    """API endpoint to get logs management status"""
    try:
        from .logging_handlers import get_logs, get_log_count
        logs_list = get_logs()
        
        # Calculate statistics
        level_counts = {}
        for log in logs_list:
            level = log.get('level', 'INFO')
            level_counts[level] = level_counts.get(level, 0) + 1
        
        return JsonResponse({
            'status': 'success',
            'server_status': 'running',
            'total_logs': get_log_count(),
            'level_breakdown': level_counts,
            'timestamp': datetime.now().isoformat(),
            'message': f'Capturing logs successfully - {get_log_count()} entries stored'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
            'server_status': 'error'
        }, status=500)
