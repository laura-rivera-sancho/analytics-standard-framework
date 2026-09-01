# Macro Correlation Fundamentals

This interview-preparation reference explains the concepts behind the A8 monitor and the judgment required to use them responsibly.

## Core concepts

**Correlation** measures linear co-movement between two variables and ranges from `-1` to `+1`. A value near `+1` indicates strong positive linear association; a value near `-1` indicates strong inverse association; a value near zero indicates little linear association. It does not establish direction, mechanism, or causality.

**Returns versus levels.** Correlating non-stationary price levels can create misleading relationships driven by shared trends. The monitor uses daily log returns for gold and DXY. For the 10-year yield it uses daily percentage-point changes because a yield is already a rate, not an investable price.

**Rolling correlation** recomputes correlation over a trailing window. A 30-day window reacts quickly but is noisy; 90 days balances responsiveness and stability; 252 trading days approximates one year and is slower to reveal regime changes.

**Regime** describes a period with a relatively coherent market environment—for example inflation concern, disinflation, risk-off liquidity demand, or changing monetary-policy expectations. Regimes should be interpreted with independently observed context, not reverse-engineered from a chart alone.

**Volatility** measures return dispersion. Annualized daily volatility is commonly estimated as the daily standard deviation multiplied by the square root of 252.

**Drawdown** is the decline from a running peak. Maximum drawdown is path-dependent and complements volatility by showing the deepest observed loss from a prior high.

**Lag exploration** compares one series with earlier or later observations of another. It can generate research hypotheses, but testing many lags creates false-discovery risk and does not prove lead–lag causality.

## Why these assets may relate

- Gold is priced in U.S. dollars, so a stronger dollar can make it more expensive in other currencies; this can contribute to an inverse gold–DXY relationship.
- Higher nominal yields can raise the opportunity cost of holding a non-yielding asset, but inflation expectations and real—not merely nominal—yields often matter more.
- During stress, gold and the dollar can both attract demand, causing a historically inverse relationship to weaken or reverse.
- Treasury yields can rise because of growth, inflation, supply, or policy expectations. The same yield change can therefore carry different implications across regimes.

These are mechanisms to investigate, not universal laws.

## Pearson correlation formula

For paired observations `x` and `y`:

`r = covariance(x, y) / (standard_deviation(x) × standard_deviation(y))`

The statistic is sensitive to outliers, captures only linear association, and can be unstable with small samples.

## Essential interpretation rules

1. Validate timestamps, units, missing values, duplicates, and market calendars before calculating anything.
2. Use economically coherent transformations before correlation.
3. Compare multiple prespecified windows rather than selecting the most dramatic one.
4. Inspect the time path; a single full-period number can hide sign changes.
5. Report source, symbol, refresh time, and whether fallback data are displayed.
6. Treat regime labels and lag tests as exploratory unless independently specified and validated.
7. Never translate correlation alone into a trade recommendation.

## Common interview questions

**Why not correlate gold price and DXY level directly?**  
Trending levels can create spurious correlation. Returns are usually closer to stationary and describe comparable daily movements.

**Why use yield changes rather than yield returns?**  
A yield is a rate. Percentage-point or basis-point changes are interpretable and avoid treating a quoted yield like an asset price.

**What does a 90-day correlation of `-0.60` mean?**  
Over those observations, larger gold returns tended to coincide with larger DXY moves in the opposite direction. It does not mean DXY caused 60% of gold's movement.

**How would you test robustness?**  
Compare Pearson with Spearman correlation, winsorized and untrimmed samples, alternate windows, subsamples, event exclusions, and independently defined regimes. Report whether the conclusion changes.

**What is the danger of overlapping rolling windows?**  
Adjacent estimates share most observations, so the chart is highly autocorrelated. It is useful for monitoring but should not be interpreted as a sequence of independent tests.

**How would you improve the model?**  
Add real yields, inflation expectations, volatility, liquidity proxies, and event annotations; predefine hypotheses; use time-series methods; and evaluate out of sample. Complexity should follow a clear decision need.

**How do you communicate uncertainty to a stakeholder?**  
State the current association, show how it changes by window and regime, explain plausible mechanisms and alternatives, and recommend the next research step rather than a causal conclusion.

## Portfolio talking point

“I built the monitor to make unstable relationships visible. The strongest analytical choice was not the chart—it was defining comparable transformations, labeling the exact instruments and freshness, and keeping the output inside a research boundary.”
