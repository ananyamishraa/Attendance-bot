import schedule
import time

def job():
    print("present..")

schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().day.at("12:42").do(job)
schedule.every().minute.at(":17").do(job)

def job_with_argument(name):
    print(f"{name}")

schedule.every(15).seconds.do(job_with_argument, name="Ananya")

while True:
    schedule.run_pending()
    time.sleep(1)