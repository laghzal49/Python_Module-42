def ft_count_harvest_recursive():
    initial_days = int(input("Days until harvest: "))

    def recursive_countdown(current_day):
        if current_day < 1:
            return
        recursive_countdown(current_day - 1)
        print(f"Day {current_day}")
    recursive_countdown(initial_days)
    print("Harvest time!")
