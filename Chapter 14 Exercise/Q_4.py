""""Write a class called Time whose only field is a time in seconds. It should have a method called
convert_to_minutes that returns a string of minutes and seconds formatted as in the following
example: if seconds is 230, the method should return '5:50'. It should also have
a method called convert_to_hours that returns a string of hours, minutes, and seconds
formatted analogously to the previous method."""

#NoteThe question has a slight mistake the Input of 230s should give an output of 3:50s and not 5:50s

class Time:

    def __init__(self,seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        if self.seconds < 60:
           return self.seconds
        else:
           minute = int(self.seconds/60)
           sec = self.seconds% 60
           return "{} minutes :{} seconds".format(minute,sec)

    def convert_to_hours(self):
        if self.seconds < 60:
            hour =0
            minute = 0
            sec = self.seconds
            return "{} Hour :{} minutes :{} seconds".format(hour,minute,sec)
        elif self.seconds > 60 and self.seconds< 3600:
            hour = 0
            minute = int(self.seconds/60)
            sec = self.seconds % 60
            return "{} Hour :{} minutes :{} seconds".format(hour, minute, sec)
        elif self.seconds >= 3600:
            hour = int(self.seconds/3600)
            if self.seconds - 3600 < 60:
               minute =0
            else:
                minute = int((self.seconds - 3600) / 60)
            sec = int(self.seconds-3600)%60
            return "{} Hour :{} minutes :{} seconds".format(hour, minute, sec)








a =Time(5000)
print(a.convert_to_minutes())
print(a.convert_to_hours())