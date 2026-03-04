import logging
from collections import deque
from datetime import datetime


# In-memory log storage (max 1000 entries)
_log_storage = deque(maxlen=1000)


class LogQueueHandler(logging.Handler):
    """Custom handler to store logs in memory"""
    def emit(self, record):
        try:
            # Format the message first
            msg = self.format(record)
            
            log_entry = {
                'timestamp': datetime.now().strftime('%d/%b/%Y %H:%M:%S'),
                'level': record.levelname,
                'logger': record.name,
                'message': msg,
                'exception': None
            }
            
            if record.exc_info:
                import traceback
                log_entry['exception'] = ''.join(
                    traceback.format_exception(*record.exc_info)
                )
            
            _log_storage.append(log_entry)
        except Exception as e:
            self.handleError(record)


def get_logs():
    """Get all stored logs"""
    return list(_log_storage)


def clear_logs():
    """Clear all stored logs"""
    _log_storage.clear()


def get_log_count():
    """Get total number of stored logs"""
    return len(_log_storage)

