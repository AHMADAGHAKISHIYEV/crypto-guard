import './globals.css';
import type { Metadata } from 'next';
import { ReactNode } from 'react';

export const metadata: Metadata = {
  title: 'Crypto Guard',
  description: 'Kripto sermaye koruma ve erken uyarı panosu'
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="tr">
      <body className="bg-slate-950 text-slate-100 min-h-screen">
        <header className="border-b border-slate-800 bg-slate-900/80 backdrop-blur">
          <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
            <h1 className="text-xl font-semibold">Crypto Guard</h1>
            <span className="text-xs uppercase tracking-wide text-amber-400">
              Yatırım tavsiyesi değildir
            </span>
          </div>
        </header>
        <main className="mx-auto max-w-5xl px-6 py-8 space-y-8">{children}</main>
        <footer className="border-t border-slate-800 bg-slate-900/80 px-6 py-4 text-center text-xs text-slate-400">
          © {new Date().getFullYear()} Crypto Guard — sermaye koruma odağı.
        </footer>
      </body>
    </html>
  );
}
