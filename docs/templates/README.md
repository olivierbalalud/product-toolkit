# Templates

Starting points for every artifact in [chapter 2](../guide/02-artifacts-and-ids.md). Copy a template into the monorepo at the path shown in its first comment, then replace the example IDs (`UC-012`, `US-012.1`, …). Guidance is in `<!-- comments -->`; delete it once a section is filled. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

| Template | Copied to | Used from |
|---|---|---|
| [`use-case.md`](use-case.md) | `docs/product/use-cases/UC-012-<slug>/use-case.md` | Use case `Draft` |
| [`story.md`](story.md) | `…/stories/US-012.1-<slug>/prd.md` (its first version) | When stories are cut |
| [`prd.md`](prd.md) | `…/stories/US-012.1-<slug>/prd.md` | *Exploring* |
| [`flows.md`](flows.md) | `…/stories/US-012.1-<slug>/flows.md` | *Exploring*, when `touches` includes `ui` |
| [`copy.md`](copy.md) | `…/stories/US-012.1-<slug>/copy.md` | *Exploring*, when `touches` includes `ui` |
| [`feature.feature`](feature.feature) | `…/stories/US-012.1-<slug>/features/<name>.feature` | *Exploring* |
| [`fit.md`](fit.md) | `…/stories/US-012.1-<slug>/fit.md` | *Exploring*, refreshed at slice start |
| [`reviews.md`](reviews.md) | `…/stories/US-012.1-<slug>/reviews.md` | Design-complete gate onwards |
| [`dcr.md`](dcr.md) | `…/stories/US-012.1-<slug>/dcr/DCR-012.1-01-<slug>.md` | After Design-complete |
| [`enb.md`](enb.md) | `docs/product/enablers/ENB-004-<slug>/enb.md` | Enabler `Draft` |
| [`adr.md`](adr.md) | `docs/adr/0007-<slug>.md` | When a gap appears |
| [`trd.md`](trd.md) | `docs/trd/TRD-012.1-<slug>.md` | Before Dev-ready |
| [`tracking-plan.md`](tracking-plan.md) | `docs/product/tracking-plan.md` | With the first measured PRD |
| [`settings.yaml`](settings.yaml) | `docs/product/settings.yaml` | Once per product |
| [`review-lanes.yaml`](review-lanes.yaml) | in our project plugin (example only) | Review lanes |
| [`skill-spec.md`](skill-spec.md) | `docs/skills/<name>.md` in this repository | Specifying one of our skills |
