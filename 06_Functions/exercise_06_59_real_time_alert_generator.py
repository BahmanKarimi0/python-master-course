def real_time_alert(data, threshold=100):
    warn_count = 0
    msg = ''
    for temp in data:
        if temp > threshold:
            msg = f'⚠️ ALERT: value exceeded! ({temp})'
            warn_count += 1
        else:
            msg = f'OK: {temp}'
        yield msg
        if warn_count >= 3:
            msg = f'🛑 Max alerts reached. Monitoring stopped.'
            print(msg)
            break


data = [45, 55, 102, 88, 120, 101, 99, 80]
gen = real_time_alert(data)
for log in gen:
    print(log)