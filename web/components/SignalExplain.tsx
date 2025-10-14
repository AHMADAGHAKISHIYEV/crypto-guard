interface SignalExplainProps {
  symbol: string;
  markdown?: string;
}

export function SignalExplain({ symbol, markdown }: SignalExplainProps) {
  return (
    <div className="card">
      <h3 className="text-base font-semibold">Sinyal Açıklaması</h3>
      <p className="mt-3 text-xs uppercase tracking-wide text-slate-500">{symbol}</p>
      <pre className="mt-4 whitespace-pre-wrap text-sm text-slate-200">{markdown ?? 'Açıklama bekleniyor…'}</pre>
      <p className="mt-4 text-xs text-slate-500">OpenAI tarafından özetlenmiş olup, yatırım tavsiyesi değildir.</p>
    </div>
  );
}
