# Project Structure

## Core Code
- `src/`: Python code only (engine, scripts, utils).

## Configuration
- `config/flows/main.yml`: main production flow.
- `config/flows/archive/`: local/experimental legacy flows.

## Prompts
- `prompts/`: active LLM prompts.
- `prompts/archive/`: legacy/duplicate prompt versions.

## Lore Content
- `content/lore/`: active lore files.
- `content/lore/archive/`: historical/alternate lore snapshots.

## Runtime Data
- `data/state/`: mutable runtime state (`position.json`, `state.json`, counters).
- `data/cache/plan/`: cache/prompts auxiliares legacy para iteración rápida.
- `data/chapters/memory/`: chapter memory snapshots.
- `data/chapters/recap/`: recap files.
- `data/archive/`: archived chapter material.

## Visual Assets
- `assets/styles/chapter.css`: PDF stylesheet.

## Generated Artifacts
- `artifacts/pdf/`: exported PDF artifacts.
- `project/`: generated story outputs by saga/book/language.

## Entrypoints
- `launch_flow.py`: runs flow (`--flow`, `--input`).
- `generate_next_chapter.py`: production runner with state rollback on failure.
- `validate_yaml.py`: validates YAML (`python validate_yaml.py [path]`).
- `src/scripts/run_flow.py`: low-level flow runner.
