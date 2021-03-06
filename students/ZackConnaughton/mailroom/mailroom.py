"""
mailroom assignment
"""

donors_list = [('Jimmy John', [100, 200, 300]),
               ('Amy Shumer', [2000, 4000, 1000]),
               ('Parker Pony', [2000, 10000]),
               ('Cher', [900, 9000, 2000]),
               ('Legolass Mario', [4000, 50])
               ]


def get_donors(donors):
    """
    Takes a list of donor information and returns a list of just the donor names
    """
    output = []
    for d in donors:
        output.append(d[0])
    return output


def add_money(person, money):
    """
    takes in a person entry in the donor_list and adds an amount of money they donated to their donations
    """
    for p in donors_list:
        if p[0] == person:
            p[1].append(money)


def thank_you():
    """
    prompts for a donor, uses that donor or creates a new one if not in the list.
    then prompts for donation to add to that donor.
    """
    response = ""
    while response != 'Q':
        print("Enter the full name of donor:")
        print("(Type list to see a full list of donors)")
        response = input(' => ').title()
        if response == "List":
            print(get_donors(donors_list))
        else:
            if response not in donors_list:
                donors_list.append((response, []))
            print("Enter the donation amount for " + response + ":")
            money = input(' => ')
            add_money(response, money)
            print("\nThank you, {person} for your donation of {donation}. We couldn't do this without you!\n".format(person=response, donation='${:,.2f}'.format(float(money))))
            response = "Q"


def stats(donations):
    """
    takes in donor information and returns the name of donor and the total, number and average of donations
    """
    name = donations[0]
    total = 0
    for d in donations[1]:
        total += float(d)
    num_of_donations = len(donations[1])
    avg_of_donations = '{:.2f}'.format(total / num_of_donations)
    return [name, total, num_of_donations, avg_of_donations]


def longest(values, min_column=12):
    """
    takes a list of values and returns the length of the longest value
    """
    cur_longest = min_column
    for i in values:
        if len(i) > cur_longest:
            cur_longest = len(i)
    return(cur_longest)


def second(element):
    """
    takes in a list and returns the second element
    """
    return element[1]


def data_header(widths):
    """
    takes in column widths and outputs a data header for a donor report in a string format for printing
    """
    output_string = "\n"
    output_string += '{:<{width0}}|{:<{width1}}|{:^{width2}}|{:^{width3}}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift', width0=widths[0], width1=widths[1], width2=widths[2], width3=widths[3])
    output_string += '\n' + '-' * (sum(widths)+3)
    return output_string


def data_print(info, widths):
    """
    takes in donor information and widths and returns a string formatted for
    printing for a donor report.
    """
    output_string = ""
    output_string += '{:<{width0}} ${:>{width1}.2f} {:^{width2}} ${:>{width3}}'.format(info[0], info[1], info[2], info[3], width0=widths[0], width1=widths[1]-1, width2=widths[2], width3=widths[3]-1)
    return output_string


def report(donors):
    """
    takes in the full donor list and returns a report to the terminal with the
    donors name, total given, number of donations and average donations
    """
    output = []
    for i in donors:
        output.append(stats(i))
    output.sort(reverse=True, key=second)
    column_widths = []
    for x in range(len(output[0])):
        print([str(item[x]) for item in output])
        column_widths.append(longest(([str(item[x]) for item in output])))
    print(data_header(column_widths))
    for j in output:
        print(data_print(j, column_widths))
    print("")



def main():
    print("Welcome to the Mailroom, you lucky duck!")
    print("")
    response = ' '
    while response != 'q':
        print('Select from the following')
        print('Thank You: "t"\n' +
              'Report: "r"\n'
              'Quit: "q"')
        response = input(' => ')[:1].lower()
        if response == 't':
            thank_you()
        elif response == 'r':
            report(donors_list)

if __name__ == '__main__':
    main()
