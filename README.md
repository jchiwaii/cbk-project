# Kenya Economic Observatory

Next.js App Router, Tailwind CSS, Recharts and self-hosted Plus Jakarta Sans.

Economic values are loaded from `public/data/economy.json`, generated from the research outputs in the parent folder. This is a dated research snapshot, not a live CBK feed. Source issues and observation dates are displayed in the UI.

## Development

Run `npm install`, `npm run data:sync`, then `npm run dev`.
Run `npm test` for period matching, changes, missing values and CSV escaping; `npm run build` also checks TypeScript and exports to `out/`.

## Refreshing data

Refresh and validate the parent research outputs first, including the snapshot date and source-quality log. Run `npm run data:sync`, test and rebuild before publishing. Do not edit economic values in components. Fiscal annual flows use June cumulative observations; rates use percentage-point changes; other changes use matching prior-year periods, with absolute differences for non-positive baselines.
