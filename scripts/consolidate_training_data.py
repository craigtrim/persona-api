#!/usr/bin/env python3
"""
Consolidate training_data/*.jsonl files into a single JSON file
with one randomly selected instruction per score combination.

Output format:
{
    "A1,C1,E1,O3,N1": "Your responses MUST reflect...",
    "A2,C3,E4,O1,N5": "You MUST adopt a personality...",
    ...
}
"""

import json
import random
from pathlib import Path

def main():
    training_dir = Path(__file__).parent.parent / "training_data"
    output_path = Path(__file__).parent.parent.parent / "persona-ui" / "src" / "lib" / "data" / "system_prompts.json"

    # Collect all instructions by score combo
    instructions_by_score: dict[str, list[str]] = {}

    jsonl_files = sorted(training_dir.glob("training_data_*.jsonl"))
    print(f"Found {len(jsonl_files)} JSONL files")

    for jsonl_file in jsonl_files:
        with open(jsonl_file, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    scores = data["inputs"]["scores"]
                    output = data["output"]

                    if scores not in instructions_by_score:
                        instructions_by_score[scores] = []
                    instructions_by_score[scores].append(output)
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error parsing line in {jsonl_file}: {e}")
                    continue

    print(f"Found {len(instructions_by_score)} unique score combinations")

    # Pick one random instruction per score combo
    random.seed(42)  # For reproducibility
    result: dict[str, str] = {}

    for scores, instructions in instructions_by_score.items():
        result[scores] = random.choice(instructions)

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {len(result)} entries to {output_path}")

if __name__ == "__main__":
    main()
