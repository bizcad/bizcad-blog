"""
ask_blog.py — Ask questions about all blog posts using Claude.

Usage:
    py scripts/ask_blog.py "why did I build PhoneBuddy?"
    py scripts/ask_blog.py "what was I working on in February?"
"""

import sys
import os
import pathlib
import anthropic

POSTS_DIR = pathlib.Path(__file__).parent.parent / "_posts"
MODEL = "claude-haiku-4-5-20251001"

# Load API key from .env if not already in environment
def _load_api_key() -> str:
    if os.environ.get("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    env_path = pathlib.Path(r"G:\repos\AI\RoadTrip\workflows\014-PPA-voice-terminal\src\phone_buddy\.env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError("ANTHROPIC_API_KEY not found. Set the env var or add it to .env")


def load_all_posts() -> str:
    posts = sorted(POSTS_DIR.glob("*.md"))
    if not posts:
        return "(no posts found)"
    parts = []
    for p in posts:
        parts.append(f"=== {p.name} ===\n{p.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def ask(question: str) -> str:
    client = anthropic.Anthropic(api_key=_load_api_key())
    corpus = load_all_posts()
    system = (
        "You are a personal assistant helping the author query their own blog posts. "
        "The blog documents their journey building AI systems, agents, and tools. "
        "Answer concisely based only on what is in the posts. "
        "If the answer is not in the posts, say so."
    )
    user = f"Here are all my blog posts:\n\n{corpus}\n\n---\nQuestion: {question}"
    msg = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return msg.content[0].text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py scripts/ask_blog.py \"your question here\"")
        sys.exit(1)
    question = " ".join(sys.argv[1:])
    print(ask(question))
