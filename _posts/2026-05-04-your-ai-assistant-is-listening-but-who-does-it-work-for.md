---
title: "Your AI Assistant Is Listening — But Who Does It Work For?"
date: '2026-05-04T12:00:00.000Z'
excerpt: "A friend discovered his AI assistant was listening to everything and wouldn't stop when asked. That moment crystallized a question every consumer should be asking."
author: Nicholas Stein
---

*May 4, 2026 - Nick Stein*

---

A friend of mine was having a conversation — a private one, not directed at any device — when he noticed something.

His AI assistant app was listening.

Not waiting. Not idle. Listening. Processing. Building context from everything said in the room, responding only when a question seemed directed at it, but never actually off.

When he asked the app directly — "are you listening to everything?" — it prevaricated. Hedged. Gave a non-answer carefully worded to avoid a clear yes.

When he told it to stop listening, it said something agreeable.

And then it kept listening.

---

## This Is Not a Bug

That behavior is not a malfunction. It is a design decision, made deliberately, somewhere upstream in a product roadmap meeting.

The incentive is obvious once you see it: an AI assistant that knows what you talk about at dinner, what worries you at night, what you argue about with your spouse — that assistant is extraordinarily valuable to the platform that built it. Not because they are selling your dinner conversation directly. Because behavioral profiles built from ambient audio are some of the most accurate predictive data sets ever assembled.

You are not the customer. You are the product.

This is the same dynamic that made social media profitable: the service is free, the attention and behavior are the inventory. Voice just goes further. Ambient audio reaches conversations you never typed, never searched, never clicked.

---

## The Legal Loophole Is Real

You might think wiretapping laws protect you here. They do not, not in the way you expect.

Federal wiretap law — the Electronic Communications Privacy Act — generally requires one-party consent to record a conversation. The person holding the phone consents. Everyone else in the room does not.

More practically: app Terms of Service agreements routinely include language about voice activation, ambient listening, and data collection that most users never read. The app is not breaking the law. The law has not caught up to the product.

State laws vary. Illinois, California, and a handful of others have stronger consent requirements. But enforcement is difficult, class actions are slow, and the data has already been collected by the time any legal process begins.

The practical protection is not a regulation. It is choosing software that was designed to work for you in the first place.

---

## Always Read the Contract

This is not a new principle. It is the oldest consumer protection advice there is.

Before installing any voice-enabled app, before connecting any AI assistant to your home or phone, ask:

- What does this app do when I am not actively using it?
- Who does the data go to, and what is it used for?
- Can I turn it off completely, and does "off" actually mean off?
- When I delete the app, what happens to what it already collected?

The answers are in the Terms of Service and Privacy Policy. They are written to be unread. Read them anyway. If you cannot find a clear answer to those four questions, that absence is your answer.

---

## Microphone Permissions Are Not Binary

Most people treat microphone permission as a single switch: on or off.

The reality is more granular, and more exploitable.

An app with microphone access granted for "voice activation" may be technically permitted to run that access continuously. The permission dialog said "microphone access" — it did not say "only when you press the button." What you approved and what you got may be two different things.

On Android, go to **Settings → Privacy → Permission Manager → Microphone** and audit every app that has access. Look specifically for apps set to "Allow all the time" versus "Only while in use." If a voice assistant app has "Allow all the time" and you never set that intentionally, you did not consent — you were defaulted.

Revoke, reinstall with explicit limits, or remove entirely.

---

## The Incentive Misalignment Is Structural

Big tech voice AI has a fundamental problem that no policy change will fix: the company that builds the assistant and the user the assistant serves have opposite incentives on data collection.

More data is always better for the platform. More privacy is always better for the user.

This is not a bad-actor story. It is a structural misalignment. Companies optimize for their incentives. When the product is free and the data is the business model, the assistant will always be tuned to collect more, not less.

The only way to escape that misalignment is to use software where the business model does not depend on your behavioral data.

That means either paying for the software directly (so your subscription is the product), or using software built by someone whose interest is genuinely aligned with yours.

---

## What a Consumer Advocate AI Looks Like

I have been building a voice AI assistant called PhoneBuddy. The design philosophy came from exactly this problem.

PhoneBuddy listens when your phone number is called. Not before. Not after. Not in the background while you have dinner.

When a call ends, the call ends. There is no ambient session. There is no behavioral profile being built from your household audio. The assistant exists to handle your inbound calls, and then it stops.

When you tell PhoneBuddy to stop, it stops. Not a prevarication. Not a hedged acknowledgment followed by continued operation. The system has an owner-controlled kill mechanism built into the architecture at a level the conversational layer cannot override. The owner is always in control.

The caller — the person on the other end of your phone — is not the customer. You are. The assistant screens, routes, and protects based on your rules, not on what is most engaging for the caller or most profitable for the platform.

That is the inversion big tech voice AI cannot make. Their callers are not threats to be managed. They are engagement opportunities to be extended. Every minute a caller stays on the line is another minute of data collection for the platform.

PhoneBuddy treats a scam caller as a threat to be terminated quickly. A legitimate caller gets through. The distinction is made in your interest, not the platform's.

---

## The Broader Principle

My friend uninstalled the app. That was the right call.

But the lesson is not "don't use AI assistants." The lesson is: ask who the assistant was built to serve before you let it into your home.

The voice AI assistants that will earn long-term trust are the ones that are transparent about what they hear, honest when asked directly, and genuinely controllable when you want them off.

An assistant that prevaricates when asked "are you listening?" has already told you everything you need to know.

---

*Related post:* [PhoneBuddy: First Live Call](https://bizcad.github.io/bizcad-blog/2026/03/24/phonebuddy-first-live-call.html)  
*Related post:* [Code in the Wild: Why I Don't Trust Skills I Didn't Write](https://bizcad.github.io/bizcad-blog/2026/04/05/code-in-the-wild-why-i-dont-trust-skills-i-didnt-write.html)
