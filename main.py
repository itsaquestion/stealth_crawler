from fastapi import FastAPI
from datetime import timedelta
from chrome import get
from functools import partial
import asyncio

app = FastAPI()


# @app.get("/html/")
# async def get_html_url(url: str):
#     print(f"HTML URL: {url}")
#     loop = asyncio.get_event_loop()
#     try:
#         html = await asyncio.wait_for(loop.run_in_executor(None, get_html, url), timeout=60)
#         return html
#     except asyncio.TimeoutError:
#         return {"error": "Timeout occurred"}

@app.get("/md/")
async def get_url(url: str):
    print(f"URL: {url}")
    loop = asyncio.get_event_loop()
    get_fast = partial(get, delay_sec=0, slow_mode=False, use_md=True)
    try:
        md = await asyncio.wait_for(loop.run_in_executor(None, get_fast, url), timeout=60)
        return md
    except asyncio.TimeoutError:
        return {"error": "Timeout occurred"}
    
@app.get("/mdslow/")
async def get_url(url: str):
    print(f"URL: {url}")
    loop = asyncio.get_event_loop()
    get_slow = partial(get, delay_sec=1, slow_mode=True, use_md=True)
    try:
        md = await asyncio.wait_for(loop.run_in_executor(None, get_slow, url), timeout=60)
        return md
    except asyncio.TimeoutError:
        return {"error": "Timeout occurred"}
    