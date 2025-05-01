from datetime import datetime
from app.backend.services import SaleService
from app.core.utils.transform import google_sheet_base_url_to_df
from app.data.sheets import ABRIL

df = google_sheet_base_url_to_df(ABRIL, use_grid=True)

service = SaleService(df)

date = datetime(2025, 4, 30)

result = service.get_money_by_date_interval(
    date,
    date
)

print(result)

for payment in result.money_by_payment_method:
    print(f"Payment Method: {payment.method}, Value: {payment.value}")