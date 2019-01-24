import sys
def simple_regex(input_string,pattern):
    """
    This method returns a boolean value if the pattern provided matches the input string.
    The method matches using any combination of the characters outlined below.
    Supported string characters and special regex characters:
    a-z
    .
    *

    Constraints: Can assume input of valid non-empty regex pattern.

    NOTE: Due to Python's command line parsing behaiour, the * regex character must be input as \* if calling the script from the command line OR enclosed in quotes like "*" or '*'.
    """

    """
    pseudo code description of core algorithm.
    ismatched=false
    for i in length(0,input_string):
        temporary_matched=false
        for j in length(0,pattern):
            if pattern[j] == "*"
                temporary_matched = true
            elif input_string[i] == pattern[j]:
                temporary_matched = true
    """

    ismatched = False
    n_characters_to_check = max([len(input_string), len(pattern)])
    print("checking "+str(n_characters_to_check)+" characters.")
    for i in range(0,n_characters_to_check):
        temporary_matched = False
        try:
            if i==0 and pattern[i] == "*":
                print("Invalid regex pattern. Exiting. ")
                sys.exit()
            if pattern[i] == "." and pattern[i+1] == "*":
                temporary_matched = True
                break
            if pattern[i] == "*" and input_string[i-1] == input_string[i]:
                temporary_matched = True
            if input_string[i] == pattern[i]:
                temporary_matched = True
            elif input_string[i] and pattern[i] == "." :
                temporary_matched = True
            elif input_string[i] == False and pattern[i] != "*" :
                temporary_matched = False
                break
            else :
                temporary_matched = False
                break
        except IndexError:
            temporary_matched = False
            break
        print(i)
    ismatched=temporary_matched
    return ismatched

def testrange():
    string = "apple"
    print("The string is "+string)
    for i in range(0,len(string)):
        print(string[i])

if __name__ == '__main__':
    print(str(sys.argv))
    print(str(sys.argv[1]))
    print(str(sys.argv[2]))
    print(simple_regex( str(sys.argv[1]) , str(sys.argv[2]) ))
