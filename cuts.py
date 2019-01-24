print("segment_char_index = "+str(segment_char_index))
print("string_index = "+str(string_index))
try:
    # if segment[segment_char_index] == "." and segment[segment_char_index+1] == "*":
    #     temporary_matched = True
    #     break
    if segment[segment_char_index] == "*" and input_string[string_index-1] == input_string[string_index]:
        temporary_matched = True
    if input_string[string_index] == segment[segment_char_index]:
        temporary_matched = True
    elif input_string[string_index] and segment[segment_char_index] == "." :
        temporary_matched = True
    # elif input_string[string_index] == False and segment[segment_char_index] != "*" :
        # temporary_matched = False
        # break
    else :
        temporary_matched = False
        break
    string_index +=1
    segment_char_index += 1
except IndexError:
    temporary_matched = False
break

# for i in range(character_start_index,len(segment)):
      # print("i = "+str(i))
      # print("input_string_index = "+str(input_string_index))
      # try:
      #     # if segment[i] == "." and segment[i+1] == "*":
      #     #     temporary_matched = True
      #     #     break
      #     if segment[i] == "*" and input_string[input_string_index-1] == input_string[input_string_index]:
      #         temporary_matched = True
      #     if input_string[input_string_index] == segment[i]:
      #         temporary_matched = True
      #     elif input_string[input_string_index] and segment[i] == "." :
      #         temporary_matched = True
      #     # elif input_string[input_string_index] == False and segment[i] != "*" :
      #         # temporary_matched = False
      #         # break
      #     else :
      #         temporary_matched = False
      #         break
      #     input_string_index +=1
      # except IndexError:
      #     temporary_matched = False
      # break



            # if segment[segment_char_index] == "." and segment[segment_char_index+1] == "*":
            #     temporary_matched = True
            #     break

            # elif string[string_index] == False and segment[segment_char_index] != "*" :
                # temporary_matched = False
                # break


#print(range(0,len(pattern_segments)))

#print("i = "+str(i))

            # print("i = "+str(i))
            #print("input_string_index = "+str(input_string_index))


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
segment_index=0
while ismatched = True:

    try:
        segment=pattern_segments[segment_index]
        print("segment_index = "+str(segment_index))
    except IndexError:
        print('No regex segment available for remaining string.')
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
