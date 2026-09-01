import type { Metadata } from 'next';
import { DM_Sans, IBM_Plex_Mono, Libre_Caslon_Display } from 'next/font/google';
import './globals.css';

const body = DM_Sans({ variable: '--font-body', subsets: ['latin'] });
const mono = IBM_Plex_Mono({
  variable: '--font-mono',
  subsets: ['latin'],
  weight: ['400', '500'],
});
const display = Libre_Caslon_Display({
  variable: '--font-display',
  subsets: ['latin'],
  weight: '400',
});

export const metadata: Metadata = {
  title: 'Macro Correlation & Market Context Monitor | Gold · US10Y · DXY',
  description:
    'A live, governed market-context layer for gold, the U.S. 10-year yield, and the U.S. Dollar Index across market regimes.',
  openGraph: {
    title: 'Macro Correlation & Market Context Monitor',
    description:
      'Live Gold · US10Y · DXY relationships and transparent rules-based context for governed research workflows.',
    images: [
      {
        url: '/social-preview.webp',
        width: 1200,
        height: 632,
        alt: 'Macro Correlation Monitor with three abstract market series',
      },
    ],
  },
  twitter: { card: 'summary_large_image', images: ['/social-preview.webp'] },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className={`${body.variable} ${mono.variable} ${display.variable}`}>
        {children}
      </body>
    </html>
  );
}
