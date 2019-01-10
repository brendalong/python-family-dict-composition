my_family = {
    'sister': {
        'name': 'Barb',
        'eyes': 'hazel',
        'kids': 2,
        'grandkids': 2,
    },
    'brother': {
        'name': 'John',
        'eyes': 'brown',
        'kids': 2,
        'grandkids': 0
    },
    'mother': {
        'name': 'Bonnie',
        'eyes': 'brown',
        'kids': 2,
        'grandkids': 5
    }
}

# comprehension
#Krista is my sister, brown eyes, 2 kids, 2 grandkids.
#Helpful hint: To convert an integer into a string in Python, it's str(integer_value)
# for (family_member, member_values) in my_family.items()}
# defines what to call the items in my_family

family_stuff = {f'{member_values["name"]} is my {family_member} and has {member_values["eyes"]} eyes and {str(member_values["grandkids"])} grandchildren' for (
    family_member, member_values) in my_family.items()}

print(family_stuff)


