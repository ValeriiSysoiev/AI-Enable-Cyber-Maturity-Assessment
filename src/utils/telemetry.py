import logging
import contextvars

correlation_id_var: contextvars.ContextVar[str] = contextvars.ContextVar("correlation_id", default="")


class CorrelationIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.correlation_id = correlation_id_var.get("-")
        return True


def get_logger(name: str = "app") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.addFilter(CorrelationIdFilter())
        formatter = logging.Formatter("%(asctime)s %(levelname)s [%(correlation_id)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
