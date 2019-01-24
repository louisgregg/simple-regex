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


def simple_regex(input_string,pattern):
    #check regex pattern is valid.
    if pattern[0] == "*":
        print("Invalid regex pattern. Exiting. ")
        sys.exit()
    pattern_segments=pattern.split("*")
    print(pattern_segments)
    #print(range(0,len(pattern_segments)))
    #define a int to store our position in the input string
    input_string_index=0

    # Begin iterating through each segment separated by a *.
    for segment_index in range(0,len(pattern_segments)):
        segment=pattern_segments[segment_index]

        # Check if this segment is first and call the character counter for * if not
        if segment_index != 0:
            print("This section of the input string has been passed to the character counter: "+str(input_string[input_string_index:] ) )
            character_to_count=pattern_segments[segment_index-1][-1:]
            character_start_index=recurring_char_counter(input_string[input_string_index:],character_to_count)
        else:
            character_start_index=0
        input_string_index=input_string_index+character_start_index
        print("segment_index = "+str(segment_index))
        #print("i = "+str(i))
        #Beginning at the first occuring of a character not captured by the * regex symbol, this loop iterates through characters in a segment to check if it matches the regex pattern supplied.
        # for i in range(character_start_index,len(segment)):
        #         print("i = "+str(i))
        for i in range(character_start_index,len(segment)):
            print("i = "+str(i))
            print("input_string_index = "+str(input_string_index))
            try:
                # if segment[i] == "." and segment[i+1] == "*":
                #     temporary_matched = True
                #     break
                if segment[i] == "*" and input_string[input_string_index-1] == input_string[input_string_index]:
                    temporary_matched = True
                if input_string[input_string_index] == segment[i]:
                    temporary_matched = True
                elif input_string[input_string_index] and segment[i] == "." :
                    temporary_matched = True
                # elif input_string[input_string_index] == False and segment[i] != "*" :
                    # temporary_matched = False
                    # break
                else :
                    temporary_matched = False
                    break
                input_string_index +=1                    
            except IndexError:
                temporary_matched = False
            break
            # print("i = "+str(i))
            #print("input_string_index = "+str(input_string_index))
    ismatched=temporary_matched
    return ismatched


if __name__ == '__main__':
    print(str(sys.argv))
    print(str(sys.argv[1]))
    print(str(sys.argv[2]))
    print(simple_regex( str(sys.argv[1]) , str(sys.argv[2]) ))
