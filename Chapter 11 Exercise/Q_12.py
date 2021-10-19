"""
Below are the notes used in music:
C C# D D# E F F# G G# A A# B

The notes for the C major chord are C, E, G. A mathematical way to get this is that E is 4 steps
past C and G is 7 steps past C. This works for any base. For example, the notes for D major
are D, F#, A. We can represent the major chord steps as a list with two elements: [4,7]. The
corresponding lists for some other chord types are shown below:

Minor [3,7]               Dominant seventh [4,7,10]
Augmented fifth [4,8]     Minor seventh [3,7,10]
Minor fifth [4,6]         Major seventh [4,7,11]
Major sixth [4,7,9]       Diminished seventh [3,6,10]
Minor sixth [3,7,9]

Write a program that asks the user for the key and the chord type and prints out the notes of
the chord. Use a dictionary whose keys are the (musical) keys and whose values are the lists
of steps.
"""

from enum import Enum

class Music(Enum):
    KEY = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    CHORD_STEPS = {1:[4,7], 2:[3,7], 3:[4,8], 4:[4,6], 5:[4,7,9], 6:[3,7,9],
                   7:[4,7,10], 8:[3,7,10], 9:[4,7,11], 10:[3,6,10]}

def validate_key(message_key):
    valid = False
    while not valid:
        try:
            user_input = input(message_key).capitalize()
            if user_input in Music.KEY.value:
                valid = True
            else:
                print('\nPlease enter a valid key.')
        except:
            pass
    return user_input

def validate_chord(message_chord):
    valid = False
    while not valid:
        try:
            user_input = int(input(message_chord))
            if user_input in Music.CHORD_STEPS.value.keys():
                valid = True
            else:
                print('\nEnter a number from the given options.')
        except ValueError:
            print('\nInvalid. Enter an integer.')
    return user_input

def get_notes(user_key, user_chord):
    notes = []
    key_list_transform = []
    for i in range(len(Music.KEY.value)):
        if user_key == Music.KEY.value[i]:
            notes.append(Music.KEY.value[i])
            key_list_transform = Music.KEY.value[i:] + Music.KEY.value[:i]
    for j in range(len(key_list_transform)):
        if j in Music.CHORD_STEPS.value[user_chord]:
            notes.append(key_list_transform[j])            
    return notes

def main():
    print('The following below are the musical keys:')
    print(Music.KEY.value)
    message_key = 'Enter a musical key: '
    user_key = validate_key(message_key)
    print('\nEnter 1 for chord type Major.')
    print('Enter 2 for chord type Minor.')
    print('Enter 3 for chord type Augmented Fifth.')
    print('Enter 4 for chord type Minor Fifth.')
    print('Enter 5 for chord type Major Sixth.')
    print('Enter 6 for chord type Minor Sixth.')
    print('Enter 7 for chord type Dominant Seventh.')
    print('Enter 8 for chord type Minor Seventh.')
    print('Enter 9 for chord type Major Seventh.')
    print('Enter 10 for chord type Diminshed Seventh.')
    message_chord = 'Enter a chord type: '
    user_chord = validate_chord(message_chord)
    chord_notes = get_notes(user_key, user_chord)
    print(f'\nThe following are the chord notes: {chord_notes}.')

if __name__ == '__main__':
    main()
