import { fetchPortfolio, fetchTopSignals } from '@/lib/api';
import { Chart } from '@/components/Chart';
import { ScoreBadge } from '@/components/ScoreBadge';
import { RiskPanel } from '@/components/RiskPanel';
import { SignalExplain } from '@/components/SignalExplain';

interface HoldingDto {
  symbol: string;
  quantity: number;
  avg_entry_price: number;
  pnl: number;
}

export default async function DashboardPage() {
  const [portfolio, { signals = [], disclaimer }] = await Promise.all([
    fetchPortfolio(),
    fetchTopSignals(5)
  ]);

  const topSignal = signals[0];

  return (
    <div className="space-y-8">
      <section className="grid" style={{ gridTemplateColumns: '2fr 1fr' }}>
        <div className="card">
          <h2 className="text-lg font-semibold">Portföy Durumu</h2>
          <p className="mt-2 text-xs text-slate-500">{disclaimer}</p>
          <table className="mt-4 w-full text-sm">
            <thead className="text-left text-slate-400">
              <tr>
                <th className="py-2">Sembol</th>
                <th className="py-2">Miktar</th>
                <th className="py-2">Maliyet</th>
                <th className="py-2">PnL</th>
              </tr>
            </thead>
            <tbody className="text-slate-200">
              {(portfolio.holdings as HoldingDto[]).map((holding) => (
                <tr key={holding.symbol} className="border-t border-slate-800">
                  <td className="py-2 font-medium">{holding.symbol}</td>
                  <td className="py-2">{holding.quantity}</td>
                  <td className="py-2">${holding.avg_entry_price.toLocaleString()}</td>
                  <td className="py-2 text-emerald-400">${holding.pnl.toLocaleString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <RiskPanel maxRiskPerTrade={0.01} maxDrawdown={0.2} leverage={3} />
      </section>

      <section className="grid" style={{ gridTemplateColumns: '1.5fr 1fr' }}>
        <div className="card space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-semibold">Top Picks</h3>
            {topSignal ? <ScoreBadge value={topSignal.composite_score} confidence={topSignal.confidence} /> : null}
          </div>
          <ul className="space-y-3 text-sm text-slate-200">
            {signals.map((signal) => (
              <li key={signal.symbol} className="flex items-center justify-between rounded-lg bg-slate-900/60 px-3 py-2">
                <span className="font-medium">{signal.symbol}</span>
                <ScoreBadge value={signal.composite_score} confidence={signal.confidence} />
              </li>
            ))}
          </ul>
        </div>
        <div className="card">
          <h3 className="text-base font-semibold">Rejim Göstergesi</h3>
          <p className="mt-3 text-sm text-slate-300">
            Capital Guard stratejisi trend-up rejiminde kademeli alım yapar, düşüş veya kill durumunda stablecoin&apos;de bekler.
          </p>
          <p className="mt-4 text-xs text-slate-500">“Yatırım tavsiyesi değildir.”</p>
        </div>
      </section>

      {topSignal ? (
        <SignalExplain symbol={topSignal.symbol} markdown={topSignal.summary} />
      ) : (
        <SignalExplain symbol="-" markdown="" />
      )}

      <section className="card">
        <h3 className="text-base font-semibold">Grafik</h3>
        <Chart symbol={topSignal?.symbol ?? 'BTCUSDT'} />
      </section>
    </div>
  );
}
