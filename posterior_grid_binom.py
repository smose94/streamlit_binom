import numpy as np
import numpyro.distributions as dist
def posterior_grid_binom(grid_points = 50, tosses=9, successes=6):

    #define grid
    p_grid = np.linspace(0,1,grid_points)

    #define prior
    prior = np.repeat(1, grid_points)
    # Define prior: 0 below 0.5, constant above 0.5
    #prior = np.where(p_grid < 0.5, 0, 1)


    #compute likelihood
    likelihood = np.exp(dist.Binomial(total_count=tosses,
    probs=p_grid).log_prob(successes))

    #compute posterior
    posterior = prior * likelihood

    #standardise posterior
    posterior = posterior / posterior.sum()
    return p_grid, posterior