# Mario Benavides
# Status - Complete
# This program reads a string from the user containing a date in the form mm/dd/yyyy.   
# It should print the date in the format March 12, 2018.  

from datetime import datetime # import object

def main():

        date = input('Enter a date in the format mm/dd/yyyy: ')

        # (month zero padded, day zero padded, year as decimal)
        date_object = datetime.strptime(date, '%m/%d/%Y') 

        # (Month as full name, day zero padded comma, year as decimal)
        print(date_object.strftime('%B %d, %Y')) 

                
# call the main function    
main()
