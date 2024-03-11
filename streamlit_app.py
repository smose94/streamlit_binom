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


# Define the multipage app structure
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the Page",
                                    ("Binomial Distribution", "Bayesian A/B Testing"))

    # Additional section for a textbox 
    st.sidebar.header("Additional Information")
    st.sidebar.markdown("""

                        This app demonstrates Bayesian inference using a simple example from Richard McElreath's 
                        [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/). It also demonstrates a simple form 
                        of Bayesian A/B testing. 
                        """)

    # Additional section for GitHub link in the sidebar
    st.sidebar.header("GitHub Repository")
    st.sidebar.markdown("""
                        Find the source code for this app on GitHub:
                        [GitHub Repository](https://github.com/smose94/streamlit_binom)
                        """)

    if app_mode == "Binomial Distribution":
        show_bayesian_inference_page()
    elif app_mode == "Bayesian A/B Testing":
        show_beta_distributions_page()

def show_bayesian_inference_page():
    # Your existing Bayesian inference code goes here
    # Title for the app
    st.title("Bayesian Inference with Binomial Likelihood")

    # User inputs for number of Water and Land rolls
    col1, col2 = st.columns(2)  # Creates two columns
    with col1:
        water_rolls = st.number_input("Number of times 'Water' is found:", min_value=0, step=1, value=6)

    with col2:
        land_rolls = st.number_input("Number of times 'Land' is found:", min_value=0, step=1, value=3)

    # 
    # Compute posterior distribution
    grid_points = 40
    p_grid, posterior = posterior_grid_binom(grid_points, water_rolls+land_rolls, water_rolls)

    # Plot posterior distribution
    plot_posterior(p_grid, posterior)

def show_beta_distributions_page():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import beta

    st.title("Bayesian A/B Testing Visualization")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Version A")
        conversions_a = st.number_input("Conversions for A", min_value=0, value=15)
        trials_a = st.number_input("Trials for A", min_value=1, value=30)
        if conversions_a > trials_a:
            st.error("Conversions cannot exceed trials. Please adjust.")


    with col2:
        st.subheader("Version B")
        conversions_b = st.number_input("Conversions for B", min_value=0, value=25)
        trials_b = st.number_input("Trials for B", min_value=1, value=30)
        if conversions_b > trials_b:
            st.error("Conversions cannot exceed trials. Please adjust.")


    # Prior parameters (you can adjust these as needed)
    alpha_prior = 1
    beta_prior = 1

    # Calculating posterior parameters
    alpha_post_a = conversions_a + alpha_prior
    beta_post_a = trials_a - conversions_a + beta_prior
    alpha_post_b = conversions_b + alpha_prior
    beta_post_b = trials_b - conversions_b + beta_prior

    x = np.linspace(0, 1, 1000)
    y_a = beta.pdf(x, alpha_post_a, beta_post_a)
    y_b = beta.pdf(x, alpha_post_b, beta_post_b)

    fig, ax = plt.subplots()
    ax.plot(x, y_a, label=f'Version A (Posterior)', color='skyblue')
    ax.fill_between(x, y_a, color='skyblue', alpha=0.2)
    ax.plot(x, y_b, label=f'Version B (Posterior)', color='#EA7E33')
    ax.fill_between(x, y_b, color='#EA7E33', alpha=0.2)
    ax.legend()
    ax.set_xlabel('Conversion Rate')
    ax.set_ylabel('Density')
    ax.set_title('Posterior Distributions of Conversion Rates for Versions A and B')

    st.pyplot(fig)

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

if __name__ == "__main__":
    main()


