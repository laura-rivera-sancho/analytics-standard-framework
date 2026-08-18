# FinFlow Challenge Answer Key — Expected Analytical Narrative

This answer key summarizes the expected interpretation for the FinFlow Pre/Post challenge. Exact numeric values may vary slightly if the synthetic generator is modified, but the analytical storyline should remain consistent.

## 1. Business framing

FinFlow launched an automated transaction-verification workflow to all eligible traffic on **2026-04-01**. Because the rollout was 100%, there is no randomized Control group. The analysis should determine whether the workflow appears to reduce transaction-processing friction and manual-review demand while maintaining payment quality, fraud controls, and support outcomes.

The key business decision is whether to continue scaling the workflow, continue with monitoring, iterate, validate further, or roll back.

## 2. Data-quality findings

The raw data intentionally contains:

- duplicate transaction IDs
- inconsistent country casing
- missing risk tier, device type, and verification duration values
- negative and implausibly high verification durations
- corrupted raw intervention flags

A strong solution should:

- remove duplicate transaction IDs
- standardize country casing
- derive `period`, `post_flag`, `days_from_launch`, `ramp_flag`, and `campaign_flag` from `transaction_date`
- keep rows for rate KPIs when possible
- exclude impossible duration values only from duration-based analysis
- document the final analytical population

## 3. Simple Pre/Post results

Expected pattern:

- verification completion rate improves after launch
- manual review rate declines materially
- verification time declines materially
- support contact rate improves or remains favorable
- payment decline rate remains broadly stable
- fraud-confirmed rate is rare and noisy, requiring careful event-count interpretation

A strong answer should not conclude causality from the simple Pre/Post result alone.

## 4. Ramp and stable Post

The first seven days after launch are a stabilization period. The synthetic data intentionally makes ramp-period performance weaker than the later stable Post period.

Expected interpretation:

- full Post shows improvement versus Pre
- stable Post usually shows a stronger or cleaner improvement
- ramp should be reported as an implementation reality, not silently removed
- the recommendation should mention post-launch monitoring and ramp management

## 5. Trend and seasonality

The data includes:

- a mild baseline improvement trend before launch
- day-of-week seasonality
- a temporary campaign in May that increases volume and shifts traffic mix

Expected interpretation:

- the KPI was not flat before launch, so simple Pre/Post overstates certainty
- daily trend visualization should show whether the launch aligns with a visible shift
- campaign timing should be reviewed before attributing all Post changes to automation

## 6. Traffic-mix diagnostics

Post-period traffic intentionally shifts modestly:

- more mobile traffic
- more new customers
- slightly different country mix
- slightly more high-risk traffic
- campaign period increases new-customer share

Expected interpretation:

Traffic mix changes could confound simple Pre/Post results. The analysis should compare distributions and use adjusted modeling or segmentation to assess whether the primary KPI improvement is still credible after accounting for mix.

## 7. Verification time and manual review

Expected pattern:

- average verification time declines
- median verification time declines
- duration is right-skewed, so mean and median should both be presented
- manual review rate declines materially, supporting the expected mechanism of the automation

A strong answer should mention that Welch's t-test and a non-parametric sensitivity check are both useful because duration is skewed.

## 8. Guardrails

Expected pattern:

- support contact rate should improve or remain favorable
- payment decline rate should be interpreted as a guardrail rather than a pure success metric
- fraud-confirmed rate is very low-frequency

A strong answer should include event counts for fraud and avoid making a strong claim from small absolute changes.

## 9. Interrupted Time Series

The ITS model should be used to move beyond two-bucket Pre/Post comparison.

Expected interpretation:

- `time_index` captures baseline trend
- `post` estimates the immediate level shift at launch
- `time_after_launch` estimates post-launch slope change
- `ramp` captures temporary first-week stabilization effect
- `campaign` controls for the temporary marketing period
- adjusted covariates help account for traffic-mix shifts

A strong answer should state that ITS improves causal confidence compared with simple Pre/Post, but it is still observational and not as strong as randomized experimentation.

## 10. Segment analysis

Expected pattern:

- improvement should be visible across several segments
- some segments may benefit more than others
- higher-risk segments may have weaker performance and should be monitored

A strong answer treats segment findings as diagnostic unless the segments were pre-specified.

## 11. Business impact

A strong answer should estimate impact using a transparent formula such as:

`Annual eligible transaction volume × selected absolute lift = estimated incremental completed verifications`

The selected lift should be justified. For example:

- simple Pre/Post lift may be too optimistic
- stable Post lift may be useful for operational steady state
- adjusted ITS lift may be better for causal interpretation

The estimate should be presented as approximate and assumption-based, not as false precision.

## 12. Causal-confidence rating

Expected rating: **Moderate**, assuming the adjusted ITS supports an improvement and guardrails are acceptable.

Why not High?

- no randomized Control group
- baseline trend exists
- traffic mix shifts after launch
- campaign overlaps with the Post period

Why not Low?

- timing aligns with launch
- improvement is visible after ramp
- mechanism metrics improve, especially manual review and verification time
- adjusted ITS helps account for trend, ramp, campaign, weekday effects, and mix covariates

## 13. Recommended decision

Suggested recommendation:

> Continue with monitoring, or continue/scale with guardrail monitoring, depending on the exact model output and guardrail comfort level.

Recommended next steps:

- continue monitoring payment decline, fraud-confirmed rate, support contacts, and verification completion
- report stable Post separately from ramp
- monitor higher-risk segments
- validate whether campaign-period behavior differs from normal traffic
- consider a future phased rollout or holdout if another workflow change is planned

## Executive summary pattern

A strong stakeholder-ready summary should sound like this:

> Verification performance improved after the automated workflow launched, and the improvement remains directionally consistent after accounting for trend, ramp, campaign timing, weekday patterns, and traffic-mix changes. Manual review and verification time improved, supporting the expected mechanism. Guardrails did not show clear material deterioration, although rare fraud outcomes should continue to be monitored using event counts. Because the design is observational, causal confidence is moderate rather than high. Recommendation: continue the workflow with defined guardrail monitoring and segment-level follow-up.
