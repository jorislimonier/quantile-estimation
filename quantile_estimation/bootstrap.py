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
    def bootstrap(quantile, nb_resample, results):
        """takes the q quantile from a resample of the results, repeats n times"""
        boot = np.array([])
        for _ in range(nb_resample):
            r = resample(results)
            r_quantile = np.quantile(r, quantile, interpolation="linear")
            boot = np.append(boot, r_quantile)
        return boot

    # def get_ci_bounds(boot, confidence_level):
    #     # returns array containing CI lower and upper bound at confidence_level
    #     bootstrap_sorted = np.sort(boot)
    #     # get bounds and compute safe quantiles
    #     lower_bound = np.quantile(bootstrap_sorted, (1 - confidence_level)/2)
    #     upper_bound = np.quantile(bootstrap_sorted, (confidence_level + (1 - confidence_level)/2))
    #     return [lower_bound, upper_bound]

    # def plot_moving_average(boot,confidence_level):
    #     first_resamples = [boot[:j] for j in range(1, len(boot)+1)]
    #     mean_first_resamples = [np.mean(first_res) for first_res in first_resamples] # the i-th element is an array with first i elements of boot
    #     # figure of moving average
    #     fig = go.Figure()
    #     ci_bounds = [get_ci_bounds(first_res, confidence_level) for first_res in first_resamples]
    #     fig.add_trace(go.Scatter(y=mean_first_resamples,name="estimation",))
    #     scatter_ci_upper = go.Scatter(name="Upper Bound", y=[bound[1] for bound in ci_bounds], showlegend=False, marker=dict(color="#444"), line=dict(width=0), fillcolor='rgba(68, 68, 68, 0.3)')
    #     scatter_ci_lower = go.Scatter(name="Lower Bound", y=[bound[0] for bound in ci_bounds], fill="tonexty", showlegend=False, marker=dict(color="#444"), line=dict(width=0), fillcolor='rgba(68, 68, 68, 0.3)')
    #     fig.add_trace(scatter_ci_upper)
    #     fig.add_trace(scatter_ci_lower)
    #     try:
    #         # get quantile provided by experiment software
    #         q_provided = st["Q" + str(k)][0]
    #         fig.add_trace(go.Scatter(x=[0, len(boot)-1],y=np.repeat(q_provided, 2),mode="lines",name="Provided value",visible="legendonly"))
    #     except Exception as e:
    #         print(e)
    #         # quantile is not provided
    #         print(f"The true value of q{k} has not been found")

    #     fig.update_layout(xaxis_title="Number of runs",yaxis_title="Value of the quantile",showlegend=True)

    #     fig.add_trace(go.Scatter(x=[0, len(boot)-1],y=np.repeat(np.quantile(results + width/2, q), 2),mode="lines",name="Computed value",visible="legendonly"))
    #     return fig
