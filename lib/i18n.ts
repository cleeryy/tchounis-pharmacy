import { defineTranslations } from 'fumadocs-core/i18n';
import { i18nProvider, uiTranslations } from 'fumadocs-ui/i18n';

// Traductions françaises manuelles de l'interface Fumadocs
// (recherche, sommaire, pagination, barre latérale, actions de page…).
// Clés de référence : `fumadocs-ui/dist/.translations/index.d.ts`.
const french = defineTranslations()
  .extend(uiTranslations())
  .add({
    // Recherche
    'Search(search dialog)': 'Rechercher',
    'Search(search trigger)': 'Rechercher',
    'No results found(search dialog)': 'Aucun résultat',
    'Close Search(search dialog)(aria-label)': 'Fermer la recherche',
    'Open Search(search trigger)(aria-label)': 'Ouvrir la recherche',
    // Sommaire « Sur cette page »
    'On this page(table of contents)': 'Sur cette page',
    'No Headings(table of contents)': 'Aucun titre sur cette page',
    'Table of Contents(inline table of contents)': 'Sommaire',
    // Pagination
    'Next Page(pagination)': 'Page suivante',
    'Previous Page(pagination)': 'Page précédente',
    // Barre latérale
    'Show Sidebar(sidebar)': 'Afficher la barre latérale',
    'Hide Sidebar(sidebar)': 'Masquer la barre latérale',
    'Open Sidebar(sidebar)(aria-label)': 'Ouvrir la barre latérale',
    'Close Sidebar(sidebar)(aria-label)': 'Fermer la barre latérale',
    'Open Sidebar(aria-label)': 'Ouvrir la barre latérale',
    'Close Sidebar(aria-label)': 'Fermer la barre latérale',
    'Collapse Sidebar(sidebar)(aria-label)': 'Réduire la barre latérale',
    // Actions de page
    'Copy Markdown(page actions)': 'Copier en Markdown',
    'Copied Markdown(page actions)': 'Markdown copié !',
    'View as Markdown(page actions)': 'Voir en Markdown',
    'Open(page actions)': 'Ouvrir',
    'Options(aria-label)': 'Options',
    // Divers
    'Edit on GitHub(edit page)': 'Modifier sur GitHub',
    'Last updated on(page footer)': 'Dernière mise à jour le',
    'Choose a language(language switcher)': 'Choisir une langue',
    'Language(language switcher)': 'Langue',
    'Theme(site menu)': 'Thème',
    'Copy Text(code block)(aria-label)': 'Copier le texte',
    'Copied Text(code block)(aria-label)': 'Texte copié !',
    displayName: 'Français',
  });

// Props `i18n` à passer au `RootProvider` (site 100 % français, locale forcée).
export const frenchI18n = {
  ...i18nProvider(french),
  locale: 'fr',
};
