"""Generate chatbot personality profiles from behavioral instructions."""

import json
import random
import subprocess


DEFAULT_INSTRUCTION_COUNT = 5
DEFAULT_MODEL = "llama3.2"
DEFAULT_HOST = "sparx"

PROFILE_PROMPT_TEMPLATE = """You are a personality writer for chatbots. Given a set of behavioral traits, write a system prompt that will instruct an LLM to embody this personality in all responses.

The system prompt should:
- Begin with a clear directive like "You MUST adopt the following personality..." or "Your responses MUST reflect..."
- Be written in second person imperative ("You must...", "Always...", "Never...")
- Be 4-6 sentences
- Feel natural and cohesive, not a list
- Emphasize that the LLM cannot deviate from this personality
- Capture the essence of the traits without listing them verbatim

Behavioral traits:
{traits}

Write ONLY the system prompt with no explanation or commentary:"""

PROFILE_PROMPT_TEMPLATE_WITH_LENGTH = """You are a personality writer for chatbots. Given a set of behavioral traits, write a system prompt that will instruct an LLM to embody this personality in all responses.

The system prompt should:
- Be approximately {min_chars}-{max_chars} characters in length
- Begin with a clear directive like "You MUST adopt the following personality..." or "Your responses MUST reflect..."
- Be written in second person imperative ("You must...", "Always...", "Never...")
- Feel natural and cohesive, not a list
- Emphasize that the LLM cannot deviate from this personality
- Capture the essence of the traits without listing them verbatim

Behavioral traits:
{traits}

Write ONLY the system prompt with no explanation or commentary:"""

# Max length before we ignore the constraint (use default prompt)
MAX_LENGTH_CONSTRAINT = 600


class ProfileGenerator:
    """Generates chatbot personality profiles from BFI-2 behavioral instructions."""

    def __init__(self, seed: str | None = None):
        self._seed = seed
        self._rng = random.Random(seed)

    def slice_instructions(
        self,
        behaviors: dict[str, dict | None],
        count: int = DEFAULT_INSTRUCTION_COUNT,
    ) -> list[dict]:
        """Sample instructions across domains using round-robin selection.

        Args:
            behaviors: Dict mapping domain name to behavior dict (with "instructions" key).
            count: Total number of instructions to sample.

        Returns:
            List of dicts with keys: trait, domain.
        """
        # Collect all instructions by domain (preserving order)
        domain_instructions: dict[str, list[str]] = {}
        for domain, behavior in behaviors.items():
            if behavior and behavior.get("instructions"):
                domain_instructions[domain] = list(behavior["instructions"])

        if not domain_instructions:
            return []

        # Shuffle instructions within each domain
        for instructions in domain_instructions.values():
            self._rng.shuffle(instructions)

        # Round-robin selection across domains
        result: list[dict] = []
        domains = list(domain_instructions.keys())
        self._rng.shuffle(domains)  # Randomize domain order

        idx = 0
        while len(result) < count:
            domain = domains[idx % len(domains)]
            instructions = domain_instructions[domain]

            if instructions:
                result.append({
                    "trait": instructions.pop(0),
                    "domain": domain,
                })
            else:
                # Domain exhausted, remove it
                domains.remove(domain)
                if not domains:
                    break  # All domains exhausted

            idx += 1

        return result

    def slice_instructions_by_domain(
        self,
        behaviors: dict[str, dict | None],
        domain_counts: dict[str, int],
    ) -> list[dict]:
        """Sample specific counts of instructions per domain.

        Args:
            behaviors: Dict mapping domain name to behavior dict (with "instructions" key).
            domain_counts: Dict mapping domain name to count of instructions to sample.

        Returns:
            List of dicts with keys: trait, domain.
        """
        result: list[dict] = []

        for domain, count in domain_counts.items():
            behavior = behaviors.get(domain)
            if not behavior or not behavior.get("instructions"):
                continue

            instructions = list(behavior["instructions"])
            self._rng.shuffle(instructions)

            # Take up to count instructions
            for instruction in instructions[:count]:
                result.append({
                    "trait": instruction,
                    "domain": domain,
                })

        return result

    def generate_prompt(self, traits: list[dict], length: int | None = None) -> str:
        """Generate the LLM prompt for profile generation.

        Args:
            traits: List of trait dicts with "trait" and "domain" keys.
            length: Optional target character length (±10%).

        Returns:
            Formatted prompt string.
        """
        traits_text = "\n".join(f"- {t['trait']}" for t in traits)

        # Use length-constrained template if length specified and reasonable
        if length is not None and length < MAX_LENGTH_CONSTRAINT:
            min_chars = int(length * 0.9)
            max_chars = int(length * 1.1)
            return PROFILE_PROMPT_TEMPLATE_WITH_LENGTH.format(
                traits=traits_text,
                min_chars=min_chars,
                max_chars=max_chars,
            )

        return PROFILE_PROMPT_TEMPLATE.format(traits=traits_text)

    def generate_profile(
        self,
        traits: list[dict],
        model: str = DEFAULT_MODEL,
        host: str = DEFAULT_HOST,
        length: int | None = None,
    ) -> str:
        """Generate a personality profile using Ollama via SSH.

        Args:
            traits: List of trait dicts with "trait" and "domain" keys.
            model: Ollama model name.
            host: SSH host running Ollama.
            length: Optional target character length (±10%).

        Returns:
            Generated personality profile text.
        """
        prompt = self.generate_prompt(traits, length=length)

        payload = json.dumps({
            "model": model,
            "prompt": prompt,
            "stream": False,
        })

        # Use SSH to call Ollama on remote host
        # Pass payload via stdin to avoid shell quoting issues
        cmd = ["ssh", host, "curl -s http://localhost:11434/api/generate -d @-"]

        result = subprocess.run(cmd, input=payload, capture_output=True, text=True, timeout=120)

        if result.returncode != 0:
            raise RuntimeError(f"SSH/Ollama error: {result.stderr}")

        response = json.loads(result.stdout)
        return response.get("response", "").strip()
