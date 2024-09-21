import streamlit as st
from responser import market_research, digital_marketing_strategy, product_design_feedback

# Set up Streamlit session state
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Title of the app
st.title("Virtual Digital Marketing Agency")

# User input for product idea
product_idea = st.text_input("Enter your product idea:")

if st.button("Analyze"):
    # Call each agent function and store results
    market_data = market_research(product_idea)
    marketing_strategy = digital_marketing_strategy(product_idea)
    design_feedback = product_design_feedback(product_idea)

    # Store responses in session state
    st.session_state.responses['Market Research'] = market_data
    st.session_state.responses['Marketing Strategy'] = marketing_strategy
    st.session_state.responses['Design Feedback'] = design_feedback

    # Display results from Agent 1
    st.subheader("Market Research Results")
    st.dataframe(market_data)

    # Display results from Agent 2
    st.subheader("Digital Marketing Strategy")
    st.write(marketing_strategy)

    # Display results from Agent 3
    st.subheader("Product Design Feedback")
    st.write(design_feedback)

# Optional: Display previous responses if any
if st.session_state.responses:
    st.subheader("Previous Responses")
    for key, value in st.session_state.responses.items():
        st.write(f"**{key}:**")
        st.write(value)