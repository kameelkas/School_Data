# school_data.py
#KAMEEL KASUMU, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.

import numpy as np
import matplotlib.pyplot as plt
import math as m #importing math module as m

class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


school_data_2018_to_2019 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True, dtype = None)#reading in a csv file representing the school data for the 2018-2019 school year
school_data_2019_to_2020 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True, dtype = None)#reading in a csv file representing the school data for the 2019-2020 school year
school_data_2020_to_2021 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True, dtype = None)#reading in a csv file representing the school data for the 2020-2021 school year

school_names = ['Centennial High School', 'Robert Thirsk School', 'Louise Dean School', 'Queen Elizabeth High School', 'Forest Lawn High School', 'Crescent Heights High School', 'Western Canada High School', 'Central Memorial High School', 'James Fowler High School', 'Ernest Manning High School', 'William Aberhart High School', 'National Sport School', 'Henry Wise Wood High School', 'Bowness High School', 'Lord Beaverbrook High School', 'Jack James High School', 'Sir Winston Churchill High School', 'Dr. E. P. Scarlett High School', 'John G Diefenbaker High School', 'Lester B. Pearson High School']#list of school names
school_codes = ['1224', '1679', '9626', '9806', '9813', '9815', '9816', '9823', '9825', '9826', '9829', '9830', '9836', '9847', '9850', '9856', '9857', '9858', '9860', '9865']#list of school codes (all strings since user input will always be a string, it will be easier to match with this specific list)
school_codes_int = [1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 9826, 9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 9860, 9865]#list of school codes (all integers as this will be more easily used in matching given input(which will be converted to an int) to the school codes in the arrays and then help print statistics and print graphs)

