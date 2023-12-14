import asyncio
import httpx

async def measure_async_speed():
    base_url = "http://127.0.0.1:8000"
    endpoints = ["/async_endpoint1/", "/async_endpoint2/", "/async_endpoint3/"]

    total_time = 0

    async with httpx.AsyncClient() as client:
        for endpoint in endpoints:
            start_time = time.time()
            response = await client.get(base_url + endpoint)
            elapsed_time = time.time() - start_time

            print(f"Endpoint: {endpoint}, Time: {elapsed_time} seconds")
            total_time += elapsed_time

    print(f"Total Time for Asynchronous Requests: {total_time} seconds")

if __name__ == "__main__":
    asyncio.run(measure_async_speed())
