# main.py
from fastapi import FastAPI
from fastapi.testclient import TestClient
import asyncio
import aiohttp
import time

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 单线程测试函数
def test_single_thread():
    start_time = time.time()
    for _ in range(5):
        response = client.get("/delay")
        assert response.status_code == 200
    end_time = time.time()
    return end_time - start_time

# 多线程测试函数
async def test_multi_thread():
    async def fetch():
        async with aiohttp.ClientSession() as session:
            async with session.get("http://127.0.0.1:8000/delay") as response:
                assert response.status == 200
                await response.text()

    start_time = time.time()
    await asyncio.gather(*[fetch() for _ in range(5)])
    end_time = time.time()
    return end_time - start_time

# 主函数
def main():
    print("开始单线程测试...")
    single_thread_time = test_single_thread()
    print(f"单线程测试完成，耗时: {single_thread_time:.2f} 秒")

    print("\n开始多线程测试...")
    multi_thread_time = asyncio.run(test_multi_thread())
    print(f"多线程测试完成，耗时: {multi_thread_time:.2f} 秒")

    print(f"\n单线程比多线程慢 {single_thread_time / multi_thread_time:.2f} 倍")

if __name__ == "__main__":
    main()