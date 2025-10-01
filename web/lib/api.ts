const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

type FetchOptions = RequestInit & { revalidate?: number };

async function request<T>(path: string, options: FetchOptions = {}): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    }
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status}`);
  }

  return response.json();
}

export interface SignalDto {
  symbol: string;
  composite_score: number;
  confidence: string;
  summary?: string;
  regime_label?: string;
  disclaimer: string;
}

export async function fetchTopSignals(limit = 5) {
  const data = await request<{ signals: SignalDto[]; disclaimer: string }>(`/signals/top-picks?limit=${limit}`, {
    cache: 'no-store'
  });
  return data;
}

export async function fetchPortfolio() {
  return request('/portfolio/holdings', { cache: 'no-store' });
}

export async function fetchNews() {
  return request('/status', { cache: 'no-store' });
}
