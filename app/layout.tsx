import { RootProvider } from 'fumadocs-ui/provider/next';
import './global.css';
import { Inter } from 'next/font/google';
import type { Metadata } from 'next';
import { frenchI18n } from '@/lib/i18n';

const inter = Inter({
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: {
    default: "Tchouni's Pharmacy — Fiches de pharmacologie IFSI",
    template: `%s | Tchouni's Pharmacy`,
  },
  description:
    'Fiches de pharmacologie claires et concises pour les études infirmières (IFSI) : classes médicamenteuses, effets indésirables et points de surveillance.',
};

export default function Layout({ children }: LayoutProps<'/'>) {
  return (
    <html lang="fr" className={inter.className} suppressHydrationWarning>
      <body className="flex min-h-screen flex-col">
        <RootProvider i18n={frenchI18n}>{children}</RootProvider>
      </body>
    </html>
  );
}
