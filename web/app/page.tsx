import Link from 'next/link';

export default function HomePage() {
  return (
    <section className="grid" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))' }}>
      <div className="card">
        <h2 className="text-lg font-semibold">Kripto Sermaye Koruma Asistanı</h2>
        <p className="mt-3 text-sm text-slate-300">
          Crypto Guard, sermayeyi korumaya odaklı erken uyarı sinyalleri, rejim filtreleri ve konservatif kaldıraç yönetimi sunar.
        </p>
        <Link href="/dashboard" className="mt-6 inline-flex items-center text-sm font-medium text-amber-400">
          Dashboard&apos;a git →
        </Link>
      </div>
      <div className="card">
        <h3 className="text-base font-semibold">Öne Çıkanlar</h3>
        <ul className="mt-3 space-y-2 text-sm text-slate-300">
          <li>• Paper trading varsayılan; canlı mod opsiyonel.</li>
          <li>• “1 gün önceden” erken uyarı skorları ve güven bantları.</li>
          <li>• OpenAI ile haber özetleri ve sinyal açıklamaları.</li>
        </ul>
      </div>
      <div className="card">
        <h3 className="text-base font-semibold">Hızlı Linkler</h3>
        <nav className="mt-3 flex flex-col gap-2 text-sm text-amber-300">
          <Link href="/alerts">Uyarılar</Link>
          <Link href="/settings">Ayarlar</Link>
        </nav>
      </div>
    </section>
  );
}
