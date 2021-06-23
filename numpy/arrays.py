import numpy as np

nums = np.array([[1,2,3,4,5],[6,7,8,9,10]])

def array_example():

    names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

    # Create a list of arrival times
    arrival_times = [*range(10,60,10)]

    # Convert arrival_times to an array and update the times
    arrival_times_np = np.array(arrival_times)
    new_times = arrival_times_np - 3

    # Use list comprehension and enumerate to pair guests to new times
    guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

    print(guest_arrivals)
