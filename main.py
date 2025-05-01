from app.backend.services import SaleService
from app.core.utils.transform import google_sheet_base_url_to_df
from app.data.sheets import MAR

df = google_sheet_base_url_to_df(MAR, use_grid=True)

service = SaleService(df)

service.export()