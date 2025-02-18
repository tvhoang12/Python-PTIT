class RainStation:
    def __init__(self, name):
        self.name = name
        self.total_rainfall = 0
        self.total_duration = 0

    def add_measurement(self, duration, rainfall):
        self.total_duration += duration
        self.total_rainfall += rainfall

    def get_average_rainfall(self):
        if self.total_duration != 0:
            average_rainfall = self.total_rainfall / self.total_duration  # Convert to hourly average
            return average_rainfall
        else:
            return 0.00


if __name__ == '__main__':
    n = int(input())  # Number of measurements

    stations = []  # Dictionary to store RainStation objects

    for _ in range(n):
        station_name = input()
        start_time = input().split(':')
        end_time = input().split(':')
        rainfall = int(input())

        duration = float((int(end_time[0]) - int(start_time[0])) + (int(end_time[1]) - int(start_time[1])) / 60)
        flag = False
        for i in range(len(stations)):
            if stations[i].name == station_name:
                stations[i].add_measurement(duration, rainfall)
                flag = True
                break
        if not flag:
            station = RainStation(station_name)
            station.add_measurement(duration, rainfall)
            stations.append(station)

    # Output the results
    for i in range(len(stations)):
        station = stations[i]
        print(f"T{i + 1:02} {station.name} {station.get_average_rainfall().__format__('.2f')}")
