"""Endpoints for insurance companies services"""
from fastapi import APIRouter
from app.service import insurance_company_service  # pylint: disable=import-error,no-name-in-module

router = APIRouter()


@router.get("/insurance-policies/average")
def get_insurance_policies_average():
    """Get average price for policy for a company"""
    return insurance_company_service.insurance_company_policies()


@router.get("/insurance-policies/total")
def get_insurance_policies_total():
    """Get total amount for insurance company"""
    return insurance_company_service.total_policies_amount_by_insurance_company()
