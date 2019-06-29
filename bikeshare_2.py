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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """I used some git hub help for this one. https://wiki.python.org/moin/WhileLoop and  https://github.com/jmportilla/Complete-Python-Bootcamp/blob/master/While%20loops.ipynb"""
    while True:
      city=input('Type the city name. Select: Chicago, New York City, or Washington')
      if city.lower() not in ['chicago','new york city','washington']:
             print("Select one of those cities")
      else:
             city=city.lower()
             break
    print('You have chosen {}')

    # get user input for month (all, january, february, ... , june)
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


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
    """I was usind online documentation of pandas and lessons from Udacity and some NumPy docs as well Udaciy Practices Solution #3"""
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
    months=['jan','feb','mar','apr','may','jun', 'all']
    if month!='all':
        month=months.index(month)
        df=df[df['month']==month]

    if day !=7:
        df=df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month=df['month'].mode()
    print ("The Most Common Month")
    print(most_common_month)


    # display the most common day of week
    most_common_day=df['day_of_week'].mode()
    print ('The Most Common Weekday')
    print(most_common_day)


    # display the most common start hour
    most_common_start_hr=df['hour'].mode()
    print('The Most Common Hour')
    print(most_common_start_hr)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_station=df['Start Station'].mode()[0]
    print('Most Popular End Station: {}'.format(most_used_station))


    # display most commonly used end station
    most_used_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station: {}'.format(most_used_end_station))


    # display most frequent combination of start station and end station trip
    dfa=df['Start Station','End Station']
    st=dfa['Start Station'].iloc[0]
    en=dfa['End Station'].iloc[0]
    print('Most Popular Combination of Start and End Stations: Start: {} End {}'.format(st,en))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total Travel Time is: {}".format(total_travel_time))


    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time is: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    type_of_user=df['User Type'].count()
    print('User Types\n',type_of_user)


    # Display counts of gender
    count_of_gender=df['Gender'].count()
    print('User Gender', count_of_gender)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year=df['Birth Year'].max()
        latest_birth_year=df['Birth Year'].min()
        most_common_birth_year=df['Birth Year'].mode()
        print('The earliest birth year is: {}'.format(earliest_birth_year))
        print('The most recent birth year is: {}'.format(latest_birth_year))
        print('The most common birth year is: {}'.format(most_common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
