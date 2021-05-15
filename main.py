from quantile_estimation.data_prep import DataPrep
from quantile_estimation.data_visualization import DataVisualization
from quantile_estimation.bootstrap import Bootstrap

file_names = ["20210417_data_CC1.ods",
              "20210417_data_TFTP4.ods", "20210417_data_VD2.ods"]
file_names = [file_names[0]]
sheet_names = ["24s", "4min", "40min", "400min"]
sheet_names = [sheet_names[1]]

for sheet_name in sheet_names:
    for file_name in file_names:
        data_prep = DataPrep(file_name, sheet_name)
        results = data_prep.results
        print(file_name, sheet_name, len(results))

        data_vis = DataVisualization()
        data_vis.plot_histogram(data_prep).write_html("fig/test.html", auto_open=True)
        # boot = Bootstrap(k=4, results=results, confidence_level=.95)
        # data_vis.hist_bootstrap(boot).show()
        # data_vis.plot_moving_average(boot).show()


