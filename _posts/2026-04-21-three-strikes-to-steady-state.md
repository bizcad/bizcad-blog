---
title: "Three Strikes to Steady State"
date: '2026-04-21T12:00:00.000Z'
excerpt: "Runaway loops do not need a complex cure. They need baseball: three strikes, bounded innings, in-game rules and between-game evolution."
author: Nicholas Stein
---

*April 21, 2026 - Nick Stein*

---

I used to treat recursive failure or a runaway loop as a bug in the architecture.

Now I treat it as a game-state problem.

The fix is not mystical. It is baseball.

Three strikes and you are out.

Not out forever. Out for this inning.

That one boundary changes everything.

---

## The Mapping

If you already know baseball, the SRCGEEE and FACA model drops in cleanly:

- **S (Sensation)** is the National Anthem and the umpire's "play ball." The game is live; the next situation is on the field.
- **R (Research or Retrieval)** is the scouting report. The weather, the opponent, the field conditions, the strategy.
- **C (Compose)** is the pitcher. It decides on the next executable play and delivers it.
- **G (Gate)** is the umpire. Ball, strike, safe, out, fair ball, or foul. No sentiment, just rule enforcement.
- **E1 (Execute)** is the batter. Swing, miss, hit, foul, advance, home run. Sometimes a walk.
- **E2 (Evaluate)** is the infield and scoring table. What actually happened?
- **E3 (Evolve)** is the dugout and staff. Coach, heal, practice, schedule the next game.

The important part is what this model forces us to admit:

Execution is not a moral event.
It is an at-bat.

Sometimes the run scores.
Sometimes it flies out.
Sometimes it dies on an error.

All of those are valid outcomes if they are scored correctly.

---

## Three Strikes Means Bounded Recursion

A recursive system without strike logic is not intelligent. It is just trapped.

The out condition should be explicit and mechanical:

1. Same failure bucket three times goes to E2 triage and E3 scheduled remediation.
2. Global transition fuse exceeded goes to safety escalation.
3. No state delta across turns means that the game is over by steady state.

That third one matters.

No state delta is not stagnation. It is convergence.
The programmatic run has reached its resting shape.
That is not a failure. It is a completion.
Completion is completion, even when it is not the outcome we wanted.

---

## Failure Is Still Completion

Most systems treat catastrophic failure as "work not done."

That framing creates silent retry loops and fake optimism.

In this model, failure is complete when:

- the exception state is captured,
- the execution history is preserved,
- the evidence packet is attached,
- remediation is scheduled.

That is an out, not a disappearance.

An unhandled 500 is not just a technical defect. It is an accounting defect.
The play happened. Score it.

---

## The Emergent DAG Is the Box Score

The execution should be planned, but the plan is not the truth.
The actual history is the truth.

That is why the emergent DAG matters. It is the box score of what the system actually did under pressure.

If the Supervisor adjusts the plan mid-run to account for unexpected information, that is not corruption. That is reality management.

A good system records the adjustment, not a fantasy of linear intent.

---

## Between Games Is Where Improvement Lives

This is the separation that keeps systems sane:

- **In game**: bounded execution.
- **Between games**: evolution.

Between games you coach, heal, trade players, train, and practice for the next opponent.

In architecture terms:

- update failure vocabularies,
- promote stable patterns,
- retire brittle workloads,
- add or replace primitives,
- tighten or loosen gates,
- adjust model routing.

Do not ask a workload to do all of that while it is still hot.

That is how systems become haunted.

---

## Why This Works

The baseball frame enforces five properties that agentic systems often lose as they scale:

1. **Termination is explicit**
No endless recursive self-conversation.

2. **Failure is auditable**
Nothing disappears into retry fog.

3. **Steady state is respected**
Convergence is not mislabeled as weakness.

4. **Learning has a lane**
Improvement happens between runs. You evolve and set up the next run. You do not interfere with the current one.

5. **Human oversight has a role without micromanagement**
HITLs are the league office, not the umpire. They write the rulebook between games; they do not call balls and strikes.

---

## The Practical Rule

If you remember one line, use this:

**No more than three strikes per failure bucket per game. Steady state delta means game over. Evolution happens between games.**

That one sentence turns runaway loops into bounded, inspectable, improvable operations.

And that is the whole point of FACA/SRCGEEE: not to avoid failure, but to metabolize it.

---

*Related post:* [The Planned Death of Memory](https://bizcad.github.io/bizcad-blog/2026/04/18/the-planned-death-of-memory.html)  
*Related post:* [Hallucinations Are Skipped Steps](https://bizcad.github.io/bizcad-blog/2026/03/31/hallucinations-are-skipped-steps.html)
