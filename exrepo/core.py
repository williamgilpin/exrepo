import random

def random_walk(x0, nsteps=100):
    """
    Generate a random walk with nsteps steps starting at x0.
    """
    all_steps = [x0]
    for _ in range(nsteps):
        all_steps.append(all_steps[-1] + random.choice([-1, 1]))
    return all_steps

def ornstein_uhlenbeck(x0, nsteps=100, theta=0.15, sigma=0.2):
    """
    Generate an Ornstein-Uhlenbeck process with nsteps steps starting at x0.
    """
    all_steps = [x0]
    for _ in range(nsteps):
        next_step = all_steps[-1] + theta * (0 - all_steps[-1]) + sigma * random.gauss(0, 1)
        all_steps.append(next_step)
    return all_steps