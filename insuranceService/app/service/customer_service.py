"""Service for customer related operations"""
from app.data.queries import get_customer_data, get_policy_data, get_insurance_company_data, \
    get_cars_data, get_agents_data

customer_df = get_customer_data()
policies_df = get_policy_data()
insurance_companies_df = get_insurance_company_data()
cars_df = get_cars_data()
agents_df = get_agents_data()


def get_policies_for_user(user_id):
    """Get all policies for the given user"""
    user_policies_df = policies_df[policies_df['customer_id'] == user_id]

    if user_policies_df.empty:
        return {'message': 'No policies found for the specified customer.'}

    enriched_policies_df = user_policies_df \
        .merge(customer_df, left_on='customer_id', right_on='id', how='left') \
        .rename(columns={'name': 'Customer Name'}) \
        .merge(cars_df, left_on='car_id', right_on='id', how='left', suffixes=('', '_car')) \
        .merge(agents_df, left_on='agent_id', right_on='id', how='left', suffixes=('', '_agent')) \
        .rename(columns={'name': 'Agent Name'}) \
        .merge(insurance_companies_df, left_on='insurance_company_id', right_on='id', how='left',
               suffixes=('', '_company')) \
        .rename(columns={'name': 'Insurance Company'})

    user_policies_details = enriched_policies_df[
        ['Customer Name', 'policy_number', 'policy_date', 'price', 'Insurance Company', 'Agent Name', 'make', 'model',
         'year']]

    result_json = user_policies_details.to_dict(orient='records')
    return result_json
