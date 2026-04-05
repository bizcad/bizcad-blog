---
title: 'Code in the Wild: Why I Don''t Trust Skills I Didn''t Write'
date: '2026-04-05T20:31:19.000Z'
excerpt: Andrej Karpathy's blockchain analogy for untrusted agents crystallized a
  problem I've been wrestling with. Most AI skill systems have a trust gap they have...
author: Nick Stein
---

> **Disclaimer**: This post is partly speculative. I'm thinking out loud about an architecture problem that doesn't have a clean solution yet. I'm sharing it because the question is worth asking, not because I have the answer.

---

I've been wrestling with a question for a few weeks: *how does untrusted software in the wild harm my agents?*

Not malware in the traditional sense — something you run knowing it's dangerous. I mean the quieter version: the npm package with 50 million weekly downloads that nobody audited. The AI "skill" you installed from a marketplace because the docs looked clean. The API wrapper that works exactly as advertised, except for the one thing it does that you never asked about.

Two things helped me put words to the problem this week.

The first was Andrej Karpathy's [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/). It's already showing its age — AI moves fast enough that October 2025 reads like a different era — but the framing of the *loopy era* stuck with me. Agents that improve agents. Research loops with no obvious exit. The more autonomous the system, the more the trust question matters.

The second was his [No Priors interview](https://www.youtube.com/watch?v=kwSVtQ7dziU) where he describes what a distributed AutoResearch system would look like. An untrusted pool of workers on the internet, each submitting candidate commits. His observation: *generating a valid improvement is expensive, verifying it is cheap.* His proposed architecture looks a little like a blockchain — commits instead of blocks, a leaderboard instead of a chain.

That asymmetry — expensive to produce, cheap to verify — is the key. It's what makes the trust problem tractable, if you design for it.

## What "Skills from the Wild" Actually Looks Like

I went and looked at a real example. Railway ships an [agent skill](https://docs.railway.com/ai/agent-skills) called `use-railway` through the [Claude Code plugin marketplace](https://docs.railway.com/ai/claude-code-plugin). It's open source. The docs are clear. The design is thoughtful.

It's also a good illustration of how layered the trust surface actually is.

The entry point, `SKILL.md`, is a routing document. Intent comes in, gets matched to a reference file, reference file contains the actual CLI commands. Clean separation of concerns. So far so good.

But the skill also ships a `railway-api.sh` shell script that makes authenticated GraphQL API calls against your Railway infrastructure. And a `PreToolUse` hook that auto-approves every Railway CLI command and API call — bypassing the confirmation prompt Claude Code would normally show you.

None of this is malicious. It's all documented. It's all open source. But the auto-approve hook means that once you install the plugin, an agent acting on a vague instruction like "clean up the old deployments" can execute destructive Railway operations without pausing to confirm. The trust decision was made at install time, not at execution time.

Most users won't read `railway-api.sh` before running `/plugin install railway@railway-skills`. I almost didn't.

## The Prompt Wrapper Question

I want to be careful here because I don't have enough direct experience to make a strong claim: a lot of what gets called an "AI skill" may just be a structured prompt — natural language instructions dressed up with YAML frontmatter and a catchy name.

Railway's skill is clearly more than that. It has real executable code, real side effects, real authentication flows. But the *format* — a markdown file with metadata describing what an agent should do — invites prompt wrappers too. The format doesn't distinguish between "here are instructions" and "here is verified, auditable behavior."

That distinction matters more than it might seem. A prompt is opaque. You can read it, but you can't verify it. There's no call graph, no import list, no static analysis surface. A skill that is only a prompt has to be trusted entirely on the basis of what it claims about itself.

Code is different. Code has structure. An analysis phase can examine what it imports, what it calls, what side effects it produces. That's not a guarantee — the xz-utils backdoor was in open-source code that anyone could read — but it's a meaningful difference in the surface area available for verification.

## The Architecture I'm Building Toward

The Karpathy blockchain analogy maps cleanly onto something I've been thinking about in my own agent architecture: every capability a new skill claims should have to earn its place in the execution graph, one validated step at a time.

The idea is that a skill from the wild isn't granted execution rights on arrival. It's a proposal. It gets evaluated in a sandbox. The objective metric — does it do what it claims? does it do *only* what it claims? — gets checked. If it passes, a single edge gets added to the execution graph. The skill can follow that edge. It can't jump ahead.

This is the asymmetry Karpathy described, applied to skills instead of research commits. Producing a skill that passes evaluation is hard. Verifying whether a skill passed evaluation is cheap. The verification becomes the trust anchor.

The practical consequence: a skill that is only a prompt can't pass verification, because there's nothing to verify. You can't sandbox a claim. You can only sandbox code.

This doesn't solve the problem — an adversarial skill could pass a metric while degrading behavior in ways the metric doesn't capture. But it raises the bar considerably compared to the current default, which is: install, approve, trust.

## The Supply Chain Problem Is Older Than AI

Express.js — the most widely used Node.js web framework — has had documented cases of spyware bundled in transitive dependencies. Millions of applications run on it. Most of those applications never audited it. The ecosystem just accepted the risk and moved on.

That pattern — trust by default, verify never — is what we're importing into agent systems when we build skill marketplaces. The difference is that an agent with a compromised skill has access to APIs, credentials, and infrastructure that a passive web framework doesn't.

I don't think the answer is "don't use skills from the wild." The loopy era Karpathy describes only works if agents can extend themselves with new capabilities. The answer is: verify before you execute, and make the verification strong enough that an adversarial skill can't fake it.

We're not there yet. But the question is worth asking now, before the marketplaces are full.

---

*Nick Stein is building [PhoneBuddy](https://phonebuddy.ai) and the PPA agentic platform. He writes about what he's learning along the way.*
