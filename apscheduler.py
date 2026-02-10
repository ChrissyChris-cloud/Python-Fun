from apscheduler.schedulers.blocking import BlockingScheduler
import time

# Function to be scheduled
def job():
    print("Hello, World!")

# Create a scheduler instance
scheduler = BlockingScheduler()

# Add job to scheduler: run `job` every 5 seconds
scheduler.add_job(job, 'interval', seconds=5)

# Start the scheduler
print("Scheduler started. Press Ctrl+C to stop.")
scheduler.start()
