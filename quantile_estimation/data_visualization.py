import plotly.graph_objects as go
from plotly.subplots import make_subplots  # used for secondary y-axis


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
    def hist_bootstrap(b):
        """takes an array with results from the bootstrap
        draws a histogram of the quantile value from the bootstrap"""
        fig = make_subplots()
        # xbins = go.histogram.XBins(size=width/3)
        hist = go.Histogram(x=b)  # , xbins=xbins)
        fig.add_trace(hist)
        fig.update_layout(
            title="Values of the quantile over all runs",
            xaxis_title="Value of the quantile",
            yaxis_title="Number of occurences",
            bargap=.05
        )
        return fig
