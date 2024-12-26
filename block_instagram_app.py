import os
import signal
import psutil

def block_instagram():
    for proc in psutil.process_iter():
        try:
            if "Instagram.exe" in proc.name():
                proc.kill()
                print("Instagram application has been blocked.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    block_instagram()
