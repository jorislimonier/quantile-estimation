import plotly.graph_objects as go
import numpy as np
from quantile_estimation.data_prep import DataPrep
from quantile_estimation.data_visualization import DataVisualization
from quantile_estimation.bootstrap import Bootstrap

file_name = "20210417_data_VD2.ods"
sheet_name = "24s"
data_prep = DataPrep(file_name, sheet_name)
results = data_prep.results
data_vis = DataVisualization()

bs = Bootstrap()
boot = bs.bootstrap(bs.quantile(4), 50, results)
data_vis.plot_histogram(data_prep).show()


# data_vis.hist_bootstrap(boot).show()
# data_vis.plot_moving_average(boot, .95, data_prep).show()

# for k in range(3, 6):
#     print(f"\n============= q{k} =============")
#     for resample_size in [100, 1000, 10000, 100000]:
#         q = bs.quantile(k)
#         n = 1000
#         boot = bs.bootstrap(
#             q, n, results, resample_size=resample_size, random_state=None)
#         ci = bs.get_ci_bounds(boot, .95)
#         print("---------------")
#         print(f"{resample_size}: ", ci, ci[1] - ci[0])
#         data_vis.hist_bootstrap(boot).show()
#         data_vis.plot_moving_average(boot, .95, data_prep).show()


