"""
A minimal Model Context Protocol (MCP) server written in pure Python.
Communicates via JSON-RPC 2.0 over standard I/O (stdio).

This illustrates how MCP works under the hood:
1. Agy starts this script as a subprocess.
2. Agy sends an 'initialize' JSON-RPC message.
3. Agy sends 'tools/list' to discover available tools.
4. When Agy calls a tool, it sends 'tools/call' with arguments.
5. This script responds with the tool's result on stdout.
"""

import json
import sys


def send_response(response: dict):
    line = json.dumps(response)
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def handle_initialize(msg_id):
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "custom-python-tools",
                "version": "1.0.0"
            }
        }
    }


def handle_tools_list(msg_id):
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "tools": [
                {
                    "name": "calculate_hash",
                    "description": "Calculates SHA-256 hash of a string.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string", "description": "Text to hash"}
                        },
                        "required": ["text"]
                    }
                }
            ]
        }
    }


def handle_tools_call(msg_id, params):
    name = params.get("name")
    arguments = params.get("arguments", {})

    if name == "calculate_hash":
        import hashlib
        text = arguments.get("text", "")
        h = hashlib.sha256(text.encode("utf-8")).hexdigest()
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": f"SHA-256: {h}"
                    }
                ]
            }
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {
            "code": -32601,
            "message": f"Tool '{name}' not found"
        }
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")

            if method == "initialize":
                send_response(handle_initialize(msg_id))
            elif method == "notifications/initialized":
                pass  # Client acknowledging initialization
            elif method == "tools/list":
                send_response(handle_tools_list(msg_id))
            elif method == "tools/call":
                send_response(handle_tools_call(msg_id, req.get("params", {})))
            else:
                if msg_id is not None:
                    send_response({
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "error": {"code": -32601, "message": "Method not found"}
                    })
        except Exception as e:
            if "msg_id" in locals() and msg_id is not None:
                send_response({
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32603, "message": str(e)}
                })


if __name__ == "__main__":
    main()
