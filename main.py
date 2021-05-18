from quantile_estimation.data_prep import DataPrep
from quantile_estimation.data_visualization import DataVisualization
from quantile_estimation.bootstrap import Bootstrap
from datetime import datetime


file_names = [
    "20210417_data_CC1.ods",
    "20210417_data_TFTP4.ods",
    "20210417_data_VD2.ods",
]
# file_names = file_names[0:2]

sheet_names = ["24s", "4mn", "40mn", "400mn"]
# sheet_names = sheet_names[0:2]

for sheet_name in sheet_names:
    print("=========", datetime.now().strftime("%H:%M:%S"), "=========")
    for file_name in file_names:
        data_prep = DataPrep(file_name, sheet_name)
        results = data_prep.results
        data_vis = DataVisualization()
        data_vis.plot_histogram(data_prep).write_image(
            f"fig/data/{data_prep.protocol}_{data_prep.sim_time}.png", scale=5
        )

        for k in range(3, 6):
            print(f"{sheet_name} -- {file_name} -- quantile {k} -- {len(results)}")
            boot = Bootstrap(k=k, results=results, confidence_level=0.95)
            hist_boot = data_vis.hist_bootstrap(boot)
            hist_boot.write_image(
                f"fig/quantile{boot.k}/{data_prep.protocol}_{data_prep.sim_time}.png",
                scale=5,
            )
            scat_moving_average = data_vis.plot_moving_average(boot)
            scat_moving_average.write_image(
                f"fig/quantile{boot.k}/{data_prep.protocol}_{data_prep.sim_time}.png",
                scale=5,
            )
