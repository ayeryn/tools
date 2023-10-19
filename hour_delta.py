from datetime import timedelta

start_hour = input('Start time? (24H) ')
start_min = input('Start minute? ')
delta_hour = input('Delta hour?')
delta_min = input('Delta minute? ')

start_time = timedelta(hours=int(start_hour),
                       minutes=int(start_min) if start_min else 0)
time_delta = timedelta(hours=int(delta_hour),
                       minutes=int(delta_min) if delta_min else 0)

end_time = start_time + time_delta
print(end_time)
