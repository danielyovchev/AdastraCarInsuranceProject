"""Queries definition"""
from app.data.db_utils import fetch_table_data  # pylint: disable=import-error,no-name-in-module


def get_cars_data():
    """Get all car data in dataframe"""
    return fetch_table_data("car")


def get_customer_data():
    """Get all customer data in dataframe"""
    return fetch_table_data("customer")


def get_agents_data():
    """Get all agent data in dataframe"""
    return fetch_table_data("agent")


def get_insurance_company_data():
    """Get all insurance company data in dataframe"""
    return fetch_table_data("insurance_company")


def get_policy_data():
    """Get all policy data in dataframe"""
    return fetch_table_data("policy")
