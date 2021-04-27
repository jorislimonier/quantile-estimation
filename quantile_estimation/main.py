from quantile_estimation.data_prep import DataPrep
from quantile_estimation.data_visualization import DataVisualization

data_prep = DataPrep()
data_vis = DataVisualization()

data_prep.results

data_vis.plot_histogram(data_prep.results).show()