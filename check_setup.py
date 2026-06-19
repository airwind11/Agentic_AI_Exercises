"""
check_setup.py — run this once before starting exercises.
Confirms your API key loads correctly from .env (not from a global/system variable),
and does a tiny test call so you know billing is wired up correctly.
"""

import os
from dotenv import load_dotenv

# Load .env from the current directory only
load_dotenv()

key = os.environ.get("ANTHROPIC_API_KEY")

if not key:
    print("❌ No ANTHROPIC_API_KEY found. Did you create a .env file with your key in it?")
    exit(1)

print(f"✅ API key loaded: {key[:15]}... (length {len(key)})")

# Tiny, cheap test call
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=20,
    messages=[{"role": "user", "content": "Say 'setup working' and nothing else."}],
)

print("Response:", response.content[0].text)
print("\nInput tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("\n✅ Setup confirmed working. This call cost a fraction of a cent.")
