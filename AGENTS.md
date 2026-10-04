# Tchouni's Pharmacy

Fiches de pharmacologie (IFSI) — site de documentation en français.
Dépôt : https://github.com/cleeryy/tchounis-pharmacy

## Stack

- Next.js 16 + Fumadocs UI v16 (layout docs **notebook**)
- Contenu MDX dans `content/docs`, navigation via `meta.json`
- pnpm 9 + Node.js 22+

## Commandes

```bash
pnpm install
pnpm dev        # http://localhost:3000
pnpm build      # build de production (génère .source/)
pnpm start      # http://localhost:3000
pnpm lint       # eslint
```

Prérequis : Node.js ≥ 22 (`node --version`), pnpm 9 (`corepack prepare pnpm@9.15.0 --activate`).

## Structure du contenu

```
content/docs/
  index.mdx        — page d'accueil des docs (/docs)
  premiers-pas.mdx — guide + modèle de fiche
  meta.json        — ordre des pages dans la barre latérale
```

Chaque sous-dossier a son propre `meta.json` (`{ "title": "…", "pages": ["…"] }`).

## Ajouter une page

1. Créer `content/docs/ma-page.mdx` avec le frontmatter :
   ```mdx
   ---
   title: Titre de la fiche
   description: Résumé en une phrase.
   ---
   ```
2. L'ajouter à `pages` dans le `meta.json` du dossier.
3. Lier avec des chemins relatifs : `[texte](./autre-page)`.
4. Vérifier : `pnpm dev` puis `pnpm build`.

Règle : écrire en français, uniquement des connaissances validées
(cours / référentiels IFSI) — `TODO` plutôt qu'inventer.

## Workflow git

- Branche `main` = source de vérité (déployée).
- Branches `feat/<sujet>` pour les changements, PR vers `main`.
- Commits conventionnels : `feat: …`, `fix: …`, `docs: …`, `chore: …`.

## Build Docker

```bash
docker build -t tchounis-pharmacy .
docker run -p 3000:3000 tchounis-pharmacy
```

Image standalone Next.js (`output: 'standalone'`, base `node:22-alpine`).
En production (Dokploy) : exposer le port **3000**, health check `/`.

## Traductions de l'interface

Site 100 % français : `lib/i18n.ts` définit les traductions manuelles
(`defineTranslations` + `uiTranslations`), appliquées via le
`RootProvider` dans `app/layout.tsx`. Pour un nouveau libellé,
ajouter la clé (référence : `fumadocs-ui/dist/.translations/index.d.ts`).
