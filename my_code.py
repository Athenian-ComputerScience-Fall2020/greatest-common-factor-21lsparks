# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  megan

def find_gcf(x,y):   # Do not change function name!
    # User code goes here
    for count in range(x, 0, -1):
        if x%count==0 and y%count==0:
            return count

if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    #print(find_gcf(6,9))

    # After you are satisfied with your results, use input() to prompt the user for two values:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(find_gcf(x,y))
