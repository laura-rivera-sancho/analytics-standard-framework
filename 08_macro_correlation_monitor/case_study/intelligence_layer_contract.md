# Market Intelligence Layer Contract

This contract defines how A8 can support later LLM and Agentic AI projects without blending observed market data, deterministic interpretation, generated narrative, and executable actions.

## Layer boundaries

| Layer | Responsibility | May produce | Must not claim |
|---|---|---|---|
| Market data | Retrieve and validate exact instruments | values, dates, source, freshness, availability | that a proxy is the underlying economic concept |
| Analytics | Apply declared transformations and methods | returns, yield changes, volatility, drawdown, rolling correlation | causation, a forecast, or a trade signal |
| Rules-based context | Map prespecified metric states to transparent labels | relationship regime, directional pressure, research priority | human sentiment, news sentiment, or a complete market thesis |
| Cited LLM research | Retrieve approved releases and news and synthesize evidence | cited facts, thesis, counter-thesis, catalysts, risks, uncertainty | unsupported facts, uncited causal claims, or autonomous advice |
| Agentic workflow | Coordinate bounded research and risk checks | traceable research package and constrained paper-trade proposal | permission to execute without recorded human approval |

## Proposed context payload

```json
{
  "as_of": "ISO-8601 timestamp",
  "data_status": "live | reference | stale | unavailable",
  "instruments": ["GC=F", "DX-Y.NYB", "^TNX"],
  "latest_common_date": "YYYY-MM-DD",
  "metrics": {
    "gold_dxy_corr_30d": 0.0,
    "gold_dxy_corr_90d": 0.0,
    "gold_dxy_corr_252d": 0.0,
    "gold_us10y_corr_90d": 0.0
  },
  "rules_context": {
    "relationship_regime": "strong_inverse | moderate | positive",
    "dollar_pressure": "headwind | tailwind | mixed",
    "yield_pressure": "headwind | tailwind | mixed",
    "research_priority": "routine | elevated"
  },
  "method_version": "a8-context-v1"
}
```

Every label must remain reproducible from versioned rules. A future LLM output belongs in a separate object containing source citations, retrieval timestamps, model/version metadata, and evaluation results.

## News and sentiment requirements

Before adding headlines or sentiment:

1. approve publishers, macro-release sources, licensing, and refresh expectations
2. retain headline URL, publisher, publication time, retrieval time, and asset/topic tags
3. distinguish publisher text from model-generated summary
4. define sentiment target precisely—for example risk appetite, gold-specific tone, or policy stance
5. evaluate classification accuracy, citation coverage, contradictory evidence, stale news, and prompt injection
6. provide neutral/unresolved states instead of forcing positive or negative labels
7. prevent sentiment or LLM narrative from directly authorizing an order

## Agent consumption rules

- reject unavailable, reference, or stale data when a live decision requires current inputs
- preserve the complete context payload and method version in the research trace
- allow the agent to request deeper research when signals conflict
- require deterministic risk checks and mandatory human approval, recorded before paper execution
- prohibit live trading
