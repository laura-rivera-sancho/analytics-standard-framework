# A/B Test Data Validation Checklist

Use this checklist before statistical inference.

## Schema and completeness
- [ ] Required columns are present
- [ ] Data types are correct
- [ ] Critical fields are populated
- [ ] Date range matches the experiment window

## Experimental unit
- [ ] Unit of randomization is clearly defined
- [ ] Duplicate units are identified and resolved
- [ ] No unit appears in both Control and Treatment

## Assignment integrity
- [ ] Only valid experiment-group labels are present
- [ ] Missing assignments are quantified
- [ ] Allocation ratio is close to the planned ratio
- [ ] Sample-ratio mismatch test is reviewed
- [ ] Treatment exposure is consistent with assignment

## Metric validation
- [ ] Binary KPIs contain only valid values
- [ ] Continuous KPIs have plausible ranges
- [ ] Metric definitions match the experiment brief
- [ ] Outliers are inspected and documented
- [ ] Missing outcome data are quantified by group

## Group comparability
- [ ] Key pre-treatment characteristics are balanced
- [ ] Country/market mix is reviewed
- [ ] Device/channel mix is reviewed
- [ ] Customer segment mix is reviewed
- [ ] Major baseline KPIs are reviewed where available

## External and operational factors
- [ ] Concurrent campaigns are documented
- [ ] Concurrent product releases are documented
- [ ] Outages/incidents are documented
- [ ] Seasonality/calendar effects are considered
- [ ] Policy or risk-rule changes are documented

## Analytical population
- [ ] Inclusion/exclusion rules are applied consistently
- [ ] Exclusion counts and reasons are documented
- [ ] Final Control and Treatment counts are reported
- [ ] Cleaning steps are reproducible

## Go/no-go for inference
Proceed with causal interpretation only when experiment assignment, exposure, and measurement are sufficiently trustworthy. If a material integrity issue exists, stop and investigate before interpreting treatment effects.
