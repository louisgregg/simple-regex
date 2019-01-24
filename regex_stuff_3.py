import sys

#Returns the number of recurring instances of a character in a segment string
#for a segment after a * regex character.
def recurring_char_counter(segment,character_to_count):
    n_repeats=0
    is_matching=True
    while is_matching == True:
        if character_to_count == segment[n_repeats]:
            n_repeats += 1
        else:
            is_matching = False
    return(n_repeats)

def char_comparison(string_index, string, segment):
    """
    Re implement the for loop below
    """
    temporary_matched = True
    segment_char_index=0
    while temporary_matched == True:
        try:
            if segment[segment_char_index] == "*" and string[string_index-1] == string[string_index]:
                temporary_matched = True
            if string[string_index] == segment[segment_char_index]:
                temporary_matched = True
            elif string[string_index] and segment[segment_char_index] == "." :
                temporary_matched = True
            else :
                temporary_matched = False
                break
        except IndexError:
            try:
                segment[segment_char_index]
            except IndexError:
                print("Have reached the end of segment.")
                # temporary_matched = True
                break
            try:
                string[string_index]
            except IndexError:
                print("Have reached the end of string.")
                temporary_matched = False
                break
        string_index += 1
        segment_char_index += 1

        print("segment_char_index = "+str(segment_char_index))
        print("string_index = "+str(string_index))
        print("temporary_matched = "+str(temporary_matched))
    return([temporary_matched, string_index])

def simple_regex(input_string,pattern):
    #check regex pattern is valid.
    if pattern[0] == "*":
        print("Invalid regex pattern. Exiting. ")
        sys.exit()

    #Break regex into list of substring segments delimeted by the * character
    pattern_segments=pattern.split("*")
    print(pattern_segments)

    #define a int to store our position in the input string
    input_string_index=0

    # Begin iterating through each segment separated by a *.
    for segment_index in range(0,len(pattern_segments)):
        segment=pattern_segments[segment_index]
        print("segment_index = "+str(segment_index))
        # Check if this segment is first and call the character counter for * if not
        if segment_index != 0:
            print("This section of the input string has been passed to the character counter: "+str(input_string[input_string_index:] ) )
            character_to_count=pattern_segments[segment_index-1][-1:]
            character_start_index=recurring_char_counter(input_string[input_string_index:],character_to_count)
        else:
            character_start_index=0
        input_string_index=input_string_index+character_start_index


        #Beginning at the first occuring of a character not captured by the * regex symbol, this loop iterates through characters in a segment to check if it matches the regex pattern supplied.
        [temporary_matched, input_string_index] = char_comparison(input_string_index,input_string, segment)

    ismatched=temporary_matched
    return ismatched


if __name__ == '__main__':
    print(str(sys.argv))
    # print(str(sys.argv[1]))
    # print(str(sys.argv[2]))
    print(simple_regex( str(sys.argv[1]) , str(sys.argv[2]) ))
