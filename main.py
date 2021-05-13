from quantile_estimation.data_prep import DataPrep
from quantile_estimation.data_visualization import DataVisualization
from quantile_estimation.bootstrap import Bootstrap

file_names = ["20210417_data_CC1.ods",
              "20210417_data_TFTP4.ods", "20210417_data_VD2.ods"]
file_names = [file_names[2]]
sheet_names = ["24s", "4min", "40min", "400min"]
sheet_names = [sheet_names[2]]

for file_name in file_names:
    for sheet_name in sheet_names:
        data_prep = DataPrep(file_name, sheet_name)
        results = data_prep.results
        print(file_name, sheet_name, len(results))

        data_vis = DataVisualization()
        data_vis.plot_histogram(data_prep).show()

# boot = Bootstrap(k=4, results=results, confidence_level=.95)
# boot.bootstrap.min()
# boot.bootstrap.max()
# len(boot.results)

# data_vis.hist_bootstrap(boot).show()
# data_vis.plot_moving_average(boot).show()

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
