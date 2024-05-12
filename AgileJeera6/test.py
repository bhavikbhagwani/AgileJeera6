import time


def main():
    start_time = time.time()
    print("Timer started. Press Enter to stop.")

    input()  

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()

