Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from concurrent.futures import ThreadPoolExecutor
import socket

def scan_port(ip, port):
    """
    Scans a single port on the given IP address.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)  # Reduced timeout for faster scanning
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN on {ip}")
    except Exception:
        pass

def scan_host(ip, max_threads=50, port_range=range(1, 1025)):
    """
    Scans a range of ports on a given host using multithreading.
...     """
...     print(f"\nStarting scan on {ip}...")
...     print(f"Scanning ports from {port_range.start} to {port_range.stop - 1} using {max_threads} threads.\n")
...     with ThreadPoolExecutor(max_threads) as executor:
...         for port in port_range:
...             executor.submit(scan_port, ip, port)
...     print("\nScan complete!")
... 
... def get_user_input():
...     """
...     Collects target IP, thread count, and port range from the user.
...     """
...     print("Welcome to the Port Scanner!")
...     print("This tool will scan a range of ports on a target IP address to check their status.\n")
... 
...     # Get target IP
...     target_ip = input("Enter the target IP address: ").strip()
... 
...     # Get maximum threads
...     while True:
...         try:
...             max_threads = int(input("Enter the number of threads to use (default is 50): ").strip() or 50)
...             if max_threads > 0:
...                 break
...             else:
...                 print("Please enter a positive number.")
...         except ValueError:
...             print("Invalid input. Please enter a number.")
... 
...     # Get port range
...     print("\nEnter the port range to scan. Press Enter to use the default range (1-1024).")
...     try:
...         start_port = int(input("Start port (default is 1): ").strip() or 1)
...         end_port = int(input("End port (default is 1024): ").strip() or 1024)
...         if start_port < 1 or end_port > 65535 or start_port > end_port:
...             raise ValueError
...         port_range = range(start_port, end_port + 1)
...     except ValueError:
...         print("Invalid range. Using default range: 1-1024.")
...         port_range = range(1, 1025)
... 
...     return target_ip, max_threads, port_range
... 
... if __name__ == "__main__":
...     target_ip, max_threads, port_range = get_user_input()
...     scan_host(target_ip, max_threads, port_range)
