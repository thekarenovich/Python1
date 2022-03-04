# BWT

Input = 'banana'

assert "$" not in Input                     				# Input string cannot contain $
Input = Input + "$"                         				# Add "$" to the end of the string

table = [Input[i:] + Input[:i] for i in range(len(Input))]  # Table of rotations of string
print('table = ', table)

table = sorted(table)
print('sorted table = ', table)

last_column = [row[-1:] for row in table]             		# Last characters of each row
bwt = ''.join(last_column)
print(bwt)

# table =  ['banana$', 'anana$b', 'nana$ba', 'ana$ban', 'na$bana', 'a$banan', '$banana']
# sorted table =  ['$banana', 'a$banan', 'ana$ban', 'anana$b', 'banana$', 'na$bana', 'nana$ba']
# annb$aa

print()

# Inverse_BWT

table = [""] * len(bwt)  # Make empty table

for i in range(len(bwt)):
    table = [bwt[i] + table[i] for i in range(len(bwt))]  # Add a column of r
    print('unsorted = ', table)
    table = sorted(table)
    print('sorted    =', table)
    
inverse_bwt = [row for row in table if row.endswith("$")][0]  # Find the correct row (ending in $)

inverse_bwt = inverse_bwt.rstrip("$")  # Get rid of start and end markers

print(inverse_bwt)

# unsorted =  ['a', 'n', 'n', 'b', '$', 'a', 'a']
# sorted    = ['$', 'a', 'a', 'a', 'b', 'n', 'n']
# unsorted =  ['a$', 'na', 'na', 'ba', '$b', 'an', 'an']
# sorted    = ['$b', 'a$', 'an', 'an', 'ba', 'na', 'na']
# unsorted =  ['a$b', 'na$', 'nan', 'ban', '$ba', 'ana', 'ana']
# sorted    = ['$ba', 'a$b', 'ana', 'ana', 'ban', 'na$', 'nan']
# unsorted =  ['a$ba', 'na$b', 'nana', 'bana', '$ban', 'ana$', 'anan']
# sorted    = ['$ban', 'a$ba', 'ana$', 'anan', 'bana', 'na$b', 'nana']
# unsorted =  ['a$ban', 'na$ba', 'nana$', 'banan', '$bana', 'ana$b', 'anana']
# sorted    = ['$bana', 'a$ban', 'ana$b', 'anana', 'banan', 'na$ba', 'nana$']
# unsorted =  ['a$bana', 'na$ban', 'nana$b', 'banana', '$banan', 'ana$ba', 'anana$']
# sorted    = ['$banan', 'a$bana', 'ana$ba', 'anana$', 'banana', 'na$ban', 'nana$b']
# unsorted =  ['a$banan', 'na$bana', 'nana$ba', 'banana$', '$banana', 'ana$ban', 'anana$b']
# sorted    = ['$banana', 'a$banan', 'ana$ban', 'anana$b', 'banana$', 'na$bana', 'nana$ba']
# banana


