import Link from 'next/link';

const subjects = [
  {
    href: '/docs/crew',
    title: "Tchouni's Crew",
    description:
      'UE 3.3 · Rôles infirmiers : histoire, équipe, dossier patient, réseau de soins.',
  },
  {
    href: '/docs/flow',
    title: "Tchouni's Flow",
    description:
      'UE 2.8 S3 · Processus obstructifs : cœur, poumons, digestif, urinaire — et le rôle IDE.',
  },
  {
    href: '/docs/immunity',
    title: "Tchouni's Immunity",
    description:
      'UE 2.5 S3 · Processus inflammatoires et infectieux : défenses de l’hôte, infections d’organes, VIH, IST, vaccination.',
  },
  {
    href: '/docs/pharmacy',
    title: "Tchouni's Pharmacy",
    description:
      'UE 2.11 S3 · Pharmacologie : classes médicamenteuses, effets indésirables et surveillance infirmière.',
  },
  {
    href: '/docs/plan',
    title: "Tchouni's Plan",
    description:
      'UE 3.2 S3 · Projet de soins : raisonnement clinique, plan de soins, transmissions.',
  },
  {
    href: '/docs/school',
    title: "Tchouni's School",
    description:
      'UE 4.6 S3 · Soins éducatifs et préventifs : ETP, entretien motivationnel, promotion de la santé.',
  },
  {
    href: '/docs/talk',
    title: "Tchouni's Talk",
    description:
      'UE 4.2 S3 · Soins relationnels : entretien, écoute, alliance thérapeutique.',
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
