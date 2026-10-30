# Agent Instructions For This Repo

## Product Context

This repo supports the IAG hackathon pitch for **CreatorTrust Shield**: a creator identity-protection and cyber liability concept for content creators, streamers, esports players, influencers, and public figures.

The strongest product story is:

> CreatorTrust Shield helps creators protect their face, voice, content, sponsors, and audience trust from deepfake, impersonation, fake sponsorship, and cyber identity incidents.

When creating presentation, design, or pitch materials, align the product to IAG's customer journey stages:

- **Realise**: creators recognise their online identity is an asset worth protecting.
- **Explore**: creators need a clear way to understand what is authentic, suspicious, or impersonation.
- **Decide**: creators need confidence that support exists if an identity incident happens.

## Pitch Deck Design Philosophy

Use a visual-first design approach inspired by high-craft canvas design principles, adapted for editable pitch decks.

Before creating or revising slides, define the visual idea in one sentence. For this project, the preferred visual direction is:

> A premium cyber-insurance command centre: dark, calm, precise, evidence-led, and trusted.

Design should feel senior, deliberate, and polished:

- Use minimal text. Each slide should communicate one main idea.
- Prefer diagrams, spatial flow, hierarchy, and contrast over paragraphs.
- Treat text as a visual element: short labels, strong headlines, sparse supporting copy.
- Use dark navy/black foundations with cyan, teal, violet, or amber accents.
- Use generous spacing and consistent alignment.
- Avoid clutter, decorative blobs, generic gradients, and busy dashboards pasted onto slides.
- Make every slide feel like it was carefully designed, not auto-generated.

## Slide Structure Guidance

For hackathon pitches, use this narrative sequence unless the user asks otherwise:

1. **Hook**: a concrete creator incident scenario.
2. **Problem**: why creator identity risk matters.
3. **Journey Fit**: Realise, Explore, Decide.
4. **Solution**: CreatorTrust Shield in one sentence.
5. **Demo**: registry -> scan -> analysis -> response.
6. **Customer Impact**: before and after.
7. **Recommendation**: pilot, learn, then scale.
8. **Iteration**: what the team improved and why.

## Responsible Technology Framing

Always be clear that the hackathon prototype uses simulated or deterministic components where applicable:

- Do not claim real deepfake detection unless implemented and validated.
- Say "simulated AI evidence" or "deterministic prototype analysis" when describing current functionality.
- Frame the prototype as a workflow demonstration and decision-support artifact, not a production insurance system.
- Emphasise that the trusted creator registry makes the approach more explainable than a generic detector.

## File And Output Preferences

- For editable slide decks, generate `.pptx` files in `presentation/`.
- Keep generator scripts in `presentation/` so decks are reproducible.
- If creating visual-only poster/art assets, create `.png` or `.pdf` plus a short design philosophy `.md`.
- Do not overwrite existing decks unless explicitly requested; create a clear versioned filename.
- Update `README.md` when adding major presentation artifacts.

## Quality Bar

Before finishing presentation work, check:

- Slide count is appropriate for a 3 minute pitch.
- Each slide has one clear message.
- No slide is text-heavy.
- No text is clipped or too small.
- The demo path matches the actual prototype.
- The deck directly supports the judging criteria:
  - customer value and impact
  - creative and responsible technology
  - pitch clarity
  - thinking and iteration
