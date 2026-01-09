'''
cs2100 
a little starter code
samplecode from lecture
1/8/26


notes:
conversion math got moved into functions, that way we can convert multiple things, code can be reused!
we always write a docstring for every function and at the top of every file

round(xx, 2) -- a float CC, and a # of decimal places to round to
 CONSTANT-- variable named in ALL CAPS, never chnage these

 validate user input -- use a while loop to re-prompt until they enter the right thing

 what can this data type do? -- in python interavtive mode try help(str)


 string methods --
    "hello",upper() returns HELLO
    "he!!0".replace("!", "") returns heo
    "43".isdecimal() returns true

conditionals: if/elif/else
    handy shortcut: x = y if condition else z
                    (if condition is true, then x = y. otherwise, x = z)


'''

def main() -> None:
    '''prompt for temo in fahrenheit, convert to celsius and report'''

    temp_fahr = float(input("What is the temp in degrees Fahrenheit?/n"))
    temp_celsius = (temp_fahr - 32) * (5 / 9)
    print(f"That is {temp_celsius} in celsius!")

if __name__ == "__main__":
    main()

CEL_COLD_THRESHOLD = 4
CEL_HOT_THRESHOLD = 30

def fahr_to_cel(fahr: float) -> float:
    '''convert given farhenheiht to float
    parameters:
        fahr (float) - starting temp in fahr
    returns:
        float - ending temp in celsius '''
    
    cel = (fahr - 32) * (5 / 9)
    return cel

def cel_to_fahr(cel: float) -> float:
    ''' convert given celsius to fahrenheit
    parameters: 
    cel(float), the starting temp in degrees celsius
    returns:
         float, the converted temp in degrees fahrenheit'''
    
    fahr = cel * (9 / 5) + 32
    return fahr

def main() -> None:
    ''' temp conversion program
    prompt user for what unit to start with, F or C, validating it's one of the two
    prompt the user for what the startung temp is, validate it;s a decimal for conversion
    convert from F or c, to C to F, and report the result'''

    start_unit = input("WHat unit to start with F or C?\n")
    start_unit = start_unit.upper()
    while start_unit != "F" and start_unit != "C":
        start_unit = input("Must be F or C, please enter again.\n").upper()

    temp_str = input(f"WHat is the temp in {start_unit}?\n")
    while not temp_str.replace(".", "").isdecimal():
        temp_str = input("That needs to be a number, try again please\n")
    temp_start = float(temp_str)

    if start_unit == "F":
        temp_converted = fahr_to_cel(temp_start)
    else:
        temp_converted = cel_to_fahr(temp_start)