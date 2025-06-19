ALLOWED_STATUSES = {"pending", "in-progress", "done"}

def validate_status(status: str):
    if status not in ALLOWED_STATUSES:
        raise ValueError(f"Invalid status. Must be one of: {ALLOWED_STATUSES}")
