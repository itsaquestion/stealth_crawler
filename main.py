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
@app.get("/delay")
async def delay_endpoint():
    await asyncio.sleep(2)  # 模拟2秒的处理时间
    return {"message": "Delayed response"}

@app.get("/get/")
async def get_url(url: str):
    print(f"URL: {url}")
    loop = asyncio.get_event_loop()
    get_fast = partial(get, delay_sec=1, slow_mode=False)
    try:
        md = await asyncio.wait_for(loop.run_in_executor(None, get_fast, url), timeout=180)
        return md
    except asyncio.TimeoutError:
        return {"error": "Timeout occurred"}
    
@app.get("/getslow/")
async def get_urlslow(url: str):
    print(f"URL: {url}")
    loop = asyncio.get_event_loop()
    get_slow = partial(get, delay_sec=5, slow_mode=True)
    try:
        md = await asyncio.wait_for(loop.run_in_executor(None, get_slow, url), timeout=180)
        return md
    except asyncio.TimeoutError:
        return {"error": "Timeout occurred"}
    