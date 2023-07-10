import time
import requests

# from concurrent.futures import ThreadPoolExecutor
import concurrent.futures


def get_wiki_page_existence(wiki_page_url, var1):
    print(f"{var1}--{wiki_page_url}")
    response = requests.get(url=wiki_page_url)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status


wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(1, 5)]
x = [1, 2, 3, 4, 5, 6, 7, 8]

print("Running threaded:")
threaded_start = time.time()

executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="wiki")
tasks = []
task = executor.map(get_wiki_page_existence, wiki_page_urls, x)

for item in task:
    print(item)
