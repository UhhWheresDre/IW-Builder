# Narrative craft

Evidence labels and compatibility: [Evidence.md](Evidence.md).

## Opening and cast

A strong opening gives the player an immediate, legible situation rather than an encyclopedia. Put deep backstory in relevant cards/lore, keep firstInput actionable, and let early choices expose the setting. Define what is interesting about success, failure and doing nothing. Distinct NPC motives create better choices than merely different appearances. For a mystery, track who knows each clue; for a social story, give relationships room to change; for a simulation, make recurring decisions and their consequences legible.

Write a few observable voice cues rather than labels alone: an impatient engineer interrupts with practical questions; a guarded diplomat answers indirectly. Describe setting-specific deviations from common knowledge, not every ordinary object. Keep instructions consistent with examples. Test the first turn as carefully as the machinery: does it introduce the right player, place, people and viable options without prematurely resolving the premise?

For an existing world, preserve IDs and unrelated fields, report intended changes, validate the complete output and test the affected behavior. A live copy and its base world are separate. Compare active blocks, Evaluation, trigger counts, PawScript errors and tracker values for the same turn when diagnosing a discrepancy. A rendered story alone cannot identify which stage failed.


## Distinct characters
Give each recurring NPC a want, a voice, a point of friction and at least one physical or behavioral distinction. A voice is more useful than a stock adjective: one person corrects estimates before discussing feelings, another answers concern with an offer of food. Put essential opening facts in firstInput or an always-on block, with concise NPC summaries. Reveal secrets through opportunities rather than an opening exposition dump.

## Player-facing opportunities
Give a concrete immediate problem with several reasonable approaches. Describe what the player can notice; reserve hidden facts for discovery. Allow ordinary social and exploratory actions without demanding a mechanical event for everything. Use failure and partial success to change the situation without erasing agency. A bounded ending needs clear accomplishment criteria; an ongoing world needs recurring tensions and evolving relationships.

See ../examples/narrative-last-ferry.json for a narrative-first world with a focused opening, distinct voices, optional lore and bounded AI memory. It is an authoring example, not a runtime-qualified benchmark.
