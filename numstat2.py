#This program reads a series of integer numbers
#from a file and determines and displays the name
#of file, sum of numbers, count of numbers, average
#of numbers, maximum value, minimum value, and
#range of values.

import statistics

def main():
    #Create control loop variable
    go_again = 'y'

    while go_again == 'y':
        while True:
            try:
                #Get filename from user
                infile = input('Enter file name: ')
                print()

                #open file
                filename = open(infile, 'r')

                #Read the contents of the file into a list
                num_list = filename.readlines()

                #close file
                filename.close()

                #Convert each element to an int 
                index = 0
                while index < len(num_list):
                    num_list[index] = int(num_list[index])                
                    index += 1

                               
            except:
                print('An error occurred when trying to read')
                print('the file', infile)
                print()
            else:
                break

        if len(num_list) != 0:
            print('File name:', infile) 
            
            #Call get_sum function and assign to variable
            sum_of_list = get_sum(num_list)

            #Call get_count function and assign to variable
            element_count = get_count(num_list)

            #Call get_ave function
            get_ave(sum_of_list, element_count)

            #Call get_max function and assign to variable
            list_max = get_max(num_list)

            #Call get_min function and assign to variable
            list_min = get_min(num_list)

            #Call get_range function 
            get_range(list_max, list_min)        

            #Call get_median function
            get_median(num_list)            

            #Call get_mode function
            get_mode(num_list)
            print()
            
        else:
            print('There are no numbers in', infile)

        go_again = input('Would you like to evaluate another file? (y/n): ')
        
#Get the sum of the numbers in the list
def get_sum(num_list):
    #Create accumulator
    sum_of_list = 0
    for num in num_list:
        sum_of_list += num
    print('Sum:', sum_of_list)
    return sum_of_list

#Get the number of elements in the list
def get_count(num_list):    
    print('Count:', len(num_list))
    return len(num_list)

#Get the average of the numbers in the list
def get_ave(sum_of_list, element_count):
    print('Average:', (sum_of_list / element_count))   

#Get the max value in the list
def get_max(num_list):
    print('Maximum:', max(num_list))
    return max(num_list)

#Get the min value in the list
def get_min(num_list):
    print('Minimum:', min(num_list))
    return min(num_list)

#Get the range of the list
def get_range(list_max, list_min):
    print('Range:', (list_max - list_min))

#Get the median of the list
def get_median(num_list):
    sorted_list = sorted(num_list)

    #even list
    if len(sorted_list) % 2 == 0:
        lower_index = sorted_list[len(sorted_list) // 2 - 1]
        upper_index = sorted_list[len(sorted_list) // 2]        
        median = (float(lower_index + upper_index)) / 2
        print('Median:', median)
    #odd list
    else:
        median = sorted_list[(len(sorted_list) + 1) // 2 - 1]
        print('Median:', median)

#Get mode of list
def get_mode(num_list):
    number_counts = {} #create dictionary
    
    mode_list = []
    max_count = 0

    #Iterate through num_list
    for number in num_list:
        #check if number is in dictionary
        #if it is increase value count
        if number in number_counts:
            number_counts[number] += 1
        #if not add number to key and set value to 1
        else:
            number_counts[number] = 1

    #find highest value count
    for number in number_counts:
        count = number_counts[number]
        #Check if the current value is higher than previous
        #and if so assign it to count
        if count > max_count:
            max_count = count

    for key, value in number_counts.items():
        if value == max_count:
            mode_list.append(key)

    print('Mode:', mode_list)

#Call main function
main()
