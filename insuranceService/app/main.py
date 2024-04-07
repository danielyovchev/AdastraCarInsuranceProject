"""Main entrypoint"""
from fastapi import FastAPI
from .endpoints import car, policy, agent, ins_company, customer

app = FastAPI()

app.include_router(car.router, tags=["Cars"])
app.include_router(policy.router, tags=["Policy"])
app.include_router(agent.router, tags=["Agent"])
app.include_router(ins_company.router, tags=["InsuranceCompany"])
app.include_router(customer.router, tags=["Customer"])
