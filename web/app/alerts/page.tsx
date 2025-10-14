export default function AlertsPage() {
  return (
    <div className="card">
      <h2 className="text-lg font-semibold">Uyarı Kuralları</h2>
      <p className="mt-3 text-sm text-slate-300">
        Telegram ve e-posta bildirimleri için skor tabanlı uyarıları yönetin. Skor 80 üstüne çıktığında uyarı tetiklenir.
      </p>
      <ul className="mt-4 space-y-2 text-sm text-slate-400">
        <li>• /alert set BTCUSDT score&gt;80 komutu ile Telegram üzerinden hızlı kurulum.</li>
        <li>• Rejim değişiklikleri ve kill-switch tetiklemeleri otomatik bildirilir.</li>
        <li>• Tüm uyarılar yatırım tavsiyesi değildir.</li>
      </ul>
    </div>
  );
}
