# Job Sequencing with Deadlines using Greedy Algorithm

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Step 1: Sort jobs by profit (highest first)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find max deadline to create slots
    max_deadline = max(job.deadline for job in jobs)
    slots = [-1] * (max_deadline + 1)

    total_profit = 0
    job_order = []

    # Step 3: Schedule each job
    for job in jobs:
        # Try to place job before its deadline
        for t in range(job.deadline, 0, -1):
            if slots[t] == -1:  # If slot is empty
                slots[t] = job.job_id
                total_profit += job.profit
                job_order.append(job.job_id)
                break

    print("Job Order:", job_order)
    print("Total Profit:", total_profit)

# Example
jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15)
]

job_sequencing(jobs)
