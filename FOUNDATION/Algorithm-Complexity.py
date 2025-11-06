import time

# Example function (you can replace it with your own)
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Measure execution time for different input sizes
input_sizes = [100, 1000, 5000, 10000, 50000, 100000]
times = []

for n in input_sizes:
    start_time = time.time()
    example_function(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Display results
print("Input Size\tTime Taken (seconds)")
for n, t in zip(input_sizes, times):
    print(f"{n}\t\t{t:.6f}")
