from datetime import date, datetime


def _next_month(base_date: date) -> date:
    if base_date.month == 12:
        return base_date.replace(year=base_date.year + 1, month=1)
    return base_date.replace(month=base_date.month + 1)


def resolve_date(value: str) -> datetime:
    result = int(value)
    base_date = date.today()

    if result < base_date.day:
        base_date = _next_month(base_date)

    return datetime(base_date.year, base_date.month, result)


def resolve_time_item(value: str) -> int:
    value = value.lstrip('0') or '0'
    return int(value)


def resolve_datetime(time: str, base_date: datetime):
    hour, minute = time.split()
    hour = resolve_time_item(hour)
    minute = resolve_time_item(minute)
    return base_date.replace(hour=hour, minute=minute)
