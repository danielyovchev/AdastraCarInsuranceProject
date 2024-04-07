"""Service for agent related operations"""
from app.data.queries import get_agents_data, get_insurance_company_data, \
    get_policy_data  # pylint: disable=import-error,no-name-in-module

policies_df = get_policy_data()
agents_df = get_agents_data()


def get_all_agents():
    """All agents data from db"""
    return agents_df.to_dict(orient='records')


def get_agents_sales():
    """Sales data for the agents"""

    policy_counts = policies_df.groupby('agent_id').size().reset_index(name='num_policies')

    agents_with_policies = agents_df.merge(policy_counts, left_on='id', right_on='agent_id')

    sorted_agents = agents_with_policies.sort_values(by='num_policies', ascending=False)

    insurance_companies_df = get_insurance_company_data()
    sorted_agents_with_companies = sorted_agents.merge(insurance_companies_df, left_on='insurance_company_id',
                                                       right_on='id', suffixes=('', '_company'))

    sorted_agents_with_companies = sorted_agents_with_companies[['name', 'num_policies', 'name_company']]

    result_json = sorted_agents_with_companies.to_dict(orient='records')
    return result_json
