from fastmcp import FastMCP
import random


mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a+b

@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Guessing the number between two values

    Args:
        min_val: minimum threshold to guess value
        max_val: maximum threshold to guess value

    Returns:
        Guessed value between min_val and max_val
    """
    return random.randint(min_val,max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """Get the information about the sever."""
    info = {
        "name":"Simple Calculator Server",
        "version":"1.0.0",
        "description":"A basic mcp server with math tools",
        "tools": ["add","random_number"],
        "author":"Your Name"
    }

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)