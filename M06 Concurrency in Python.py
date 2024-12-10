
# In[ ]:
from datetime import date
current_date = date.today()
date_string = current_date.strftime("%Y-%m-%d")
with open("today.txt", "w") as file:
    file.write(date_string)

print("Date has been written to today.txt.")
# In[ ]:
with open("today.txt", "r") as file:
    today_string = file.read()

print("Contents of today.txt have been read into today_string.")

# In[ ]:
from datetime import datetime
parsed_date = datetime.strptime(today_string, "%Y-%m-%d").date()
print("Date has been parsed from today_string.")
# In[ ]:
import multiprocessing
import random
import time
from datetime import datetime
def process_function():
    wait_time = random.random()
    
    time.sleep(wait_time)
    
    current_time = datetime.now().strftime("%H:%M:%S")
    
    print(f"Current time: {current_time}")
    
    multiprocessing.current_process().terminate()
if __name__ == "__main__":
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=process_function)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    print("All processes have finished.")

