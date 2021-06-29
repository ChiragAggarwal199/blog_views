from torrequest import TorRequest
import threading
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

proxyPort, ctrlPort = 9050, 9051
EnterYourSiteName = r"" 

views = int(input("Views TO Give: "))
sent = 0
verify = True
TimePassed = time.time()


def run():
    global sent, TimePassed
    tr.get(site, headers=headers, verify=verify)
    sent += 1
    tr.reset_identity()
    print(f"\rSent: {sent} TimePassed: {time.time() - TimePassed}", end="")


if __name__ == '__main__':
    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
        views_multiple = 5
        for _ in range(0, int(views / views_multiple)):
            threads = []
            for i in range(views_multiple):
                t = threading.Thread(target=run)
                threads.append(t)
            for i in range(views_multiple):
                threads[i].start()
            for i in range(views_multiple):
                threads[i].join()

