# Contribuer aux fiches

Guide de contribution à la documentation (français, IFSI). Sans inventer : uniquement
des connaissances validées (cours / référentiels IFSI), sinon `TODO`.

## 1. Déposer les supports de cours

- Copier les PDF reçus dans `tchouni-sources/<section>/` (`crew`, `flow`, `immunity`,
  `pharmacy`, `plan`, `school`, `talk`).
- Ces supports (p. ex. PDF Moodle / cours) restent **locaux** : ne jamais les committer
  ni les pousser (`/tchouni-sources/` est ignoré par git).
- Une fois le dépôt terminé, annoncer quand la section est complète avant de rédiger.

## 2. Rédiger les fiches

- Repérer les pages cibles dans `content/docs/<section>/`.
- Lire les supports fournis **avant** de rédiger ; résumer pour un public IFSI, en français.
- Citer les supports utilisés (titre / année).
- Source manquante ou doute : mettre `TODO`, ne pas inventer.
- Seuils, traitements ou recommandations datés : les dater, préciser les limites, renvoyer
  aux protocoles / référentiels en vigueur. Une fiche ne remplace pas une prescription.
- Prose obligatoire : chaque fiche commence par une intro narrative de 3 à 5 phrases,
  chaque liste ou tableau est précédé d'un paragraphe expliquant le pourquoi et suivi
  d'un paragraphe retenant l'essentiel, avec des transitions entre sections et une
  vigilance IDE expliquée en prose. Des listes ou tableaux seuls sont indigestes :
  la prose qui les encadre fait la qualité pédagogique de la fiche.

## 3. Composants Fumadocs

- Pas de `mdx-components` global : import explicite par fichier, après le frontmatter,
  uniquement des composants utilisés (exemple avec `Tabs` / `Steps` dans
  `content/docs/pharmacy/anti-infectieux/antibiotiques.mdx`) :

  ```mdx
  import { Tabs, Tab } from 'fumadocs-ui/components/tabs';
  import { Step, Steps } from 'fumadocs-ui/components/steps';
  ```

- `Callout` : `error` = urgences, `warn` = vigilances et rappels datés, `info` = méthode.
- `Tabs` = variantes parallèles ; `Steps` = procédures séquentielles.
- `Accordions` = compléments « pour aller plus loin » uniquement, jamais le cœur de la fiche.
- `Cards` « Voir aussi » en fin de fiche, avec liens relatifs.

## 4. Règles du dépôt

- Garder le frontmatter (`title`, `description`), la structure des fiches et les liens
  relatifs (`[texte](./autre-page)`). Pour une nouvelle page, partir de ce modèle :

  ```mdx
  ---
  title: Titre de la fiche
  description: Résumé en une phrase.
  ---
  ```

- Ajouter une nouvelle page à `pages` dans le `meta.json` du dossier correspondant.

## 5. Vérifier

```bash
pnpm lint
pnpm types:check
pnpm build
```

## 6. Branche, commit et PR

- Créer une branche `feat/<sujet>` ; vérifier `git status`.
- Ne stage que les MDX / configs intentionnels — jamais les sources locales.
- Commit conventionnel (`feat: …`, `fix: …`, `docs: …`, `chore: …`), push, puis PR vers `main`.
- Attendre la CI verte ; merger seulement si demandé / autorisé.
- Le merge sur `main` déclenche le déploiement Dokploy : ne pas le déclarer terminé
  sans vérification.

## Check-list

- [ ] PDF copiés dans `tchouni-sources/<section>/`, section annoncée complète.
- [ ] Supports lus, fiche résumée en français, supports cités (titre / année).
- [ ] Prose pédagogique : intro narrative, paragraphes avant/après chaque liste ou tableau, transitions, vigilance IDE en prose (pas de listes seules).
- [ ] `TODO` si source manquante ; seuils / traitements datés et caveatés.
- [ ] Frontmatter, structure, `meta.json`, liens relatifs OK.
- [ ] Composants Fumadocs : imports explicites après le frontmatter (utilisés uniquement), Callout / Tabs / Steps / Accordions / Cards « Voir aussi » selon leurs usages.
- [ ] `pnpm lint`, `pnpm types:check`, `pnpm build` verts.
- [ ] Branche `feat/<sujet>`, `git status` vérifié, sources exclues du stage, PR vers `main`.

## Commandes utiles

```bash
pnpm install
pnpm dev        # http://localhost:3000
pnpm build      # build de production
pnpm start      # http://localhost:3000
pnpm lint       # eslint
pnpm types:check
```
