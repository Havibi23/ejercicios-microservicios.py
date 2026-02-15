def health_check(latencia, uso_cpu, estado_db):
    return latencia < 200 and uso_cpu < 80 and estado_db

print(health_check(150, 75, True)) 
print(health_check(250, 70, True))  