import logging
from datetime import datetime, timedelta
from django.utils import timezone


class TiDBLogHandler(logging.Handler):
    """Custom handler to store logs in TiDB"""
    def emit(self, record):
        try:
            # Avoid circular imports
            from .models import SystemLog
            
            exception_text = None
            if record.exc_info:
                import traceback
                exception_text = ''.join(
                    traceback.format_exception(*record.exc_info)
                )
            
            # Create log entry in database
            SystemLog.objects.create(
                timestamp=timezone.now(),
                level=record.levelname,
                logger=record.name,
                message=self.format(record),
                exception=exception_text
            )
            
            # Clean up old logs (older than 30 days)
            cutoff_date = timezone.now() - timedelta(days=30)
            SystemLog.objects.filter(timestamp__lt=cutoff_date).delete()
            
        except Exception as e:
            self.handleError(record)


def get_logs(limit=1000):
    """Get logs from TiDB"""
    from .models import SystemLog
    logs = SystemLog.objects.all()[:limit]
    return [
        {
            'timestamp': log.timestamp.strftime('%d/%b/%Y %H:%M:%S'),
            'level': log.level,
            'logger': log.logger,
            'message': log.message,
            'exception': log.exception
        }
        for log in logs
    ]


def clear_logs():
    """Clear all logs from TiDB"""
    from .models import SystemLog
    SystemLog.objects.all().delete()


def get_log_count():
    """Get total number of logs in TiDB"""
    from .models import SystemLog
    return SystemLog.objects.count()


