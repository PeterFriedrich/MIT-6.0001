# Problem Set 4A
# Name: Peter Friedrich
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # base case
    if len(sequence) == 1:
        permutations = []
        permutations.append(sequence)
        return permutations

    # recursive case
    else:
        # call for permutations of smaller case
        temp = get_permutations(sequence[1:])
        permutations = []
        # insert new permutations using first sequence letter
        for i in range(len(temp)):
            for j in range(len(sequence)):
                    permutations.append(temp[i][j:] + sequence[0] + temp[i][:j])

        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    # Case 1: dog
    example_input = 'dog'
    print('Input:', example_input)
    print('Expected Output:', ['dog', 'dgo', 'odg', 'ogd', 'god', 'gdo'])
    print('Actual Output:', get_permutations(example_input))

    # Case 2: sam
    example_input = 'sam'
    print('Input:', example_input)
    print('Expected Output:', ['sam', 'sma', 'ams', 'asm', 'mas', 'msa'])
    print('Actual Output:', get_permutations(example_input))

    # Case 3: pal
    example_input = 'pal'
    print('Input:', example_input)
    print('Expected Output:', ['pal', 'pla', 'apl', 'alp', 'lap', 'lpa'])
    print('Actual Output:', get_permutations(example_input))

    print(get_permutations('blam'))
