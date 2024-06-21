import time
import os
import sys

__version__ = "1.1.0"
StartTime = time.time()

def main():
    # Your bot code goes here
    print(f"Bot started with version {__version__} at {time.ctime(StartTime)}")

    while True:
        current_time = time.time()
        elapsed_time = current_time - StartTime
        print(f"Bot is running. Elapsed time: {elapsed_time:.2f} seconds.")
        
        # Your bot functionality here
        # ...

        # Wait for 5 minutes
        time.sleep(30)

        # Restart the script
        print("Restarting the bot...")
        os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    main()
