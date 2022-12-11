from app.plugins.backend.api.user import user_methods, verify_user
from app.plugins.backend.api.investments import (
    investment_methods,
    get_investment_master_data,
)
from app.plugins.backend.api.calendar import calendar_methods, get_calendar_date_id

api_methods = {
    "user": user_methods,
    "investments": investment_methods,
    "calendar": calendar_methods,
}
