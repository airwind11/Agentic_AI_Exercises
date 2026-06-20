import argparse
import json
import os
from dotenv import load_dotenv
from anthropic import Anthropic

from tools import TOOLS, process_tool_call

load_dotenv()


def run_agentic_loop(verbose: bool = False):
    """Run the agentic loop: send messages to Claude, check stop_reason, handle tool calls."""
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    model = "claude-haiku-4-5-20251001"
    MAX_ITERATIONS = 20
    iteration = 0

    messages = [
        {
            "role": "user",
            "content": "Search the web for 'agentic AI', then take the number of results returned and calculate that number multiplied by 12",
        }
    ]

    print(f"User: {messages[0]['content']}\n")

    while True:
        if verbose:
            print("\n[VERBOSE] Messages being sent to Claude:")
            print(json.dumps(messages, indent=2))

        response = client.messages.create(
            model=model,
            max_tokens=1000,
            tools=TOOLS,
            messages=messages,
        )

        iteration += 1

        messages.append({
                "role": "assistant",
                "content": [block.model_dump() for block in response.content]
            })

        if verbose:
            print("\n[VERBOSE] Full response object:")
            print(json.dumps(response.model_dump(), indent=2, default=str))

        print(f"Stop reason: {response.stop_reason}")

        if response.stop_reason == "tool_use":

            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    result = process_tool_call(tool_name, tool_input)
                    print(f"Tool: {tool_name}")
                    print(f"  Input: {tool_input}")
                    print(f"  Result: {result}\n")

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )

            messages.append({"role": "user", "content": tool_results})

        elif response.stop_reason == "end_turn":
            for block in response.content:
                if block.type == "text":
                    print(f"Claude: {block.text}")
            break
        else:
            print(f"Unexpected stop reason: {response.stop_reason}")
            break

        if iteration >= MAX_ITERATIONS:
            print(f"\nWarning: Safety cap of {MAX_ITERATIONS} API calls reached. Exiting loop.")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the agentic loop")
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print full JSON payloads of messages and responses"
    )
    args = parser.parse_args()
    run_agentic_loop(verbose=args.verbose)
