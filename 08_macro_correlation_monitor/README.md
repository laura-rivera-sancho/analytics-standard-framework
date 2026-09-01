# Macro Correlation Monitor

> **Status: Complete.** A live, decision-oriented research dashboard for exploring how gold, the U.S. 10-year Treasury yield, and the U.S. Dollar Index move across market regimes.

**Portfolio shortcut:** [Open the private live dashboard](https://macro-correlation-monitor.nachilu10.chatgpt.site)

## Business question

How stable are gold's relationships with the dollar and the U.S. 10-year yield, and when do changes in those relationships warrant deeper macro research?

This monitor is designed for analysts, research leads, and downstream research systems. It supports disciplined exploration and produces a governed market-context foundation that can later be enriched by a cited LLM research layer and consumed by a human-approved Agentic AI workflow. It does not generate forecasts, investment recommendations, or trading signals.

## What this module demonstrates

- live API ingestion with source, symbol, and freshness metadata
- an explicit source contract for COMEX gold futures (`GC=F`), the ICE U.S. Dollar Index (`DX-Y.NYB`), and the Cboe 10-year yield index (`^TNX`)
- inner-join alignment on common trading dates
- log returns for price/index series and percentage-point changes for yields
- 30-, 90-, and 252-trading-day rolling Pearson correlations
- common-baseline indexed performance and regime-aware interpretation
- deterministic fallback data when the upstream service is unavailable
- a responsive Sites dashboard with accessible controls and honest analytical boundaries
- rules-based relationship context that separates observed market state from future LLM interpretation
- a documented context contract for later cited-news, LLM, and human-governed agent integrations

## Review path

| Resource | Purpose |
|---|---|
| [Live dashboard source](site) | Interactive dashboard, live API route, design system, and deployment configuration |
| [Macro fundamentals](macro_correlation_fundamentals.md) | Key concepts, transformations, interpretation guidance, limitations, and practical analytical questions |
| [Methodology](methodology.md) | Reusable source-to-decision analytical workflow |
| [Source contract](case_study/data_source_contract.md) | Instruments, fields, transformations, freshness, limitations, and fallback behavior |
| [Intelligence-layer contract](case_study/intelligence_layer_contract.md) | Boundary between observed metrics, rules-based context, cited LLM analysis, and agent actions |
| [Stakeholder readout](reports/stakeholder_readout.md) | Executive interpretation and safe next actions |
| [Analytical utilities](src/market_analysis.py) | Tested alignment, transformation, rolling-correlation, volatility, and drawdown logic |
| [Automated tests](../tests/test_macro_correlation_monitor.py) | Known-result tests and data-integrity controls |

## Run the analytical checks

From the repository root:

```bash
pytest tests/test_macro_correlation_monitor.py
```

## Run the live site locally

```bash
cd 08_macro_correlation_monitor/site
pnpm install
pnpm dev
```

The site attempts to refresh the three public market series on load. If the upstream service is blocked or unavailable, the interface displays a clearly labeled deterministic reference dataset rather than silently presenting stale values as live.

## Role in the broader portfolio

A8 is the **market-context layer**, not the final research product:

1. **Analytics (A8):** acquires and validates market data, calculates transformations and rolling relationships, and emits transparent rules-based context.
2. **LLM system:** will retrieve approved macro releases and news, cite every external claim, compare supporting and conflicting evidence, and explain uncertainty.
3. **Agentic AI system:** may orchestrate research and prepare a paper-trade proposal, but must preserve freshness checks, traceability, risk constraints, and mandatory human approval before any paper execution.

News sentiment and narrative generation are intentionally not presented as complete in A8. Their sources, labeling taxonomy, citation requirements, evaluation set, and failure behavior will be agreed during the LLM/Agentic design phase.

## Decision boundary

Correlation is symmetric association, not causation. Results depend on measurement choice, sampling frequency, rolling-window length, overlapping observations, outliers, and market regime. This case is educational research and not investment advice.
