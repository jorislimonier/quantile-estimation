import numpy as np
from sklearn.utils import resample


class Bootstrap():
    def __init__(self, k, results, confidence_level):
        self.k = k
        self.kth_quantile = self.quantile(k)
        self.results = results
        self.confidence_level = confidence_level
        self.nb_replicates = self.compute_nb_replicates()
        self.bootstrap = self.compute_bootstrap()
        self.ci_bounds = self.compute_ci_bounds(self.bootstrap)

    @staticmethod
    def quantile(k):
        """Get quantile of k zeros"""
        return 1 - 10**(-k)

    def compute_nb_replicates(self):
        """number of bootstrap replicates as advised by Jean-Yves Le Boudec
        in `Performance Evaluation of Computer and Communication Systems`"""
        return np.ceil(50 / (1 - self.confidence_level) - 1).astype(int)

    def compute_bootstrap(self, random_state=None):
        """takes the k-th quantile from a replicate
        of the results, repeats nb_replicates times"""
        bootstrap = np.array([])
        for _ in range(self.nb_replicates):
            r = resample(self.results, random_state=random_state)
            r_quantile = np.quantile(
                r, self.kth_quantile, interpolation="linear")
            bootstrap = np.append(bootstrap, r_quantile)
        return bootstrap

    def compute_ci_bounds(self, my_arr):
        """returns array containing CI lower and upper bound at confidence_level"""
        # get bounds and compute safe quantiles
        lower_bound = np.quantile(
            my_arr, (1 - self.confidence_level)/2)
        upper_bound = np.quantile(
            my_arr, (self.confidence_level + (1 - self.confidence_level)/2))
        return [lower_bound, upper_bound]
