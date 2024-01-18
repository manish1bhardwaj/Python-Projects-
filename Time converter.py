# 8. Problem: Time Converter 
# Description: Create a Time class that converts seconds to minutes, minutes to hours, and 
# vice versa. 


class Time:
    staticmethod
    def seconds__to__minutes(seconds):
        return seconds / 60
    staticmethod
    def seconds__to__hours(seconds):
        return seconds / 3600
    staticmethod
    def minutes__to__seconds(minutes):
        return minutes * 60
    staticmethod
    def minutes__to__hours(minutes):
        return minutes / 60
    staticmethod
    def hours__to__seconds(hours):
        return hours * 3600
    staticmethod
    def hours__to__minutes(hours):
        return hours * 60

# Example Usage
print(f"1200 seconds is {Time.seconds__to__minutes(1200)} minutes")
print(f"1200 seconds is {Time.seconds__to__hours(1200)} hours")

print(f"20 minutes is {Time.minutes__to__seconds(20)} seconds")
print(f"20 minutes is {Time.minutes__to__hours(20)} hours")

print(f"2 hours is {Time.hours__to__seconds(2)} seconds")
print(f"2 hours is {Time.hours__to__minutes(2)} minutes")