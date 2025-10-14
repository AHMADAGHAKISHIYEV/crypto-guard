interface ScoreBadgeProps {
  value: number;
  confidence: string;
}

export function ScoreBadge({ value, confidence }: ScoreBadgeProps) {
  const tone = value >= 80 ? 'bg-emerald-500/20 text-emerald-300' : value >= 60 ? 'bg-amber-500/20 text-amber-300' : 'bg-slate-500/20 text-slate-300';
  return (
    <span className={`badge ${tone}`}>
      {Math.round(value)} · {confidence}
    </span>
  );
}
