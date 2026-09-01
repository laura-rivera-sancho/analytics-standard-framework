# Harbor & Pine Experiment Data Dictionary

## Dataset purpose and grain

The experiment-assignment dataset contains one intended row per customer assignment within an experiment. It combines pre-treatment eligibility attributes, frozen assignment, delivery diagnostics, fixed-window outcomes, business-value components, and guardrails for a synthetic portfolio case.

The raw generated dataset deliberately contains invalid and duplicate rows. The validated analytical population must restore the declared grain and reconcile every exclusion.

## Experiment identifiers

| Field | Type | Definition | Validation rule |
|---|---|---|---|
| `assignment_id` | string | Unique assignment record identifier | Required and unique after quarantine |
| `customer_id` | string | Synthetic customer identifier | Required; unique within `experiment_id` |
| `experiment_id` | string | Stable experiment identifier | One of the two declared experiments |
| `experiment_type` | category | `split_test` or `factorial` | Must agree with `experiment_id` |
| `assigned_at` | timestamp | Frozen randomization timestamp in UTC | Required; before exposure and outcomes |
| `extract_at` | timestamp | UTC cutoff of the analytical extract | Required and not earlier than assignment |
| `outcome_matured_at` | timestamp | End of the customer's 14-day outcome window | Equals assignment plus 14 days and must not exceed extract time |

## Pre-treatment customer fields

| Field | Type | Definition | Validation rule |
|---|---|---|---|
| `lifecycle_segment` | category | A6 lifecycle group at assignment | `At Risk` or `Needs Attention`; never derived from post-treatment behavior |
| `value_band` | category | Prespecified trailing-value stratum | `High`, `Medium`, or `Standard` |
| `email_consent` | boolean | Email eligibility frozen before assignment | Required `True` for both experiments |
| `sms_consent` | boolean | SMS eligibility frozen before assignment | Required `True` for the factorial experiment |

The factorial population is dual-consented because channel plan is randomized. This design limitation must remain visible when interpreting generalizability.

## Assignment and factor fields

| Field | Type | Definition | Validation rule |
|---|---|---|---|
| `arm` | category | Complete assigned condition | Must belong to the arm catalog for the experiment |
| `message_framing` | category | Message factor | Split: `current_reminder` or `benefit_led`; factorial active: `benefit_led` or `urgency_led`; holdout: `none` |
| `offer` | category | Offer factor | Factorial active: `free_shipping` or `discount_10`; otherwise `none` |
| `channel_plan` | category | Assigned contact plan | `email_only`, `email_plus_sms`, or `none` for holdout |
| `is_holdout` | boolean | No-contact assignment indicator | True only for factorial holdout |
| `planned_allocation` | float | Expected probability of the assigned arm | Positive and sums to one across declared arms within an experiment |

The factorial active-arm name is deterministically composed from message, offer, and channel levels. This makes invalid combinations inspectable.

## Delivery and exposure diagnostics

| Field | Type | Definition | Validation rule |
|---|---|---|---|
| `delivered_email` | integer | Email delivery indicator | Binary; zero for holdout |
| `delivered_sms` | integer | SMS delivery indicator | Binary; allowed only for `email_plus_sms` |
| `exposed_at` | timestamp | First delivered treatment timestamp | Null for holdout; never before assignment |

Delivery fields describe implementation. They do not determine inclusion in the intention-to-treat population.

## Outcomes and value components

| Field | Type | Definition | Validation rule |
|---|---|---|---|
| `converted_14d` | integer | At least one qualifying completed purchase within 14 days | Binary and consistent with conversion timestamp |
| `conversion_timestamp` | timestamp | First qualifying conversion in the fixed window | Required only when converted; between assignment and outcome maturity |
| `recognized_revenue_14d` | decimal | Recognized revenue from qualifying purchases | Nonnegative; zero when not converted |
| `product_cost_14d` | decimal | Estimated product cost for qualifying purchases | Nonnegative and not greater than revenue |
| `discount_cost_14d` | decimal | Cost attributed to the assigned discount | Nonnegative; normally zero without `discount_10` |
| `shipping_subsidy_14d` | decimal | Shipping subsidy caused by the assigned offer | Nonnegative; normally zero without `free_shipping` |
| `messaging_cost` | decimal | Assigned email and SMS delivery cost | Nonnegative; zero for holdout |
| `refunded_30d` | integer | Qualifying purchase refunded inside the observation rule | Binary and cannot equal one without conversion |

Contribution margin is derived from the stored components. The eventual analysis will report both observed value and sensitivity to approved cost assumptions.

## Guardrail fields

| Field | Type | Definition | Validation rule |
|---|---|---|---|
| `unsubscribed_14d` | integer | Email unsubscribe inside 14 days | Binary; zero for holdout in the reference generator |
| `complained_14d` | integer | Campaign complaint inside 14 days | Binary; zero for holdout in the reference generator |
| `sms_opt_out_14d` | integer | SMS opt-out inside 14 days | Binary; allowed only for email-plus-SMS assignment |

Consent-policy violations are detected by comparing assignment factors with frozen consent fields. They are not represented as a favorable or unfavorable customer outcome.

## Experiment and arm catalog

### Split test

| Arm | Message | Offer | Channel | Planned share |
|---|---|---|---|---:|
| `control_current_reminder` | Current reminder | None | Email only | 0.50 |
| `treatment_lifecycle_message` | Benefit-led | None | Email only | 0.50 |

### Factorial test

The active catalog contains all combinations of:

- message: benefit-led, urgency-led
- offer: free shipping, 10% discount
- channel: email only, email plus SMS

Each of the eight active cells and the no-contact holdout has a planned share of `1/9` in the reference design.

## Deliberate raw-data defects

The default generated dataset contains:

- 20 duplicated assignment records
- 12 exposures before assignment
- 10 conversions before assignment
- 10 SMS-consent violations
- 10 missing lifecycle segments
- 8 invalid arm labels
- 8 immature 14-day outcome windows

Defect categories are selected from distinct source rows before duplicate rows are appended. Validation reports may identify an invalid row under more than one logical rule when one inconsistency necessarily implies another; the quarantine population is deduplicated by row identity.

## Privacy and use boundary

Every identifier and outcome is synthetic. The schema intentionally excludes names, email addresses, phone numbers, and message content. A production extract would require access controls, retention rules, purpose limitation, auditable consent history, and deletion handling.
