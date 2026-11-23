import math
seconds_in_a_day2 = 24*60*60
seconds2 = int(input("Necha sekund o`tkanini yozing: "))
hours = (seconds_in_a_day2-seconds2)//60//60 # soatni qoldiqsiz topish uchun
print(f"soat {hours}")

minutes = math.ceil((((seconds_in_a_day2-seconds2)/60/60)-hours))
print(f"minut {minutes}")

seconds_left = (seconds_in_a_day2-seconds2)%60%60
print(f"sekund {seconds_left}")
print(f"{hours}:{minutes}:{seconds_left} qoldi")







