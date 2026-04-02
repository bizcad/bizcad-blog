---
title: Claude Token Optimization — Analysis & Action Plan
date: 2026-04-02
sources:
  - "https://www.youtube.com/watch?v=5ztI_dbj6ek — Your Claude Limit Burns In 90 Minutes Because Of One ChatGPT Habit (Nate B Jones)"
  - "https://www.youtube.com/watch?v=49V-5Ock8LU — 18 Claude Code Token Hacks in 18 Minutes (Nate Herk)"
transcripts: analysis/Transcripts/combined-token-usage-videos-20260402.md
---

# Claude Token Optimization — Analysis & Action Plan

## Source Videos

| # | Title | Creator | Tips Extracted |
|---|-------|---------|---------------|
| V1 | Your Claude Limit Burns In 90 Minutes Because Of One ChatGPT Habit | Nate B Jones | 18 |
| V2 | 18 Claude Code Token Hacks in 18 Minutes | Nate Herk | 23 |
| | **Total** | | **41** |

---

## Part 1: Combined Tip List

### Category: CLAUDE.md / System Prompt

| # | Source | Tip | Confidence |
|---|--------|-----|-----------|
| SP-1 | V1-9 | Prune system prompt regularly — especially instructions written for older, less capable models | HIGH |
| SP-2 | V1-10 | Don't load entire repo into context if you haven't tested whether it's still necessary | HIGH |
| SP-3 | V1-12 | For API builders: enable prompt caching for stable context (system prompts, tool definitions, reference docs) | HIGH |
| SP-4 | V2-12 | Keep CLAUDE.md under 200 lines — treat it as an index, not a document. Point to files by path rather than embedding content. | HIGH |
| SP-5 | V2-21 | Use CLAUDE.md as a "systems constitution" — store stable architecture decisions, not conversations | HIGH |
| SP-6 | V2-22 | Add token-aware routing rules to CLAUDE.md: use Haiku sub-agents for multi-file exploration | MEDIUM |
| SP-7 | V2-23 | Add an "applied learning" section to CLAUDE.md that self-updates with one-line bullets on repeated failures (watch for bloat) | LOW-MEDIUM |

### Category: Conversation Discipline

| # | Source | Tip | Confidence |
|---|--------|-----|-----------|
| CD-1 | V1-3 | Start fresh sessions every 10–15 turns — every turn re-reads the entire history | HIGH |
| CD-2 | V1-6 | If exploratory, declare intent at top and summarize before switching to execution | HIGH |
| CD-3 | V2-1 | Use /clear between unrelated tasks — don't carry context from topic A into topic B | HIGH |
| CD-4 | V2-5 | Edit original message and regenerate instead of sending follow-up corrections | HIGH |
| CD-5 | V2-14 | Run /compact manually at ~60% context capacity, not at the default 95% auto-compact threshold | HIGH |
| CD-6 | V2-15 | Compact or clear before stepping away — prompt cache expires after 5 minutes, causing full re-read on return | MEDIUM |

### Category: File & Input Hygiene

| # | Source | Tip | Confidence |
|---|--------|-----|-----------|
| FH-1 | V1-1 | Convert documents to Markdown before feeding them to Claude (can reduce 100k+ tokens → 4-6k for a PDF) | HIGH |
| FH-2 | V1-2 | Avoid screenshots when text will do — screenshots are "terribly inefficient" | HIGH |
| FH-3 | V2-10 | Paste only the relevant section, not the whole file | HIGH |
| FH-4 | V2-13 | Name specific files and functions in prompts — don't say "check the repo," say "check verify_user() in auth.js" | HIGH |

### Category: Workflow Design

