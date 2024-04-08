"""Service for car related operations"""
from app.data.queries import get_cars_data

cars_df = get_cars_data()


def get_all_cars():
    """All cars data"""
    return cars_df.to_dict(orient='records')


def get_average_model_year_by_make():
    """Average car year the manufacturer"""
    return cars_df.groupby('make')['year'].mean()
