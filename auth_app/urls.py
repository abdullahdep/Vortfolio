from django.urls import path 
from . import views
from .analytics_handlers import logs_analytics_api


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path("api/save-location/", views.save_location, name="save_location"),
    path("pay/", views.initiate_payment, name="pay"),
    path("payment/callback/", views.payment_callback, name="callback"),
    path('logs/', views.logs_page_view, name='logs_page'),
    path('logs/analytics/', views.logs_analytics_page_view, name='logs_analytics_page'),
    path('api/logs/', views.logs_api, name='logs_api'),
    path('api/logs/analytics/', logs_analytics_api, name='logs_analytics_api'),
    path('api/logs/status/', views.logs_status_api, name='logs_status'),
]