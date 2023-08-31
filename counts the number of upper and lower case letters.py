
def counting_upper_lower_case(string):
    upper_case =0
    lower_case =0
    special_char =0
    space_count =0
    for char in string:
        if char.isupper():
            upper_case=upper_case+1
        elif char.islower():
            lower_case=lower_case+1
        elif char.isspace():
              space_count=space_count+1
        else:
            special_char=special_char+1
            print(upper_case)
            print(lower_case)
            print(special_char)
            print(space_count)

    

my_string= input("enter input string:") 
counting_upper_lower_case(my_string)
