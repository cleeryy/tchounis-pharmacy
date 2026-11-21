# tchounis-pharmacy

> Contribution aux fiches : voir [CONTRIBUTING.md](./CONTRIBUTING.md).

This is a Next.js application generated with
[Create Fumadocs](https://github.com/fuma-nama/fumadocs).

Run development server:

```bash
npm run dev
# or
pnpm dev
# or
yarn dev
```

## Déploiement Docker (GHCR)

Chaque push sur `main` (et chaque tag `v*` ou lancement manuel) construit et
publie l'image sur GitHub Container Registry via
`.github/workflows/docker-publish.yml` :

```text
ghcr.io/cleeryy/tchounis-pharmacy:latest
ghcr.io/cleeryy/tchounis-pharmacy:sha-<commit>
```

Sur un serveur (VPS) avec Docker Compose :

```bash
docker compose pull
docker compose up -d
# accessible sur http://<ip-du-serveur>:3000
```

Si le package GHCR est privé, se connecter d'abord avec un token
`read:packages` : `echo "$TOKEN" | docker login ghcr.io -u cleeryy --password-stdin`.

Open http://localhost:3000 with your browser to see the result.

## Explore

In the project, you can see:

- `lib/source.ts`: Code for content source adapter, [`loader()`](https://fumadocs.dev/docs/headless/source-api) provides the interface to access your content.
- `lib/layout.shared.tsx`: Shared options for layouts, optional but preferred to keep.

| Route                     | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `app/(home)`              | The route group for your landing page and other pages. |
| `app/docs`                | The documentation layout and pages.                    |
| `app/api/search/route.ts` | The Route Handler for search.                          |

### Fumadocs MDX

Collections are defined with the [Macro API](https://fumadocs.dev/docs/mdx/macro) in `lib/source.ts`.

Read the [Introduction](https://fumadocs.dev/docs/mdx) for further details.

## Learn More

To learn more about Next.js and Fumadocs, take a look at the following
resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js
  features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Fumadocs](https://fumadocs.dev) - learn about Fumadocs
