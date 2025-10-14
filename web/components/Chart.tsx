'use client';

import { useEffect, useRef } from 'react';

interface ChartProps {
  symbol: string;
}

export function Chart({ symbol }: ChartProps) {
  const container = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!container.current) return;
    container.current.innerHTML = '';
    const iframe = document.createElement('iframe');
    iframe.src = `https://s.tradingview.com/widgetembed/?frameElementId=tradingview_${symbol}&symbol=${symbol}&interval=60&hidesidetoolbar=1&symboledit=1&hide_top_toolbar=1`;
    iframe.width = '100%';
    iframe.height = '320';
    iframe.style.border = '0';
    container.current.appendChild(iframe);
  }, [symbol]);

  return <div ref={container} className="rounded-xl border border-slate-800" />;
}
