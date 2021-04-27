import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots  # used for secondary y-axis
from quantile_estimation.bootstrap import Bootstrap


class DataVisualization():

    @staticmethod
    def plot_histogram(results, show_cdf=True):
        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # make histogram
        hist = go.Histogram(
            x=results,
            histnorm="probability",
            name="Histogram",
            marker_color="#0f802d"
        )
        fig.add_trace(hist)
        fig.update_layout(bargroupgap=.1)  # space between bars
        if show_cdf:
            hist_cumul = go.Histogram(
                x=results,
                histnorm="probability",
                name="Cumul. histogram",
                cumulative_enabled=True,
                opacity=.25,
            )
            fig.add_trace(hist_cumul, secondary_y=True)
        return fig

    @staticmethod
    def hist_bootstrap(boot):
        """takes an array with results from the bootstrap
        draws a histogram of the quantile value from the bootstrap"""
        fig = make_subplots()
        xbins = go.histogram.XBins(size=0.001)
        hist = go.Histogram(x=boot, xbins=xbins)  # , xbins=xbins)
        fig.add_trace(hist)
        fig.update_layout(
            title="Values of the quantile over all runs",
            xaxis_title="Value of the quantile",
            yaxis_title="Number of occurences",
            bargap=.05
        )
        return fig

    @staticmethod
    def plot_moving_average(boot, confidence_level, data_prep):
        """plots the evolution of the quantile
        measure in boot"""
        # the i-th element is an array with first i elements of boot
        first_resamples = [boot[:i] for i in range(1, len(boot)+1)]
        mean_first_resamples = [np.mean(first_res)
                                for first_res in first_resamples]
        # figure of moving average
        fig = go.Figure()
        ci_bounds = [Bootstrap.get_ci_bounds(first_res, confidence_level)
                     for first_res in first_resamples]
        fig.add_trace(go.Scatter(y=mean_first_resamples, name="estimation",))
        scatter_ci_upper = go.Scatter(
            name="Upper Bound",
            y=[bound[1] for bound in ci_bounds],
            showlegend=False,
            marker=dict(color="#444"),
            line=dict(width=0),
            fillcolor='rgba(68, 68, 68, 0.3)'
        )
        scatter_ci_lower = go.Scatter(
            name="Lower Bound",
            y=[bound[0] for bound in ci_bounds],
            fill="tonexty",
            showlegend=False,
            marker=dict(color="#444"),
            line=dict(width=0),
            fillcolor='rgba(68, 68, 68, 0.3)'
        )
        fig.add_trace(scatter_ci_upper)
        fig.add_trace(scatter_ci_lower)
        fig.update_layout(
            xaxis_title="Number of runs",
            yaxis_title="Value of the quantile",
            showlegend=True
        )
        return fig
