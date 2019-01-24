import sys

#Returns the number of recurring instances of a character in a segment string
#for a segment after a * regex character.
def recurring_char_counter(string_section,character_to_count):
    n_repeats=0
    is_matching=True
    while is_matching == True:
        try:
            if character_to_count == string_section[n_repeats]:
                n_repeats += 1
            else:
                is_matching = False
        except IndexError:
            print("String counter has reached the end of the string.")
            break
    return(n_repeats)

def char_comparison(string_index, string, segment):
    """
    Re implement the for loop below
    """
    ismatched = True
    segment_char_index=0
    while ismatched == True:
        try:
            if segment[segment_char_index] == "*" and string[string_index-1] == string[string_index]:
                ismatched = True
            if string[string_index] == segment[segment_char_index]:
                ismatched = True
            elif string[string_index] and segment[segment_char_index] == "." :
                ismatched = True
            else :
                ismatched = False
                break
        except IndexError:
            try:
                segment[segment_char_index]
            except IndexError:
                print("Have reached the end of segment.")
                ismatched = True
                break
                # pass
            try:
                string[string_index]
            except IndexError:
                print("Have reached the end of string.")
                ismatched = False
                break
        string_index += 1
        segment_char_index += 1
        # print("segment_char_index = "+str(segment_char_index))
        # print("string_index = "+str(string_index))
        # print("ismatched = "+str(ismatched))
    return([ismatched, string_index])

def any_char_counter(string_section, next_regex_segment):
    """
    TODO:
    The use of the in operator is really nice here.
    However, it does not allow for wildcard characters.
    This means that we may need to rewrite this method to proceed through the string comparison incrementally on a character by character basis.
    This will be harder.
    """
    string_section_index = 0
    while segment_not_found == True:
        if next_regex_segment in string_section[string_section_index:]:
            Print(str(next_regex_segment)+" is present in "+str(string_section[string_section_index:]))
            string_section_index += 1
        elif next_regex_segment not in string_section[string_section_index:] and string_section_index == 0:
            Print("Regex expression "+str(next_regex_segment)+"is not present in "+str(string_section[string_section_index:]))
            is_matching = False
            break
        else :
            print("Regex expression "+str(next_regex_segment)+"has been located in string.")
            next_regex_segment
        return(is_matching)


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
    #Define an int to store which regex segment being used.
    segment_index=0
    ismatched=True
    while ismatched == True:

        try:
            segment=pattern_segments[segment_index]
            print("segment_index = "+str(segment_index))
        except IndexError:
            print('No regex segment available for remaining string.')
            try:
                input_string[input_string_index]
                ismatched = False
                break
            except IndexError:
                print("Input String has also finished.")
                break


    # Check if this segment is first and call the character counter for * if not
        if segment_index != 0:
            print("Input string section passed to the character counter: "+str(input_string[input_string_index:] ) )
            character_to_count=pattern_segments[segment_index-1][-1:]
            print("counting character: "+str(character_to_count))

            if character_to_count == ".":
                try:
                    if pattern_segments[segment_index+1] == "":
                        break
                    else:
                        character_start_index = any_char_counter(input_string[input_string_index:], pattern_segments[segment_index+1])
                except IndexError:
                    break


            character_start_index=recurring_char_counter(input_string[input_string_index:],character_to_count)
        else:
            character_start_index=0
        input_string_index=input_string_index+character_start_index

        #Beginning at the first occuring of a character not captured by the * regex symbol, this loop iterates through characters in a segment to check if it matches the regex pattern supplied.
        print("Comparing substring: "+str(input_string[input_string_index:]))
        print("with regex segment: "+str(segment))
        [ismatched, input_string_index] = char_comparison(input_string_index,input_string, segment)
        print("char_comparison returned: "+str(ismatched))

        # input_string_index += 1
        segment_index += 1
    ismatched=ismatched
    return ismatched


if __name__ == '__main__':
    print(str(sys.argv))
    # print(str(sys.argv[1]))
    # print(str(sys.argv[2]))
    print(simple_regex( str(sys.argv[1]) , str(sys.argv[2]) ))
