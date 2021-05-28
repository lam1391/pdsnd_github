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
	city =''
    while city not in CITY_DATA.keys():
        city = input("which city do you like check out Chicago, New York or whashington?").lower()
        if city not in CITY_DATA.keys():
            print("\nI don't understand that city, please try again.\n")
                

    # TO DO: get user input for month (all, january, february, ... , june)
    monthB = True
    while monthB == True :
        month = input("which month do you like to choose?").lower()
        
        Month_data ={'all':1,'january':2,'february':3,'march':4,'april':5,'may':6,'june':7,'july':8}
        if month in month_data.keys():
            monthB = False
        else:
            print("\nI don't understand that month, please try again.\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayB = True
    while dayB == True :
        day = input("which day do you like to choose?")
        if day.lower() == "all" or day.lower() == "monday" or day.lower() == "tuesday" or day.lower() == "wendesday" or day.lower() == "thrusday"             or day.lower() == "friday" or day.lower() == "saturday" or day.lower() == "sunday":
            dayB = False
        else:
            print("\nI don't understand that city, please try again.\n")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != "all" :
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','agost','september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day !="all":
        df = df[df['day_of_week'] == day.title()]
        

    return df

def display(df):
    
    BIN_RESPONSE_LIST = ['yes', 'no']
    viewdata = ''
    
    counter = 0
    while viewdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")

        viewdata = input().lower()

        if viewdata == "yes":
            print(df.head())
        elif viewdata not in BIN_RESPONSE_LIST:
            print("\nPlease try again an check your input.")
            
    while viewdata =='yes':         
        print("Do you wish more raw data?")
        counter = counter + 5
        viewdata = input().lower()
        
        if viewdata == 'yes':
            print(df[counter:counter+5])
        elif viewdata != 'yes':
            break
            
    print('-'*40)
            
    
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['month'] = df['Start Time'].dt.month
    CommonMonth = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june','july','agost','september','october','november','december']
    month = months[CommonMonth-1] 
        
    print ('\nthe most common month:\n',month)
    # TO DO: display the most common day of week
    #df['day'] = df['Start Time'].dt.day
    Commonday = df['day_of_week'].mode()[0]
    print ('\nthe most common day:\n',Commonday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Commonhour = df['hour'].mode()[0]
    print ('\nthe most common hour:\n',Commonhour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    CommonStartStation = df['Start Station'].mode()[0]
    
    print ('\nthe most commonly used start station:\n',CommonStartStation)

    # TO DO: display most commonly used end station
    CommonEndStation = df['End Station'].mode()[0]
    
    print ('\nthe most commonly used end station:\n',CommonEndStation)

    # TO DO: display most frequent combination of start station and end station trip
    df['CombineStation'] = df['Start Station'].str.cat(df['End Station'], sep=' TO ')
    
    FrequentCombination = df['CombineStation'].mode()[0]
    
    print ('\nthe most frequent combination of start station and end station trip:\n',FrequentCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TotalTravelTime = df['Trip Duration'].sum()
        
    print('\ntotal travel time...\n',TotalTravelTime,'hrs')

    # TO DO: display mean travel time
    AverageTraverlTime = df['Trip Duration'].mean()
    
    print('\ntotal mean travel time...\n',AverageTraverlTime,'hrs')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    UserTypes = df['User Type'].value_counts()
    
    print('\ncounts of user types...\n',UserTypes)

    # TO DO: Display counts of gender
    genderCount = df['Gender'].value_counts()
    
    print('\ncounts of gender...\n',genderCount)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    
    print('\nearliest year of birth...\n',earliest)
    
    recent = int(df['Birth Year'].max())
    
    print('\nrecent year of birth...\n',recent)
    
    commonYear = int(df['Birth Year'].mode()[0])
    
    print('\nCommon year of birth...\n',commonYear)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
