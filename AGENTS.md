# Tchouni's Pharmacy

Fiches de pharmacologie (IFSI) — site de documentation en français.
Dépôt : https://github.com/cleeryy/tchounis-pharmacy

Tâches de rédaction / complétion de fiches : appliquer `CONTRIBUTING.md`
(source de vérité du workflow : supports locaux, rédaction sourcée, vérifications, PR).

## Préférences standing (rappelées par l'utilisateur, à appliquer systématiquement)

- **Sources** : rédiger uniquement depuis les PDF de `tchouni-sources/<section>/`
  (jamais committés, ignorés par git) et les référentiels IFSI validés.
  `TODO` plutôt qu'inventer. Contenus datés (seuils, stratégies, chiffres) :
  les signaler comme repères de cours + renvoi aux protocoles en vigueur,
  jamais comme consignes actuelles. Aucune posologie détaillée.
  Supports cités (titre/année) en fin de chaque fiche.
- **Forme** : prose pédagogique obligatoire — intro narrative 3-5 phrases,
  paragraphe avant ET après chaque liste/tableau, transitions, vigilance IDE
  en prose (les listes seules sont indigestes). Composants Fumadocs avec imports
  explicites par fichier : Callout (error=urgences, warn=vigilances et rappels
  datés, info=méthode), Tabs (variantes), Steps (procédures), Accordions
  (compléments uniquement), Cards « Voir aussi » en fin de fiche.
  Frontmatter, `meta.json` et liens relatifs conservés. Français, ton IFSI.
- **Intouchables** : `content/docs/pharmacy` est la référence — ne jamais le
  modifier (annuler toute retouche hors périmètre).
- **Autonomie** : après chaque lot fini, commit + push systématiques ;
  PR vers `main` + merge sans attendre la validation (checks CI verts requis).
  Une PR par périmètre. `CHANGELOG.md` tenu à jour à chaque PR.
- **Discipline de délégation** : un résultat de sous-agent vague n'est pas une
  preuve — toujours vérifier dans le workspace (grep/lecture/diff). Ne pas
  relancer indéfiniment une session qui ne livre pas : dispatch frais avec
  périmètre resserré. Scopes d'écriture disjoints entre lots parallèles.

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
