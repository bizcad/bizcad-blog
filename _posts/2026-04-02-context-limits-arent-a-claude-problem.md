---
title: "Context Limits Aren't a Claude Problem — They're a Hygiene Problem"
date: '2026-04-02T12:00:00.000Z'
excerpt: "Context limits aren't a Claude problem — they're a hygiene problem. Here's what two YouTubers and a SOP taught me."
author: Nick Stein
---

I was mid-session on a feature last week — deep into a multi-file refactor — when Claude hit its context limit. Not at the end of a logical unit. Right in the middle of a thought.

My first instinct was frustration. My second instinct was to check whether I was the problem.

I was.

## Two Videos, Same Week

Around the same time, two YouTube presenters I follow independently posted about the same thing:

- **[Your Claude Limit Burns In 90 Minutes Because Of One ChatGPT Habit](https://www.youtube.com/watch?v=5ztI_dbj6ek)** — Nate B Jones
- **[18 Claude Code Token Hacks in 18 Minutes](https://www.youtube.com/watch?v=49V-5Ock8LU)** — Nate Herk

Different angles, same diagnosis. Nate Herk put it directly: *"Most people don't need a bigger plan — they need to stop resending their entire conversation history 30 times. It's not a limits problem. It's a context hygiene problem."*

That landed. I'd been treating context limits like a Claude constraint to work around. They're actually a mirror — they show you exactly how much noise you've been generating.

## What Actually Burns Your Context

Every time you send a message, Claude re-reads the entire conversation from the beginning. Not just your new line. Everything. That 200-line error message you pasted three turns ago? Still there, re-read on every turn.

And that's just the visible waste. The invisible waste is worse: connected MCP servers inject their full tool schemas into every message whether you use them or not. My Railway MCP was costing me 2,800 tokens per turn during sessions where I wasn't touching Railway at all.

Then there's the always-on context — `CLAUDE.md`, `MEMORY.md`, skill manifests — loaded fresh at the start of every conversation and re-read with every message. I had never audited any of these files. My `CLAUDE.md` was 268 lines. The recommended ceiling is 200.

## The Five Tips That Survived Scrutiny

I ran the combined tip list from both videos through an adversarial debate — steelmanning each recommendation, then attacking it, then rendering a verdict. Most tips held up. A few were cargo cult. These five had the clearest ROI:

**1. Run `/compact` at 60% context capacity, not the default 95%.**
By the time auto-compact fires at 95%, context quality is already degraded and the summary loses nuance. Compacting at 60% keeps the signal sharp. This is purely mechanical — no judgment required.

**2. Paste only the relevant section, not the whole file.**
If the bug is in one function, paste that function. Pasting a 2,000-line file to ask about 30 lines is a 66x overhead — and it compounds on every subsequent turn. The discipline is: if you're reaching for Ctrl+A, pause first.

**3. Use plan mode before any multi-file or architectural task.**
The most expensive failure mode in Claude Code is executing confidently in the wrong direction. A wrong-path correction at turn 15 costs roughly 15 turns of tokens plus the rework. Plan mode adds one turn of overhead and eliminates multi-turn rework. For anything involving more than one file, the math is clear.

**4. Watch Claude work and interrupt at turn 3, not turn 15.**
Most developers let Claude run to completion out of habit. Watching and intervening early is the highest-leverage human action in the loop. Catching a wrong path at turn 3 versus turn 10 is roughly a 3-7x token difference.

**5. Keep `CLAUDE.md` under 200 lines — treat it as an index, not a document.**
This one compounds permanently. A leaner `CLAUDE.md` pays a dividend on every conversation that follows, not just the current one. The rule: if a section can be replaced by a file path reference, replace it.

## The Files That Hurt Most

The most expensive context isn't the file you just pasted. It's the files loaded silently every session that you've never looked at.

For me that list included: a `CLAUDE.md` that had grown to include documentation style guides, PowerShell alias usage examples, and a "Shell Integration Ready" note that served no one. A `MEMORY.md` with implementation-status bullets that were just a slower way of reading the code. MCP servers connected because they seemed useful at some point and never disconnected.

None of these feel expensive individually. Together they were the reason I was hitting limits.

## The SOP

I codified everything — the tips that survived the adversarial review, the SRCGEEE-specific rules, the artifact transformation pattern (PDF → Markdown → file reference), the always-on context audit checklist — into a single reference document:

**[Context Economy SOP](https://github.com/bizcad/RoadTrip/blob/main/docs/context-economy-sop.md)**

It's written to be readable by both humans and agents. Ten sections, each short enough to actually use. The quick reference table at the bottom is the part I find myself returning to most.

These aren't automated rules. They're judgment calls — and judgment calls are exactly what shouldn't be delegated to a machine that can't see the full picture of what a session is trying to accomplish. But writing them down means you only have to figure them out once.

---

*The full adversarial analysis, combined transcript, and application notes for three repos live in [token-optimization-analysis-20260402.md](https://bizcad.github.io/bizcad-blog/assets/artifacts/token-optimization-analysis-20260402.txt).*
