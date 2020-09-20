import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
 
        print("Enter the name of the city to be anlyzed.\nNote the name of the city must be one of the following cities and entered in the format shown below.")
        city= input("(chicago, new york city, washington): ")

        if city =="chicago" or city =="new york city" or city =="washington":
            print(city)
            break

        print("Oops try again")
        print("\n")
 

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
 
        print("\nEnter the name of the month that you want anlyzed.\nNote the month must be one of the following and entered in the format shown below.")
        month= input("(all, january, february, march, april, may, or june): ")

        if month =="all" or month =="january" or month =="february" or month =="march" or month=="april" or month=="may" or month=="june":
            print(month)
            break

        print("Oops try again")
        print("\n")
 
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
 
        print("\nEnter the name of the day of the week that you want anlyzed.\nNote the day of the week must be entered in the format shown below.")
        day=input("(all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday): ")

        if day=="all" or day =="monday" or day =="tuesday" or day =="wednesday" or day=="thursday" or day=="friday" or day=="saturday" or day=="sunday":
            print(day)
            break

        print("Oops try again")
        print("\n")


    print("Awesome!!! You selected City: {}, Month: {} and Day: {}".format(city,month,day) )

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def scroll_raw_data(df):
    """Displays statistics on the total and average trip duration."""
    #while loop to prompt user and check response
    while True:
        print('\nWould you like to browse the selected data?')
        scroll_data= input("(yes or no?) ")
    
    
        if scroll_data =="yes" or scroll_data =="no":
          
            break
        print("Oops try again")
        print("\n")
    if scroll_data=="yes":
        a=0
        b=5
        print(df[a:b])
    #nested hile loops to prompt user to see if they would like to see more data and check for valid response
    while True:
        if scroll_data =="yes":
            
            while True:
                print('\nWould you like to browse more data?')
                scroll_data= input("(yes or no?) ")
             
                if scroll_data =="yes" or scroll_data =="no":
                    break
                print("Oops try again")
                print("\n")  
                
            if scroll_data=="yes":
                a=a+5
                b=b+5
                print(df[a:b])
        else:
            break
     
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    # extract month from the Start Time column to create an popular_month column
    df['popular_month'] = df['Start Time'].dt.month

    # find the most popular day
    popular_month = df['popular_month'].mode()[0]

    print('Most Popular Month:', popular_month)


    # TO DO: display the most common day of week
     # extract day_of_week from the Start Time column to create an day_of_week column
    df['day_of_week'] = df['Start Time'].dt.weekday

    # find the most popular day
    day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular Day of the Week:', day_of_week)


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]
    most_popular_start_station_count = df['Start Station'].value_counts()

    print('\nMost Popular Start Station:', most_popular_start_station)
    print("Number of Commuters:", most_popular_start_station_count[most_popular_start_station ])
   

    # TO DO: display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]
    most_popular_end_station_count = df['End Station'].value_counts()

    print('\nMost Popular End Station:', most_popular_end_station)
    print("Number of Commuters:", most_popular_end_station_count[most_popular_end_station ])

    # TO DO: display most frequent combination of start station and end station trip
    df["Combined_Stations"]=df['Start Station']+" to "+df['End Station']
    most_popular_start_end_station_combo = df['Combined_Stations'].mode()[0]
    most_popular_start_end_station_combon_count = df['Combined_Stations'].value_counts()

    print('\nMost Popular Trip:',  most_popular_start_end_station_combo)
    print("Number of Commuters:",  most_popular_start_end_station_combon_count[ most_popular_start_end_station_combo])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_commute_time=df['Trip Duration'].sum()
    print("\nApproximate Total Commuter Comute Time (in minutes)",total_commute_time//60)
    
    # TO DO: display mean travel time
    average_commute_time=df['Trip Duration'].mean()
    print("\nApproximate Average Commuter Comute Time (in minutes)",average_commute_time//60)
    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('\nTypes of Customers:\n',df['User Type'].value_counts())
    #excluding washington from processing birth and gender retrieves. Washington does not have this data in the csv data file.
    if city !="washington":
       # TO DO: Display counts of gender
        print('\nGender of Customers:\n', df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
 
        most_common_birth_year = df['Birth Year'].mode()[0]
        oldest_commuters_birth_year = df['Birth Year'].min()      
        youngest_commuters_birth_year = df['Birth Year'].max()                             
        print('\nMost Common Commuter Birth Year:',most_common_birth_year)
        print("\nOldest Commuter Birth Year: ", oldest_commuters_birth_year)
        print("\nYoungest Commuter Birth Year: ", youngest_commuters_birth_year)
    else:
        print("\nData was not collected on Gender and Birth year for the city of Washington\n")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        scroll_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
      
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()