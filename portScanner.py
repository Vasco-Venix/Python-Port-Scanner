#!/usr/bin/env python3

import socket
import time
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

TIMEOUT = 1


def port_scanner(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    try:
        result = s.connect_ex((host, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"

            print(f"\n[+] Port {port:<5} OPEN ({service.upper()})")

    except socket.error:
        pass

    finally:
        s.close()


def main():

    print("=" * 45)
    print("        PYTHON MULTITHREADED PORT SCANNER")
    print("=" * 45)

    host = input("Target IP or Hostname: ")

    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))

    ports = list(range(start_port, end_port + 1))

    start_time = time.time()

    print("\n Scanning...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:

        futures = []

        for port in ports:
            futures.append(executor.submit(port_scanner, host, port))

        for future in tqdm(futures, desc="Progress", unit="port"):
            future.result()

    end_time = time.time()

    print("\nScan Finished")
    print(f"Scanned {len(ports)} ports")
    print(f"Time elapsed: {end_time-start_time:.2f} seconds")

if __name__ == "__main__":
    main()
