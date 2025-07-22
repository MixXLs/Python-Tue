def display_info(**kwargs): #**kwargs คือการรับอาร์กิวเมนต์แบบระบุชื่อ
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Mix", age=18, city="Betone")