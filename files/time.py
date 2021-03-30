import time, schedule

# count_runtime
start = time.time()
# your code hear
print("time :", time.time() - start)

# current time
print(time.localtime())
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(current_time, flush=True)

# shcedule
def job: return 'hi'

schedule.every().day.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
