import random
import simpy
from models.customer import customer

def customer_generator(env, bank, interval):
    i = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / interval))
        service_time = random.uniform(3, 10)
        env.process(customer(env, f'Customer {i}', bank, service_time))
        i += 1

def run(env, bank, interval, sim_time):
    env.process(customer_generator(env, bank, interval))
    env.run(until=sim_time)
