"""Endpoint for agent data"""
from fastapi import APIRouter
from app.service import agent_service  # pylint: disable=import-error,no-name-in-module

router = APIRouter()


@router.get("/agents")
def get_all_agents():
    """Get all agents"""
    return agent_service.get_all_agents()


@router.get("/agents/sales")
def get_agents_sales():
    """Get all agents sales"""
    return agent_service.get_agents_sales()