| # | Source | Tip | Confidence |
|---|--------|-----|-----------|
| WF-1 | V1-4 | Separate exploration/thinking sessions from execution sessions — never mix the two | HIGH |
| WF-2 | V1-5 | Front-load your intent so the model can act in a single pass without clarification turns | HIGH |
| WF-3 | V1-11 | Match model tier to task — Opus for reasoning, Sonnet for execution, Haiku for polish | MEDIUM |
| WF-4 | V1-17 | Instrument every agent call: track input tokens, output tokens, model mix, cost ratio | HIGH (agent builders) |
| WF-5 | V2-4 | Batch multi-step instructions into a single prompt message | MEDIUM |
| WF-6 | V2-6 | Use plan mode before any real task to prevent wrong-path token waste | HIGH |
| WF-7 | V2-7 | Run /context and /cost to make invisible token consumption visible | HIGH |
| WF-8 | V2-8 | Set up a terminal status line to see real-time context usage as a progress bar | MEDIUM |
| WF-9 | V2-9 | Keep usage dashboard open; check every 20-40 minutes to pace yourself | LOW |
| WF-10 | V2-11 | Watch Claude work in real time and interrupt if it goes off track | HIGH |
| WF-11 | V2-17 | Pick right model per job: Sonnet for coding, Haiku for sub-agents/simple tasks, Opus sparingly (<20% of usage) | MEDIUM |
| WF-12 | V2-18 | Use sub-agents deliberately — delegate one-off tasks to Haiku; avoid multi-agent teams unless necessary | HIGH |
| WF-13 | V2-19 | Schedule heavy sessions and multi-agent runs for off-peak hours (afternoons, evenings, weekends) | LOW |
| WF-14 | V2-20 | Go heavy when near a reset and budget remains; step away when near limit with time remaining | MEDIUM |

### Category: Tool Use

| # | Source | Tip | Confidence |
|---|--------|-----|-----------|
| TU-1 | V1-7 | Audit and prune plugins/connectors — each injects tokens into every turn whether used or not | HIGH |
| TU-2 | V1-8 | Run /context before typing — see what's loaded at session start | HIGH |
| TU-3 | V1-13 | Route web searches through Perplexity (via MCP) rather than native Claude browsing — saves 10-50k tokens/search | HIGH |
| TU-4 | V2-2 | Disconnect MCP servers not actively in use | HIGH |
| TU-5 | V2-3 | Prefer CLIs over MCP servers when a CLI equivalent exists | MEDIUM |
| TU-6 | V2-16 | Deny permissions for shell commands that produce large outputs Claude doesn't need | HIGH |

### Category: Agent Memory / Retrieval

| # | Source | Tip | Confidence |
|---|--------|-----|-----------|
| AM-1 | V1-14 | Use indexed retrieval — never dump full document sets into the context window on every call | HIGH |
| AM-2 | V1-15 | Pre-process and pre-summarize reference documents before they enter context | HIGH |
| AM-3 | V1-16 | Scope each agent's context to the minimum it needs for its specific role | HIGH |

### Category: Infrastructure

| # | Source | Tip | Confidence |
|---|--------|-----|-----------|
| IN-1 | V1-18 | Build guardrails infrastructure: auto-Markdown conversion, index-first retrieval, minimum-viable context scoping | HIGH (teams) |

---

## Part 2: Adversarial Debate — Cluster Verdicts

### Cluster 1: Conversation Hygiene
**Verdict: HIGH confidence** — compaction and fresh-start discipline are correct as general principles. The 60% manual compact rule is actionable; the 10-15 turn rule is too coarse. Context entropy, not a counter, is the real signal. The "edit original and regenerate" tip (CD-4) is underused and eliminates a correction turn entirely.

### Cluster 2: File & Input Hygiene
**Verdict: HIGH confidence** — strongest and cheapest wins in the list. FH-3 (paste only relevant section) and FH-4 (name specific files) require no tooling. FH-1 (Markdown conversion) requires quality conversion tooling — naive conversion can be worse than the original. FH-2 has legitimate exceptions for visual/UI problems.

### Cluster 3: Tool & Plugin Discipline
**Verdict: HIGH confidence in principle, MEDIUM for tactics** — auditing tool lists is clearly correct. MCP-vs-CLI preference is useful but not absolute. TU-6 (deny large-output shell commands) is high-ROI and underappreciated. The cognitive overhead of frequent MCP lifecycle management is a real cost — set up defaults, not per-session toggling.

### Cluster 4: System Prompt & CLAUDE.md
**Verdict: HIGH confidence for pruning (SP-1, SP-4); MEDIUM for index pattern (SP-5); LOW-MEDIUM for self-updating applied learning section (SP-7)**. The 200-line ceiling is a proxy metric, not a mechanistic limit — optimize for signal density, not line count. The applied learning section (SP-7) introduces a feedback loop with no clear governance — monitor aggressively for drift.

