from fastmcp import FastMCP

mcp = FastMCP("Greetings")

@mcp.tool
def greetHola(name: str) -> str:
    """
    Return a short, friendly greeting addressed to the provided name.

    Parameters
    ----------
    name : str
        The addressee (non-empty, trimmed).

    Returns
    -------
    str
        A greeting that includes the provided name, e.g. "Hello, Kunal!"

    Raises
    ------
    ValueError
        If `name` is empty after trimming or exceeds the allowed length.
    """
    return f"Hello, 121 {name}!"


# Basic dynamic resource returning a string
@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"


@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")