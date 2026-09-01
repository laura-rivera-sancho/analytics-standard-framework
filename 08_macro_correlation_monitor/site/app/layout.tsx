import type { Metadata } from 'next';
import { DM_Sans, IBM_Plex_Mono, Libre_Caslon_Display } from 'next/font/google';
import './globals.css';

const body = DM_Sans({ variable: '--font-body', subsets: ['latin'] });
const mono = IBM_Plex_Mono({ variable: '--font-mono', subsets: ['latin'], weight: ['400', '500'] });
const display = Libre_Caslon_Display({ variable: '--font-display', subsets: ['latin'], weight: '400' });

export const metadata: Metadata = {
  title: 'Macro Correlation Monitor | Gold · US10Y · DXY',
  description: 'A live, decision-oriented view of gold, the U.S. 10-year yield, and the U.S. Dollar Index across market regimes.',
  openGraph: {
    title: 'Macro Correlation Monitor',
    description: 'Live Gold · US10Y · DXY relationship monitoring across rolling market regimes.',
    images: [{ url: '/social-preview.png', width: 1729, height: 910, alt: 'Macro Correlation Monitor with three abstract market series' }],
  },
  twitter: { card: 'summary_large_image', images: ['/social-preview.png'] },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body className={`${body.variable} ${mono.variable} ${display.variable}`}>{children}</body></html>;
}
