# git-subdex — Documentation Site Scaffold

> Non-monolithic, recursive doc system for OBINexus (GitHub/GitLab friendly). Includes schema, migration path, semverx policy, polyglot bindings and install targets.

---

## Goals (today)

- Produce a GitBook-like *non-monolithic* doc site powered by small, indexed repos using `git-subdex`.

- Ensure **bi-directional integration**: docs can be edited in repo and published to site; site edits can open PRs back to source repos.

- Support GitHub + GitLab + self-hosted Git endpoints, public/private access, and automated semverx tagging.

- Provide polyglot packaging and install paths for consumers: Node, Rust, Python, Go, Lua.

- Define a migration recipe so OBINexus teams can move existing monolithic docs into the new indexed system.

---

## Naming / URL Schema

This schema doubles as both DNS/URL and a repo/folder layout:

```
<service>.<operation>.obinexus.<division>.<department>.<country>.<tld>
```

Where:

- `service` — project name (e.g. `git-subdex`)

- `operation` — `docs` | `spec` | `api` | `guides` | `archive`

- `division` — `computing` | `publishing` | `education` | `fashion` | ...

- `department` — `dev` | `ops` | `legal` | `infra` | ...

- `country` — locale code `en`, `ch`, `ng`, ...

- `tld` — internal tld for org routing (`org` reserved for internal routing)

**Example**

- URL: `git-subdex.docs.obinexus.computing.dev.en.org`

- Repo path: `/git-subdex/docs/computing/dev/en/`

This maps cleanly into CI/CD and static-site builders.

---

## Repository layout (recommended)

Each repository should expose a shallow docs directory conforming to the schema. Example repo: `obinexus/git-subdex-docs`.

```
/git-subdex-docs/
├─ index.subdex.yml        # registry index for git-subdex
├─ docs/                   # canonical docs content
│  ├─ computing/dev/en/
│  │  ├─ README.md         # landing page -> maps to URL root
│  │  ├─ getting-started.md
│  │  ├─ api.md
│  │  └─ assets/
│  └─ ...
├─ hooks/
│  ├─ pre-push            # runs git-subdex sync checks
│  └─ post-checkout
├─ .subdex/                # local subdex metadata (generated)
└─ package.json            # optional for JS-centric tooling
```

`index.subdex.yml` is the registry file that declares doc slices and metadata. A minimal example is included below.

---

## `index.subdex.yml` (example stub)

```yaml
version: 1
entries:
  - id: git-subdex.docs.computing.dev.en
    path: docs/computing/dev/en
    access: public
    semverx: true
    languages: [node, rust, python, go, lua]
    hooks:
      pre-push: hooks/pre-push
      post-checkout: hooks/post-checkout
    checksum: auto
```

Notes:

- `semverx: true` enables the extended semantic-versioning policy (see SemverX section).

- `checksum: auto` indicates `git-subdex` should compute and verify artifact checksums during sync.

---

## SemverX (policy)

`SemverX` is OBINexus's opinionated extension of semantic versioning for documentation slices and bindings.

Key principles:

- Versions are `MAJOR.MINOR.PATCH+meta` where `meta` can include `build` and `poly` tags (e.g. `1.2.3+poly.rust.20250829`).

- Docs change that break structure (TOC, frontmatter fields used by the site) -> increment `MAJOR`.

- Non-breaking content edits -> `PATCH`.

- Additive content (new pages, examples) -> `MINOR`.

- `poly` metadata indicates language binding updates (see `libpolycall2semverx`).

SemverX is enforced at publish time by CI: publishes require tag format `vMAJOR.MINOR.PATCH+...`.

---

## libpolycall2semverx — binding model

`libpolycall2semverx` is the binding layer that maps language-specific package versions to SemverX metadata.

Concepts:

- Each language binding (Node, Rust, Python, Go, Lua) maintains its own package versioning (npm, cargo, pypi, go mod, luarocks).

- `libpolycall2semverx` resolves the package version and embeds a `+poly.<lang>.<pkgver>` suffix into the SemverX tag for the doc slice.

- The binding is responsible for:
  
  - Querying package registry for current package version
  
  - Mapping compat constraints to SemverX
  
  - Signing/attesting the mapping (optional)

Example mapping:

- `git-subdex@1.4.0` (npm) → docs slice tag: `v2.3.0+poly.node.1.4.0`

- `git-subdex v2.3.0 (cargo 0.8.1)` → `v2.3.0+poly.rust.0.8.1`

This provides a single canonical place to see which language runtime/package a doc version is tied to.

---

## Bi-directional integration

Two-way flow required:

