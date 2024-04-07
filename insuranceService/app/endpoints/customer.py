"""Endpoints for customer related services"""
from fastapi import APIRouter
from app.service import customer_service  # pylint: disable=import-error,no-name-in-module

router = APIRouter()


@router.get("/customer/data/{customer_id}")
def get_customers(customer_id: int):
    """Get policies for given user by his id"""
    return customer_service.get_policies_for_user(customer_id)
