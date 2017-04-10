#  A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

# Define a set that contains tuples. Each tuple should contain two strings:
# The name of an artist
# A song by that artist
# Example set
songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Beyonce', 'Single Ladies'),
    ('The Beatles', 'Submarine')
}
# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

no_nickelback = {song for song in songs if song[0] not in 'Nickelback'}
print(no_nickelback)