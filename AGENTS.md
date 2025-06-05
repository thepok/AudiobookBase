# Agent Instructions

When creating a new story, follow this systematic approach:

## Phase 1: Story Foundation
1. Create a temporary folder such as `temp/<story-name>` at the repository root.
2. Inside this folder create `brainstorm.md` to explore initial story ideas, themes, and potential plot directions.
3. Create `characters.md` to define key characters with detailed backgrounds, motivations, and arcs.

## Phase 2: Hierarchical Story Structure

### Step 1: Initial Table of Contents
4. Create `toc_level1.md` with a high-level table of contents containing 8-15 major story sections with descriptive names.
   - Each section should represent a major story beat or arc
   - Use descriptive names like "The Mysterious Arrival" or "Confronting the Past" rather than generic "Chapter 1"
   - Include a 2-3 sentence description of what happens in each section

### Step 2: Detailed Breakdown
5. Create `toc_level2.md` where you break down EACH Level 1 section into 4-8 detailed story beats.
   - Each beat should be a specific moment, conversation, revelation, or action
   - Use very descriptive names that capture the essence of that moment
   - Include detailed 3-4 sentence descriptions of exactly what happens
   - This should result in 30-100 final story beats

## Phase 3: Chapter Writing
7. Create individual chapter files for EACH Level 2 story beat:
   - Name files as `chapter_1.3.txt` where the numbers correspond to the Level 1 section and Level 2 beat
   - Each chapter should be 1,500-2,500 words (focused on one specific story beat)
   - Write detailed, immersive prose for each story beat
   - Include rich descriptions, dialogue, character thoughts, and sensory details

## Phase 4: Final Assembly
8. Create `final_outline.md` that lists all chapters in order with their descriptive titles
9. Concatenate all chapter files in numerical order into `stories/<story-name>.txt`
10. Only commit the final file in `stories/`. Do not commit the temporary folder or intermediate files.

## Table of Contents Examples

### Level 1 Example:
```
1. The Stranger's Arrival - A mysterious figure appears in the quiet town, disrupting the peaceful routine
2. Uncovering Secrets - The protagonist begins to investigate the stranger's true purpose
3. The Hidden Truth - Revelations about the town's dark past come to light
```

### Level 2 Example (breaking down "The Stranger's Arrival"):
```
1.1 Morning Routine Interrupted - The protagonist's normal day is disrupted by unusual events in the town square
1.2 First Glimpse - Protagonist spots the mysterious stranger from across the street, noting their unusual appearance
1.3 Coffee Shop Encounter - Protagonist enters local café and has an awkward first conversation with the stranger
1.4 Unsettling Questions - Stranger asks specific questions about local history that seem too informed for a tourist
1.5 Town Gossip - Protagonist discusses the stranger with locals, learning everyone has different theories
1.6 Growing Unease - Protagonist returns home feeling disturbed by the encounter and begins to worry
```

## Writing Guidelines for Each Chapter

### Content Requirements:
- **Scene Setting**: Start each chapter by establishing time, place, atmosphere
- **Character Focus**: Center each chapter around character thoughts, feelings, and reactions
- **Dialogue**: Include natural conversations that advance the story
- **Sensory Details**: Use all five senses to make scenes vivid
- **Internal Monologue**: Show character's thought processes and decision-making
- **Action and Movement**: Describe physical actions and character movements in detail

### Length and Pacing:
- Each chapter should fully develop its assigned story beat
- Don't rush - take time to explore the moment thoroughly
- Include transitions between scenes within the chapter
- End with a natural pause or minor cliffhanger that leads to the next beat

## Tips for Writing Audiobook Content
- Write prose that flows naturally when read aloud
- Use dialogue tags consistently to help listeners track speakers
- Avoid complex sentence structures that could confuse listeners
- Include natural pauses and rhythm in the narrative flow
- Choose words that are clear and easy to pronounce
- Vary sentence length to maintain interest
- Use descriptive language that helps listeners visualize scenes

## Final Story Targets
- **Total chapters**: 30-100 individual chapters (one per Level 2 story beat)
- **Total word count**: 45,000-250,000 words (comprehensive novel length)
- **Story depth**: Every major plot point, character interaction, and story moment gets detailed coverage
- **Natural pacing**: The hierarchical breakdown ensures proper story flow and development

This systematic approach ensures comprehensive story coverage and prevents rushing through important plot points.