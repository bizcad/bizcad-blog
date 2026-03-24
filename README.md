# bizcad blog

Nick's notes on AI agents, autonomous systems, and building things that work.

Live at: https://bizcad.github.io

## Writing a post

1. Write the post as markdown in the RoadTrip workspace (`docs/blog-posts/`)
2. Run `blog-publish` from any PowerShell terminal in the RoadTrip workspace
3. GitHub Actions builds and deploys automatically (~30 seconds)

## Post format

```markdown
---
title: "Your Post Title"
date: 2026-03-24
tags: [tag1, tag2]
excerpt: "One sentence shown on the index page."
---

# Your Post Title

Post content here...
```

## Asking questions

```powershell
ask-blog "what did I build in February?"
ask-blog "why did I start PhoneBuddy?"
```

## Local preview (optional)

```bash
gem install bundler
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```
