# git-subdex

**Submodule Indexing and Delivery Exchange**

---

### OBINexus

**obinexus · biz**
35 followers · 39 following
📍 United Kingdom
🕓 04:22 (UTC -12:00)
📧 [support@obinexus.org](mailto:support@obinexus.org)
🌐 [https://www.obinexus.org](https://www.obinexus.org)
🐙 [https://github.com/obnexus](https://github.com/obnexus)
🛒 [https://payhip.com/obinexus](https://payhip.com/obinexus)
🦊 [https://gitlab.com/obinexus](https://gitlab.com/obinexus)
✍🏽 [https://medium.com/@obinexus](https://medium.com/@obinexus)

---

## About

`git-subdex` is a **Submodule Indexing and Delivery Exchange** tool developed by OBINexus.
It enables structured `.md`, `.pdf`, `.html`, `.css`, `.js` documentation to be versioned and delivered across multiple Git repositories via `git submodule`.

### Key Features

* Recursive Git submodule indexing
* Secure doc syncing via Python
* Hook-ready (pre-push, post-checkout)
* YAML-based registry (`index.subdex.yml`)
* CLI-powered document sync and validation

Stay organized, recursive, and reproducible — the OBINexus way.

---

## Problem Statement

### Context

In large-scale projects and ecosystems like OBINexus, documentation is scattered across multiple repositories. This includes everything from API docs to specs, license terms, and manuals — often stored in separate folders and formats.

### The Gap

There is no unified, recursive system that:

* **Separates concerns** between raw artifacts (`.md`, `.pdf`, `.html`) and operational sync logic.
* **Preserves version control integrity** while enabling real-time syncing.
* **Supports delivery** across submodules without manual index management.

This creates confusion, duplication, outdated references, and broken links across repositories.

### Proposed Solution

`git-subdex` introduces a **formal separation of concerns** between:

* **Artifacts** (documents, specs, and static resources)
* **Delivery Logic** (Python sync layer, Git hook coordination)

By using a **YAML-based index (`index.subdex.yml`)**, recursive `git submodule` workflows, and hook-based triggers, `git-subdex` creates a reproducible, organized, and verifiable document system.

This ensures that every `.md`, `.html`, `.pdf`, or `.js` file lives in context, with traceability and structure across project boundaries.

---

🏆 **Achievement: Pull Shark**
