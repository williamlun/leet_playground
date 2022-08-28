import numpy as np

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,3] = nums[:,3] + 1
print(nums)


######################################################
# Create a list of arrival times
arrival_times = [*range(10,60,10)]

print(arrival_times)

arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)

guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

print(guest_arrivals)

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')