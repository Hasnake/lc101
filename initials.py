def get_initials(fullname):#if you haven't argument,then you have to call your function name to end.
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    xs = (fullname)
    name_list = xs.split()

    initials = ""

    for name in name_list:  # go through each name
        initials += name[0].upper()  # append the initial

    return initials


def main():
    strName = str(input("What is your full name?:"))
    answer = get_initials(strName)
    print("The initials of" , strName , "are" , answer)
if __name__ == '__main__':
        main()