### Cluster 5: Workflow Design
**Verdict: HIGH for WF-6 (plan mode) and WF-10 (watch and interrupt)**. These have clear, measurable payoffs. MEDIUM for explore/execute separation (WF-1) — correct as principle, impractical as strict rule. Batching (WF-5) is better for experienced users with well-formed prompts.

### Cluster 6: Model Tier Routing
**Verdict: HIGH confidence in principle; MEDIUM for specific assignments** — tier labels are snapshots that change as models improve. The sub-agent Haiku pattern (WF-12) is the most concrete application. Calibrate routing based on observed error rate per model per task, not generic tier labels.

### Cluster 7: Visibility & Instrumentation
**Verdict: HIGH for /context + /cost (TU-2, WF-7); MEDIUM for status line (WF-8); LOW for dashboard every 20-40 minutes (WF-9)**. Dashboard-watching is reactive and breaks flow — ambient monitoring (status line) is strictly better.

### Cluster 8: Retrieval & Memory Architecture
**Verdict: HIGH confidence, LOW daily relevance for individual Claude Code users** — these are production agentic system tips. Correct and important for building PPA/PhoneBuddy pipelines, not for daily conversational use.

### Cluster 9: Usage Pacing
**Verdict: MEDIUM for WF-20 (session reset strategy); LOW for WF-13 (off-peak scheduling)** — the off-peak performance claim is undocumented by Anthropic. Rate limit behavior is plan-dependent, not load-based.

### Cluster 10: Prompt Caching & Infrastructure
**Verdict: HIGH confidence, LOW relevance for Claude Code users; HIGH relevance for API builders** — prompt caching is an API feature. Irrelevant to conversational Claude Code use. Critical for ppa-api Phase 2.

---

## Part 3: Master Top 5 Tips (Highest Daily ROI)

| Rank | Tip | Why |
|------|-----|-----|
| **#1** | CD-5: /compact at 60%, not 95% | Purely mechanical, zero setup, immediately measurable. Better context quality per session. |
| **#2** | FH-3: Paste only the relevant section | Highest-leverage behavior with lowest implementation cost. 98% token reduction on file inputs. |
| **#3** | WF-6: Plan mode before any real task | Eliminates the most expensive failure mode — executing confidently in the wrong direction. |
| **#4** | WF-10: Watch and interrupt in real time | Catching a wrong path at turn 3 vs turn 15 is a 3-7x token multiplier difference. No setup required. |
| **#5** | SP-1 + SP-4: Prune system prompt / Keep CLAUDE.md lean | Compounds permanently across every future session. Highest long-term ROI of any single action. |

**Honorable mention:** CD-4 (edit original and regenerate) — eliminates correction turns entirely when caught early enough.

---

## Part 4: Application to This Codebase

### Current Token Budget at Session Start (RoadTrip workspace)

| Source | ~Tokens | Action |
|--------|---------|--------|
| Deferred tools | 10.1k | Unavoidable framework overhead |
| RoadTrip CLAUDE.md | 2.5k | **Reduce: 268 lines → target 170** |
| MEMORY.md (auto-mem) | 2.7k | **Prune stale implementation-status entries** |
| System tools | 7.9k | Unavoidable |
| Skills manifest | 1k | Acceptable |
| MCP (Railway) | 2.8k | **Disconnect during non-Railway sessions** |
| **Total** | **~27k** | **Target: ~22k** (save ~5k per session) |

---

### RoadTrip (research/planning workspace) — Biggest Opportunity

**CLAUDE.md: 268 lines → target 170 lines**

Bloat candidates:

| Section | ~Lines | Why |
|---------|--------|-----|
| Documentation Style Guide (emojis, tone, example pattern) | ~30 | Aesthetic preference. Not correctness-critical. Move to a reference file. |
| Quick Reference + Common Scenarios examples | ~25 | Redundant with the alias descriptions above them |
| "Shell Integration Ready" note | ~5 | Informational, not instructional |
| PowerShell alias full usage examples (gpush, gpush-dry, etc.) | ~40 | Point to `infra/RoadTrip_profile.ps1` instead of documenting inline |
| Plan Validation Process 5-step | ~15 | Better as a SKILL.md entry or linked document than always-on context |
| Session Logging alias list (log-help, log-start, log-end) | ~10 | Move to profile.ps1 comments |

