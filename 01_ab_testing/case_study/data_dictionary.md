# NovaPay Data Dictionary

All fields are synthetic.

| Field | Type | Description | Analytical use |
|---|---|---|---|
| `customer_id` | string | Synthetic unique customer identifier | Randomization unit; duplicate check |
| `experiment_group` | string | `Control` or `Treatment` | Main treatment assignment |
| `experiment_date` | date | Date of experiment exposure | Duration, trend, weekday checks |
| `country` | string | Synthetic market (`US`, `MX`, `CR`, `BR`) | Balance and segment analysis |
| `device_type` | string | `Mobile` or `Desktop` | Pre-specified segment; heterogeneous effect analysis |
| `customer_tenure` | string | `New` or `Existing` | Balance and segment analysis |
| `transaction_value_usd` | float | Synthetic transaction amount in USD | Behavioral/segment analysis; intentionally right-skewed |
| `checkout_completed` | integer | `1` completed, `0` not completed | **Primary KPI** |
| `checkout_time_seconds` | float | Time spent in checkout journey | Secondary KPI; continuous and right-skewed |
| `payment_declined` | integer | `1` decline, `0` otherwise | Guardrail KPI |
| `support_contact` | integer | `1` customer contacted support, `0` otherwise | Guardrail KPI |
| `fraud_flag` | integer | `1` synthetic fraud/risk flag, `0` otherwise | Guardrail KPI |

## Expected data-quality checks

Before analysis:

1. Verify expected columns and data types.
2. Confirm one row per experimental unit after cleaning.
3. Check missing `experiment_group` values.
4. Standardize country labels/casing.
5. Verify `Control`/`Treatment` are the only valid assignments.
6. Check that binary outcomes contain only `0`/`1`.
7. Check experiment date range.
8. Review impossible/implausible continuous values.
9. Confirm a customer does not appear in both groups.
10. Report the final analytical population after exclusions.

## Synthetic raw-data imperfections

The generator deliberately introduces examples of:
- duplicate customer records
- missing experiment assignments
- inconsistent country casing

The committed sample file also contains examples of these issues so the validation workflow can be practiced without generating the full dataset.

These issues are deliberate and should be identified and resolved before statistical inference.
