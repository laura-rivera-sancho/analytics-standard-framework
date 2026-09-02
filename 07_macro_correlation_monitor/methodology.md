# Methodology

## 1. Frame the decision

The monitor answers when a relationship has materially changed enough to justify deeper macro research. It does not answer what to buy or sell.

## 2. Enforce the source contract

Request five years of daily closes for the three declared symbols. Preserve symbol, venue description, unit, source, and retrieval timestamp. Reject empty responses and non-finite values.

## 3. Align observations

Deduplicate each series by date, sort ascending, and inner-join on common dates. Do not forward-fill across asset calendars because doing so can manufacture zero returns and distort correlation.

## 4. Transform consistently

- Gold and DXY: `log(value_t / value_t-1)`
- US10Y: `yield_t - yield_t-1` in percentage points
- Indexed comparison: `100 × value_t / value_base`

## 5. Estimate descriptive risk and association

Compute rolling Pearson correlations over prespecified 30-, 90-, and 252-day windows. Complement them with annualized volatility and drawdown where used in offline research. Correlations require the complete window and are not treated as independent hypothesis tests.

## 6. Explore regimes and lags carefully

Use independently observable context—policy periods, inflation surprises, or volatility states—to interpret changes. Lag scans are hypothesis-generating and require multiplicity controls or out-of-sample validation before stronger claims.

## 7. Publish with operational controls

The site displays live/reference status, latest common date, exact symbols, source, and retrieval time. A deterministic reference dataset prevents a blank demo but is always labeled. The live endpoint revalidates hourly.

## 8. Emit reusable market context

Translate prespecified correlation and directional states into transparent labels such as relationship regime, dollar pressure, yield pressure, and research priority. These labels must be reproducible from documented rules and must not be described as news sentiment or an LLM conclusion.

## 9. Enrich in separate governed layers

A future LLM layer may add cited macro releases, approved news, thesis/counter-thesis, and uncertainty. A future agentic layer may coordinate research and prepare a constrained paper-trade proposal. Generated narrative remains separate from observed metrics, and every paper execution requires recorded human approval.

## 10. Communicate the boundary

Every view states that correlation does not establish causation and the monitor is not investment advice, a forecast, or an automated trading signal.
