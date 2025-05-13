import simpy
import random

from config import RANDOM_SEED, CUSTOMER_INTERVAL, SIM_TIME, NUM_COUNTERS
from simulation.environment import run
from simulation.analysis import print_results, show_histogram

def main():
    print("Simulation started...\n")
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    bank = simpy.Resource(env, capacity=NUM_COUNTERS)
    run(env, bank, CUSTOMER_INTERVAL, SIM_TIME)
    print("\nSimulation finished.")
    print_results()
    show_histogram()

if __name__ == "__main__":
    main()
