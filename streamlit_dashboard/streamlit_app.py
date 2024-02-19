import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from posterior_grid_binom import posterior_grid_binom

# Function to plot posterior distribution
def plot_posterior(p_grid, posterior):
    fig, ax = plt.subplots()
    ax.plot(p_grid, posterior, '-o', color='skyblue', linewidth=2, markersize=8)
    ax.fill_between(p_grid, posterior, color='skyblue', alpha=0.3)
    ax.set_xlabel('Probability of Water', fontsize=14)
    ax.set_ylabel('Posterior Probability', fontsize=14)
    ax.set_title('Posterior Distribution', fontsize=16)
    ax.grid(False)
    st.pyplot(fig)

# Title for the app
st.title("Bayesian Inference with Binomial Likelihood")

# User inputs for number of Water and Land rolls
st.sidebar.header("User Inputs")
water_rolls = st.sidebar.number_input("Number of times 'Water' is found:", min_value=0, step=1, value=6)
land_rolls = st.sidebar.number_input("Number of times 'Land' is found:", min_value=0, step=1, value=3)

# Compute posterior distribution
grid_points = 40
p_grid, posterior = posterior_grid_binom(grid_points, water_rolls+land_rolls, water_rolls)

# Plot posterior distribution
plot_posterior(p_grid, posterior)

# Additional section for a textbox 
st.sidebar.header("Additional Information")
st.sidebar.markdown("""

                    This app demonstrates Bayesian inference using a simple example from Richard McIlreath's 
                    [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/).
                    """)

# Additional section for GitHub link in the sidebar
st.sidebar.header("GitHub Repository")
st.sidebar.markdown("""
                    Find the source code for this app on GitHub:
                    [GitHub Repository](https://github.com/smose94/streamlit_binom)
                    """)

# Styling
st.markdown(
    """
    <style>
        .st-bb {
            background-color: #f0f5f5;
            padding: 10px;
            border-radius: 5px;
        }
        .st-bd {
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