dict_school_names_and_codes = dict(zip(school_names, school_codes))#combines school_names list and school_codes list into a dictionary with the former as the keys and the latter as the values
def main():

    def get_school_stats(code, list_codes, data_18_19, data_19_20, data_20_21):
        """
        Takes in the code of the school, a list of all the school codes, and three np arrays and prints the requested statistics and draws the graphs 

        Arguments:
        code(int): Integer representing the code of the school user entered
        list_code(list): List of all school codes
        data_18_19(array): Array representing data read in from a CSV file (school data from 2018-2019)
        data_19_20(array): Array representing data read in from a CSV file (school data from 2019-2020)
        data_20_21(array): Array representing data read in from a CSV file (school data from 2020-2021)


        Returns:
        None
        """
        found_code = 0#setting a int varaible to 0
        for index, i in enumerate(list_codes):#searching through the integer version of the school_codes list for the given input (no matter what user enters, the school code of whatever they searched for will be used here) and returning the index that code is at
            if i == code:
                found_code = index

        total_10 = m.floor((data_18_19[found_code][1] + data_19_20[found_code][1] + data_20_21[found_code][1])/3)#using the found index in the lines above to attain the populations of each grade and using those integer values to calculate the mean enrollment for each grade across all three school years
        total_11 = m.floor((data_18_19[found_code][2] + data_19_20[found_code][2] + data_20_21[found_code][2])/3)
        total_12 = m.floor((data_18_19[found_code][3] + data_19_20[found_code][3] + data_20_21[found_code][3])/3)

        graduates = data_18_19[found_code][3] + data_19_20[found_code][3] + data_20_21[found_code][3]#using found index to search for number of graduates for all three years and calculate number of graduates across all three years
        print(f'Mean enrollment for Grade 10:  {total_10}')#printing out the requested statitistics
        print(f'Mean enrollment for Grade 11:  {total_11}')
        print(f'Mean enrollment for Grade 12:  {total_12}')
        print(f'Total number of students who graduated in the past three years:  {graduates}')

        fig1 = 1#assigning values to fig 1 and fig2 to use to print both plots using only one plt.show() call
        fig2 = 2
        enrol_18_19 = [data_18_19[found_code][1], data_18_19[found_code][2], data_18_19[found_code][3]]#3 lists containing all the y coordinates for the first plot (number of students)
        enrol_19_20 = [data_19_20[found_code][1], data_19_20[found_code][2], data_19_20[found_code][3]]
        enrol_20_21 = [data_20_21[found_code][1], data_20_21[found_code][2], data_20_21[found_code][3]]
        x = [1, 2, 3]#list containing x coordinates for first plot
        labels = [10, 11, 12]#list containing labels that will show on x axis in place of the x coordinates (grade level)
        
        plt.figure(fig1)# creating the first plot with all required attributes
        plt.plot(x, enrol_20_21, 'bo', label = '2021 Enrollment')
        plt.plot(x, enrol_19_20, 'go', label = '2020 Enrollment')
        plt.plot(x, enrol_18_19, 'ro', label = '2019 Enrollment')
        plt.xticks(x,labels)
        plt.xlabel('Grade Level')
        plt.ylabel('Number of Students')
        plt.title('Grade Enrollment by Year')
        plt.legend(shadow = True)


        gr_10_pop = [data_18_19[found_code][1], data_19_20[found_code][1], data_20_21[found_code][1]]# 3 lists containing all the y coordinates for the first plot (number of students)
        gr_11_pop = [data_18_19[found_code][2], data_19_20[found_code][2], data_20_21[found_code][2]]
        gr_12_pop = [data_18_19[found_code][3], data_19_20[found_code][3], data_20_21[found_code][3]]
        x_bonus = [1, 2, 3]# list containing x coordinates for second plot
        labels_bonus = [2019, 2020, 2021]# list containing labels that will show on x axis in place of the x coordinates (enrollment year)

        plt.figure(fig2)# creating the second plot with all required attributes (3 subplots)
        plt.subplot(3, 1, 1)# subplot one with data of grade 10 populations over three years
        plt.title('Enrollment by Grade')
        plt.plot(x_bonus, gr_10_pop, 'y:', label = 'Grade 10')
        plt.legend(shadow = True)
        plt.ylabel('Number of Students')
        plt.xticks(x_bonus, labels_bonus)


        plt.subplot(3, 1, 2)# subplot two with data of grade 11 populations over three years
        plt.plot(x_bonus, gr_11_pop, 'm:', label = 'Grade 10')
        plt.legend(shadow = True)
        plt.ylabel('Number of Students')
        plt.xticks(x_bonus, labels_bonus)

        plt.subplot(3, 1, 3)# subplot three with data of grade 12 populations over three years
        plt.xlabel('Enrollment Year')
        plt.plot(x_bonus, gr_12_pop, 'c:', label='Grade 10')
        plt.legend(shadow = True)
        plt.ylabel('Number of Students')
        plt.xticks(x_bonus, labels_bonus)
        plt.show()

    print("ENDG 233 School Enrollment Statistics\n")
    print('Array data for 2020 - 2021')# printing all three data arrays
    print(school_data_2020_to_2021)
    print('Array data for 2019 - 2020')
    print(school_data_2019_to_2020)
    print('Array data for 2018 - 2019')
    print(school_data_2018_to_2019)

    given_input = input('Please enter the school name or school code of the school you wish to search for: ')# asking for user input
    given_input = given_input.strip()# removes all whitespace before and/or after the input string
    if given_input in dict_school_names_and_codes:# if statement checking to see if given input is in dectionary keys
        output = School(given_input, int(dict_school_names_and_codes[given_input]))# creating an instance of the school class so the school name and school code can be printed using the School Class
        print("\n***Requested School Statistics***\n")
        output.print_all_stats()# printing the the school name and code of the user input using the School Class method, print.all.stats()
        get_school_stats(int(dict_school_names_and_codes[given_input]), school_codes_int, school_data_2018_to_2019, school_data_2019_to_2020, school_data_2020_to_2021)# calls get_school_stats function, taking in the the school code of the verified input, the integer version of the school codes list, and the three arrays and prints school statistics and draw the graphs
    elif given_input in dict_school_names_and_codes.values():# elif part of if statement checking to see if given input is in dectionary values
        for key, value in dict_school_names_and_codes.items():# for loop running through the dictionary keys and values and findinf the inputted school code to get the corresponding key for that school code
            if given_input == value:
                found_key = key
        output = School(found_key, int(given_input))# creating an instance of the school class so the school name and school code can be printed using the School Class
        print("\n***Requested School Statistics***\n")
        output.print_all_stats()# printing the the school name and code of the user input using the School Class method, print.all.stats()
        get_school_stats(int(given_input), school_codes_int, school_data_2018_to_2019, school_data_2019_to_2020, school_data_2020_to_2021)# calls get_school_stats function, taking in the the school code of the verified input, the integer version of the school codes list, and the three arrays and prints school statistics and draw the graphs
    elif given_input not in dict_school_names_and_codes or given_input not in dict_school_names_and_codes.values():# elif part of if statement checking if input is not in dictionary keys or values, telling the user to input a valid school code/name and looping continuously until the user does so
        invalid_input = True
        while invalid_input == True:
            print("You must enter a valid school name or code:")
            given_input = input('Please enter the school name or school code of the school you wish to search for: ')
            given_input = given_input.strip()# removes all whitespace before and/or after the input string
            if given_input in dict_school_names_and_codes or given_input in dict_school_names_and_codes.values():# checks if new input is valid, if so then will do same process as above, checking if the input was a a school code or school name and then printing the appropiate stats and graphs, else, just keeps looping until a valid input is provided. No comments (for the most part) have been added from here until the end of the program because the code is just a copy of what is above.
                if given_input in dict_school_names_and_codes:
                    output = School(given_input, int(dict_school_names_and_codes[given_input]))
                    print("\n***Requested School Statistics***\n")
                    output.print_all_stats()
                    get_school_stats(int(dict_school_names_and_codes[given_input]), school_codes_int, school_data_2018_to_2019, school_data_2019_to_2020, school_data_2020_to_2021)
                    break# breaks the while loop since a valid input has been given
                elif given_input in dict_school_names_and_codes.values():
                    for key, value in dict_school_names_and_codes.items():
                        if given_input == value:
                            found_key = key
                    output = School(found_key, int(given_input))
                    print("\n***Requested School Statistics***\n")
                    output.print_all_stats()
                    get_school_stats(int(given_input), school_codes_int, school_data_2018_to_2019, school_data_2019_to_2020, school_data_2020_to_2021)
                    break# breaks the while loop since a valid input has been given

    # Print school name and code using the given class
    # Add data processing and plotting here

if __name__ == '__main__':
    main()

 