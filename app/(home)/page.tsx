import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col items-center justify-center px-6 py-16 text-center">
      <p className="mb-3 text-sm font-medium tracking-wide uppercase opacity-60">
        Fiches de pharmacologie · IFSI
      </p>
      <h1 className="mb-4 text-4xl font-bold tracking-tight">
        Tchouni&apos;s Pharmacy
      </h1>
      <p className="mb-8 max-w-xl opacity-80">
        Des fiches de pharmacologie claires et concises pour réviser : classes
        médicamenteuses, mécanismes d&apos;action, effets indésirables et points
        de surveillance infirmière.
      </p>
      <p>
        <Link href="/docs" className="font-medium underline">
          Commencer à réviser
        </Link>
      </p>
    </main>
  );
}
