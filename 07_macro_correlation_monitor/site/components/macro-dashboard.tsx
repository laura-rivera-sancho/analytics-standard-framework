'use client';

import { useEffect, useMemo, useState } from 'react';
import {
  Activity,
  ArrowDownRight,
  ArrowUpRight,
  BookOpen,
  Clock3,
  Database,
  Info,
  RefreshCw,
  ShieldCheck,
} from 'lucide-react';
import {
  CartesianGrid,
  Line,
  LineChart,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

type Point = { date: string; value: number };
type Instrument = {
  key: 'gold' | 'dxy' | 'us10y';
  symbol: string;
  label: string;
  unit: string;
  points: Point[];
};
type ApiResponse = {
  status: 'live';
  provider: string;
  fetchedAt: string;
  instruments: Instrument[];
};
type Joined = { date: string; gold: number; dxy: number; us10y: number };
type Window = 30 | 90 | 252;

const COLORS = { gold: '#c99324', dxy: '#426d8f', us10y: '#9d5548' };

function syntheticData(): Instrument[] {
  const end = new Date('2026-08-29T00:00:00Z');
  const rows: Record<'gold' | 'dxy' | 'us10y', Point[]> = {
    gold: [],
    dxy: [],
    us10y: [],
  };
  let gold = 2040,
    dxy = 104,
    us10y = 4.18;
  for (let i = 720; i >= 0; i -= 1) {
    const date = new Date(end);
    date.setUTCDate(end.getUTCDate() - i);
    if ([0, 6].includes(date.getUTCDay())) continue;
    const t = 720 - i;
    const shock = Math.sin(t * 0.17) * 0.004 + Math.cos(t * 0.041) * 0.003;
    dxy *= 1 + Math.sin(t * 0.063) * 0.0012 + Math.cos(t * 0.021) * 0.0006;
    us10y = Math.max(
      2.5,
      us10y + Math.sin(t * 0.052) * 0.009 + Math.cos(t * 0.017) * 0.004,
    );
    gold *=
      1 +
      0.00045 +
      shock -
      (dxy / 104 - 1) * 0.00015 -
      (us10y - 4.18) * 0.00012;
    const iso = date.toISOString().slice(0, 10);
    rows.gold.push({ date: iso, value: gold });
    rows.dxy.push({ date: iso, value: dxy });
    rows.us10y.push({ date: iso, value: us10y });
  }
  return [
    {
      key: 'gold',
      symbol: 'GC=F',
      label: 'COMEX Gold Futures',
      unit: 'USD/oz',
      points: rows.gold,
    },
    {
      key: 'dxy',
      symbol: 'DX-Y.NYB',
      label: 'U.S. Dollar Index',
      unit: 'index',
      points: rows.dxy,
    },
    {
      key: 'us10y',
      symbol: '^TNX',
      label: 'U.S. 10Y Yield',
      unit: '%',
      points: rows.us10y,
    },
  ];
}

function join(instruments: Instrument[]): Joined[] {
  const maps = Object.fromEntries(
    instruments.map((item) => [
      item.key,
      new Map(item.points.map((p) => [p.date, p.value])),
    ]),
  );
  return instruments[0].points.flatMap((p) => {
    const dxy = maps.dxy.get(p.date),
      us10y = maps.us10y.get(p.date);
    return dxy !== undefined && us10y !== undefined
      ? [{ date: p.date, gold: p.value, dxy, us10y }]
      : [];
  });
}

function returns(rows: Joined[]) {
  return rows
    .slice(1)
    .map((row, i) => ({
      date: row.date,
      gold: Math.log(row.gold / rows[i].gold),
      dxy: Math.log(row.dxy / rows[i].dxy),
      us10y: row.us10y - rows[i].us10y,
    }));
}

function corr(x: number[], y: number[]) {
  if (x.length < 3) return 0;
  const mx = x.reduce((a, b) => a + b, 0) / x.length,
    my = y.reduce((a, b) => a + b, 0) / y.length;
  const numerator = x.reduce(
    (sum, value, i) => sum + (value - mx) * (y[i] - my),
    0,
  );
  const dx = Math.sqrt(x.reduce((sum, value) => sum + (value - mx) ** 2, 0));
  const dy = Math.sqrt(y.reduce((sum, value) => sum + (value - my) ** 2, 0));
  return dx && dy ? numerator / (dx * dy) : 0;
}

function rolling(rows: ReturnType<typeof returns>, window: Window) {
  return rows.slice(window - 1).map((row, index) => {
    const sample = rows.slice(index, index + window);
    return {
      date: row.date,
      goldDxy: corr(
        sample.map((r) => r.gold),
        sample.map((r) => r.dxy),
      ),
      goldYield: corr(
        sample.map((r) => r.gold),
        sample.map((r) => r.us10y),
      ),
    };
  });
}

function formatValue(key: Instrument['key'], value: number) {
  if (key === 'gold')
    return `$${value.toLocaleString(undefined, { maximumFractionDigits: 0 })}`;
  if (key === 'us10y') return `${value.toFixed(2)}%`;
  return value.toFixed(2);
}

function Signal({ value }: { value: number }) {
  const positive = value >= 0;
  return (
    <span
      className={`inline-flex items-center gap-1 text-xs font-medium ${positive ? 'text-emerald-700' : 'text-rose-700'}`}
    >
      {positive ? <ArrowUpRight size={14} /> : <ArrowDownRight size={14} />}
      {positive ? '+' : ''}
      {value.toFixed(2)}%
    </span>
  );
}

export function MacroDashboard() {
  const [instruments, setInstruments] = useState<Instrument[]>(syntheticData);
  const [status, setStatus] = useState<'loading' | 'live' | 'reference'>(
    'loading',
  );
  const [fetchedAt, setFetchedAt] = useState(
    'Reference snapshot · 29 Aug 2026',
  );
  const [window, setWindow] = useState<Window>(90);

  useEffect(() => {
    fetch('/api/market-data')
      .then((response) => {
        if (!response.ok) throw new Error('Unavailable');
        return response.json() as Promise<ApiResponse>;
      })
      .then((data) => {
        setInstruments(data.instruments);
        setFetchedAt(new Date(data.fetchedAt).toLocaleString());
        setStatus('live');
      })
      .catch(() => setStatus('reference'));
  }, []);

  const joined = useMemo(() => join(instruments), [instruments]);
  const daily = useMemo(() => returns(joined), [joined]);
  const corrRows = useMemo(
    () => rolling(daily, window).slice(-420),
    [daily, window],
  );
  const indexed = useMemo(() => {
    const rows = joined.slice(-504);
    if (!rows.length) return [];
    const base = rows[0];
    return rows.map((r) => ({
      date: r.date,
      gold: (r.gold / base.gold) * 100,
      dxy: (r.dxy / base.dxy) * 100,
      us10y: (r.us10y / base.us10y) * 100,
    }));
  }, [joined]);
  const latest = joined.at(-1),
    previous = joined.at(-2);
  const latestCorr = corrRows.at(-1) ?? { goldDxy: 0, goldYield: 0 };
  const context = useMemo(() => {
    const c30 = rolling(daily, 30).at(-1) ?? { goldDxy: 0, goldYield: 0 };
    const c90 = rolling(daily, 90).at(-1) ?? { goldDxy: 0, goldYield: 0 };
    const c252 = rolling(daily, 252).at(-1) ?? { goldDxy: 0, goldYield: 0 };
    const move = daily.at(-1) ?? { gold: 0, dxy: 0, us10y: 0 };
    const relationship =
      c90.goldDxy <= -0.5
        ? 'Strong inverse'
        : c90.goldDxy >= 0.5
          ? 'Strong positive'
          : 'Mixed / moderate';
    const dollarPressure =
      move.dxy > 0 && move.gold < 0
        ? 'Dollar headwind'
        : move.dxy < 0 && move.gold > 0
          ? 'Dollar tailwind'
          : 'Mixed dollar impulse';
    const yieldPressure =
      move.us10y > 0 && move.gold < 0
        ? 'Yield headwind'
        : move.us10y < 0 && move.gold > 0
          ? 'Yield tailwind'
          : 'Mixed yield impulse';
    const regimeShift =
      Math.abs(c30.goldDxy - c252.goldDxy) >= 0.35 ||
      Math.sign(c30.goldDxy) !== Math.sign(c252.goldDxy);
    return {
      c30,
      c90,
      c252,
      relationship,
      dollarPressure,
      yieldPressure,
      priority: regimeShift
        ? 'Elevated research priority'
        : 'Routine monitoring',
    };
  }, [daily]);

  return (
    <main className="min-h-screen">
      <header className="border-b border-[#cbc1af] bg-[#f8f4eb]/90 backdrop-blur">
        <div className="mx-auto flex max-w-[1480px] items-center justify-between px-5 py-4 sm:px-8">
          <a
            href="#top"
            className="flex items-center gap-3"
            aria-label="Macro monitor home"
          >
            <span className="grid h-9 w-9 place-items-center bg-[#14233d] text-[#e0b54f]">
              <Activity size={19} />
            </span>
            <span>
              <b className="block text-sm tracking-[0.14em]">MACRO SIGNALS</b>
              <small className="mono text-[10px] text-[#687482]">
                RESEARCH MONITOR / A8
              </small>
            </span>
          </a>
          <nav className="hidden items-center gap-7 text-sm text-[#566270] md:flex">
            <a href="#dashboard">Dashboard</a>
            <a href="#context">Context</a>
            <a href="#method">Method</a>
            <a
              href="https://github.com/laura-rivera-sancho/analytics-standard-framework/tree/main/07_macro_correlation_monitor"
              target="_blank"
              rel="noreferrer"
            >
              GitHub repository ↗
            </a>
          </nav>
        </div>
      </header>

      <section id="top" className="paper-grid border-b border-[#cbc1af]">
        <div className="mx-auto grid max-w-[1480px] gap-9 px-5 py-14 sm:px-8 lg:grid-cols-[1.35fr_.65fr] lg:py-20">
          <div>
            <p className="mono mb-5 text-xs font-medium tracking-[0.18em] text-[#9b6d13]">
              GOLD · US10Y · DXY
            </p>
            <h1 className="display max-w-4xl text-5xl leading-[1.02] tracking-[-0.04em] sm:text-6xl lg:text-7xl">
              When macro relationships shift, context matters.
            </h1>
            <p className="mt-6 max-w-2xl text-lg leading-8 text-[#53606e]">
              Explore how gold returns co-move with the U.S. Dollar Index and
              daily changes in the 10-year Treasury yield—then convert the
              observed state into transparent research context for later cited
              LLM and Agentic AI workflows.
            </p>
          </div>
          <div className="self-end border-l-2 border-[#c99324] pl-5">
            <p className="text-sm font-semibold">Current read</p>
            <p className="mt-2 text-2xl font-medium">
              {latestCorr.goldDxy < -0.35
                ? 'Dollar sensitivity is elevated'
                : latestCorr.goldDxy > 0.35
                  ? 'Gold and dollar are moving together'
                  : 'Dollar relationship is moderate'}
            </p>
            <p className="mt-3 text-sm leading-6 text-[#65717e]">
              The {window}-day gold–DXY correlation is{' '}
              <b>{latestCorr.goldDxy.toFixed(2)}</b>. Treat this as monitoring
              evidence, not a causal or trading signal.
            </p>
          </div>
        </div>
      </section>

      <section
        id="dashboard"
        className="mx-auto max-w-[1480px] px-5 py-10 sm:px-8"
      >
        <div className="mb-5 flex flex-wrap items-end justify-between gap-4">
          <div>
            <p className="mono text-[11px] tracking-[0.16em] text-[#7b6850]">
              MARKET SNAPSHOT
            </p>
            <h2 className="display mt-1 text-3xl">Cross-asset dashboard</h2>
          </div>
          <div className="flex items-center gap-2 border border-[#cec5b5] bg-[#fbf8f0] px-3 py-2 text-xs text-[#627080]">
            <span
              className={`h-2 w-2 rounded-full ${status === 'live' ? 'bg-emerald-500' : status === 'loading' ? 'bg-amber-500' : 'bg-slate-400'}`}
            />
            <span>
              {status === 'live'
                ? 'Live market feed'
                : status === 'loading'
                  ? 'Refreshing live feed'
                  : 'Reference data displayed'}
            </span>
            <Clock3 size={13} />
            <span className="hidden sm:inline">{fetchedAt}</span>
          </div>
        </div>

        <div className="grid gap-4 md:grid-cols-3">
          {instruments.map((item) => {
            const now = latest?.[item.key] ?? 0,
              prior = previous?.[item.key] ?? now;
            const change = prior ? (now / prior - 1) * 100 : 0;
            return (
              <article
                key={item.key}
                className="card-shadow border border-[#d5cbbb] bg-[#fbf8f0] p-5"
              >
                <div className="flex items-start justify-between">
                  <div>
                    <p className="mono text-[10px] tracking-[0.15em] text-[#71808d]">
                      {item.symbol}
                    </p>
                    <h3 className="mt-1 font-semibold">{item.label}</h3>
                  </div>
                  <span
                    className="h-2.5 w-2.5 rounded-full"
                    style={{ background: COLORS[item.key] }}
                  />
                </div>
                <div className="mt-7 flex items-end justify-between">
                  <strong className="display text-4xl font-normal">
                    {formatValue(item.key, now)}
                  </strong>
                  <Signal value={change} />
                </div>
                <p className="mt-3 text-xs text-[#78838d]">
                  Latest common trading date · {latest?.date ?? '—'}
                </p>
              </article>
            );
          })}
        </div>

        <article
          id="context"
          className="card-shadow mt-4 border border-[#d5cbbb] bg-[#fbf8f0] p-5 sm:p-7"
        >
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div>
              <p className="mono text-[10px] tracking-[0.15em] text-[#8a651c]">
                RULES-BASED MARKET CONTEXT
              </p>
              <h3 className="mt-1 text-xl font-semibold">
                A governed handoff—not generated sentiment
              </h3>
              <p className="mt-2 max-w-3xl text-sm leading-6 text-[#65717e]">
                These labels are reproduced from current price/yield moves and
                prespecified correlation thresholds. They create a structured
                input for future cited news analysis; they are not an LLM
                opinion, headline sentiment, or a trade signal.
              </p>
            </div>
            <span
              className={`mono border px-3 py-2 text-[10px] font-medium tracking-[0.1em] ${context.priority.startsWith('Elevated') ? 'border-amber-600/40 bg-amber-100 text-amber-900' : 'border-emerald-700/30 bg-emerald-50 text-emerald-800'}`}
            >
              {context.priority.toUpperCase()}
            </span>
          </div>
          <div className="mt-6 grid gap-px border border-[#d5cbbb] bg-[#d5cbbb] sm:grid-cols-2 lg:grid-cols-4">
            {[
              [
                '90D relationship',
                context.relationship,
                `Gold–DXY ${context.c90.goldDxy.toFixed(2)}`,
              ],
              [
                'Dollar impulse',
                context.dollarPressure,
                'Latest common session',
              ],
              ['Yield impulse', context.yieldPressure, 'Latest common session'],
              [
                'Window divergence',
                context.priority,
                `30D ${context.c30.goldDxy.toFixed(2)} · 252D ${context.c252.goldDxy.toFixed(2)}`,
              ],
            ].map(([label, value, detail]) => (
              <div key={label} className="bg-[#f8f4eb] p-4">
                <p className="mono text-[9px] tracking-[0.13em] text-[#7a8691]">
                  {label.toUpperCase()}
                </p>
                <p className="mt-3 font-semibold text-[#14233d]">{value}</p>
                <p className="mt-1 text-xs text-[#78838d]">{detail}</p>
              </div>
            ))}
          </div>
          <div className="mt-5 grid gap-4 border-t border-[#ddd4c5] pt-5 md:grid-cols-[1fr_auto]">
            <p className="text-sm leading-6 text-[#5d6975]">
              <b className="text-[#14233d]">Next intelligence layer:</b>{' '}
              approved macro releases and licensed headlines, with publisher
              metadata, citations, contradictory-evidence handling, a defined
              sentiment target, and evaluation. Until that layer is built, the
              monitor reports only observed metrics and deterministic context.
            </p>
            <a
              href="https://github.com/laura-rivera-sancho/analytics-standard-framework/blob/main/07_macro_correlation_monitor/case_study/intelligence_layer_contract.md"
              target="_blank"
              rel="noreferrer"
              className="self-center text-sm font-semibold text-[#8a651c]"
            >
              View intelligence contract ↗
            </a>
          </div>
        </article>

        <div className="mt-4 grid gap-4 xl:grid-cols-[1.45fr_.55fr]">
          <article className="card-shadow border border-[#d5cbbb] bg-[#fbf8f0] p-5 sm:p-7">
            <div className="mb-5 flex flex-wrap items-start justify-between gap-4">
              <div>
                <p className="mono text-[10px] tracking-[0.15em] text-[#71808d]">
                  ROLLING PEARSON CORRELATION
                </p>
                <h3 className="mt-1 text-xl font-semibold">
                  Gold relationship monitor
                </h3>
                <p className="mt-1 text-sm text-[#6c7781]">
                  Gold log returns vs. DXY log returns and US10Y daily
                  percentage-point changes.
                </p>
              </div>
              <fieldset
                className="flex border border-[#cfc5b5] bg-[#eee8dc] p-1"
                aria-label="Correlation window"
              >
                {([30, 90, 252] as Window[]).map((w) => (
                  <button
                    key={w}
                    onClick={() => setWindow(w)}
                    className={`px-3 py-1.5 text-xs font-semibold transition ${window === w ? 'bg-[#14233d] text-white' : 'text-[#5e6975] hover:bg-white/70'}`}
                  >
                    {w}D
                  </button>
                ))}
              </fieldset>
            </div>
            <div className="h-[340px] w-full">
              <ResponsiveContainer>
                <LineChart
                  data={corrRows}
                  margin={{ top: 8, right: 10, left: -20, bottom: 0 }}
                >
                  <CartesianGrid
                    stroke="#dfd7c9"
                    strokeDasharray="3 4"
                    vertical={false}
                  />
                  <XAxis
                    dataKey="date"
                    tick={{ fontSize: 10, fill: '#78838d' }}
                    tickFormatter={(value) => value.slice(0, 7)}
                    minTickGap={45}
                  />
                  <YAxis
                    domain={[-1, 1]}
                    ticks={[-1, -0.5, 0, 0.5, 1]}
                    tick={{ fontSize: 10, fill: '#78838d' }}
                  />
                  <Tooltip
                    contentStyle={{
                      background: '#101a2d',
                      border: 0,
                      color: '#fff',
                      fontSize: 12,
                    }}
                    labelFormatter={(value) => `Window ending ${value}`}
                    formatter={(value, name) => [
                      Number(value).toFixed(2),
                      name === 'goldDxy' ? 'Gold–DXY' : 'Gold–US10Y',
                    ]}
                  />
                  <ReferenceLine y={0} stroke="#9da5ad" />
                  <Line
                    type="monotone"
                    dataKey="goldDxy"
                    stroke={COLORS.dxy}
                    strokeWidth={2.2}
                    dot={false}
                  />
                  <Line
                    type="monotone"
                    dataKey="goldYield"
                    stroke={COLORS.us10y}
                    strokeWidth={2.2}
                    dot={false}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
            <div className="mt-4 flex flex-wrap gap-5 text-xs text-[#5d6975]">
              <span className="flex items-center gap-2">
                <i className="h-0.5 w-5 bg-[#426d8f]" />
                Gold–DXY: <b>{latestCorr.goldDxy.toFixed(2)}</b>
              </span>
              <span className="flex items-center gap-2">
                <i className="h-0.5 w-5 bg-[#9d5548]" />
                Gold–US10Y: <b>{latestCorr.goldYield.toFixed(2)}</b>
              </span>
            </div>
          </article>

          <aside className="border border-[#24344c] bg-[#14233d] p-6 text-[#f7f2e8]">
            <p className="mono text-[10px] tracking-[0.16em] text-[#d7aa47]">
              INTERPRETATION GUIDE
            </p>
            <h3 className="display mt-3 text-3xl">
              Read the relationship, then the regime.
            </h3>
            <div className="mt-7 space-y-6 text-sm leading-6 text-[#ced5dd]">
              <div>
                <b className="text-white">−1.0 to −0.5 · Strong inverse</b>
                <p>
                  Gold is moving against the comparison asset. This is
                  historically common against a strengthening dollar, but not
                  guaranteed.
                </p>
              </div>
              <div>
                <b className="text-white">−0.5 to +0.5 · Weak or unstable</b>
                <p>
                  A single macro narrative is unlikely to explain the period.
                  Inspect volatility, policy, liquidity, and event context.
                </p>
              </div>
              <div>
                <b className="text-white">+0.5 to +1.0 · Strong positive</b>
                <p>
                  The assets are moving together. Treat this as a regime-change
                  prompt, not proof of a durable relationship.
                </p>
              </div>
            </div>
            <div className="mt-8 border-t border-white/15 pt-5 text-xs leading-5 text-[#aeb9c5]">
              <Info className="mb-2 text-[#d7aa47]" size={17} />
              Correlation changes with the sample window, frequency, outliers,
              and market regime. It does not establish causation.
            </div>
          </aside>
        </div>

        <article className="card-shadow mt-4 border border-[#d5cbbb] bg-[#fbf8f0] p-5 sm:p-7">
          <div className="mb-5">
            <p className="mono text-[10px] tracking-[0.15em] text-[#71808d]">
              TWO-YEAR INDEXED PERFORMANCE
            </p>
            <h3 className="mt-1 text-xl font-semibold">
              Common baseline = 100
            </h3>
          </div>
          <div className="h-[300px]">
            <ResponsiveContainer>
              <LineChart
                data={indexed}
                margin={{ top: 5, right: 10, left: -15, bottom: 0 }}
              >
                <CartesianGrid
                  stroke="#dfd7c9"
                  strokeDasharray="3 4"
                  vertical={false}
                />
                <XAxis
                  dataKey="date"
                  tick={{ fontSize: 10, fill: '#78838d' }}
                  tickFormatter={(value) => value.slice(0, 7)}
                  minTickGap={45}
                />
                <YAxis tick={{ fontSize: 10, fill: '#78838d' }} />
                <Tooltip
                  contentStyle={{
                    background: '#101a2d',
                    border: 0,
                    color: '#fff',
                    fontSize: 12,
                  }}
                  formatter={(value, name) => [Number(value).toFixed(1), name]}
                />
                <ReferenceLine y={100} stroke="#9da5ad" />
                <Line
                  type="monotone"
                  dataKey="gold"
                  name="Gold"
                  stroke={COLORS.gold}
                  strokeWidth={2.3}
                  dot={false}
                />
                <Line
                  type="monotone"
                  dataKey="dxy"
                  name="DXY"
                  stroke={COLORS.dxy}
                  strokeWidth={1.8}
                  dot={false}
                />
                <Line
                  type="monotone"
                  dataKey="us10y"
                  name="US10Y"
                  stroke={COLORS.us10y}
                  strokeWidth={1.8}
                  dot={false}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </article>
      </section>

      <section id="method" className="border-y border-[#cbc1af] bg-[#e7e0d3]">
        <div className="mx-auto grid max-w-[1480px] gap-8 px-5 py-12 sm:px-8 lg:grid-cols-[.7fr_1.3fr]">
          <div>
            <p className="mono text-[10px] tracking-[0.16em] text-[#8a651c]">
              ANALYTICAL CONTRACT
            </p>
            <h2 className="display mt-2 text-4xl">
              Built for disciplined exploration.
            </h2>
            <p className="mt-4 max-w-md text-sm leading-6 text-[#5d6975]">
              The monitor makes transformations, source choices, rules, and
              downstream boundaries visible so every layer can be challenged—not
              merely admired.
            </p>
          </div>
          <div className="grid gap-4 sm:grid-cols-2">
            <div className="bg-[#f8f4eb] p-5">
              <Database className="text-[#9b6d13]" size={20} />
              <h3 className="mt-4 font-semibold">Source transparency</h3>
              <p className="mt-2 text-sm leading-6 text-[#65717e]">
                Yahoo Finance chart service; COMEX gold futures, ICE U.S. Dollar
                Index, and Cboe 10-year yield index. Symbols and timestamps
                remain visible.
              </p>
            </div>
            <div className="bg-[#f8f4eb] p-5">
              <RefreshCw className="text-[#9b6d13]" size={20} />
              <h3 className="mt-4 font-semibold">Comparable changes</h3>
              <p className="mt-2 text-sm leading-6 text-[#65717e]">
                Log returns for gold and DXY; daily percentage-point changes for
                the yield. Series are inner-joined by trading date.
              </p>
            </div>
            <div className="bg-[#f8f4eb] p-5">
              <ShieldCheck className="text-[#9b6d13]" size={20} />
              <h3 className="mt-4 font-semibold">Layer separation</h3>
              <p className="mt-2 text-sm leading-6 text-[#65717e]">
                Observed metrics, reproducible rule labels, future cited LLM
                analysis, and agent actions remain separate in the contract and
                audit trail.
              </p>
            </div>
            <div className="bg-[#f8f4eb] p-5">
              <BookOpen className="text-[#9b6d13]" size={20} />
              <h3 className="mt-4 font-semibold">Decision boundary</h3>
              <p className="mt-2 text-sm leading-6 text-[#65717e]">
                This is research context—not investment advice, a forecast, or
                an automated trading signal. Paper execution will always require
                human approval.
              </p>
            </div>
          </div>
        </div>
      </section>
      <footer className="bg-[#101a2d] text-[#d6dde5]">
        <div className="mx-auto flex max-w-[1480px] flex-col justify-between gap-5 px-5 py-8 text-xs sm:px-8 md:flex-row">
          <p>
            Designed and developed by Laura Rivera Sancho · Analytics Standard
            Framework
          </p>
          <p className="mono text-[#9eabb8]">A8 / MACRO CORRELATION MONITOR</p>
        </div>
      </footer>
    </main>
  );
}
