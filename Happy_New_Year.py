from time import sleep

countdown = int(input("how many seconds until new year? "))
while countdown > 0:
    print(countdown)
    sleep(1)
    countdown -= 1
print("Happy New Year!!!")