1. **Repo -> Site (publish)**
   
   - `git-subdex sync` reads `index.subdex.yml`, validates checksums and semverx, renders Markdown to HTML, and publishes to the doc site (static host or CDN).
   
   - CI pipeline tags release and optionally publishes language binding metadata.

2. **Site -> Repo (edit)**
   
   - The rendered site exposes an "Edit this page" button that opens an edit flow.
   
   - Edits can either open a PR against the origin repository or create a change proposal stored as a `subdex` patch.
   
   - Site edits are validated against `index.subdex.yml` rules before creating PRs.

Security & trust:

- PRs created from site edits must be signed or go through bot accounts.

- For private repos, the edit flow requires OAuth scopes and explicit user approval.

---

## Migration plan (monolith -> subdex)

Steps to migrate a monolithic GitBook/Git repo into the `git-subdex` indexed system.

1. **Audit**: list all docs, frontmatters, asset locations, broken links.

2. **Slice**: choose slices according to schema (service/operation/division/department/locale).

3. **Create index**: add `index.subdex.yml` entries for each slice.

4. **Add hooks**: provide `pre-push` and `post-checkout` hooks scaffolds.

5. **CI**: add a `subdex` pipeline job that validates index and builds preview site.

6. **Publish**: run `git-subdex sync` to publish initial site.

7. **Verify**: link-check, asset-check, and semverx conformance.

8. **Deprecate**: remove monolithic site once team confirms parity.

Time estimate: modular — do one service at a time. Start with `git-subdex` itself as an internal pilot.

---

## Install targets and polyglot packaging

Doc slices and the binding layer should provide clear instructions for installing language-specific packages that relate to docs.

Top-level install paths (examples):

- Node
  
  ```bash
  npm install @obinexuscomputing/git-subdex
  # or global CLI
  npm i -g @obinexuscomputing/git-subdex
  ```

- Rust (cargo)
  
  ```bash
  cargo add git-subdex --version ^0.8
  ```

- Python
  
  ```bash
  pip install obinexus-git-subdex
  ```

- Go
  
  ```bash
  go get github.com/obinexus/git-subdex@v1.2.3
  ```

- Lua (luarocks)
  
  ```bash
  luarocks install git-subdex
  ```

> Each language binding must include a `README.lang.md` inside the docs slice, showing exact commands and an example.

---

## Server pages / library binding (serverx2libpolycall)

`serverx2libpolycall` is the server-side adapter that exposes runtime bindings for docs and performs semantic version resolution.

Responsibilities:

- Serve rendered markdown as static pages

- Expose API to query semverx metadata for any doc slice

- Provide endpoints used by `libpolycall2semverx` to register package bindings

- Offer an auth layer for private slices

API sketch (REST):

```
GET /api/v1/docs/{slice}            # returns HTML + metadata
GET /api/v1/semverx/{slice}        # returns semverx tag and poly bindings
POST /api/v1/register-binding      # registers a binding mapping
POST /api/v1/sync                  # trigger a sync for a slice (CI-only)
```

---

## CI/CD flow (recommended)

- On push to `main`:
  
  - Run `git-subdex validate` (checks `index.subdex.yml`, checksums)
  
  - Build preview site and run link-check
  
  - Run `libpolycall2semverx` to update binding metadata
  
  - If `semverx: true` and tag created -> publish static site to CDN

- On tag release:
  
  - Enforce semverx tag format
  
  - Publish language binding artifacts

---

## Example: Minimal `git-subdex sync` CLI usage

```bash
# validate and preview
git-subdex validate
git-subdex preview --slice git-subdex.docs.computing.dev.en

# publish slice
git-subdex sync --slice git-subdex.docs.computing.dev.en --publish
```

---

## Best Practices checklist for teams

- Keep slices small and coherent (single responsibility)

- Maintain frontmatter schema for renderers (title, summary, version, semverx)

- Use `libpolycall2semverx` to track language binding versions

- Protect private slices behind OAuth and scoped tokens

- Automate link-check and asset checksum in CI

- Provide `README.lang.md` for each language target

---

## Next steps / TODOs

- Implement `libpolycall2semverx` prototype that queries npm/cargo/pypi and emits semverx tags.

- Build `git-subdex` CLI commands: `validate`, `preview`, `sync`, `register-binding`.

- Create site edit-to-PR flow (site -> repo) with bot account and signing option.

- Pilot migration for `git-subdex` docs.

---

## Appendix: sample frontmatter (Markdown)

```yaml
---
title: Getting Started
summary: Quick start for git-subdex
version: 1.0.0+poly.node.1.4.0
locale: en
slice: git-subdex.docs.computing.dev.en
---
```

---

*Document created as scaffold — edit and iterate. When you're ready I can produce the `index.subdex.yml` for a specific repo or generate the initial CI job YAML for GitHub Actions and GitLab CI.*
