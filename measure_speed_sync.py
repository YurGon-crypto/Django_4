import time
import httpx


def measure_sync_speed():
    base_url = "http://127.0.0.1:8000"
    endpoints = ["/endpoint1/", "/endpoint2/", "/endpoint3/"]

    total_time = 0

    with httpx.Client() as client:
        for endpoint in endpoints:
            start_time = time.time()
            response = client.get(base_url + endpoint)
            elapsed_time = time.time() - start_time

            print(f"Endpoint: {endpoint}, Time: {elapsed_time} seconds")
            total_time += elapsed_time

    print(f"Total Time for Synchronous Requests: {total_time} seconds")


if __name__ == "__main__":
    measure_sync_speed()
