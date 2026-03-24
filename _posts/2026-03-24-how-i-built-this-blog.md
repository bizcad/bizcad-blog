---
title: "How I Built This Blog (With the AI That Was Already Doing My Other Work)"
date: 2026-03-24
tags: [blogging, github-pages, jekyll, claude, ppa, workflow]
excerpt: "Three failed attempts, one session, one command. How a conversation about PhoneBuddy turned into a working blog."
---

# How I Built This Blog (With the AI That Was Already Doing My Other Work)

I have been trying to get a blog running for months. Today it finally worked. Here is how.

---

## Three Failures Before This

The graveyard of attempts is all still on my disk:

- `G:\repos\AI\roadtrip-blog-nextjs`
- `G:\repos\AI\roadtrip-blog-repo`
- `G:\repos\AI\roadtrip-blog`

None of them worked. Every time, the same ending: Vercel detected that the repository had a Next.js template and tried to run a Node.js build. The Node.js upgrade kept failing in Vercel's CI/CD pipeline. I could not debug it because I did not want to learn Next.js just to maintain a blog. I took them all down.

---

## What I Actually Wanted

I described it in a single message during today's session, after we had been building PhoneBuddy all day:

> *"I want an Index page so the reader can go to a list of older pages or at least the last 5 posts from a list. I want an easy way to have my work here written as a blog post, the way you just did. I want a workflow or skill to add the new posts with an easy command like `Add-Posts-to-Blog` the way that `scrape-now` does. It would be nice to be able to ask the blog questions."*

> *"Desired workflow: do some work with claude → create a blog post about it → call-some-code (essentially gpush) → it magically appears in the blog and index."*

That was the spec. Four requirements. One sentence of desired workflow.

---

## The Root Cause of All Three Failures

Once I described what I wanted, Claude identified the problem immediately:

> *"The 3 failed repos had the same root cause: Vercel detected a JS framework and tried to run Node.js builds. The fix was already written in that file — set `outputDirectory: public` with no build command. The blog code itself was never the problem."*

The architecture was already designed in a file called `static-roadtrip-blog.md` sitting in one of the failed repos. A complete working spec, including `build.py`, templates, and a `vercel.json` config that would have prevented the Node.js problem. It was never implemented.

What broke was not the blog code. It was the deployment toolchain. Switching from Vercel to **GitHub Pages** eliminated the Node.js problem permanently — GitHub runs Jekyll on their servers, nothing to install locally.

---

## The Cross-Repo Writing Problem

There was one more obstacle I thought was blocking me. My previous attempts all used a separate repo for the blog. Copilot could not write files to a repo that was not open in the VS Code workspace. So I kept everything in the RoadTrip repo, even though a separate repo is the right design for a public blog.

Claude Code is not bound by that restriction. It writes to any path on the filesystem, not just files open in the current workspace. The `blog-publish` command is a PowerShell function that changes directory to `G:\repos\AI\bizcad-blog` and runs `git push`. It does not care which workspace is open in VS Code.

This is now a separate repo: **[bizcad-blog](https://github.com/bizcad/bizcad-blog)**. The blog lives there. The RoadTrip workspace is where I write.

---

## How It Was Built

The entire blog was created in a single session, in parallel with other work.

**The repo:** `G:\repos\AI\bizcad-blog` — initialized, committed, and ready to push in one pass.

**The stack:**
- Jekyll on GitHub Pages — GitHub runs the build server-side, zero local toolchain
- `minima` theme — clean, readable, no configuration required
- Posts in `_posts/YYYY-MM-DD-slug.md` — the Jekyll naming convention handles chronological ordering automatically

**The posts:** Eight previous posts were migrated from three dead repos, with Lorem ipsum Next.js template placeholders discarded. The frontmatter from the old Next.js format (`coverImage`, `ogImage`, `author.picture`) is silently ignored by Jekyll — no post files needed rewriting.

**GitHub Actions workflow:** A `.github/workflows/pages.yml` that runs Jekyll and deploys to GitHub Pages on every push to `main`. Approximately 30 seconds from `git push` to live.

---

## The Commands

Two PowerShell functions were added to the RoadTrip profile:

```powershell
# Publish a specific post, or all new posts from docs/blog-posts/
blog-publish docs/blog-posts/my-post.md
blog-publish   # auto-discovers new posts

# Ask questions about all blog posts via Claude Haiku
ask-blog "what did I build in February?"
ask-blog "why did I start PhoneBuddy?"
```

`blog-publish` without arguments scans `G:\repos\AI\RoadTrip\docs\blog-posts\` for any markdown files not already in the blog, copies them to `bizcad-blog\_posts\` with a date prefix, and pushes. It runs from any directory — not just the RoadTrip workspace.

`ask-blog` reads all posts from `_posts\` and passes them to Claude Haiku with the question. It loads the Anthropic API key from the PhoneBuddy `.env` file as a fallback, so no separate API key setup is needed.

---

## Why the Blog Matters Beyond Publishing

I described the real reason I want a blog in a session note today:

> *"From a corporate standpoint, blogs are part of the company's knowledge base... Most enterprises and people have stuff they did in the heat of battle that never got codified. It is one of the reasons I want a PPA. Oddly enough its memory is more important to me than it is to the AI."*

This is the distinction that took me a while to understand. The blog is not primarily for readers. It is a **structured, timestamped record of decisions with context** — the kind of tacit knowledge that disappears when the person who made the decision leaves the room.

Every post I write is a record that Claude's Retrieve step can find. The session log captures the raw conversation. The blog post distills the decision. The `ask-blog` command closes the loop: any future session can query the full history in natural language.

That is what makes the blog worth building. Not the publishing. The retrieval.

---

## The Workflow

```
work with Claude
  → write a post in docs/blog-posts/
    → blog-publish
      → GitHub Pages rebuilds (~30s)
        → live at https://bizcad.github.io/bizcad-blog
          → ask-blog "why did I build X?" answers from the full archive
```

This post was written from the session log of today's work. Published the same way.

---

*Source: RoadTrip developer workspace, session log 2026-03-24. The blog lives at `G:\repos\AI\bizcad-blog`. The workflow lives in `infra\RoadTrip_profile.ps1`.*
