# File Name: the_social_entrepreneur.py

#Import libraries
import math
import pandas as pd
import numpy as np

#Define variables
social_entrepreneur_skills = ['problem-solving', 'creativity', 'initiative', 'persistence', 'adaptability']
business_plan_stages = ['idea generation', 'feasibility analysis', 'financial forecasting', 'branding', 'marketing']

# Create a function to calculate the ROI of a social enterprise
def calculate_return_on_investment(costs, revenues):
  return revenues/costs

# Create a function to generate a financial forecast
def financial_forecast(costs, revenues, time):
  return (revenues/costs)**time

# Create a function to analyze the feasibility of the project
def analyze_feasibility(costs, revenues, time):
  return_on_investment = calculate_return_on_investment(costs, revenues)
  financial_forecast = financial_forecast(costs, revenues, time)
  
  if return_on_investment > 1 and financial_forecast >= 0.2:
    return 'project is feasible!'
  else:
    return 'project is not feasible!'

# Create a function to build a business plan
def build_business_plan(idea, target_market, costs, revenues, time):
  feasibility = analyze_feasibility(costs, revenues, time)
  
  if feasibility == 'project is feasible!':
    business_plan = {
      'idea': idea,
      'target_market': target_market,
      'costs': costs,
      'revenues': revenues,
      'time': time,
      'feasibility': feasibility
      }
  return business_plan

# Create a function to evaluate the skills of a social entrepreneur
def evaluate_skills(skills_list):
  total_score = 0
  
  for skill in skills_list: 
    if skill in social_entrepreneur_skills:
      skill_score = 1
    else: 
      skill_score = 0
    total_score += skill_score
  return total_score

# Create a function to track a business plan
def track_business_plan(business_plan):
  stages = business_plan_stages
  progress = []
  for stage in stages:
    if stage in business_plan.keys():
      progress.append(stage)
  return progress

# Create a function to measure the success of a social enterprise
def measure_success(business_plan, skills_list):
  progress = track_business_plan(business_plan)
  skill_score = evaluate_skills(skills_list)
  success_score = len(progress) + skill_score
  return success_score

# Create a function to track the performance of a social enterprise
def track_performance(business_plan, skills_list, time):
  success_score = measure_success(business_plan, skills_list)
  financial_forecast = financial_forecast(business_plan['costs'], business_plan['revenues'], time)
  performance_score = success_score * financial_forecast
  return performance_score