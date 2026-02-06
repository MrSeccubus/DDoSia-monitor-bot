#!/usr/bin/env python3

import yaml
from telethon import TelegramClient, events
import asyncio
import os
import yaml
from datetime import datetime
import requests
import re

# Load config
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

api_id = config['telegram']['api_id']
api_hash = config['telegram']['api_hash']

group_invite = config['telegram']['group_invite']  # e.g. "https://t.me/+IJqmkbjguH04MTFk"

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        entity = await client.get_entity(group_invite)
        async for msg in client.iter_messages(entity, limit=1):
            if msg.date.timestamp() != state["last_msg"] : 
                state["last_msg"] = msg.date.timestamp()
                save_state(state)
                output(msg)
            

def read_state() :
    state = {}
    if os.path.isfile("state.yml") :
        with open("state.yml") as f:
            state =  yaml.safe_load(f)
    else:
        state = {
            "last_msg" : 0
        }
        save_state(state)
    return state

def save_state(state) :
    with open("state.yml", "w") as f:
        yaml.dump(state, f,default_flow_style=False)   

def output(msg) :   
    dutch = False  
    new_dutch = ""  
    if ".nl\n" in msg.message :
        dutch = True
    for line in msg.message.split("\n") :
        if re.match("^\+ .*\.nl$",line) :
            new_dutch="NEW"
    if "console" in config["out"] and config["out"]["console"] :
        if dutch:
            print(f"There are {new_dutch} Dutch tagets in the DDosia list\n")
        print(msg.message)
    if "slack" in config["out"] and len(config["out"]["slack"]) > 0:
        payload = { "text" : msg.message }
        if dutch:
            payload["text"] = f"<!here> {new_dutch} Dutch targets observed in DDoSia config\n\n"+payload["text"]
        for hook in config["out"]["slack"]:
            response = requests.post(hook, json=payload)


if __name__ == '__main__':
    state = read_state()
    asyncio.run(main())
