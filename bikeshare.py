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
    #Create an empty city variable
    city = ''
    #While loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print("\nWelcome to Bikeshare.py. Kindly select a city.")
        print("\nYour options are: 1. chicago 2. new york city 3. washington")
        print("\nCity name input is not case sensitive. Please type name of city in full")
        #Standardize user input for city
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nIncorrect input. Please check input and try again.")

    print(f"\nYou have chosen to analyse data from {city.upper()}.")


    # TO DO: get user input for month (all, january, february, ... , june)
    #Dictionary to store all options for month
    print('\nMonth_options:code = [january: 1, february: 2, march: 3, april: 4, may: 5, june: 6, all: 7]')
    MONTHS = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTHS.keys():
        print("\nPlease enter a month from January to June, spelt fully")
        print("\nYou can view data for all months by typing 'all'")
        print("\nMonth selection input is not case sensitive")
        month = input().lower()

        if month not in MONTHS.keys():
            print("\nIncorrect input. Please check your input and try again")
            print("\nKindly re-enter month choice")

    print(f"\nYou have elected to analyse data for the month of {month.upper()}")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Use a list to store all options for day
    print('\nDay options = [monday, tuesday, wednesday, thursday, friday, saturday, sunday, all]')
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    while day not in DAYS:
        print("\nPlease type a day in the week spelt fully to view its data")
        print("\nYou can view data for all days by typing 'all'")
        print("\nDay selection input is not case sensitive")
        day = input().lower()

        if day not in DAYS:
            print("\nIncorrect input. Please check your input and try again\n")
            print("\nKindly re-enter day choice\n")

    print(f"\nYou have elected to view data for {day.upper()}")
    print(f"\nYou have chosen to analyse data for city: {city.upper()}, month: {month.upper()}, day: {day.upper()}.")

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
    #Load data for city
    df = pd.read_csv(CITY_DATA[city])



    #Format Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extracting month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filtering by month
    if month != 'all':
        #Use index of the months in months list as reference
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create new df
        df = df[df['month'] == month]

     #Filtering by day of week
    if day != 'all':
      #Filter by day of week to create new df
        df = df[df['day_of_week'] == day.title()]

    return df
     #Returns dataframe based on city, month, and day selection

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print(f"\nThe most common month has code: {common_month}")

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day: {common_day}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    common_start_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]

    print(f"The most commonly used start station: {start_station_mode}")

    # TO DO: display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]

    print(f"\nThe most commonly used end station: {end_station_mode}")

    # TO DO: display most frequent combination of start station and end station trip
    # Use str.cat to pair start stations and end stations
    # Assign concatenation to new column 'Start - End'
    # Find mode of 'Start - End'
    df['Start - End'] = df['Start Station'].str.cat(df['End Station'], sep=' and ')
    pair = df['Start - End'].mode()[0]

    print(f"\nThe most common pair of Start Station and End Station is {pair}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()


    minute, second = divmod(total_duration, 60)

    hour, minute = divmod(minute, 60)
    print(f"Total trip duration is {hour} hours, {minute} minutes, {second} seconds.")

    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())

    minute, second = divmod(mean_travel_time, 60)
    #For if mean travel time exceeds 60 mins
    if minute > 60:
        hour, minute = divmod(minute, 60)
        print(f"\nMean travel time is {hour} hours, {minute} minutes, {second} seconds.")
    else:
        print(f"\nMean travel time is {minute} minutes, {second} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(f"Subscriber and Customer user counts:\n{user_types}")

    # TO DO: Display counts of gender
    try:
        gender_frame = df['Gender'].value_counts()
        print(f"\nBikeshare usage by gender:\n{gender_frame}")
    except:
        print("\nGender statistics unavailable for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])

        print(f"\nThe earliest year of birth is: {earliest_year}\n")
        print(f"\nThe most recent year of birth is: {most_recent_year}\n")
        print(f"\nThe most common year of birth is: {most_common_year}\n")

    except:
        print("Year of birth statistics unavailable for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #For printing raw data 5 rows at a time

def view_data(df):

    options = ['yes', 'no']
    raw_data = ''
    start_loc = 0

    while raw_data not in options:
        print('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        raw_data = input().lower()
        if raw_data == 'yes':
            print(df.head())
            start_loc += 5
        elif raw_data == 'no':
            print('Thank you')

    while raw_data == 'yes':
        print('Do you want to see 5 more rows of raw data?')

        raw_data = input().lower()
        if raw_data == 'yes':
            print(df[start_loc:start_loc+5])
        elif raw_data != 'yes':
            break

print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)



        restart = input('\nWould you like to restart? Yes or no.\n')
        if restart.lower() != 'yes':
         break


if __name__ == "__main__":
	main()
