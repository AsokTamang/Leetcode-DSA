class Solution:
    def whichWeekDay(self, day):
         switch={
              1:'Monday',
              2:'Tuesday',
              3:'Wednesday',
              4:'Thursday',
              5:'Friday',
              6:'Saturday',
              7:'Sunday',
            

         } # type: ignore
         return switch.get(day,'Invalid')   # type: ignore  #here we are returning the switch.get value as the switch is a dictionary consisting of the key-value pairs of nnumber and the name of the days
         
          

