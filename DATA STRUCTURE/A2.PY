class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    n = max(job.deadline for job in jobs)
    slots = [-1] * (n + 1)
    total_profit = 0
    job_order = []

    for job in jobs:
        for t in range(job.deadline, 0, -1):
            if slots[t] == -1:
                slots[t] = job.job_id
                job_order.append(job.job_id)
                total_profit += job.profit
                break

    print("Job Order:", job_order)
    print("Total Profit:", total_profit)

jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15)
]

job_sequencing(jobs)
