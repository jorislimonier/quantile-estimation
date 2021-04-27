import plotly.graph_objects as go
from plotly.subplots import make_subplots  # used for secondary y-axis


class DataVisualization():
    def plot_histogram(self, results, show_cdf=True):
        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # make histogram
        hist = go.Histogram(
            x = results,
            histnorm="probability",
            name="Histogram",
            marker_color="#0f802d"
        )
        fig.add_trace(hist)
        fig.update_layout(bargroupgap=.1)  # space between bars
        if show_cdf:
            hist_cumul = go.Histogram(x=results, histnorm="probability", name="Cumul. histogram",
                                      cumulative_enabled=True, opacity=.25,)
            fig.add_trace(hist_cumul, secondary_y=True)
        return fig
