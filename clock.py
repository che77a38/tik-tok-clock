import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == '__main__':
    minutes = int(input("请输入专注时长（分钟）："))
    countdown(minutes)
