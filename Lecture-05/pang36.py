counter = 0
def increment():
    global counter #global คือ เอาตัวแปรที่อยู่นอกฟังชั่น
    counter += 1

increment() #รันฟังชั้น
increment()


print(counter)