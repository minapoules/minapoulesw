import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please type a city  your input must be : ch for Chicago,ny for New York City and w for Washington!\n").lower()    
    #loop to handle the wrong input          
    while city not in CITY_DATA :
        print("That is invalid input")
        city = input("Please type a city  your input must be : ch for Chicago,ny for New York City and w for                  Washington!\n").lower()
             
             

    # TO DO: get user input for month (all, january, february, ... , june)
    months =['all','jan', 'feb', 'mar', 'apr', 'may', 'jun']
    month = input ("For city {} you did pickup, Please for filtering select a month if you don't wan't to filter choose all:\n-all\n-jan\n-feb\n-mar\n-apr\n-may\n-jun\n".format(city)).lower()
    #loop to handle the wrong input 
    while month not in months:
        print("That is invalid input")
        month = input("For city {} you did pickup, Please for filtering select a month if you don't want to filter choose all:\n all\n-jan\n-feb\n-mar\n-apr\n-may\n-jun\n".format(city)).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("For city {} and month {} you did pickup, Please for filtering select a day if you don't want to filter choose all:\n-all\n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-saturday\n-sunday\n".format(city,month)).lower()
    
    #loop to handle the wrong input
    while day not in days :
        print("That is invalid input")
        day = input("For city {} and month {} you did pickup, Please for filtering select a day if you don't want to filter choose all:\n-all\n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-saturday\n-sunday\n".format(city,month)).lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file 
    df = pd.read_csv(CITY_DATA[city])
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #make a new column with name month 
    df['month'] = df['Start Time'].dt.month
    #make a new column with name day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #loop to hanle any answer instead of 'all' for months
    if month != 'all' :
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        #index function to be added 
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    #loop to handle any answer instead of 'all' for months    
    if day != 'all' :
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is : {} ".format(common_month))


    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print("The most common day of week is : {} ".format(day))


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    hour = df['hour'].mode()[0]
    print("The most common start hour is : {} ".format(hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is : {} ".format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is : {} ".format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Start End comb'] = df['Start Station'] + '//' + df['End Station']
    comb_start_end = df['Start End comb'].mode()[0]
    print("The most frequent combination of start station and end station trip : {} ".format(comb_start_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df['Trip Duration'].sum() // 60 // 60
    print("The total travel time is : {}  Hours.".format(tot_travel_time))


    # TO DO: display mean travel time
    mtv = df['Trip Duration'].mean() 
    mean_travel_time = int(mtv)
    print("The mean travel time is : {}  Hours.".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types are \n", user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df and 'Birth Year' in df :
        genders = df['Gender'].value_counts().to_frame()
        print("\n\nThe counts of each gender type are\n ", genders)
     
    else :
        print("\n\nThe gender cann't appeare for this city") 
  
              
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df :
        earliest_year = df['Birth Year'].min()
        print("\n\nThe earliest year of birth is ", int(earliest_year))
        recent_year = df['Birth Year'].max()
        print("\nThe recent year of birth is ", int(recent_year))
        common_year = df['Birth Year'].mode()[0]
        print("\nThe most common year of birth is ", int(common_year))
    else :
        print("\n\nThe gender cann't appeare for this city")                                                           


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    
def display_raw_data(df):
    """The fuction takes the name of the city produced by the get_filters fuction as input and returns the raw data of that
    city as chunks of 5 rows based upon user input."""

    print('\nRaw data is available to check... \n')

    # setting counter for the rows
    count = 0
    #display message to user to choose again raw data 
    
    #loop to handle the wrong type
    while True : 
        message = input("Dear user if you want to display 5 rows  type yes .. type no to exit\n").lower()

        if message not in ['yes', 'no'] :
            print("Unfortunately you typed a wrong word...\n")
            #print("Dear user if you want to display 5 rows type yes \n")#.lower()
        #message = input
        #loop to handle the right answer
        elif message == 'yes' :
            print(df.iloc[count : count + 5])
            count +=5
        #message = input("If you want 5 more raws to appeare please retype : yes or no for exit \n").lower()
        #exit the function 
        elif message == 'no' :
            print("Exiting..\n") 
            break
    
def main():
    while True:
        city,month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        #loop to handle the invalid input 
        while restart.lower()  not in [ 'yes', 'no' ] :
            print("that's invalid input...")
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            
        if restart.lower() != 'yes':
            break
           

        #except:  
        #while restart.lower() != 'yes' :
            
           # restart = input('\nWould you like to restart? Enter yes or no.\n')
if __name__ == "__main__":
	main()


    