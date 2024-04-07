"""Car endpoints"""
from fastapi import APIRouter
from app.service import car_service  # pylint: disable=import-error,no-name-in-module

router = APIRouter()


@router.get("/cars")
def get_all_cars():
    """Get all cars"""
    return car_service.get_all_cars()


@router.get("/cars/model-average-year")
def get_cars_model_average_year():
    """Get all cars with the average year for a model"""
    return car_service.get_average_model_year_by_make()
