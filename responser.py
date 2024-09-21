import pandas as pd

def market_research(product_idea):
    # Simulate market research on the given product idea
    data = {
        'Consumer Segment': ['Tech Enthusiasts', 'Small Businesses', 'Freelancers'],
        'Interest Level': [85, 70, 75],  # Interest levels in percentages
        'Estimated Market Size (USD)': [500000, 200000, 300000]
    }
    df = pd.DataFrame(data)
    return df

def digital_marketing_strategy(product_idea):
    # Simulate creation of a marketing strategy for the product idea
    strategy = {
        'Campaign Type': ['Social Media Ads', 'Email Marketing', 'Content Marketing'],
        'Target Audience': ['Tech Enthusiasts', 'Business Owners', 'Freelancers'],
        'Estimated Budget (USD)': [2000, 1500, 1000],
        'Projected Reach': ['100,000', '50,000', '20,000']
    }
    return strategy

def product_design_feedback(product_idea):
    # Simulate a feedback analysis for product design
    feedback = {
        'Design Element': ['User Interface', 'Functionality', 'Performance'],
        'User Rating (out of 5)': [4.5, 4.0, 4.2],
        'Top Recommendation': ['Make it more intuitive', 'Add more features', 'Enhance speed']
    }
    return feedback