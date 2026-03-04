import logging
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import SystemLog


@require_http_methods(["GET"])
def logs_analytics_api(request):
    """API endpoint for logs analytics data"""
    try:
        # Overall statistics
        total_logs = SystemLog.objects.count()
        
        # Stats by level
        level_stats = {}
        for level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            count = SystemLog.objects.filter(level=level).count()
            level_stats[level] = count
        
        # Last 24 hours stats
        last_24h = timezone.now() - timedelta(hours=24)
        logs_24h = SystemLog.objects.filter(timestamp__gte=last_24h).count()
        
        # Errors in last 24 hours
        errors_24h = SystemLog.objects.filter(
            level__in=['ERROR', 'CRITICAL'],
            timestamp__gte=last_24h
        ).count()
        
        # Top loggers
        from django.db.models import Count
        top_loggers = SystemLog.objects.values('logger').annotate(
            count=Count('id')
        ).order_by('-count')[:10]
        
        # Hourly distribution (last 24 hours)
        hourly_data = []
        for i in range(24):
            hour_start = timezone.now() - timedelta(hours=24-i)
            hour_end = hour_start + timedelta(hours=1)
            count = SystemLog.objects.filter(
                timestamp__gte=hour_start,
                timestamp__lt=hour_end
            ).count()
            hourly_data.append({
                'hour': hour_start.strftime('%H:%M'),
                'count': count
            })
        
        # Recent logs
        recent_logs = SystemLog.objects.all()[:10]
        recent_logs_list = [
            {
                'timestamp': log.timestamp.strftime('%d/%b/%Y %H:%M:%S'),
                'level': log.level,
                'logger': log.logger,
                'message': log.message[:100]  # First 100 chars
            }
            for log in recent_logs
        ]
        
        return JsonResponse({
            'status': 'success',
            'total_logs': total_logs,
            'logs_24h': logs_24h,
            'errors_24h': errors_24h,
            'level_stats': level_stats,
            'top_loggers': list(top_loggers),
            'hourly_data': hourly_data,
            'recent_logs': recent_logs_list,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
