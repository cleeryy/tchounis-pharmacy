import Link from 'next/link';

const subjects = [
  {
    href: '/docs/pharmacy',
    title: "Tchouni's Pharmacy",
    description:
      "Fiches de pharmacologie (UE 2.11) : classes médicamenteuses, effets indésirables et surveillance infirmière.",
  },
];

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col items-center px-6 py-16">
      <p className="mb-3 text-sm font-medium tracking-wide uppercase opacity-60">
        Les cours de Tchouni · IFSI
      </p>
      <h1 className="mb-4 text-4xl font-bold tracking-tight text-center">
        Tchouni&apos;s
      </h1>
      <p className="mb-10 max-w-xl text-center opacity-80">
        Tous les cours, matière par matière : des fiches claires et sourcées
        pour réviser. Choisis ta matière pour commencer.
      </p>
      <div className="grid w-full max-w-2xl gap-4 sm:grid-cols-2">
        {subjects.map((subject) => (
          <Link
            key={subject.href}
            href={subject.href}
            className="rounded-xl border p-6 text-left transition-colors hover:bg-fd-accent/50"
          >
            <p className="mb-1 font-semibold">{subject.title}</p>
            <p className="text-sm opacity-80">{subject.description}</p>
          </Link>
        ))}
      </div>
    </main>
  );
}
