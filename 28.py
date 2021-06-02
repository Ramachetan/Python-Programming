'''
Write a class called Time whose only field is a time in seconds.
It should have a method called convert_to_minutes that returns a string of
minutes and seconds formatted as in the following example:
if seconds is 230, the method should return '5:50'.
It should also have a method called convert_to_hours that returns a string
of hours, minutes, and seconds formatted analogously to the previous method.
'''
class Time:
    def __init__(self,sec):
        self.sec=sec
    def convert_to_minutes(self):
        n=self.sec
        minutes=n//60
        seconds=n%60
        return(str(minutes)+":"+str(seconds))
    def convert_to_hours(self):
        n=self.sec
        hours=n//3600
        minutes=(n//60)%60
        seconds=n%60
        return(str(hours)+":"+str(minutes)+":"+str(seconds))
a=int(input("Enter seconds: "))
c=Time(a)
print("Time in minutes:seconds format --->",c.convert_to_minutes())
print("Time in hours:minutes:seconds format --->",c.convert_to_hours())
