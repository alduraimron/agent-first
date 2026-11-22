# Interaction skill provenance

The selector and 20 `interaction-*` skills are adapted from the user-supplied **Agent-First Interaction & Reasoning Skills - Source Overlay**, supplied as `agent-first-interaction-skills/agent-first-interaction`. Its `README.md`, section **Source and attribution**, states:

> The names and general interaction concepts are informed by publicly available examples in pstack (Lauren Tan, `cursor/plugins`) and Agent Skills (Addy Osmani). The procedures here are newly authored and not a verbatim copy of those projects. Their existing trademarks, licenses and attribution requirements apply if you later copy upstream files. Names like `idea-refine` and `in-your-own-words` are functional patterns, not assertions of exact matching upstream implementations.

This import preserves that supplied attribution. It does not assert an upstream license grant or claim that upstream files were copied. The supplied README is the provenance source, not evidence that native behavioral evaluations passed.

Local adaptations retain all 20 intents and concrete procedures while repairing YAML descriptions, using ASCII hyphens, clarifying selective loading and engineering routing, limiting requested artifact writes, preserving optional interaction advisors, distinguishing source/history from runtime proof, and keeping private reasoning and unobserved cleanup claims out of handoffs and evidence summaries. Shared interaction boundaries are in [the selector](skill://af-interaction).

The agreement-before-changes gate is informed by [Matt Pocock's `grilling` skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): settle material decisions with the user and get confirmation before acting. Agent-First asks one decision per turn and exempts exact, low-risk edits.
