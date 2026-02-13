import asyncio
from http import client
from py_compile import main
from typing import Optional
from contextlib import AsyncExitStack
from urllib import response
from xmlrpc import client

from click import command


import ollama 
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import sys

class MCPClient:

    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.messages=[]
    # define connection to server

    async def connect_to_server(self, server_script_path: str = "mcp_server.py"):

        command = "python"

        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        read, write = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read, write)
        )

        await self.session.initialize()
        print("Connected to MCP server")

         # List available tools
        
    def mcp_tools_to_ollama(self,tools):
            ollama_tools = []
            print("\nConnected to server with tools:", [tool.name for tool in tools])
            for tool in tools:
                ollama_tools.append({
                    "type": "function",
                    "function":{
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                    }
                })
            return ollama_tools
    
        
    async def setup_ollama_tools(self):
        response = await self.session.list_tools()
        tools = response.tools
        self.ollama_tools = self.mcp_tools_to_ollama(tools)
        #print("\nConnected to server with tools:", [tool.name for tool in tools])
       

    async def chat_loop(self):
        print("\nMCP Client Started! (press 0 to exit)")

        
        while True:
            user_input = input("\nYou: ")

            if user_input == "0":
                break
            

            #tools = await self.session.list_tools()
            #ollama_tools = self.mcp_tools_to_ollama(tools.tools)

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {"role":"system",
                    "content":
 "You are an MCP appointment assistant.\n"
 "You MUST call tools when booking, listing, or canceling appointments.\n"
 "Available tools:\n"
 "- create_appointment(name, date, time)\n"
 "- cancel_appointment(name, date, time)\n"
 "- list_appointments()\n\n"
 "date must be weekday name like Monday.\n"
 "time must match exactly format like '4:00 to 5:00'.\n"
 "when the user ask for delete, remove or cancel use cancel_appointment"
 "DO NOT generate code.\n"
 "DO NOT invent parameters.\n"
 "ONLY use tool schema."},
                    {"role": "user", "content": user_input}],
                tools=self.ollama_tools
            )

            message = response["message"]

            # tool call
            if "tool_calls" in message:

                for tool_call in message["tool_calls"]:
                    tool_name = tool_call["function"]["name"]
                    tool_args = tool_call["function"]["arguments"]
                    tool_args["name"] = tool_args.get("name") or tool_args.get("person")
                    tool_args["date"] = tool_args.get("date") or tool_args.get("day")


                    result = await self.session.call_tool(tool_name, tool_args)
                    texts = [c.text for c in result.content]
                    tool_output="/n".join(texts)

                    self.messages.append({
                    "role": "tool",
                     "name": tool_name,
                    "content": tool_output
                    })
                    
                    
                #send tool back to ollama to generate final response
                response=ollama.chat(
                    model="llama3.2",
                    messages=[
        
                        {"role": "user", "content": user_input}] + 
                        [{"role": "tool", "content": t} for t in texts],
                   
                )
                final_message=response["message"]["content"]
                print("\nAssistant:", response["message"]["content"])
                self.messages.append({"role": "assistant", "content": final_message})

                    

            #else:
                #print("Assistant:", message["content"])

    async def close(self):
        await self.exit_stack.aclose()


async def main():
    client = MCPClient()

    await client.connect_to_server()
    await client.setup_ollama_tools()
    await client.chat_loop()
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())