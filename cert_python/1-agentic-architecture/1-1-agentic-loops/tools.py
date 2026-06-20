import json


TOOLS = [
    {
        "name": "calculator",
        "description": "Evaluates a mathematical expression and returns the numeric result.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A mathematical expression (e.g., '2 + 2 * 3')",
                }
            },
            "required": ["expression"],
        },
    },
    {
        "name": "web_search",
        "description": "Searches the internet and returns a list of relevant search results with titles and snippets.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query",
                }
            },
            "required": ["query"],
        },
    },
]


def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"


def web_search(query: str) -> str:
    """Return mock web search results."""
    results = [
        {
            "title": "Claude AI Documentation",
            "url": "https://docs.anthropic.com",
            "snippet": "Official documentation for Claude API and Claude models.",
        },
        {
            "title": "Agentic AI Patterns",
            "url": "https://anthropic.com/research",
            "snippet": "Research on agentic AI systems and tool use patterns.",
        },
        {
            "title": "Python Anthropic SDK",
            "url": "https://github.com/anthropics/anthropic-sdk-python",
            "snippet": "Official Python client library for the Anthropic API.",
        },
    ]
    return json.dumps(results)


def process_tool_call(tool_name: str, tool_input: dict) -> str:
    """Dispatch a tool call to the appropriate handler."""
    if tool_name == "calculator":
        return calculate(tool_input["expression"])
    elif tool_name == "web_search":
        return web_search(tool_input["query"])
    else:
        return f"Error: Unknown tool '{tool_name}'"


if __name__ == "__main__":
    print("Calculator test:")
    print(f"  2 + 2 * 3 = {calculate('2 + 2 * 3')}")
    print(f"  (2 + 2) * 3 = {calculate('(2 + 2) * 3')}")
    print(f"  10 / 3 = {calculate('10 / 3')}")

    print("\nWeb search test:")
    results = web_search("agentic AI")
    print(f"  Results: {results}")

    print("\nTool dispatch test:")
    print(f"  calculator: {process_tool_call('calculator', {'expression': '5 ** 2'})}")
    print(f"  web_search: {process_tool_call('web_search', {'query': 'test'})}")
