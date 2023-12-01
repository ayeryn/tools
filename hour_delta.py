from datetime import timedelta


def calculate():
    start_time = input('Start time? (HH:MM) ')
    delta_time = input('Delta time? (HH:MM) ')

    start = start_time.split(':')
    delta = delta_time.split(':')

    start_time = timedelta(hours=int(start[0]),
                           minutes=int(start[1]) if start[1] else 0)
    time_delta = timedelta(hours=int(delta[0]),
                           minutes=int(delta[1]) if delta[1] else 0)

    end_time = start_time + time_delta
    print(end_time)


again = True
while again:
    calculate()
    again = input('Run again? (Y/N) ').lower() == 'y'

print('Goodbye!')