**MEMORY.md: prune stale entries**

Entries that are code-derivable (not worth loading every session):
- Implementation status bullets (rules-engine DONE, auth-validator DONE, etc.) — read the code
- Python environment paths — run `which python`
- "Next session" goal entries that are past their session

**Action:** Move implementation status tracking out of MEMORY.md and into a `docs/status.md` that's not auto-loaded.

**MCP servers:** Railway MCP is 2.8k tokens injected every turn. Only connect when doing Railway work. For research-only sessions, disconnect at session start.

---

### PhoneBuddy (production) — Medium Opportunity

**CLAUDE.md: 100 lines — acceptable but trimmable**

| Section | ~Lines | Recommendation |
|---------|--------|---------------|
| File Structure tree | ~15 | Remove — derivable from `ls`. Just say "flat structure, no src/ nesting" |
| Docker + Azure Container Apps deploy sections | ~15 | Rarely needed. One line: "see Dockerfile for non-Railway deploy options" |
| Local Dev block | ~10 | README territory. Remove from CLAUDE.md. |

Estimated savings: 25-30 lines → from 100 to ~70.

**Production system prompt (highest-ROI change):**
PhoneBuddy uses Claude Haiku for call classification. The classification prompt in `main.py` was likely written for an older model version. Haiku's current capabilities mean:
- Multi-shot examples can often be reduced or removed
- Explicit "think step by step" scaffolding is less necessary
- Intent classification instructions can be shorter
- **Action:** Audit the classification prompt in `main.py`. Test with a 30% shorter prompt — if quality holds, the per-call cost drops proportionally. In production, this compounds across every call received.

---

### ppa-api (production) — Minimal Immediate Opportunity, High Future Impact

**CLAUDE.md: 54 lines — already lean. Leave as is.**

**Phase 2 preparation: enable prompt caching**

When Phase 2 adds SRCGEEE pipeline calls, the following should be cached at the API layer:
- System prompt / pipeline role definition
- Tool definitions
- SRCGEEE phase descriptions
- Static reference context (routing rules, agent constitution)

Per Nate B Jones: "Prompt caching can give you a 90% discount on repeated content... $0.50/M vs $5/M for Opus standard." For a pipeline that runs many times per day, this is the single highest-ROI architectural decision.

**Indexed retrieval for Phase 2:**
When Phase 2 adds Retrieve phase, implement indexed retrieval (AM-1) — never dump full history into each call. Retrieve only the relevant caller history chunks.

---

## Part 5: Immediate Action Items

Priority ordered by ROI × ease:

| # | Action | Where | Impact |
|---|--------|--------|--------|
| 1 | Add `/compact at 60%` habit to personal workflow | Personal habit | Immediate |
| 2 | Trim RoadTrip CLAUDE.md from 268 → ~170 lines | `RoadTrip/CLAUDE.md` | Every session |
| 3 | Prune MEMORY.md — remove implementation-status entries | `memory/MEMORY.md` | Every session |
| 4 | Disconnect Railway MCP during non-Railway sessions | MCP settings | Per session |
| 5 | Audit PhoneBuddy classification prompt in `main.py` | `PhoneBuddy/main.py` | Per API call |
| 6 | Add prompt caching to ppa-api Phase 2 plan | Phase 2 design | Future |
| 7 | Trim PhoneBuddy CLAUDE.md from 100 → ~70 lines | `PhoneBuddy/CLAUDE.md` | Every session |
| 8 | Move Plan Validation Process from CLAUDE.md to SKILL.md | `RoadTrip/CLAUDE.md` | Every session |

---

## Appendix: Key Quotes

> "Every time you take a turn in a conversation, you read it as sending one line back. But Claude reads it as sending the entire conversation back." — Nate B Jones

> "Keep [CLAUDE.md] under 200 lines. Treat this like an index route to where more data lives." — Nate Herk

> "Passing everything to every agent is architectural laziness and it has real costs both in tokens burned and frankly in degraded agent performance." — Nate B Jones

> "Most people don't need a bigger plan — they need to stop resending their entire conversation history 30 times. It's not a limits problem. It's a context hygiene problem." — Nate Herk

> "If your system prompt, your tool definitions, your reference documents aren't cached, what are you doing?" — Nate B Jones
