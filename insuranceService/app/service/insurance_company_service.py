"""Service for operations related to insurance company"""
import pandas as pd
from app.data.queries import get_insurance_company_data, get_policy_data, \
    get_agents_data  # pylint: disable=import-error,no-name-in-module

companies_df = get_insurance_company_data()
policies_df = get_policy_data()
agents_df = get_agents_data()
insurance_companies_df = get_insurance_company_data()


def insurance_company_policies():
    """Average policy price of the insurance company"""

    policies_agents = pd.merge(policies_df, agents_df, left_on='agent_id', right_on='id')
    policies_agents_companies = pd.merge(policies_agents, companies_df, left_on='insurance_company_id', right_on='id',
                                         suffixes=('_policy', '_company'))

    avg_policy_price = policies_agents_companies.groupby('name_company').agg(
        average_policy_price=pd.NamedAgg(column='price', aggfunc='mean')
    ).reset_index()

    result_dict = avg_policy_price.to_dict(orient='records')
    return result_dict


def total_policies_amount_by_insurance_company():
    """Total amount of policies for the insurance company"""

    policies_with_agents = pd.merge(policies_df, agents_df, left_on='agent_id', right_on='id', how='left')

    policies_with_company_names = pd.merge(policies_with_agents, insurance_companies_df, left_on='insurance_company_id',
                                           right_on='id', how='left', suffixes=('_policy', '_company'))

    total_amounts_by_company = policies_with_company_names.groupby('name_company')['price'].sum().reset_index(
        name='total_amount')

    result_json = total_amounts_by_company.to_dict(orient='records')
    return result_json
