# Quantile Estimation

Working with real-world data to estimate confidence intervals of quantiles, using Bootstrap.

## Bootstrap

We use the Bootstrap method to estimate the confidence we have when computing "high quantiles", which represent (highly) unlikely occurences within the data. The quantiles are defined as follows:

$$q_n = 1 - 10^{-n} = 0.\underbrace{999\ldots}_{n \text{ times}}$$

More details can be found in the [**full report**](https://github.com/jorislimonier/quantile-estimation/blob/main/report/main.pdf).