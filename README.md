# Crypto Guard

Kripto sermaye koruma ve erken uyarı platformu. Monorepo yapısı FastAPI tabanlı API, Celery worker, Next.js dashboard ve Telegram bot bileşenlerini içerir. Varsayılan olarak paper trading modunda çalışır.

## Özellikler

- **Capital Guard stratejisi:** Rejim filtresi, ATR tabanlı trailing stop ve kill-switch mantığı.
- **Erken uyarı skorları:** Momentum, hacim anomali, volatilite sıkışması, orderflow ve duygu verilerini birleştirir.
- **OpenAI entegrasyonu:** Haber özetleme, duygu sınıflandırma, sinyal ve rejim açıklamaları.
- **Telegram botu:** Watchlist, risk, mod ve backtest komutları ile bildirimler.
- **Next.js dashboard:** Portföy görünümü, Top Picks, rejim paneli ve haber/sinyal açıklamaları.
- **Docker Compose:** API, worker, web, bot, PostgreSQL, Redis ve opsiyonel Prometheus/Grafana servisleri.

> **Uyarı:** Crypto Guard çıktıları yatırım tavsiyesi değildir.

## Başlangıç

### 1. Depoyu klonlayın

```bash
git clone <repo-url>
cd crypto-guard
```

### 2. Ortam değişkenlerini ayarlayın

`.env.example` dosyasını `.env` olarak kopyalayın ve ilgili alanları doldurun.

```bash
cp .env.example .env
```

Zorunlu alanlar:

- `OPENAI_API_KEY` (opsiyonel fakat haber/sentiment için önerilir)
- `BINANCE_API_KEY` ve `BINANCE_API_SECRET` (paper için sandbox, live için dikkat)
- `TELEGRAM_BOT_TOKEN`
- `MODE` (`paper` varsayılan, `live` için Binance anahtarları zorunlu)

### 3. Docker Compose ile servisleri başlatın

```bash
docker compose up --build
```

Servis adresleri:

- API: [http://localhost:8000/docs](http://localhost:8000/docs)
- Web Dashboard: [http://localhost:3000](http://localhost:3000)
- Prometheus (opsiyonel profil `ops`): [http://localhost:9090](http://localhost:9090)
- Grafana (opsiyonel profil `ops`): [http://localhost:3001](http://localhost:3001)

Bot konteyner loglarında `Starting Crypto Guard bot` mesajını görmelisiniz.

### 4. Demo kullanıcı

Varsayılan demoda `demo@cryptoguard.ai / demo` ile giriş yapabilirsiniz. Kimlik doğrulama ve kullanıcı yönetimi örnek amaçlıdır.

### 5. Seed verisi

İlk açılışta `api` servisi tablo şemalarını otomatik oluşturur. `api/app/db/seed.py` scripti BTCUSDT ve ETHUSDT için 90 günlük sahte OHLCV üretir; gerekirse manuel çalıştırabilirsiniz.

```bash
docker compose exec api python -m app.db.seed
```

### 6. Testler

Python testleri için:

```bash
pip install -r api/requirements.txt
pytest
```

Web arayüzü için Playwright testi örneği `tests/` klasöründe sağlanmıştır (geliştirilmeye açıktır).

### 7. Paper → Live geçişi

- `.env` içinde `MODE=live` yapın.
- Binance anahtarlarınızda yalnızca gerekli izinleri açın.
- Risk parametrelerini (`RISK_MAX_R_PER_TRADE`, `RISK_MAX_PORTFOLIO_DRAWDOWN`, `LEVERAGE_MAX`) güncelleyin.
- Servisleri yeniden başlatın.

Live modda emirler ccxt aracılığıyla Binance REST API'sine gönderilir; OCO ve zorunlu stop/TP parametreleri ile korunur.

### 8. Uyarılar ve bildirimler

Telegram bot komutları:

- `/start` — bot tanıtımı ve uyarılar
- `/watchlist add BTCUSDT` — izleme listesine ekle
- `/alert set BTCUSDT score>80` — skor tabanlı uyarı
- `/backtest run capital_guard BTCUSDT 90d` — hızlı backtest kuyruğu
- `/risk` — risk parametrelerini görüntüle
- `/mode` — paper/live mod bilgisi

### 9. Mimarinin kısa özeti

```
/crypto-guard
├── api          # FastAPI servisleri
├── worker       # Celery görevleri
├── web          # Next.js dashboard
├── bot          # Telegram botu
├── shared       # Paylaşılan util/constant
└── docker-compose.yml
```

## Uyarılar

- Crypto Guard yalnızca sermaye koruma odaklı analiz sağlar; **yatırım tavsiyesi değildir**.
- Paper trading varsayılanıdır. Live modda küçük miktarlarla test edin ve tüm riskleri değerlendirin.
- Binance API anahtarlarınızı güvenli saklayın; konteynerler içinde `.env` üzerinden sağlanır.
