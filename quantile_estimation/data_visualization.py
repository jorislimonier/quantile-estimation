import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots  # used for secondary y-axis


class DataVisualization():
    @staticmethod
    def plot_histogram(data_prep, show_cdf=True):
        results = data_prep.results
        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # make histogram
        xbins = dict(
            start=data_prep.data["Value"].min(),
            end=data_prep.data["Value"].max() + data_prep.width,
            size=data_prep.width
        )
        hist = go.Histogram(
            x=data_prep.results,
            xbins=xbins,
            histnorm="probability",
            name="Histogram",
            marker_color="#0f802d",
        )
        fig.add_trace(hist)
        fig.update_layout(
            bargroupgap=.1,  # space between bars
            title=f"Distribution of the durations after {data_prep.sheet_name} of simulation",
            xaxis_title="Duration",
            yaxis_title="Number of occurences",
        )
        if show_cdf:
            hist_cumul = go.Histogram(
                x=results,
                xbins=xbins,
                histnorm="probability",
                name="Cumulative histogram",
                cumulative_enabled=True,
                opacity=.3,
            )
            fig.add_trace(hist_cumul, secondary_y=True)
        return fig

    @staticmethod
    def hist_bootstrap(bootstrap):
        """takes an array with results from the bootstrap
        draws a histogram of the quantile value from the bootstrap"""
        fig = make_subplots()
        hist = go.Histogram(x=bootstrap.bootstrap,)
        fig.add_trace(hist)
        fig.update_layout(
            title="Values of the quantile over all bootstrap replicates",
            xaxis_title="Value of the quantile",
            yaxis_title="Number of occurences",
            bargap=.05
        )
        return fig

    @staticmethod
    def plot_moving_average(bootstrap):
        """plots the evolution of the quantile
        measure in `bootstrap`"""
        # the i-th element is an array with first i elements of boot
        boot_val = bootstrap.bootstrap
        first_resamples = [boot_val[:i] for i in range(1, len(boot_val)+1)]
        mean_first_resamples = [np.mean(first_res)
                                for first_res in first_resamples]
        # figure of moving average
        fig = go.Figure()
        ci_bounds = [bootstrap.compute_ci_bounds(first_res)
                     for first_res in first_resamples]
        fig.add_trace(
            go.Scatter(
                y=mean_first_resamples, 
                name="estimation",
                marker_color="#921b96",
                line_width=4,
            )
        )
        scatter_ci_upper = go.Scatter(
            name="Upper Bound",
            y=[bound[1] for bound in ci_bounds],
            showlegend=False,
            marker=dict(color="#444"),
            line=dict(width=0),
        )
        scatter_ci_lower = go.Scatter(
            name="Confidence interval",
            y=[bound[0] for bound in ci_bounds],
            fill="tonexty",
            # showlegend=False,
            marker=dict(color="#444"),
            line=dict(width=0),
            fillcolor='rgba(217, 82, 82, 0.3)'
        )
        fig.add_trace(scatter_ci_upper)
        fig.add_trace(scatter_ci_lower)
        fig.update_layout(
            xaxis_title="Number of runs completed",
            yaxis_title="Value of the quantile",
            showlegend=True
        )
        return fig
