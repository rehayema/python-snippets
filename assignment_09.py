"""

We have 2 variables. fr and d. fr ios a list of strings and d is a dictionary with emal addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with the associated value of that email looked up from the dictionary d. if the dictionary does not contain the email found in the list, add a new entry in the dictionary for the email found in the fr list. The value for this new email key will be the next highest value in the dictionary in string format. 

Once the dictionary is populated with this new email key and a new number value, replace that email's occurence in the fr list with the number value.

The output of running your completed code should be the following:


"""

fr = [
    '7@comp1.COM|4|11|GDSPV',
    '7@comp1.COM|16|82|GDSPV',
    '13@comp1.COM|12|82|GDSPV',
    '26@comp1.COM|19|82|GDSPV',
    '28@comp1.COM|19|82|GDSPV',
    '30@comp1.COM|19|82|GDSPV'
]

d = {
    '7@comp1.COM' : '199',
    '8@comp4.COM' : '200',
    '13@comp1.COM' : '205'
}


# Find the highest value in current dictionary
d_values = [int(n) for n in d.values()]
d_values.sort()

#split string at sprite char
list_length = len(fr)

for i in range(list_length):

    single_fr = fr[i].split('|', 1)
    email = single_fr[0]


    #search dictionary for email string
    if email in d:
        # if found in fr dictionary replace email with value from dictionary
        fr_value=d[email]
        new_fr = fr_value +'|'+ single_fr[1]
        fr[i]=new_fr
        
    else:
        # if not found - find the highest number value in the dictionary
        new_value = d_values[-1] + 1
    
        # add email to dictionary with number value plus one as key
        d[email] = str(new_value)

        # replace email in list with new value in dictionary
        fr_value=d[email]
        new_fr = fr_value +'|'+ single_fr[1]
        fr[i]=new_fr

        # define the new highest value in dictionary
        d_values[-1] = new_value
        
print(fr)
print(d)