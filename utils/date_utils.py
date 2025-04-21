from datetime import datetime
import dateparser


def resolve_datetime(natural_text: str) -> str:
    dt = dateparser.parse(
        natural_text,
        settings={"PREFER_DATES_FROM": "future", "RELATIVE_BASE": datetime.now()},
    )
    return dt.isoformat() if dt else None
