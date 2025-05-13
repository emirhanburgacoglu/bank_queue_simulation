import statistics
import matplotlib.pyplot as plt
from models.customer import wait_times

def print_results():
    average = statistics.mean(wait_times)
    print(f"\nAverage wait time: {average:.2f} minutes")
    print(f"Total customers served: {len(wait_times)}")

def show_histogram():
    plt.hist(wait_times, bins=10, color='skyblue', edgecolor='black')
    plt.title("Customer Wait Times")
    plt.xlabel("Wait Time (minutes)")
    plt.ylabel("Number of Customers")
    plt.grid(True)
    plt.show()
