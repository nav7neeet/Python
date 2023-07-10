import time
import requests

# from concurrent.futures import ThreadPoolExecutor
import concurrent.futures


def get_wiki_page_existence(wiki_page_url, timeout=10):
    # if wiki_page_url == "https://en.wikipedia.org/wiki/10":
    #     print("************* sleeping")
    #     time.sleep(10)
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status


print("Running threaded:")
threaded_start = time.time()

"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    tasks = []

    for url in wiki_page_urls:
        # print(get_wiki_page_existence(wiki_page_url=url))
        task = executor.submit(get_wiki_page_existence, wiki_page_url=url)
        tasks.append(task)
    for item in concurrent.futures.as_completed(tasks):
        print(item.result())
"""

wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(1, 5)]

executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="wiki")
tasks = []
# tasks = {}

# for url in wiki_page_urls:
# print(get_wiki_page_existence(wiki_page_url=url))
# task = executor.submit(get_wiki_page_existence, wiki_page_url=url)
task = executor.map(get_wiki_page_existence, "test", wiki_page_urls, chunksize=50)
# tasks.append(task)
# tasks[url] = task

for item in task:
    print(item)
    # print(tasks[]


executor.shutdown()

print("Time:", time.time() - threaded_start)

# print("Running without threads:")
# without_threads_start = time.time()

# for url in wiki_page_urls:
#     # print(get_wiki_page_existence(wiki_page_url=url))
#     pool = ThreadPoolExecutor()
#     status = pool.submit(get_wiki_page_existence, wiki_page_url=url)
#     print(status.result())

# print("Time:", time.time() - without_threads_start)
