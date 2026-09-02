import { NextResponse } from 'next/server';

type YahooPoint = { date: string; value: number };
type YahooResponse = {
  chart?: {
    result?: Array<{
      timestamp?: number[];
      indicators?: { quote?: Array<{ close?: Array<number | null> }> };
    }>;
  };
};

const instruments = [
  { key: 'gold', symbol: 'GC=F', label: 'COMEX Gold Futures', unit: 'USD/oz' },
  { key: 'dxy', symbol: 'DX-Y.NYB', label: 'U.S. Dollar Index', unit: 'index' },
  { key: 'us10y', symbol: '^TNX', label: 'U.S. 10Y Yield', unit: '%' },
] as const;

async function getSeries(symbol: string): Promise<YahooPoint[]> {
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(symbol)}?range=5y&interval=1d&events=history`;
  const response = await fetch(url, {
    headers: { 'User-Agent': 'Mozilla/5.0 A8-Macro-Correlation-Monitor' },
    next: { revalidate: 3600 },
  });
  if (!response.ok)
    throw new Error(`Market data request failed (${response.status})`);
  const json = (await response.json()) as YahooResponse;
  const result = json.chart?.result?.[0];
  if (!result?.timestamp?.length)
    throw new Error('Market data response was empty');
  const close: Array<number | null> =
    result.indicators?.quote?.[0]?.close ?? [];
  return result.timestamp.flatMap((timestamp: number, index: number) => {
    const value = close[index];
    return Number.isFinite(value)
      ? [
          {
            date: new Date(timestamp * 1000).toISOString().slice(0, 10),
            value: Number(value),
          },
        ]
      : [];
  });
}

export async function GET() {
  try {
    const fetched = await Promise.all(
      instruments.map(async (item) => ({
        ...item,
        points: await getSeries(item.symbol),
      })),
    );
    return NextResponse.json({
      status: 'live',
      provider: 'Yahoo Finance chart service',
      fetchedAt: new Date().toISOString(),
      instruments: fetched,
    });
  } catch (error) {
    return NextResponse.json(
      {
        status: 'unavailable',
        message:
          error instanceof Error ? error.message : 'Unknown market-data error',
      },
      { status: 503 },
    );
  }
}
