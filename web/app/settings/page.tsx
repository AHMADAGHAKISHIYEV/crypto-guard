export default function SettingsPage() {
  return (
    <div className="space-y-6">
      <div className="card">
        <h2 className="text-lg font-semibold">API ve Risk Ayarları</h2>
        <p className="mt-3 text-sm text-slate-300">
          Binance anahtarlarınızı ve risk parametrelerini güvenli şekilde yönetin. Canlı moda geçmeden önce paper modda test edin.
        </p>
        <p className="mt-4 text-xs text-slate-500">Anahtarlar veritabanında Fernet ile şifrelenir.</p>
      </div>
      <div className="card">
        <h3 className="text-base font-semibold">Parametreler</h3>
        <ul className="mt-3 space-y-2 text-sm text-slate-300">
          <li>• MODE varsayılan paper; live için .env güncelleyin.</li>
          <li>• RISK_MAX_R_PER_TRADE = %1.</li>
          <li>• RISK_MAX_PORTFOLIO_DRAWDOWN = %20 kill-switch.</li>
        </ul>
      </div>
    </div>
  );
}
