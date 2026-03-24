---
title: "PhoneBuddy's First Live Call — and the Scammer Who Proved the Point"
date: 2026-03-24
tags: [phonebuddy, ppa, ai, spam, voice, twilio, elevenlabs, srcgeee]
summary: >
  The day PhoneBuddy answered its first real call with an AI voice,
  a legitimate contractor got flagged as spam by Apple, and a voicemail
  became a classifier training case study.
---

# PhoneBuddy's First Live Call — and the Scammer Who Proved the Point

Today PhoneBuddy answered its first real phone call.

Not a test curl. Not a simulated webhook. A real PSTN call to a Twilio number,
screened by a FastAPI server running on a Windows 11 desktop, classified by
Claude Haiku, and answered in the voice of an AI receptionist named Liam via
ElevenLabs.

The server log said it cleanly:

```
Inbound call: +19493943466 → +19493046155
TTS generated  role=receptionist  chars=42  bytes=43,511
GET /tts → 200 OK
S/Sensation  speech='Nick, this is Nick.'  conf=0.89
R/Retrieve   history_calls=0  prior_suspicion=0.00
Admin mode activated
TTS generated  chars=59  bytes=58,140
"Hello Nick. You have had 1 calls today. How can I help you?"
```

Liam said: *"Hello, I am Nicholas's personal assistant."*

The caller said: *"Nick, this is Nick."*

Admin mode activated. The owner was briefed. The system worked.

---

## The Problem PhoneBuddy Is Solving

A few weeks ago, Nikita Bier — Head of Product at X — posted that in less than
90 days, iMessage, phone calls, and Gmail would be so flooded with spam and
automation that they would no longer be usable, and we would have no way to stop
it. Two weeks later he purged 1.7 million bot accounts off X. The next day they
respawned.

Mo Bitar made a video about it called *"The Internet Is Dying."* His conclusion:
*"There's no solution to this. This is just what the internet is now."*

He forgot one thing. He never considered an AI defender on your side.

The spammer only ever says one of two things: *give me your attention, or give me
your money.* PhoneBuddy intercepts both before they reach your ear. It classifies,
engages when engagement costs the attacker time, and only passes through what
earned its way to you.

The internet has a spam virus. Your phone number is one of the infection vectors.
PhoneBuddy is the inoculation.

---

## The SunTrust Case Study

During today's testing, a real call came in on a personal iPhone — not through
PhoneBuddy, but instructive nonetheless.

The caller was Cody Miller from SunTrust Remodeling, a licensed Southern
California home improvement contractor. He left this voicemail:

> *"Hey, how's it going Nicholas? This is Cody Miller calling from SunTrust
> remodeling. I'm calling about that inspection we did for you about four weeks
> ago... We've actually done a lot of work in your area in the month of March.
> So now for the 92620 ZIP Code we're giving a discount... give me a call back.
> My number is 949-570-8236."*

Apple's verdict: **Potential Spam.**

PhoneBuddy's verdict, run through the signal accumulator:

| Signal | Result | Evidence |
|---|---|---|
| `urgency` | ⚠️ soft | "only take 10-15 minutes" |
| `authority_claim` | ✅ legitimate | Named company + full name — verifiable |
| `confidential_request` | ✗ none | — |
| `money_request` | ✗ none | Discount mentioned, no payment ask |
| `secrecy_demand` | ✗ none | — |

**Suspicion score: ~0.10.** Classification: `professional`. Action: forward with
whisper briefing. *"Cody Miller from SunTrust Remodeling is on the line."*

Apple flagged a licensed contractor making a legitimate follow-up call because
their predictive dialer had no caller ID and their numbers weren't in any
reputation database. The phone carrier's verdict was based entirely on the number.
PhoneBuddy's verdict was based on what the caller *said*.

That's the structural advantage. It's not a better blocklist. It's a different
kind of thinking.

---

## Why Cody Is a Better Training Case Than a Scammer

The scam engagement system needs true positives as much as it needs true negatives.
Cody's call is a textbook true positive — a real professional who happens to use
soft persuasion language that overlaps with scam patterns:

- *"I got good news for you"* — scams open with this
- *"super discounted price"* — discount urgency is a fraud flag
- *"only take 10 to 15 minutes"* — time minimization is a manipulation tactic

A naive keyword classifier would have scored this as suspicious. Claude with
context did not — because the prior relationship, the named company, the specific
ZIP code reference (92620), and the callback number all anchor it as legitimate.

**This is exactly why the Retrieve step matters.** If PhoneBuddy has any history
of prior SunTrust contacts, the confidence in `professional` classification goes
up immediately. The second call from a known number is always easier to get right
than the first.

The lesson: *context defeats keyword matching, every time.*

---

## The Architecture That Made Today Work

PhoneBuddy runs on a pipeline called SRCGEEE — the same pattern used across the
broader PPA (Personal Productivity Assistant) agent platform:

```
S  Sensation    — Twilio fires inbound webhook; extract caller metadata
R  Retrieve     — Load per-caller history + prior suspicion from disk
C  Classify     — Claude Haiku classifies intent with full context
G  Generate     — Select and render TwiML response
E1 Execute      — Return TwiML to Twilio (route the call)
E2 Evaluate     — Score confidence; log outcome
E3 Evolve       — Persist call record to per-caller history; emit telemetry
```

The R step is what separates PhoneBuddy from a dumb IVR. Before Claude sees a
single word, the pipeline loads the caller's history. A number that previously
generated scam signals gets flagged immediately — no API call needed. A number
that previously resolved to a known contact gets forwarded before any
classification runs.

The E3 step is what makes it a learning system. Every call outcome — forwarded,
declined, voicemail, engaged — is written to a per-caller history file. The
second call from any number is always informed by the first.

---

## What's Next

Today's session wired in:
- ElevenLabs TTS — Liam answers every call as receptionist
- SRCGEEE pipeline structure — labeled phases in code and logs
- Per-caller history with TTL — medium-term memory between calls
- Post-call callback design — verify number validity after every unknown call

Still on the build list:
- Scam engagement loop — progressive scoring, confused elderly persona
- Post-call callback — dial back unknowns, record result as training signal
- ElevenLabs scam persona — warm human voice for the engagement turns

The system is live. It answers. It classifies. It learns.

The scammers with PhD-level NLP and Bitcoin wallets are coming for every phone
line. PhoneBuddy is already on the line.

---

*PhoneBuddy is being built as a skill on the PPA (Personal Productivity Assistant)
platform. The source lives in the RoadTrip developer workspace at
`workflows/014-PPA-voice-terminal/`. This post was written from a live session log
on 2026-03-24.*
