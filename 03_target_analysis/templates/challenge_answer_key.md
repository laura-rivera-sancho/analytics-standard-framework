# Target Analysis Challenge Answer Key

This key provides one defensible solution. Alternative recommendations are acceptable when assumptions, safeguards, and tradeoffs are explicit.

## Reference workflow

1. Preserve the raw quality report before cleaning.
2. Deduplicate merchant IDs, normalize country, label missing industry as `Unknown`, and quarantine impossible volume or tenure.
3. Apply all seven eligibility gates and reconcile 25,805 eligible merchants.
4. Score only eligible merchants using the documented need, value, and fit points.
5. Rank by score, monthly volume, and merchant ID.
6. Compare 3,000, 6,000, and 9,000-contact scenarios.
7. Review selection rates by country and industry without causal claims.
8. Recommend 6,000 as a controlled first wave and retain a randomized holdout.

## Reference decision

Select all 2,573 High-priority merchants and the top 3,427 Medium-priority merchants. Under the stated illustrative assumptions, expect about 806 adopters and $386.8K in annualized contribution.

## Essential caveats

- The score is not a propensity or causal model.
- Adoption and contribution assumptions are not observed outcomes.
- Geography and industry are monitoring dimensions, not score inputs.
- Activation requires compliance approval, a fresh suppression pass, list expiry, and minimal-data export.
- Measure incremental adoption with a randomized holdout before scaling.
