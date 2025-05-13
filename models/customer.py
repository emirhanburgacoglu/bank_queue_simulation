wait_times = []

def customer(env, name, bank, service_time):
    arrive = env.now
    print(f'{name} arrives at {arrive:.2f}')

    with bank.request() as request:
        yield request
        wait = env.now - arrive
        wait_times.append(wait)
        print(f'{name} starts at {env.now:.2f}, waited {wait:.2f}')
        yield env.timeout(service_time)
        print(f'{name} leaves at {env.now:.2f}')
