"""Endpoints for policies service"""
from fastapi import APIRouter
from app.service import policy_service  # pylint: disable=import-error,no-name-in-module

router = APIRouter()


@router.get("/policy/count")
def get_policy_names():
    """Get number of policies for a customer"""
    return policy_service.transform_policies_data()


@router.get("/policy/full")
def get_full_policy_data():
    """Get full policy data"""
    return policy_service.merge_insurance_data()
