import os

# گرفتن تمام متغیرهای محیطی
environment_variables = os.environ

# چاپ تک تک متغیرها
for key, value in environment_variables.items():
    print(f"{key} = {value}")

# به ترتیب حروف الفبا چاپ می‌کند
#for key in sorted(os.environ):
  #  print(f"{key:25} : {os.environ[key]}")