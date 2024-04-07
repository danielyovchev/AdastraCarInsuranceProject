"""Service for policies related operations"""
from functools import reduce
import pandas as pd
from app.data.queries import get_policy_data, get_customer_data, get_cars_data, \
    get_insurance_company_data, get_agents_data  # pylint: disable=import-error,no-name-in-module

df_customer = get_customer_data()
df_car = get_cars_data()
df_agent = get_agents_data()
df_insurance_company = get_insurance_company_data()
df_policy = get_policy_data()


def transform_policies_data():
    """Policy count for the customers"""
    policies_per_customer = df_policy.groupby('customer_id').size().reset_index(name='policy_count')

    customer_policy_counts = pd.merge(df_customer, policies_per_customer, left_on='id', right_on='customer_id',
                                      how='left')

    customer_policy_counts = customer_policy_counts[['name', 'policy_count']].fillna(0)

    customer_policy_counts_json = customer_policy_counts.to_dict(orient='records')

    return customer_policy_counts_json


def merge_insurance_data():
    """Full policy data"""
    data_frames = [df_policy, df_customer, df_car, df_agent, df_insurance_company]

    # Keys for merging. The first item of each tuple is the merge key for the left dataframe,
    # and the second item is for the right dataframe.
    keys = [('customer_id', 'id'), ('car_id', 'id'), ('agent_id', 'id'), ('insurance_company_id', 'id')]

    # Perform the merge using reduce
    policy_full_details = reduce(
        lambda left_df, args: pd.merge(left_df, args[0], left_on=args[1][0], right_on=args[1][1], how='left',
                                       suffixes=args[2]),
        zip(data_frames[1:], keys, [('', '_customer'), ('', '_car'), ('', '_agent'), ('', '_ins_comp')]),
        data_frames[0])

    return policy_full_details.to_dict(orient='records')
