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
5. Create `toc_level2.md` where you break down EACH Level 1 section into 3-5 sub-sections.
   - Each sub-section should be a distinct scene or story moment
   - Use descriptive names and include 1-2 sentence descriptions
   - This should result in 25-50 total sub-sections

### Step 3: Fine-Grained Structure  
6. Create `toc_level3.md` where you break down EACH Level 2 sub-section into 2-4 detailed story beats.
   - Each beat should be a specific moment, conversation, revelation, or action
   - Use very descriptive names that capture the essence of that moment
   - Include detailed 3-4 sentence descriptions of exactly what happens
   - This should result in 50-150 final story beats

## Phase 3: Chapter Writing
7. Create individual chapter files for EACH Level 3 story beat:
   - Name files as `chapter_3.2.5.txt` where the numbers correspond to the Level 1, Level 2, and Level 3 sections
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
1.1 Morning Routine Interrupted - The protagonist's normal day is disrupted by unusual events
1.2 First Encounter - The protagonist meets the mysterious stranger for the first time
1.3 Town Reactions - Various townspeople react differently to the stranger's presence
1.4 Growing Suspicion - The protagonist begins to sense something is not right
```

### Level 3 Example (breaking down "First Encounter"):
```
1.2.1 The Coffee Shop Meeting - Protagonist enters local café and notices the stranger sitting alone, observing everyone with unusual intensity
1.2.2 Awkward Introduction - Stranger approaches protagonist, introduces themselves with a story that doesn't quite add up
1.2.3 Unsettling Questions - Stranger asks specific questions about local history that seem too informed for a tourist
1.2.4 The Quick Exit - Protagonist makes an excuse to leave, feeling disturbed by the encounter
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
- **Total chapters**: 50-150 individual chapters (one per Level 3 story beat)
- **Total word count**: 75,000-300,000 words (comprehensive novel length)
- **Story depth**: Every major plot point, character interaction, and story moment gets detailed coverage
- **Natural pacing**: The hierarchical breakdown ensures proper story flow and development

This systematic approach ensures comprehensive story coverage and prevents rushing through important plot points.