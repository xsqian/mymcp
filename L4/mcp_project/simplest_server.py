from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.middleware.cors import CORSMiddleware  # <--- Add this
import uvicorn

# mcp = FastMCP("Python SSE Server")
mcp = FastMCP("Python SSE Server",
              host="0.0.0.0",
              port=8000)

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

# Create the Starlette app
app = Starlette(
    routes=[
        Mount("/", app=mcp.sse_app()),
    ]
)

# ⚠️ Add this block to fix the "SSE Error"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows the Inspector to connect
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # Instead of uvicorn.run(app...)
    # mcp.run(transport="sse")