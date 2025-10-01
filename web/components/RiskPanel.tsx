interface RiskPanelProps {
  maxRiskPerTrade: number;
  maxDrawdown: number;
  leverage: number;
}

export function RiskPanel({ maxRiskPerTrade, maxDrawdown, leverage }: RiskPanelProps) {
  return (
    <div className="card">
      <h3 className="text-base font-semibold">Risk Parametreleri</h3>
      <dl className="mt-4 space-y-2 text-sm text-slate-300">
        <div className="flex justify-between">
          <dt>İşlem başı max risk</dt>
          <dd>{(maxRiskPerTrade * 100).toFixed(1)}%</dd>
        </div>
        <div className="flex justify-between">
          <dt>Portföy max düşüş</dt>
          <dd>{(maxDrawdown * 100).toFixed(0)}%</dd>
        </div>
        <div className="flex justify-between">
          <dt>Kaldıraç tavanı</dt>
          <dd>x{leverage}</dd>
        </div>
      </dl>
      <p className="mt-4 text-xs text-slate-500">Kill-switch, max düşüş aşıldığında tüm pozisyonları kapatır.</p>
    </div>
  );
}
