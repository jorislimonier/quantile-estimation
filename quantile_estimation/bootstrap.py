import numpy as np
from sklearn.utils import resample

class Bootstrap():
    def __init__(self):
        return

    @staticmethod
    def quantile(k):
        """Get quantile of k zeros"""
        return 1 - 10**(-k)

    @staticmethod
    def bootstrap(quantile, nb_resample, results, resample_size, random_state=None):
        """takes the q quantile from a resample of the results, repeats n times"""
        boot = np.array([])
        for _ in range(nb_resample):
            r = resample(results, n_samples=resample_size, random_state=random_state)
            r_quantile = np.quantile(r, quantile, interpolation="linear")
            boot = np.append(boot, r_quantile)
        return boot

    @staticmethod
    def get_ci_bounds(boot, confidence_level):
        # returns array containing CI lower and upper bound at confidence_level
        bootstrap_sorted = np.sort(boot)
        # get bounds and compute safe quantiles
        lower_bound = np.quantile(bootstrap_sorted, (1 - confidence_level)/2)
        upper_bound = np.quantile(bootstrap_sorted, (confidence_level + (1 - confidence_level)/2))
        return [lower_bound, upper_bound]
