Kill Nickelback

In this exercises, you're going to use a conditional statement inside a comprehension. Let's look at a basic example.

nums = range(10)
small_numbers = [num for num in nums if num < 6]
# Only add numbers to the new list if the value is less than 6

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [ word.title() for word in words if len(word) == 3 ]
# len(stringVariable) is equivalent to stringVariable.length in JavaScript
Setup

mkdir -p ~/workspace/python/exercises/sets && cd $_
touch nickelback.py
Instructions

Define a set that contains tuples. Each tuple should contain two strings:

The name of an artist
A song by that artist
Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

# Example set
songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}
Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.