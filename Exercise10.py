#Write a program that tests if a value is even or odd. Follow the instructions outlined
def even_odd(number):
    return "The number is even." if number % 2 == 0 else "The number is odd." #Two can be ouputed here, one is if the number has a remainder of 0 when devided by 2 and the other is when the remainder is not 0 meaning the number is odd
def main():
    entered_value = input("Enter a number: ") #User is asked for a number
    try:
        number = int(entered_value)
    except ValueError:
        print("The number is incorrect") #If the inputed is not a number, the user is given the info with the number being shown wrong
        return
    result = even_odd(number)
    print(result)
if __name__ == "__main__":
    main()
#In the code above, the user is asked for a number to which output is shown if the number is odd or even.