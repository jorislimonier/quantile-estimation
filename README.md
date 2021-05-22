# Quantile Estimation

Working with real-world data to estimate confidence intervals of quantiles, using Bootstrap.

## Bootstrap

We use the Bootstrap method to estimate the confidence we have when computing "high quantiles", which represent (highly) unlikely occurences within the data. The quantiles are defined as follows:

<p style="
    text-align: center; 
    margin-top:1cm;
    ">
    <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\large&space;q_n&space;=&space;1&space;-&space;10^{-n}&space;=&space;0.\underbrace{999\ldots}_{n&space;\text{&space;nines}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bg_white&space;\large&space;q_n&space;=&space;1&space;-&space;10^{-n}&space;=&space;0.\underbrace{999\ldots}_{n&space;\text{&space;nines}}" title="\large q_n = 1 - 10^{-n} = 0.\underbrace{999\ldots}_{n \text{ nines}}" /></a>
</p>

More details can be found in the [**full report**](https://github.com/jorislimonier/quantile-estimation/blob/main/report/main.pdf).