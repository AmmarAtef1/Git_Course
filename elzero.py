#                                        بسم الله الرحمن الرحيم                            
#                                    ________________________________


# print("mpppp")
# print("njjjj")

# ___________________________________________________________________________________________

# if True:
#    if True:
#       print("My world")
#       print("ammar")
#       print("ammmmm")


# if True:
# if True:                 # Indentation Error
#    print("My world")
#    print("ammar")
#    print("ammmmm")


# if True:
#     if True:
#     print("My world")   # IndentationError
#       print("ammar")
#       print("ammmmm")

# _____________________________________________________________________________________________        

# This is a comment not a code:   (Triple " or ')

"""  
sahjg,a
dbjk
vjdkbv
"""  

'''  
sahjg,a
dbjk
vjdkbv
'''   

# _______________________________________________________________________________________________



# ---------------------------------- Data types (6) --------------------------------------------
# ---------------------------------------------------------------------------------------------
# print(type(10))                   #=> int     (integer)
# print(type(-50))                  #=> int     (Integer)
# print(type(10.9))                 #=> float   (floating point number)
# print(type(-100.9595))            #=> float   (Floating Point Number)
# print(type("Hello"))             #=> str     (string) 
# print(type([1, 2, 3, 4, 5]))       #=> list    (list) 
# print(type({1, 2, 3, 4, 5}))       #=> set     (set)
# print(type((1,2,3,4,5)))           #=> tuple   (tuple)
# print(type({"one":1, "two":2, "three": 3}))              #=> dict   (dictionary)
# print(2==2)     # true or false                          #=> bool   ()

# _______________________________________________________________________________________________                              



# ------------------------------------ Variables (7) ------------------------------------------
# --------------------------------------------------------------------------------------------
# Syntax => [Variable Name] [Assignment Operator(=)] [Value]

# Name Convention and Rules:
# [1] Can Start With (a-z A-Z) Or Underscore(_)
# [2] You Cannot Start With Num Or Special Characters(@,#,$,%,dash(-))
# [3] Can Include(between it) (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] "Name" is Not Like "name" [ Case-Sensitive ]

# Note:
# You must first assign the variable then print it not vice versa     
# -------------------------------------------------------

# Types of variables 'Naming conventions':
# [1] Normal: 
# The var is a single word.   
# Ex: name = "string"   => name is a single word

# [2] camelCase: 
# The var is two words, first letter of each word is lowercase, and the first letter of each subsequent 
# concatenated word is Capitalised, and it doesn't have any characters between the words.
# Ex: myName = "string"      => m is small @ N is Capital    

# [3] PascalCase: 
# Each word starts with an uppercase letter, and there are no separators between words.
# Ex: MyName = "ammar"       => M is Capital @ N is Capital

# [4] snake_case or Underscore:  
# Each word is separated by an underscore, and all letters are lowercase @ Best Practice In Python
# Ex: my_name = "Ammar"      => m is small, n is small @ separated by an underscore

# print(name)
# print(myName)
# print(MyName)
# print(my_name)

# myVariable= "Ammar"
# print(myVariable)

# _myVariable= "Ammar"
# print(_myVariable)

# _______________________________________________________________________________________________



# ----------------------------------- Variables (8) ----------------------------------------------
# -----------------------------------------------------------------------------------------------
# The Source Code:  The Original Code You Write on Computer
# Translation:      Converting Source Code Into Machine Language
# Compilation:      Translate Code Before Run Time
# Run-Time:         The Duration Which The App Takes To Execute Commands
# Interpreted:      Code Translatation On The Fly During Execution
# -------------------------------------------------------------

# x = 10
# x = "hello"
# x = 5
# x = "ammar"
# print(x)   
# Note=> variable x here equal "ammar" which means variable = the last variable   
#           and this is because python is dynamically typed language    
#              أي أنها يمكن أن تغير الداتا أثناء run time
#------------------------------------------------------------------------  

# Reserved Words:
# [1] There are Reserved Words that u can't use in naming variables, as in Windows u can't name folder 
#                             by words like "aux" or "con".
# [2] To know the Reserved Words u can't use in naming variables, write this code => help("keywords")

# help("keywords")   #=> ex: class, if ....etc

# Note that the name of variable has a white color.
# -----------------------------------------------------

# reserved words
# help("keywords") 

# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

# _____________________________________________________________________________________________
 


#-------------------------------- Escape Sequences Characters (9) ---------------------------
#------------------------------------- Special Characters -----------------------------------
# [1] \b        => BackSpace          => Removes the char before it
# [2] \newline  => Escape NewLine + \
# [3] \\        => Escape BackSlash
# [4] \'        => Escape Single Quotes
# [5] \"        => Escape Double Quotes
# [6] \n        => Line Feed
# [7] \r        => Carriage Return
# [8] \t        => Horizontal Tab
# [9] \xhh      => Hexadecimal representation or Character Hex Value  
# [10] \ooo     => Octal representation
# [11] \a       => Alert
# ------------------------------------------
            
# [1] \b => BackSpace (The removable char\): 
# =>  Removes the char before it

# print("Hello\b World")                # Will Remove o           => Hell World
# print("Hello \b World")               # Will Remove nothing    => Hello World
# print("Hello\b\bWorld")               # Will Remove o and l     => HelWorld
# print("Hello\b\b World")              # Will Remove o and l     => Hel World
# print("Hello \b\b World")             # Will Remove only o     => Hell World
# print("Hello \b \b World")            # Will Remove nothing     => Hello World


# [2] \newline => Escape New Line (At the end of the escaped line\):  
# =>  prevent making new lines and put the all command in one line:

# print("Hello \
# I Love \
# Python")         # => Hello I Love Python


# [3] \\ => Escape Back Slash (\\):
# print("I Love Back Slash \\")     # => I Love Back Slash \


# [4] \' => Escape Single Quote (" \'string\' "):
# print("\'ammar and ahmed\'")                # => 'ammar and ahmed'
# print('I Love Single Quote \'test\'')       # =>  I Love Single Quote 'test'


# [5] \" => Escape Double Quotes (' \"string\" '):
# print('\"ammar and ahmed\"')                # => "ammar and ahmed"
# print("I Love Double Quotes \"Test\" ")     # => I Love Double Quotes "Test" 


# [6] (\n) Line Feed : 
# =>  Makes a new line  Vs Escape new line
# print("Hello World\nSecond Line")       # => Hello World
#                                         # => Second Line


# [7] (\r) Carriage Return : 
# =>  Replace what before \ with after \r
# print("123456 \rAbcde")          # Abcde6
# print("ammar \rahmed")           # ahmed
# print("ammar atef \rahmed")      # ahmed atef
# print("ammar \rahmed atef")      # ahmed atef
# print("12345 \rAbcde")           # Abcde
# print("1 \rAbcde")               # Abcde


# [8] (\t) Horizontal Tab :
#  => Makes spaces 
# print("Hello \tPython")           # => Hello   Python


# [9] (\x + Hex value) Character Hex Value or Hexadecimal representation :
# => Represents a character using its hexadecimal value. 
# For example, '\x48' represents the character 'H'.
# print("\x41\x6D\x6D\x61\x72 \x49\x73 \x54\x48\x45 \x47\x52\x45\x41\x54\x45\x53\x54 \
# \x42\x49\x4F\x49\x4E\x46\x4F\x52\x4D\x41\x54\x49\x43\x49\x41\x4E")
# => Ammar Is THE GREATEST BIOINFORMATICIAN


# [10] (\ooo) Octal representation:
# => Represents a character using its octal value. 
# For example, '\110' represents the character 'H'.
# print("Octal representation: \110")                   # => Octal representation: H


# [11] (\a) Alert:
# => Produces an audible or visible alert. Its effectiveness may vary across different platforms.
# print("This is an alert! \a")
# ________________________________________________________________________________________________



#----------------------------------------- Concatenation (10) --------------------------------
# ---------------------------- "connect two strings or more to each other" ----------------------
#------------------------------------------------------------------------------------------------
# WE use plus sympol (+) to concatenate in Python @ Java script

# ana = "I Love"
# kink = "myself"
# print(ana+kink)         # => I Lovemyself
# print(ana + kink)       # => I Lovemyself
# print(ana+" "+kink)     # => I Love myself
# OR:
# full = ana + " " + kink
# print( full)


# There are 3 ways to print space between two strings:
# 1) Make space after the first str => "I Love "
# 2) Make space before the sec str => " myselff"
# 3) Connect the space in the print comamndline as a str to concatenate 
#    to variables(ana,king) as they also str => print(ana + " " + kink)
  

# a = "first \
# second \
# third"
#                 # WE USE \ TO ESCAPE NEW LINE WHERE ALL ARE IN THE SAME LINE  
# b = "a \
# b \
# c"
# print(a + "\n" +b)  
#                 # We make new line by "\n" and must be as a string to concatenate to str variables(a,b)


# Note: Can only concatenate str (not "int") to str
# print("Hello" + 1)       # => TypeError: can only concatenate str (not "int") to str

# _________________________________________________________________________________________________



#-------------------------------------- Strings (11) -----------------------------------------
#---------------------------------------------------------------------------------------------

# 1) strings are put inside single or double quotes:

#my_string_one = 'These are Single Quotes'
#mystringtwo = "These are Double Quotes"
#print(my_string_one)
#print(mystringtwo)


# 2) I can insert single quote inside double quotes and vise versa 
#       and this is an alternative way to Escape seq charcs:

# print("These are Double Quotes\"test\" ")
# print("These are Single Quotes\'test\' ")
# OR:
# my_string_three = 'These are Single Quotes "Test"'
# my_string_four = "These are Double Quotes 'Test'"
# print(my_string_three)
# print(my_string_four)


# 3) How can I print multible lines?:

# [First]: This is for print multible lines in a single line by using escape seq charc
#                      To escape new line by \

# my_string_five = """First \
# Second "test" 'test'\
# Third"""
# print(my_string_five) 
# Note: Triple single and triple double quotes also make escape for "" @ '' also for \


# [Sec]: This is for print multiple lines as separated lines we use triple single or triple double quotes:
# my_string_five = '''First
# Second 
# Third'''
# print(my_string_five)
 
# my_string_six = """First
# Second
# Third"""
# print(my_string_six)

# 4) Triple single and triple double quotes also make escape for "" , '' , \ :

# my_string_five = '''First
# Second 'Test' "Test"
# Third'''
# print(my_string_five)

# my_string_six = """First
# Second "Test" \ 'Test'
# Third"""
# print(my_string_six)

# my_string_seven = """First
# Second "Test" \\ 'Test'              # one \ make escape and the other one appears
# Third"""
# print(my_string_seven)

# my_string_eight = """First
# Second "Test" \\\ 'Test'       # one \ make escape and the other tow appear
# Third"""
# print(my_string_eight)

# my_string_six = """first \
# second "test" \\\ 'test' \
# third"""                       # \ in the end of line, it make ignorance or escape of new line
# print(my_string_six)

# _________________________________________________________________________________________________



#------------------------------- Strings Indexing & Slicing (12) ------------------------------
#-----------------------------------------------------------------------------------------------

# String Indexing & Slicing:
# [1] All Data in Python is Object
# [2] Object Contains Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets [] To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# [7] Spaces are considered as characters
# --------------------------------------------------------------------------------------


#---------------------------- Indexing ( Access Single Item ) ---------------------------
# my_string = "I Love Python"
# print(my_string[0])  # Index 0 => I => 1st Character From The Beginning, Output => I
# print(my_string[9])  # Index 9 => t => 10th Character From The Beginning, Output => t
# print(my_string[1])  # Index 1 => t => 10th Character From The Beginning, Output => space

# print(my_string[-1])  # Index -1 => First Character From The End, Output => n
# print(my_string[-6])  # Index -6 => 6th Character From The End, Output => P


#--------------------------- Slicing ( Access Multiple Sequence Items ) ---------------------
# [Start:End] End Not Included
# [Start:End:Steps]

# my_string = "I Love Python"
# print(my_string[8:11])   # Start from index 8 and end at index 10, Output => yth 
#                                     as End Not Included
# print(my_string[7:13])    # Start from index 7 and end at index 12, Output => Python
# print(my_string[2:6])     # Start from index 2 and end at index 5, Output  => Love

# print(my_string[:10])     # If Start is not written, it will start from 0, output => I Love Pyt
# print(my_string[7:])      # If End is not written, it will go to the end, output => Python
# print(my_string[:])       # Full Data, Output => I Love Python

# more steps:
# my_string = "I Love Python"
# print(my_string[0::1])    # Full Data, Output => I Love Python
# print(my_string[::1])     # Full Data, Output => I Love Python
# print(my_string[::2])     # Will Move 2 Steps, Output => ILv yhn
# print(my_string[::3])     # Will Move 3 Steps, Output => Io tn

# ________________________________________________________________________________________________________________



#------------------------------------- Strings Methods1 (13) ---------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#                                      (1) len(variable)
# => "len" means "length".
# => Method return the number of items in a container 
#    and count from 1 not zero unlike index:
# => Note:
# => Spaces are in count.

# a = ("I love python")
# b = ("   I love python   ")
# print(len(a))        # => 13
# print(len(b))        # => 19


#                                     (2) strip(), rstrip(), lstrip() 
# "strip" means to "remove or cut"
# => Method returns a new string with the leading and trailing characters(الأطراف) removed

# Note that: 
# Write the char u wanna remove inside () and if u let it empety, it will remove whitespaces if 
# they are existed @ if not, it remove nothing:

# b = "I Love Python"
# print(b.strip())            # remove nothing as there is no whitespaces not from R or L
  
# a = "   I Love Python   "
# print(a.strip())            # Remove all whitespaces from right @ left
# print(a.rstrip())           # Remove whitespaces only from right
# print(a.lstrip())           # Remove whitespaces onlr from left
# print(len(a.lstrip()))      # Counting char after lstrip() 
#                               To make sure that whitespaces from left are removed 


# c = "I Love Python"
# print(c.strip("I Love"))      # Remove "I Love" بيشتغل ع الأطراف سواء يمين أو شمال طالما محددتش
# print(c.strip("Python"))      # Remove "Python" بيشتغل ع الأطراف سواء يمين أو شمال طالما محددتش 

# c = "I Love Python III"
# print(c.rstrip("I"))             # Remove "I" only from right and all of I from right are removed
# print(c.lstrip("I"))             # Remove "I" only from left
# print(c.lstrip("i"))             # Remove nothing as it's case sensitive

# b = "#####I Love Python####"
# print(b.strip("#"))              # All of # are removed from R and L
# print(b.rstrip("#"))             # All of # are removed from R only
# print(b.lstrip("#"))             # All of # are removed from L only

# c = "@#@#@#I Love Python@#@#@#"
# print(c.strip("#@"))
# print(c.rstrip("@#"))
# print(c.lstrip("@#"))
 

#                                           (3) title() 
# => Method capitalizes "the first letter of each word" in a string and also "the letter afer numbers" 
#                             and leaves the rest of the letters unchanged. 

# d = "i love 255d graphics and 3g technology and python"
# print(d.title())
 

#                                           (4) capitalize() 
# =>  Method capitalizes "only the first character of a string", 
#     and leaves all other characters in the string unchanged.

# e = "i love 2d graphics and 3g technology and python"
# print(e.capitalize())
 

#                                           (5) zfill(one argument)
# => means "zerofill" is a string method that can be used to pad a string with leading zeros 
#                             to a specified length: 

# f, g, h, i = "1", "11", "111", "1111"
# print(f.zfill())            # Erorr as str.zfill() takes exactly one argument (0 given)
# print(f.zfill(4))           # 0001
# print(g.zfill(4))           # 0011
# print(h.zfill(4))           # 0111
# print(i.zfill(4))           # 1111
 

#                                           (6) upper() 
# => is a string method which returns a new string with "all alphabetic characters in uppercase"

# j = "ammar"
# print(j.upper())       # AMMAR


#                                           (7) lower() 
# => is a string method which returns a new string with "all alphabetic characters in lowercase".

# o = "AMMAR"
# print(o.lower())       # ammar

# _________________________________________________________________________________________________________________________



#------------------------------------- Strings Methods2 (14) -------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#                                      8) split() - rsplit()
# Takes The elements of the str and put them in a list and split them by space (default) 
# If there is no spaces, so there is no split as it put the whole str as one element in a list.

# a = "I Love Python and PHP"
# print(type(a.split()))             # list
# print(a.split())                   # ['I', 'Love', 'Python', 'and', 'PHP']

# b = "ILovePythonandPHP"
# print(b.split())                   # ['ILovePythonandPHP']

# c = "I-Love-Python-and-PHP"
# print(c.split())                   # ['I-Love-Python-and-PHP']

# c = "I-Love-Python-and-PHP"
# print(c.split("-"))                # ['I', 'Love', 'Python', 'and', 'PHP']


# Max split: Makes # of splits and put the rest of the str as one element in the list:
# e = "I-Love-Python-and-PHP" 
# print(e.split("-", 2))     # ['I', 'Love', 'Python-and-PHP'] makes only two splits

# rsplit(): makes split from the right side
# a = "I-Love-Python-and-HP" 
# print(a.rsplit("-", 2))     # ['I-Love-Python', 'and', 'PHP'] makes two splits from the right


#                                         9) center(at least 1 argument)
# g = "ammar"
# print(g.center())          # Need to incorborate at least an argument between parentheses
# print(g.center(9))         # it adds 2 spaces at the right and 2 at the left as ammar is 5 letter
# print(g.center(9, "#"))    # it adds 2 hashes at the right and 2 at the left
# print(g.center(10, "@"))   # it adds 3 at sign at the right and 2 at the left


#                                         10) count(one argument"TEXT")
#                                        count(substring(TEXT), start, end)

# => counts How many times the argument existed or repeated between the whole string:
# => to count the occurrences of a particular element.

# k="I Love Python and PHP becuase PHP is easy"
# print(k.count())           # Need to incorborate at least an argument between parentheses
# print(k.count("PHP", "I"))        # 2   
# print(k.count("PHp"))        # 0 because It's case-sensitive
# print(k.count("PHP",0,25))   # only one "PHP" as we write the start and end index         

 
#                                          11) swapcase() 
# exchanges/ replaces the uppercase with the lowercase and vice versa:

# i="I LOVE PYTHON"       
# m="i love python"       
# print(i.swapcase())       # i love python
# print(m.swapcase())       # I LOVE PYTHON


#                                           12) startswith(prefix)
#                                        startswith(prefix, start, end)

# It shows if the str starts with this char or not by using bolean value:

# n="I Love Python"
# print(n.startswith("I"))         # True
# print(n.startswith("i"))         # False
# print(n.startswith("P",7))       # True
# print(n.startswith("L",2,5))     # True

#                                           13) endsswith(suffix)
#                                        endsswith(suffix, start, end)
# It shows if the str ends with this char or not by using bolean value:

# o="I Love Python"
# print(o.endswith("n"))         # True
# print(o.startswith("N"))       # False
# print(o.endswith("e",2,5))     # False as 5 index not included
# print(o.endswith("e",2,6))     # True

# __________________________________________________________________________________________________



#-------------------------------------- Strings Methods3 (15) -------------------------------------- 
#--------------------------------------------------------------------------------------------------
#                                   14) index(substring(TEXT), start, end)
#                                      or index(substring, start, end) 
  
# Searches on the position of an element inside the str 
# and index it (refer to it by its arranging # in str )

# a="I love my self"
# print(a.index("m"))         # 7
# print(a.index("m",0,10))    # 7
# # print(a.index("m",0,5))   # => error as substring not found


#                                   15) find(substring(text))
#                                  or find(substring, start, end)
# The same as index() BUT index() stops the code execution by error but find() doesn't

# b = "I love my self"
# print(b.find("m"))              # 7
# print(b.find("m",0,10))         # 7
# print(b.find("m",0,5))          # => -1  not error (unlike index())



#                                  16) rjust(width, fillchar) 
#                                      ljust(width, fillchar)
# "justify" is The same as center() BUT it is more specific than center()

# c="ammar"
# print(c.rjust(8))          # It will add 3 spaces on the right 
# print(c.rjust(8, "4"))     # It will add 444 on the right
# print(c.ljust(8))          # It will add 3 spaces on the left 
# print(c.ljust(8, "4"))     # It will add 444 on the left


#                                   17) splitlines()
# makes all lines in a list

# d="""first line
# second line
# third line"""
# print(d.splitlines())         # ['first line', 'second line', 'third line']
# print(type(d.splitlines()))   # make sure that it is a list

# e="first line\nsecond line\nthridline" 
# print(e.splitlines())         # ['first line', 'second line', 'thridline']
 

#                                   18) expandstab(# of tabs)
# makes tabs or spaces and you can control of its number

# f="Hello\tworld\tI\tam\tAmmar"
# print(f)               # Hello  world   I       am      Ammar
# print(f.expandtabs(1)) # only one tab or space: Hello world I am Ammar
# print(f.expandtabs(2)) # only 2 tabs(spaces): Hello  world I am  Ammar



#                                  19) Built-in finctions 
#                                  That check bolean value:
 

#                                        a) istitle()
# a = "I Love Python And 3G"    
# b = "I Love Python And 3g"      
# print(a.istitle())              # True
# print(b.istitle())              # False as the char(g) after the no(3) is not capital


#                                        b) isspace()
# a = " "
# b = ""
# print(a.isspace())    # True
# print(b.isspace())    # False


#                                        c) islower()
# a = 'i love python'
# b = 'I Love Python'
# print(a.islower())         # True
# print(b.islower())         # False


#                                        d) isidentifier()
# Check if the variable name is valid or not:

# n = "ammar_atef"
# o = "ammaratef100"
# p = "ammar--atef100"
# print(n.isidentifier())    # True
# print(o.isidentifier())    # True
# print(p.isidentifier())    # False


#                                        e) isalpha()

# a = "AaaaaBbbbbb"
# b = 'AaaaaBbbbbb111'
# print(a.isalpha())       # True
# print(b.isalpha())       # False as it contains numbers

#                                        f) isalnum()
# "is alphabetnumber" checks if the str contains alph or # or both:

# a = "AaaaaBbbbbb"
# b= "1111111111"
# d = "AaaaaBbbbbb111"

# print(a.isalnum())       # True
# print(b.isalnum())       # True
# print(d.isalnum())       # True
 
# _______________________________________________________________________________________________



#-------------------------------------- Strings Methods4 (16) -------------------------------------
#-------------------------------------------------------------------------------------------------
#                                       20) replace(Old value, New value, count)

# mystring = "Hello One Two Three One One" 
# print(mystring.replace("One", "1"))       # Hello 1 Two Three 1 1
# print(mystring.replace("One", "1", 1))    # Hello 1 Two Three One One
# print(mystring.replace("One", "1", 2))    # Hello 1 Two Three 1 One

      
#                                       21) "Separator".join(Iterable object) 
#                                            Vs splitlines()
# Makes the list be string

# mylist = ["ammar", "atef", "ahmed"]
# print("".join(mylist))              # ammaratefahmed
# print(" ".join(mylist))             # ammar atef ahmed
# print("-".join(mylist))             # ammar-atef-ahmed
# print(", ".join(mylist))            # ammar, atef, ahmed
# print(type("-".join(mylist)))       # str ,To make sure that it is string

# ________________________________________________________________________________________________

 

#--------------------------------------- Strings Formatting "old way" (17) ------------------------
#-------------------------------------------------------------------------------------------------
#                                     1) placeholder (%s, %d., %f,....) 
#                                              and concatenate
               
#                                        print("...... %s" % "......")
#                                        print("...... %s" % variable)
#             print("..... %s and ..... %d and ..... %f" % (variable1,variable2,variable3))

# also known "string interpolation": the process of inserting string or variables in a text":
# PLACEHOLDER (%): is a word,characters or a string of characters that 
#                temporarily takes the place of the final data: 

# name= "ammar"
# age= 23
# rank= 10

# print("my name is: " + name)                              # my name is: ammar
# print("my name is: " + name + "my age is: " + age)        # Type error as
#                                                   "only concatenate str (not "int") to str"
 
# print("my name is %s" % "ammar")
# print("my name is %s" % name)
# print("my name is %s and my age is %d and my rank is %f" % (name,age,rank))

# %S    => string: perform the concatenation of strings together
# %d    => number(digital): a placeholder for decimal value
# %f    => float: a placeholder for float value

# n = "ammar"
# l = "python"
# y = 10
# print("my name is %s I am %s developer with %d years experience" % (n,l,y))#


#                                    Controle of floating point number: 
# There are six zeros after the integral as usaual but I can control this number by:

# myfloat = 10
# print("my float is %f" % myfloat)         # => 10.000000
# print("my float is:",  myfloat)           # => 10
# print("my float is %.2f" % myfloat)       # => 10.00 
 

#                                      Truncate string (slice string)

# mymessage = "Hello guys, Welcome at my humble organiztion of bioinformatics"
# print("my meesage is %s" % mymessage)     # print all the message
# print("my meesage is %.5s" % mymessage)   # only print the first 5 char "my message is Hello"

# ________________________________________________________________________________________________



#--------------------------------- st1rings formatting "new way" (18) ----------------------
#-----------------------------------------------------------------------------------------------
#                                       2) format() method 
                           
#                                 placeholder ({:s}, {:d}, {:f},....) 

#                                              Syntax:
#                                  print("..... {}".format("....."))
#                                  print("..... {}".format(variable))
#           print(".... {} and .... {} and .... {}" .format(variable1,variable2,variabl31))


# name= "ammar"
# age=23
# rank=10

# print("my name is {}".format("ammar"))
# print("my name is {}".format(name))
# print("my name is {}".format(age))
# print("my name is {}".format(rank))
# print("MY NAME IS {} AND MY AGE IS {} AND MY RANK IS {}" .format(name,age,rank))
# print("MY NAME IS {:s} AND MY AGE IS {:d} AND MY RANK IS {:f}" .format(name,age,rank))

# {:s} => STRING
# {:d} => NUMBER
# {:f} => FLOATING POINT NUMBER


# n= "ammar"
# l="python"
# y=10
# print("my name is {} I am {} developer with {:d} years exp" .format(n,l,y))


#                                   Control floating point number:

# myfloat=10
# print("my float is {:f}" .format(myfloat))     # => 10.000000
# print("my float is {:.2f}" .format(myfloat))   # => 10.00


#                                    Truncate string (slice string)

# mymessage = "Hello guys, Welcome at my humble organiztion of bioinformatics"
# print("my meesage is {:s}" .format(mymessage))
# print("my meesage is {:.5s}" .format(mymessage))    # only print 5 char "Hello"
# print("my meesage is {:.10s}" .format(mymessage))   # only print 10 char "Hello guys"

# fname = "Ammar"
# mname = "Atef"
# lname = "Ahmed"
# print("My Full Name is {} {:.1s} {}" .format(fname, mname, lname)) # My Full Name is Ammar A Ahmed


#                                    Format Money

# mymoney = 545854222595
# print("my money in bank is: {:d}" .format(mymoney))   # 545854222595
# print("my money in bank is: {:_d}" .format(mymoney))  # 545_854_222_595
# print("my money in bank is: {:,d}" .format(mymoney))  # 545,854,222,595

# Note: not all signs are used for coordination as at sign "@"
# print("my money in bank is: {:@d}" .format(mymoney))             # => wrong
 


#                                    Items Rearrangement

# a,b,c= "one", "two", "three"
# print("Hello {} {} {}" .format(a,b,c))       # Hello one two three
# print("Hello {} {} {}" .format(b,a,c))       # Hello two one three
# print("Hello {1} {2} {0}" .format(a,b,c))    # Hello two three one
# print("Hello {2} {0} {1}". format(a,b,c))    # Hello three one two 

# print("Hello {2} {0} {}".format(a,b,c))      #ValueError
# print("Hello {2} {} {}".format(a,b,c))       #ValueError
# ValueError: cannot switch from manual field specification to automatic field numbering  

# # print("Hello {2} {} {}".format(a,b))  # => IndexError: Replacement index 2 out of range for positional args tuple
# print("Hello {} {}".format(a,b))        # => Hello one two

# x,y,z= 10,20,30
# print("Hello {} {} {}" .format(x,y,z))                 # Hello 10 20 30
# print("Hello {1:d} {2:d} {0:d}".format(x, y, z))       # Hello 20 30 10
# print("Hello {2:f} {0:f} {1:f}".format(x, y, z))       # Hello 30.000000 10.000000 20.000000
# print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z)) # Hello 30.00 10.0000 20.00000



#                                3) F-strings, or formatted string literals

# Formate in version 3.6+
# Syntax:                   print(f"..... {variable1} and .... {variable2}")  

# A benefit of using f-strings is that the code is easy to interpret due to the variable names
# being displayed in the string itself, compared to the format() method 
# where the variable names are bunched at the end of the string.


# myname= "ammar"
# myage=23
# print("name is {myname} and age is {myage}")  # my name is {myname} and my age is {myage}
# print(f"name is {myname} and age is {myage}") # my name is ammar and my age is 23
 
# ___________________________________________________________________________________________



#----------------------------------------- Numbers###(19) ----------------------------------------
#-------------------------------------------------------------------------------------------------
#                                           1) Integer #
# print(type(1))
# print(type(100))
# print(type(-10))         # int
# print(type(0))


# #                                           2) Float #                       
# print(type(1.50))
# print(type(100.50))
# print(type(-10.9))       # float
# print(type(0.26))
# print(type(-0.26))


#                                           3) Complex # 
# In the form a + bj, where a and b are real numbers, and j is the imaginary unit
# Consists of two parts (Real part) and (Imaginary part)  Ex: 6+5j (Real=6), (Imag=5), 1 - 1j
 
# mycomplexnumber=8+4j
# print(type(mycomplexnumber))                              # complex

# print("Real part is: {}".format(mycomplexnumber.real))    # 8.0
# print("Real part is: {}".format(mycomplexnumber.imag))    # 4.0



# Notes:
# can convert int to float or to complex
# can convert float to int or to complex
# can't convert complex to int or to float

# print(float(100))      # 100.0
# print(complex(100))    # 100+0j

# print(int(10.50))      # 10
# print(complex(10.50))  # 10.50+0j

# print(int(5+4j))         # error => can't convert to int
# print(float(5+4j))       # error => can't convert to float

# ________________________________________________________________________________________________



#---------------------------------------- Arithmetic Operators(20) ------------------------------       
#-------------------------------------------------------------------------------------------------
#                                          1) Addition (+)
# print(10+4)
# print(-10+4)
# print(10.4+4.6)

#                                          2) Substraction (-)
# print(60-30)
# print(-60-30)
# print(-60- -30)
# print(2.5-2.1)

#                                          3) Multiplication (*)
# print(4*10)
# print(5+4*10)    # 45  # Here it starts with multiplication then addition
# print((5+4)*10)  # 90  # Here it starts with bracketes solving then multiplication

#                                          4) Devision (/)
# print(100/5)       # 20.0
# print(int(100/5))  # 20

#                                          5) Modulus (%)
# print(8%2)    # 0
# print(9%2)    # 1
# print(20%5)   # 0
# print(22%5)   # 2

#                                          6) Exponent (**)
# print(2**5)   # = 2*2*2*2*2*2
# print(6**3)   # = 6*6*6        

#                                          7) Floor Division (//)
# print(100//20)   # 5
# print(110//20)   # 5
# print(140//20)   # 7
# print(142//20)   # 7

# _______________________________________________________________________________________________


#                                 (Data structures types in Python)

# The most common built-in data structures in Python include:
# [1] List
# [2] Tuple
# [3] Set
# [4] Dictionary

# Note:
# => A key concept used to differentiate Python data structures is MUTABILITY. 
# => Mutability refers to whether or not a data structure can be modified after it has been created.
# => Python data structures can be classified into two main categories based on their mutability.
# => That is, mutable or immutable:

# [1] Immutable data structures
# These are data structures that cannot be changed once they are created. 
# The tuple is an immutable data structure in Python.

# [2] Mutable data structures
# These are data structures that can be modified in some way after creation. 
# Mutable data structures in Python include the list, set, and dictionary.


# _______________________________________________________________________________________________



#------------------------------------------ lists1[] (21) -------------------------------------------
#------------------------------------------------------------------------------------------------

# Notes:
# lists items are enclosed in square brackets
# lists are ordered, use index(zero-based indexing) to access items of the list 
# lists are mutable (can be edited, removed or added)
# lists items aren't unique "can have duplicated items and nonordered" as I can write ["one","two","one"]
# lists can have diff data types


# SO,
# => Lists are therefore suitable for storing a dynamic collection of elements that may need 
#    to change, and whose order needs to be maintained.
# ----------------------------------------------------------------------------------

#                                     =>  list()

# => use the list() constructor to create a list from an iterable, such as a tuple.

# my_tuple = ("Eagle", "Penguin", "Parrot") 
# # my_list = list(my_tuple)
# # print(my_list)                          #  ['Eagle', 'Penguin', 'Parrot'] 
# --------------------------------------------------------------


#                                     =>  range()
#                           Syntax: range(start, stop, step)

# => use the range() function to generate a sequence of numbers based on a given start and end point.

# => Syntax: range(start, stop, step):
# start: An integer number specifying the start point (included).
# stop: An integer number specifying the end point (not included).
# step: An integer number specifying the incrementation. The default is 1.

# We then pass the result of the range function to the list() constructor to convert it to a list.

# range_list = list(range(0,6))
# print(range_list)                              # [0, 1, 2, 3, 4, 5]

# range_list = list(range(0,5,2))
# print(range_list)                              # [0, 2, 4, 6]

# range_list = list(range(0,5,3))                # [0, 3]
# print(range_list)

# --------------------------------------------------------------------------------------


#                                      => Duplicates 

# => Since lists are ordered and indexed, they allow duplicate elements.
# a = [1, 2, 3]
# b = a + a
# print(b)                      # [1, 2, 3, 1, 2, 3]

# -----------------------------------------------------------------------------------------


#                     => How to access to a single item (indexing):

# mylist = ["one","two","three", 1, 2.2, True] 
# print(mylist)           # The Whole list
# print(mylist[2])        # "three"
# print(mylist[5])        # True
# print(mylist[-1])       # True
# print(mylist[-3])       # 1
# print(mylist[100])      # IndexError: list index out of range

# ------------------------------------------------------------------------------------


#                     => How to access multible sequence items (Slicing):

# mylist = ["one","two","three", 1, 2.2, True] 
# print(mylist[1:4])      # ['two', 'three', 1]
# print(mylist[:4])       # ['one', 'two', 'three', 1]
# print(mylist[1:])       # ['two', 'three', 1, 2.2, True]
# print(mylist[1:6])      # ['two', 'three', 1, 2.2, True]
# print(mylist[::1])      # ['one', 'two', 'three', 1, 2.2, True]
# print(mylist[::2])      # ['one', 'three', 2.2]



# Edit in lists:

# mylist=["one","two","three", 1, 2.2, True] 
# mylist[1]="one"
# print(mylist)                   # ['one', 'one', 'three', 1, 2.2, True]
# mylist[1]=2                     # EDIT INDIX 1"TWO" BY 2
# print(mylist)                   # ['one', 2, 'three', 1, 2.2, True]
# mylist[-1]=False                # = mylist[5]=False     
# print(mylist)                   # ['one', 2, 'three', 1, 2.2, False]


# mylist=["one","two","three", 1, 2.2, True] 
# mylist[1:5]=[]
# print(mylist)                  # ['one', True]
# mylist[0:2]=[]                 # will remove "one","two" as edited by space
# print(mylist)                  # ['three', 1, 2.2, True]
# mylist[0:3]=["am", "ma", "r"]  # will remove "one","two","three" and edited by "am", "ma", "r"
# print(mylist)                  # ['am', 'ma', 'r', 1, 2.2, True]
# mylist[0:3]=["am"]             # will remove "one","two","three" and edited by only "am"
# print(mylist)                  # ['am', 1, 2.2, True]

# _________________________________________________________________________________________________


#                                     => Nested Lists

# => Nested lists occur when we have a list containing another list or lists as its element(s).
# => They are useful when working with structured data.                      =================
# => We can create a nested list by assigning two or more list variable names, 
#    separated by commas, to a variable.

# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# c = [a, b]
# print(c)                   # [[1, 2, 3], ['a', 'b', 'c']]

# OR => Alternatively, we can create a nested list by using lists directly in the variable definition. 
# c = [[1, 2, 3], ['a', 'b', 'c']]
# print(c)                   # [[1, 2, 3], ['a', 'b', 'c']] 

# -------------------------------------------------------------------------------------------


#                           =>  Access to specific items in the Nested list:

# => To access an entire inner list, we use the index corresponding to the list's position
#    within the nested list.
# x = [[1, 2, 3], ['a', 'b', 'c']]
# print(x[0])                           # [1, 2, 3]
# print(x[1])                           # ['a', 'b', 'c']


# => To access a specific element within an inner list, we use multiple indices, 
#    each corresponding to a level of nesting
# x = [[1, 2, 3], ['a', 'b', 'c']]
# print(x[0][1])                           # 2
# print(x[1][2])                           # c


# => Complicated Ex:
# myfamily = ["omy","baba","ammar","fatema"]
# myfamily1 = ["khadija","menassa","ahmed","kharamella"]

# myfamily.append(myfamily1)
# print(myfamily)          # ['omy', 'baba', 'ammar', 'fatema', ['khadija', 'menassa', 'ahmed', 'kharamella']]

# print(myfamily[4])       # accesss to indix ""baba"
# print(myfamily[-1])      # accesss to the sec list ['khadija', 'menassa', 'ahmed', 'kharamella'], 
#                                       it is considered as one element 
# print(myfamily[-1][1])   # access to a pecific element in the sec list "menassa"

# ------------------------------------------------------------------------------------


#                     =>  There are other ways to concatenate more lists:

# a=[1,2,3]
# b=["A","B","C"]
# c=["one","two","three"]

# a += b             # => a = a + b
# print(a)                               # [1, 2, 3, 'A', 'B', 'C']

# a += b + c         # a = a + b + c
# print(a)                               # [1, 2, 3, 'A', 'B', 'C', 'one', 'two', 'three']
# OR:
# a = a + b + c
# print(a)  
                      
# ------------------------------------------------------------------------------------


#                                       => Check membership 

# => We can check for the presence of an element in a list using the in keyword. 
# => If present, True is returned.
# x = ['ammar', 'b', 1, 2]
# print('ammar' in x)              # True

# _________________________________________________________________________________________



#---------------------------------------- Lists2 Methods (22) -------------------------------------
#-------------------------------------------------------------------------------------------------

#                                      => MODIFICATION

# => Lists are also mutable allowing us to ADD, REMOVE, or MODIFY elements in an existing list.

#                                => [1] Adding elements by using:

# a) append(): This adds the element passed into it as a single element to the end of the list.
# b) extend(): This adds elements passed into it as separate elements to the end of the list.
# c) insert(): This inserts an element at a specified position.


#                                   1) append(one argument)

# => Adds only one element (str,int,float,bolean value) in each time at the end of the list.
# => adds the element passed into it as a single element to the end of the list.

# x = [1, 2, 3]
# x.append([4, 6])
# print(x)              # [1, 2, 3, [4, 6]]


# myfamily=["omy","baba","ammar","fatema"]
# myfamily1=["khadija","menassa","ahmed","kharamella"]

# myfamily.app
# myfamily.append("khadija")
# myfamily.append(1)
# myfamily.append(1.2)
# myfamily.append(True)
# myfamily.append(myfamily1)   # =>  This list is added as a single element
# print(myfamily)           
# ['omy','baba','ammar','fatema','khadija',1,1.2,True,['khadija', 'menassa', 'ahmed', 'kharamella']]


# myfamily.append()
# print(myfamily)            # TypeError: list.append() takes exactly one argument (0 given)
# myfamily.append("khadija","menassa")
# print(myfamily)            # TypeError: list.append() takes exactly one argument (2 given)

# ------------------------------------------------------------------------------------------


#                                    2) extend(one argument[])

# => Used to add more than one element but in a list ( also add another list not as 
#    a single element -as append does- but it incorborates the lists as one string)
# => adds elements passed into it as separate elements to the end of the list.

# x = [1, 2, 3]
# x.extend([4, 6])
# print(x)              # [1, 2, 3, 4, 6]


# a=[1,2,3]
# b=["A","B","C"]
# c=["one","two","three"]

# a.extend(b)
# a.extend(c)
# a.extend([-1])
# print(a)            # [1, 2, 3, 'A', 'B', 'C', 'one', 'two', 'three', -1]

# a.extend()
# print(a)            # TypeError: list.extend() takes exactly one argument (0 given)

# -----------------------------------------------------------------------------------------


#                                          10) insert(index,object)

# => Insert object BEFORE the wanted index:
# => It's better than append() as append() only adds aitems in the list end, but here I can choose the position I want
# => inserts an element at a specified position.

# x = [1, 2, 3]
# x.insert(0,'A')
# x.insert(1,'B')
# x.insert(-1,'C')
# print(x)                      # ['A', 'B', 1, 2, 'C', 3]


# a=["No",2,3,"name","ammar","ahmed"]
# a.insert(0,1)                 # inert 1 at the start of the list
# a.insert(5,"atef")            # inserted before the index 5 "ahmed"
# a.insert(-1,"atef")           # inserted before the last index 5 "ahmed"
# print(a)                      # [1, 'No', 2, 3, 'name', 'atef', 'ammar', 'atef', 'ahmed']

# ---------------------------------------------------------------------------------------


#                               => [2] Removing elements by using:

# a) del(): This deletes an element or multiple elements from the list at the specified index value/s.
# b) remove(): This removes the first occurrence of a specified value from the list.
# c) pop(): This removes and returns the element at the specified index.
 
#                                     => del()
#                                => del var[index]

# => deletes an element or multiple elements from the list at the specified index value/s.
# x = [1, 2, 3, 4, 5, 6]
# del x[2:4]                 # Remove the elements at index 2 and 3 from x
# print(x)                   # [1, 2, 5, 6]

# --------------------------------------------------------------------------------------


#                                  3) remove(one argument)

# => only removes one element from the list and if the removable element are existed 
#    more than one time, it will remove only the first element.
# => removes the first occurrence of a specified value from the list.

# x = [1,2,3,"ammar","ahmed", True,"ammar","ammar"]
# x.remove("ammar")
# print(x)       # removes only the first "ammar" => [1, 2, 3, 'ahmed', True, 'ammar', 'ammar']

# x.remove("ammar","ammar")
# print(x)           # TypeError: list.remove() takes exactly one argument (2 given)

# -----------------------------------------------------------------------------------------


#                                       11) pop(one argument)
#                                         => var.pop(index)

# => Removes and returns item at index (default last).
# => Raises IndexError if list is empty or index is out of range.
   

# a = [1,2,3,4,"ammar"]
# print(a.pop(-1))        # ammar
# print(a)                # [1, 2, 3, 4]

# a = [1,2,3,4,"ammar"]
# print(a.pop(5))         # IndexError: pop index out of range
 

# Note: 
# => If I write pop() without any index inside (), it will removes the last item:
# a = [1,2,3,4,"ammar"]
# print(a.pop())            # "ammar"
# print(a)                  # [1, 2, 3, 4]

# ----------------------------------------------------------------------------------------


#                             => [3] Modifying elements by:

# => We can change the value of an element at a given index:
# Ex: Modify element at index 1
# x = [10, 4, 5, 8]
# x[1] = 'Ammar'
# print(x)             # [10, 'Ammar', 5, 8]

# --------------------------------------------------------------------------------------


#                                    => Ordering a list
# => We can sort the elements in a list using two primary methods:
# [1] sort()
# [2] sorted()

#                                          4) sort()

# => Used to arrange the list that include only numbers or only strings, but not both of them 
#    in the same list:
# => sorts the list in ascending order in place.

# x = [1, 50, -5, 22, -100, 0, 60]
# x.sort()
# print(x)                          # [-100, -5, 0, 1, 22, 50, 60]


# Note => it cannot be used directly in print statement,
#         as it alters the original variable and returns None 

# x = [1, 50, -5, 22, -100, 0, 60]
# print(x.sort())           # None

# x = x.sort()
# print(x)                  # None     
 
# => Note: sort() by default has (reverse=False) means sort in ascending order.
# => So, To sort the list in descending order, we can specify the reverse parameter as True.

# x=[1,50,-5,22,-100,0,60]
# x.sort(reverse=False)
# print(x)                  # [-100, -5, 0, 1, 22, 50, 60]

# x=[1,50,-5,22,-100,0,60]
# x.sort(reverse=True)
# print(x)                  # [60, 50, 22, 1, 0, -5, -100]
 
# x=[1,50,-5,22,-100,0,60,"ammar"]
# x.sort(reverse=True)
# print(x)                  # TypeError: '<' not supported between instances of 'int' and 'str'

# y= ["A","C","D","B"]
# y.sort()                    # = y.sort(reverse=False)
# print(y)                    #  ['A', 'B', 'C', 'D']

# y= ["A","C","D","B"]
# y.sort(reverse=True)
# print(y)                    # ['D', 'C', 'B', 'A']

# ---------------------------------------------------------------------------------------


#                                   =>  sorted()

# => This returns a new sorted list without modifying the original one.
# => Note: To sort the list in descending order, we can specify the reverse parameter to True.

# x = [55, 88, 5, 10, 52.4, 45.3]
# z = sorted(x)
# print(x)                   # [55, 88, 5, 10, 52.4, 45.3]
# print(z)                   # [5, 10, 45.3, 52.4, 55, 88]

# x = [55, 88, 5, 10, 52.4, 45.3]
# z = sorted(x, reverse = True)
# print(x)                   # [55, 88, 5, 10, 52.4, 45.3]
# print(z)                   # [88, 55, 52.4, 45.3, 10, 5]

# Note => Both sort() and sorted() allow us to order our lists, but an important difference 
#         between them is that sort() returns a None value (modifying the original variable),
#         whereas sorted() returns a list.

# -----------------------------------------------------------------------------------------


#                                   => Boolean methods
# a) any()
# b) all()

#                                       => any()

# => Returns True if at least one element in the list evaluates to True.
# => Note: Values that evaluate to true include non-zero numbers, non-empty sequences, 
#    and the boolean value True.

# x = [True, False, 0]
# print(any(x))                    # True  

# c = [False, 0, '']               
# print(any(c))                    # False

# -----------------------------------------------------------------------------------------


#                                        => all()         

# => Returns True if all the elements in the list are True.
# x = [True,1,'a']
# print(all(x))                   # True

# x = [True, 0, 'a']
# print(all(x))                   # False

# -----------------------------------------------------------------------------------------


#                                     => Other list methods


#                                        => len()

# => We use the len() function to determine how many elements a list has.
# x = [1,2,5,58,8,8]
# print(len(x))              # 6

# --------------------------------------------------------------------------------------------




#                                          5) reverse()

# => This function only revesres (not sorts or arranges) the elements of the list 
# => "starts with the end"
                   
# z=["ammar",1,5,8,"ahmed"]
# z.reverse()
# print(z)            # ['ahmed', 8, 5, 1, 'ammar']

# _______________________________________________________________________________________________



#------------------------------------ Lists3 Methods (23) ---------------------------------------
#------------------------------------------------------------------------------------------------
#                                          6) clear() 

# REMOVES ALL ITEMS FROM THE LIST:

# a=[1,2,"ammar"]
# a.clear()
# print(a)            # []   

# -------------------------------------------------------------------------------------------


#                                          7) copy()

# => Returns a shallow copy not deep copy of the list:
# => useful when we want to modify a copy of a list while keeping the original unchanged.

# a  = [1,2,3,4]
# b = a.copy()
# print(a)     # Main list        => [1,2,3,4]
# print(b)     # Copied list      => [1,2,3,4]

# OR:
# b = a
# print(b)

# Note: 
# => If I append an item to the main list (after I COPIED THE LIST BY COPY() METHOD
#    NOT BY THIS WAY => A=B) and then print both lists (the main and the copied), 
#    the copied list won't incorborate the appended item and this what we call "shallow copy".

# [1] by copy() method:
# a = [1,2,3,4]
# b = a.copy()
# a.append(5)

# print(a)   # [1, 2, 3, 4, 5]
# print(b)   # [1, 2, 3, 4]     => NO CHANGE


# [2] by var1 = var2 way:
# a = [1,2,3,4]
# b = a
# a.append(5)

# print(a)   # [1, 2, 3, 4, 5]
# print(b)   # [1, 2, 3, 4, 5]


# => But if I appended first and then copied, the two lists (main @ copy) would contain 
#    the appended item:
# a = [1,2,3,4]
# a.append(5)
# b = a.copy()

# print(a)   # [1, 2, 3, 4, 5]
# print(b)   # [1, 2, 3, 4, 5]

# -----------------------------------------------------------------------------------


#                                          8) count(one argument)

# => to count the occurrences of a particular element.
# => To know the no. repeats of an item in the list:

# a=[1,2,3,4,1,5,1,6]
# print(a.count(1))        # 3 => means it's existed three times in the list

# a=[1,2,3,4,1,5,1,6]
# print(a.count())         # TypeError: list.count() takes exactly one argument (0 given)

# a=[1,2,3,4,1,5,1,6]
# print(a.count(1,2))      # TypeError: list.count() takes exactly one argument (2 given)

# ----------------------------------------------------------------------------------------


#                                          9) index(one argument)

# => To know if the item in the list is existed or not and this by displaying
#    the index of the item that I searched about in the list: 

# a = ["ammar","ahmed","atef","ali"]
# print(a.index("atef"))             # 2  

# a = ["ammar","ahmed","atef","ali"]
# print(a.index())                   # TypeError: index expected at least 1 argument, got 0


# Note:
# => If the specified value appears multiple times in the list, the index() function 
#    will return the index of the first occurrence of that value.

# a = ["ammar","ahmed","atef","ali","atef"]
# print(a.index("atef"))             # 2         


# Note: 
# => It is case-sensitive:

# a = ["ammar","ahmed","atef","ali","atef"]
# print(a.index("ate"))              # ValueError: 'ate' is not in list

# ________________________________________________________________________________________________
                                 


#----------------------------------------- Tuples1()"", (24) -------------------------------------------
#-------------------------------------------------------------------------------------------------

#Notes:
# [1] Tuble items are enclosed in parentheses
# [2] You can remove the parentheses if u want
# [3] Tuples are ordered, which means that they maintain the specific position in which 
#                                   they were added.
# [3] Each position is denoted by an index, starting with zero, so we use index to access items
# [4] immutable => u can't change, add or delete items from a tuple once it has been created.
# [5] Tuple items aren't unique, so Tuples also allow duplicate items since they can be 
#                              differentiated using their index. 
# [6] Tuple can have different data types
# [7] Operators used in strings and lists are available in tuples


# SO,
# => Tuples are Python data structures that store a constant group of items defined within
#    round brackets or parentheses.
# => Tuples are useful when we want to represent a fixed collection of items that should 
#    not be changed after creation and have a specific order.
# -----------------------------------------------------------------

#                                (Tuple syntax @ Type test)

# [1] Enclosed in Parantheses:
# _ = ("ana", "ahmed")
# print(type(_))         # tuple

# [2] Without the Parantheses:
# a1 = "ana", "ammar"
# print(type(a1))        # tuple


#                                   (Tuple Indexing)

# [3] Using index to access item:
# a2 = (1, 2, 3, 4, 5)
# print(a2[0])             # 1
# print(a2[-1])            # 5
# print(a2[-3])            # 5
                             

#                                   (Tuple Slicing)
# => use slicing when we wish to return a portion of a tuple instead of just a single value.
# => Syntax: tuple[start:end]
# start: The index from which the slicing begins (included).
# stop: The index at which the slicing ends (not included).

# animal_tuple = tuple(["Yellow anaconda", "Reptile", 30.5, 20])
# sliced_tuple = animal_tuple[1:4]
# print(sliced_tuple)                   # => ('Reptile', 30.5, 20)



#                                   (Tuple Assign Values)

# [4] are immutable "can't add or delete any items":
# a3 = (1, 2, 3, 4, 5)
# a3[1] = "one"
# print(a3)                # TypeError: 'tuple' object does not support item assignment

# a4 = (1, 2, 3, 4, 5)
# a4[1] = []
# print(a4)                # TypeError: 'tuple' object does not support item assignment


#                                   (Tuple Items)

# [5,6] Tuples Items aren't unique "can be repeated" and have different data types:
# a5 = ("ammar", "ammar", 1, 2, 3, 100.2, True) 
# print(a5[0])       # ammar
# print(a5[-1])      # True

# ___________________________________________________________________________________________________



# ------------------------------------------ Tuples2 (25) -------------------------------------------
# -------------------------------------------------------------------------------------------------

#                                    (Tuple with single item)

# =>  How can I know that it's a tuple not a string?
# => Note: 
# => To create a tuple with a single item, we need to include a trailing comma 
#    after the item for it to be interpreted.
# => In tuple, after the element must be comma ","

# a = ("ammar")
# b = "ahmed"
# print(type(a))    # str
# print(type(b))    # str

# d = ("ammar",)
# c = "ahmed",
# print(type(d))    # tuple
# print(type(c))    # tuple

# To make sure that the comma isn't considered as an element:
# d = ("ammar",)
# c = "ahmed",
# print(len(d))      # 1
# print(len(c))      # 1


#                                    (Tuple concatenation)

# => We can add elements to an existing tuple by appending another tuple to it.
# => We use the + operator to perform the concatenation.

# a = (1, 2, 3, 4)
# b = (5, 6)

# c = a + b 
# print(c)              # (1, 2, 3, 4, 5, 6)

# d = a + ("A", "B", True) + b
# print(d)              # (1, 2, 3, 4, 'A', 'B', True, 5, 6)



#                                        (Duplicates)
#                               ( Tuple, List, String Repeat (*))

# => Since tuples are ordered, they allow duplicates as they can be 
#    differentiated by their index.

# mystring = "ammar"
# print(mystring * 6)      # ammarammarammarammarammaramma

# mylist = [1, 2]
# print(mylist * 6)        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

# mytuple = ("z", "v")
# print(mytuple * 2)       # ('z', 'v', 'z', 'v')
 

# ------------------------------------------------------------------------
#                                 ( Other tuple methods)
#                             -------------------------------

#                                         count()    
#                               =>    count(only one value)
#                               => count(value, start, end)

# => To count the occurrences of a particular element.

# g = (1, 2, 3, 1, 4, 1)
# print(g.count(1))             # 3 => no.1 repeats 3 times

# g = (1, 2, 3, 1, 4, 1)
# print(g.count(1,2))           # TypeError: tuple.count() takes exactly one argument (2 given)
# ---------------------------------------------------------------------------------------

#                                        index()

# => use the index() method to return the index of a specified value.

# a = (1, 5, 6, 4, 2)
# print(a.index(5))         # index no. 1

# a = (1, 5, 6, 4, 2)
# print("THE POSITION IS:" + a.index(5))   # TypeError: can only concatenate str (not "int") to str   

# a = (1, 5, 6, 4, 2)
# print("THE POSITION IS: {}" .format(a.index(5)))      # THE POSITION IS: 1

# a = (1, 5, 6, 4, 2)
# print(f"THE POSITION IS: {a.index(5)}")               # THE POSITION IS: 1 
# --------------------------------------------------------------------------------------

#                               (Tuple unpacking) OR (Tuple Destruct) 
                                   
# => Tuple unpacking refers to the assignment of tuple elements to individual variables 
#    that can be used separately.

# a = ("A", "B", "C")
# x, y, z = "A", "B", "C"
# print(x)    # A
# print(y)    # B
# print(z)    # C

# a = ("A", "B", "C")
# x, y, z = a
# print(x)    # A
# print(y)    # B
# print(z)    # C

# a = ("A", "B", 4, "C")
# x, y, z = a
# print(x)               # ValueError: too many values to unpack (expected 3)


# Note: If u wanna ignore an item =>  write simecolon (,) instead of this item
# a = ("A", "B", 4, "C")
# x, y, _, z = a         # Write simecolon to ignore 4
# print(x)
# print(y)
# print(z)

# ______________________________________________________________________________________________



# ----------------------------------------- Set1{} (26) -----------------------------------------
# --------------------------------------------------------------------------------------------


# Notes:
# [1] Set Items are enclosed in CURLY BRACES.
# [2] Unlike lists, tuples and dict, Set Items are NOT ORDERED and NOT INDEXED For this reason, 
#     we cannot access an element in a set using an index since it will have a different position 
#     each time.
# [3] Set items are UNIQUE, The unordered nature of sets does not allow them to have duplicates
#     since we can't differentiate them by their positions.
#  => So, Items with the same value are considered to be the same thing.
# [4] Set indexing and slicing can't be done.
# [5] Sets are also MUTABLE, in that we can add and remove items from the set. 
#  => However, we can NOT CHANGE an element that already exists in a set.
# [6] Set HAS ONLY IMMUTABLE DATA TYPES (#s, str, tuple) but not has Lists and Dict. 


# SO,
# => Sets are great for carrying out membership tests; that is, checking if an element belongs 
#    to a collection. They are also useful when we wish to perform combinations or comparisons 
#    among collections using set operations. 
# => Sets are also effective when we want to keep unique elements and eliminate duplicates.
# -------------------------------------------------


# [1,2]: enclosed in curly braces, not ordered and not indexed:

# a = {"ammar", "ahmed", 12} 
# print(a)        # {"ammar", "ahmed", 12}, {'ammar', 12, 'ahmed'}, {'ahmed', 12, 'ammar'} => Not ordered
# print(a[1])     # TypeError: 'set' object is not subscriptabl  => Not indexed


# [3] Not sliced:

# b = {"ammar", "ahmed", 12, 5} 
# print(b[1:3])                 # TypeError: 'set' object is not subscriptable   => Not sliced

# c = ("ammar", "ahmed", 12, 5)  
# print(c[1:3])                 #   ('ahmed', 12)  = > Tuple is sliced

# c = ["ammar", "ahmed", 12, 5]  
# print(c[1:3])                 #  ['ahmed', 12]   => List is sliced


# [4] Has only immutabl data types (#s, str, tuple) not lists and dict:

# d = {"anna", "ammar", 100, 1.2, [1, 2, 3]}
# print(d)            # TypeError: unhashable type: 'list'

# e = {"anna", "ammar", 100, 1.2, (1, 2, 3)}
# print(e)            # {1.2, 'ammar', 100, (1, 2, 3), 'anna'}  => but not ordered  


# [5] Its items are unique: => remove the repeats and non-ordered

# f = {1, "ammar","ahmed", "ammar", 1}
# print(f)                      # {1, 'ammar', 'ahmed'}, 
# print(f)                      # {1, 'ahmed', 'ammar'}, 
# print(f)                      # {'ammar', 1, 'ahmed'} 

# _____________________________________________________________________________________________________


#                                        => Create a set by two ways:

# [1] Create a set by assigning a group of comma-separated values enclosed within curly brackets to a variable
# [2] Can also use the set() constructor to create a set from other iterables such as lists.
# Note: The set will retain only unique elements and any duplicates in the list will be removed.

# x = {1, 2, 3, 4, 4}
# print(x)             # {1, 2, 3, 4}

# z = set([1, 1, 4, 4, 5])
# print(z)             # {1, 4, 5}        

# -------------------------------------------------------------------------------------------


#                               => Check membership in a set

# => Sets are unordered, which means elements are not assigned indexes. 
#    Therefore, they do not support indexing to access specific elements.


#                                  By  => in operator

# => Used to check for the presence of an element in a set using the in keyword. 
# => If present, True is returned.

# family = {'ammar', 'ahmed', 'omar', 'ez'}
# print('ez' in family)                         # True
# print('anas' in family)                       # False

# Note: 
# If there are two sets and u wanna check for the presence of one of them in the other,
# U can't use in operator, as it will treat the wanted set as an element, but u can use
# other ways such as issubset or <=

# x = {1,2,3,'s'}
# c = {1,2}
# print(c in x)              # false

# -------------------------------------------------------------------------------------


#                                    By  => Subset:  
#                            [2] issubset()  => VS issuperset()

# => equals to this sign <=                                  
# => returns True if the set is a subset of another set, otherwise it will return False.
# Report whether another set contains this set.
# Asks whether the items of the original set(a) are all found in the other set (b)

# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# print(a.issubset(b))      # False
# print(a <= b)             # False

# a = {1, 2, 3, 4}
# c = {1, 2, 3, 4, 5}
# print(a.issubset(c))      # True

# ----------------------------------------------------------------------------------------


#                             [1] issuperset() => Vs => issubset()

# Reports whether this set contains another set.
# Asks whether the items of the other set(b) are all found in the original set(a) 

# a = {1, 2, 3, 4, 5}
# b = {1, 2, 3, 4}
# print(a.issuperset(b))       # True                         

# a = {1, 2, 3, 4, 5}
# c = {1, 2, 3, 4, 5, 6}
# print(a.issuperset(c))       # False



# ----------------------------------------------------------------------------------------


#                                       => Duplicates

# => Since sets are unordered, they do not allow duplicates.
# => Items with the same value are considered to be the same thing and will only be listed once.

# x = {1, 2, 3, 4, 4}
# print(x)             # {1, 2, 3, 4}

# ___________________________________________________________________________________________



# ----------------------------------- Set Methods (26-29) ----------------------------------
# --------------------------------------------------------------------------------------------

#                                      => Modification

# => Sets are also mutable. They support various methods for ADDING and REMOVING elements.

#                                 => Adding elements by two ways:

# [1] add(): This adds a single element to the set.
# [2] update(): This adds elements from an iterable, such as lists and other sets, to the set.


#                                         [3] add()

# => Adds only an element to the set:

# x = {1, 2, 3}
# x.add(4,5)
# print(x)     # TypeError: set.add() takes exactly one argument (2 given)

# y = {1, 2, 3}
# y.add(4)
# y.add(5)
# print(y)     # {1, 2, 3, 4, 5}                                

# ----------------------------------------------------------------------------------------


#                                           [8] update()

# Updates a set with the union of itself and others.
# => adds elements from an iterable, such as lists and other sets, to the set.

# x = {1,2,3,4,5,5}
# x.update({7,6,7})
# print(x)             # {1, 2, 3, 4, 5, 6, 7}

# r = {"c", 5, 4}
# t = {True, False, 5}
# r.update(t)
# print(r)         # {False, True, 4, 5, 'c'}
 
# r = {"c", 5, 4}
# t = {True, False, 5}
# r.update(["b", "f"])
# r.update(t)
# print(r)           # {False, True, 'b', 'c', 4, 5, 'f'}

# -------------------------------------------------------------------------------------------


#                                  Removing elements by two ways:

# [1] remove(): Removes a specified element and 
#               it will raise an error if the element is not present.
# [2] discard(): Removes a specified element but 
#                it will not raise an error if the element is not present.


#                                     [5] remove()

# Removes an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.

# h = {0, 1, 2, 3}
# h.remove(3)
# print(h)         # {0, 1, 2}

# g = {0, 1, 2, 3}
# g.remove(2, 3)
# print(g)         # TypeError: set.remove() takes exactly one argument (2 given)

# i = {0, 1, 2, 3}
# i.remove(5)
# print(i)         # KeyError: 5  => bcz 5 not found

# ---------------------------------------------------------------------------------------


#                                         [6] discard()

# Removes an element from a set if it is a member.
# Unlike remove(), the discard() method not raise an exception when an element is missing from the set.

# k = {1, 2, 3}
# k.discard(5)
# print(k)           # {1, 2, 3}  => No Error


# => Note: We can add and remove elements from a set but 
#          we cannot change the value of an existing element in the set.

# -----------------------------------------------------------------------------------------


#                                       => Set operations

# The speed and efficiency we get from set operations are due to sets containing unique elements.
# We can easily combine and compare sets using a few basic operations, discussed below


#                                           [2] union() = a | b

# Returns the union of sets as a new set.
# => Returns a new set containing a combination of all unique elements from both sets.

# a = {"ana", "ammar", 1}
# b = {2, 3}
# print(a | b)          # {1, 2, 3, 'ammar', 'ana'}
# print(a.union(b))     # {1, 2, 3, 'ammar', 'ana'}

# a = {"ana", "ammar", 1}
# b = {2, 3,}
# c = {"A", "B"}
# print(a|b|c)            # {'ammar', 1, 2, 3, 'B', 'ana', 'A'}
# print(a.union(b, c))    # {'ammar', 1, 2, 3, 'B', 'ana', 'A'}

# x = {1,2}
# z = {'three','four'}
# y = {'e','d'} 

# v = x.union(z,y)
# print(v)                # {1, 2, 'd', 'four', 'e', 'three'}
# print(x)

# Note: It Returns a new set, not modify the existed one:
# x = {1,2,3}
# b = {'f','g'}
# x.union(b)
# print(x)                # {1, 2, 3}

# ------------------------------------------------------------------------------------------


#                                    [11] intersection()   = a & b

# => returns a new set without modifying the original set.
# => returns a new set containing common elements between two sets or more sets.
# Return the intersection of two or more sets as a new set. There is no update
# (i.e. all elements that are in both sets.)

# g = {1, 2, 3, 'x'}
# h = {1, "ammar", 3}
# print(g)                      # {'x', 1, 2, 3}
# print(g.intersection(h))      # {1, 3} = g & h   
# print(g & h)                  # {1, 3}
# print(g)                      # {'x', 1, 2, 3}    => There is no update 
 
# x = {1,2,3,1,3}
# y = {'b','a',1,3}
# z = x.intersection(y)
# print(z)                 # {1, 3}
# print(x)                 # {1, 2, 3}              => There is no updat

# x = {1,2,3}
# y = {'b','a',1,3}
# x.intersection(y)
# print(x)                 # {1, 2, 3}              => There is no updat

# a = {1,2,3,4}
# b = {1,2,5,6}
# c = {1,2,8,10}
# d = {'f','u',1,2}
# e = a.intersection(b,c,d)
# print(e)                     # {1, 2}

# --------------------------------------------------------------------------------------


#                               [12] inersection_update = a & b

# => modifies the original set directly and does not return any value (returns None).

# g = {1, 2, 3, 'x'}
# h = {1, "ammar", 3}
# print(g)                       # {'x', 1, 2, 3}
# g.intersection_update(h)       # = g & h 
# print(g & h)                   # {1, 3}
# print(g)                       # {1, 3}           # There is update
 
 
# x = {1,2,3}
# y = {'b','a',1,3}
# z = x.intersection_update(y)
# print(z)                    # None
# print(x)                    # {1, 3}              => There is update

# -----------------------------------------------------------------------------------------


#                                   {9} difference() = a - b

# => Returns a new set containing elements that are only present in the first set 
#    but not in the other sets without modifying the original set.
# Returns the difference of two or more sets as a new set."not make update as the main set still the same" 
# All elements that are in this set but not the others.) # اللي موجود فيها ومش موجود ف غيرها

# a = {1, 2, "a", "b", "c"}
# b = {1, 2, 3}
# print(a.difference(b))       # {'b', 'a', 'c'}   => = a - b
# print(a - b)                 # {'b', 'a', 'c'}

# c = {1, 2, 3, 4}
# d = {1, 2, "ammar", "ahmed"}
# print(c)                     # {1, 2, 3, 4}
# print(c.difference(d))       # {3, 4}    => = c - d
# print(c - d)                 # {3, 4}
# print(c)                     # {1, 2, 3, 4}   the set is the same "not updated"

# x = {1,2,3,1,3}
# y = {'b','a',1,3}
# z = x.difference(y)
# print(z)                 # {2}
# print(x)                 # {1, 2, 3}              => There is no update

# x = {1,2,3}
# y = {'b','a',1,3}
# x.difference(y)
# print(x)                 # {1, 2, 3}              => There is no update

# a = {1,2,3,4}
# b = {1,2,5,6}
# c = {1,2,8,10}
# d = {'f','u',1,2}
# e = a.difference(b,c,d)
# print(e)                     # {3, 4}

# -------------------------------------------------------------------------------------------


#                            [10] difference_update() = a - b

# => modifies the original set directly by removing the common elements and 
#    does not return any value (returns None).
# => makes update to the main set 

# c = {1, 2, 3, 4}
# d = {1, 2, "ammar", "ahmed"}
# print(c)                              # {1, 2, 3, 4}
# c.difference_update(d)                # => = c - d
# print(c - d)                          # {3, 4}
# print(c)                              # {3, 4}       => There is updat


# x = {1,2,3}
# y = {'b','a',1,3}
# z = x.difference_update(y)
# print(z)                    # None
# print(x)                    # {2}              => There is update

# ----------------------------------------------------------------------------------------


#                             [13] symmetric_difference() = a ^ b

# => returns a new set without modifying the original set.
# Return the symmetric difference of  only two sets "not more sets"  as a new set.  
# All elements that are in exactly one of the sets, not in the other set 
# contains elements found in one of these sets onlyيعني اللي موجود هنا ومش موجود هناك والعكس

# A = {"Z", 1, 2, 3, 'X'}
# B = {"Z", 1, 5, "T"}
# print(A)                            # {1, 2, 3, 'Z', 'X'}
# print(A.symmetric_difference(B))    # {2, 3, 5, 'X', 'T'}   = A ^ B
# print(A ^ B)                        # {2, 3, 5, 'X', 'T'}
# print(A)                            # {1, 2, 3, 'Z', 'X'}    # No update

# x = {1,2,3,1,3}
# y = {'b','a',1,3}
# z = x.symmetric_difference(y)
# print(z)                 # {2, 'b', 'a'}
# print(x)                 # {1, 2, 3}              => There is no update

# x = {1,2,3}
# y = {'b','a',1,3}
# x.symmetric_difference(y)
# print(x)                 # {1, 2, 3}              => There is no update

# a = {1,2,3,4}
# b = {1,2,5,6}
# c = {1,2,8,10}
# d = {'f','u',1,2}
# e = a.symmetric_difference(b,c)
# print(e)          # TypeError: set.symmetric_difference() takes exactly one argument (2 given)

# --------------------------------------------------------------------------------------------------


#                              [14] symmetric_difference_update()

# => modifies the original set directly by updating it with the symmetric difference and 
#    does not return any value (returns None)
# Returns the symmetric difference of two sets as a new set. There is update
# All elements that are in exactly one of the sets not in the both sets

# A = {"Z", 1, 2, 3, 'X'}         
# B = {"Z", 1, 5, "T"}
# print(A)                             # {1, 2, 3, 'Z', 'X'}   
# A.symmetric_difference_update(B)     # = A ^ B
# print(A ^ B)                         # {1, 2, 3, 'Z', 'X'}   
# print(A)                             # {2, 3, 'T', 5, 'X'}        => Updated

# x = {1,2,3,1,3}
# y = {'b','a',1,3}
# z = x.symmetric_difference_update(y)
# print(z)                 # None
# print(x)                 # {2, 'a', 'b'}              => Updated 

# x = {1,2,3}
# y = {'b','a',1,3}
# x.intersection(y)
# print(x)                 # {1, 2, 3}                  => Updated 

# a = {1,2,3,4}
# b = {1,2,5,6}
# c = {1,2,8,10}
# d = {'f','u',1,2}
# e = a.symmetric_difference_update(b,c,d)
# print(e)   # TypeError: set.symmetric_difference_update() takes exactly one argument (3 given)

# -----------------------------------------------------------------------------------------------


#                                      => Subset  
#                            [2] issubset()  => VS issuperset()

# => equals to this sign <=                                  
# => returns True if the set is a subset of another set, otherwise it will return False.
# Report whether another set contains this set.
# Asks whether the items of the original set(a) are all found in the other set (b)

# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# print(a.issubset(b))      # False
# print(a <= b)             # False

# a = {1, 2, 3, 4}
# c = {1, 2, 3, 4, 5}
# print(a.issubset(c))      # True

# ----------------------------------------------------------------------------------------


#                             [1] issuperset() => Vs => issubset()

# Reports whether this set contains another set.
# Asks whether the items of the other set(b) are all found in the original set(a) 

# a = {1, 2, 3, 4, 5}
# b = {1, 2, 3, 4}
# print(a.issuperset(b))       # True                         

# a = {1, 2, 3, 4, 5}
# c = {1, 2, 3, 4, 5, 6}
# print(a.issuperset(c))       # False

# ----------------------------------------------------------------------------------------


#                                       [3] isdisjoint()

# Returns True if two sets have a null "Nothing" intersection".

# a = {1,2,3,4}
# b = {1, 2, 3}
# print(a.isdisjoint(b))     # False

# a = {1,2,3,4}
# c = {11, 22, 33}
# print(a.isdisjoint(c))     # True

# ------------------------------------------------------------------------------------------


#                                 => Other set methods

#                                      => len( )

# => We use the len() function to determine the number of elements in a set.
# x = {1,2,3,4,5,6}
# print(len(x))          # 6

# _____________________________________________________________________________________________



# --------------------------------------- Set2 Methods1 (27) ---------------------------------
# -------------------------------------------------------------------------------------------

#                                           [1] clear()

# Removes all elements from the set:
# a = {"ammar", "ahmed", 1}
# a.clear()
# print(a)     # set()

# --------------------------------------------------------------------------------------------


#                                            [4] copy()

# Returns a shallow copy of a set not a deep shallow.
# n = {'A', 'B', 'C'}
# m = n.copy()
# print(n)      # {'C', 'B', 'A'}
# print(m)      # {'C', 'B', 'A'}

# n.add('D')
# print(n)      # {'B', 'D', 'A', 'C'}
# print(m)      # {'B', 'A', 'C'}
 
# -----------------------------------------------------------------------------------------

#                                        [7] pop()

# Removes and return a random element bcz there is no indxing in the set and bcz set is not ordered
# l = {"A", 1, 1.2, True}
# print(l.pop())          # A or 1.2 or 1 or any item

 # ____________________________________________________________________________________________



# ------------------------------------ Set4 Methods3 (29) -----------------------------------
# -------------------------------------------------------------------------------------------------

# These three methods return  value (True or false):

#                                      [1] issuperset() Vs issupset()

# Reports whether this set contains another set.
# Asks whether the items of the other set(b) are all found in the original set(a) 

# a = {1, 2, 3, 4, 5}
# b = {1, 2, 3, 4}
# print(a.issuperset(b))       # True                         

# a = {1, 2, 3, 4, 5}
# c = {1, 2, 3, 4, 5, 6}
# print(a.issuperset(c))       # False

# ----------------------------------------------------------------------------------------


#                            [2] issubset()  => VS => issuperset()

# => returns True if the set is a subset of another set, otherwise it will return False.
# Report whether another set contains this set.
# Asks whether the items of the original set(a) are all found in the other set (b)

# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# print(a.issubset(b))      # False

# a = {1, 2, 3, 4}
# c = {1, 2, 3, 4, 5}
# print(a.issubset(c))      # True

# --------------------------------------------------------------------------------------


#                                       [3] isdisjoint()

# Returns True if two sets have a null "Nothing" intersection".

# a = {1,2,3,4}
# b = {1, 2, 3}
# print(a.isdisjoint(b))     # False

# a = {1,2,3,4}
# c = {11, 22, 33}
# print(a.isdisjoint(c))     # True

# ________________________________________________________________________________________________



# ------------------------------------- Dictionary1 (30) -----------------------------------
# -------------------------------------------------------------------------------------------

# Notes:
# [1] Dict items are enclosed in CURLY BRACES
# [2] Dict items contain "KEY : VALUE"
# [3] Dict KEYS must be IMMUTABLE (#s, str, tuple) but NOT LISTS
# [4] Dict value can have any data types
# [5] Dict KEYS must be UNIQUE "No Repeats" and no duplicates are allowed.
# [6] Dict is NOT OREDERED, u only can access to its element with its key name not by indexing.
# [7] Dictionaries are MUTABLE in that we can modify the value associated with a particular key.
#     It is also possible for us to add or remove key: value pairs from an existing dictionary.


# SO, 
# => DICTS store a collection of key-based items, of any data type, defined within curly brackets.
# => The key difference between dictionaries and previous data structures is that they are stored 
#    in pairs; that is, the key and the value itself, separated by a colon.
# => The key is used to identify the value. Therefore, we can access an item in a dictionary 
#    using its respective key.
# => Dictionaries are suitable for storing dynamic and structured data collections that are 
#    labelled or have unique identifiers. 
# => They are also great if we are focused on fast and efficient data retrieval based on keys.
# -------------------------------------------------------------------------


# [1,2]:
# user = {
#     "name" : "ammar",
#     "age" : 36,
#     "length" : 1.70
# }
# print(user)


# [3]
# user = {
#     "name" : "ammar",
#     "age" : 36,
#     "length" : 1.70,
#     [1, 2, 3] : "test"
# }
# print(user)      # TypeError: unhashable type: 'list' => Dict key needs to be Immutable  
#                               (#s, str, tuple)  but not list
 
# user = {
#     "name" : "ammar",
#     "age" : 36,
#     "length" : 1.70,
#     (1, 2, 3) : "test", 
#     1 : "test" 
# }
# print(user)

# [4] 
# user = {
#     "name" : "ammar",
#     "age" : 36,
#     "skills" : ["python", 'C#', 'R'],
#     'level' : [99.1]
# }


# [5]
# => Dictionary items are unique, specifically referring to the keys. 
# => If we were to duplicate a key when creating a dictionary, the original key's value 
#    is replaced by the new value, rather than being added to the dictionary.

# user = {
#     "name" : "ammar",
#     "age" : 36,
#     "skills" : ["python", 'C#', 'R'],
#     'level' : [99.1],
#     'name' : 'ahmed',
#     'name' : 'atef'
# }
# print(user)       # name => atef


# [6]
# => If we wanted to extract the value for this key, we could do it by using:
   
# 1) The key as an index   
# 2) get(key) => Returns the value for key if key is in the dictionary, else default.
# 3) keys()
# 4) values()

# user = {
#     "name" : "ammar",
#     "age" : 36,
#     "skills" : ["python", 'C#', 'R'],
#     'level' : [99.1]
# }
# print(user["age"])                     # 36
# print(user['name'])                    # ammar 
  
# print(user.get('age'))                 # 36
# print(user.get("level"))               # [99.1]

# print(user.keys())      # dict_keys(['name', 'age', 'skills', 'level'])
# print(user.values())    # dict_values(['ammar', 36, ['python', 'C#', 'R'], [99.1]])

# -----------------------------------------------------------------------------------------


#                   => Using the dict() function to create a dictionary

#                                    => dict()

# => dict(**kwargs) -> new dictionary initialized with the name=value pairs
# => in the keyword argument list. For example: dict(one=1, two=2)
# => create a dictionary by specifying the values from the start, and 
#    then making use of the dict() function.

# x = dict(name = 'ammar', age = 23, father = 'atef')
# print(x)               # {'name': 'ammar', 'age': 23, 'father': 'atef'}

# Note:
# =>  We have now shown two ways of creating dictionaries:
# [1] The first by specifying it with curly brackets, 
# [2] The second by using the dict() function.
 
# Note that: 
# when we use the dict() function, we don't need to put the keys in quotes, 
# which could save us some time when creating longer dictionaries!


# => OR:
# a = (('name',"ammar"), ("age", 23) , ('position', 'manager'))
# print(dict(a))            # {'name': 'ammar', 'age': 23, 'position': 'manager'}

#-----------------------------------------------------------------------------------------


#                     => Printing the key and value in a dictionary

# When printing the contents of a dictionary, we can show dictionaries in their entirety, 
# or per key, formatted using f-strings.

# x = {
#     'name':'ammar',
#     'age' : 23
# }
# print(f"name: {x['name']}")            # name: ammar


# Note:
# Strings nested within an f-string cannot use the same quote character 
# as the f-string prior to Python 3.12 Pylance:

# x = {
#     'name':'ammar',
#     'age' : 23
# }
# print(f'name: {x['name']}')        # SyntaxError: f-string: unmatched '['
# print(f"name: {x["name"]}")        # SyntaxError: f-string: unmatched '['

# ------------------------------------------------------------------------------------------


#                         => Characteristics of dictionaries

# [1] => Dictionary items are unique, specifically referring to the keys. 
#        If we were to duplicate a key when creating a dictionary, the original key's value 
#        is replaced by the new value, rather than being added to the dictionary.

# me ={
#     'name' : 'ammer',
#     'age' : 19,
#     'height' : 175,
#     'age' : 23
# }
# print(me)               # {'name': 'ammer', 'age': 23, 'height': 175}


# [2] => From Python 3.7 onwards, dictionaries are ordered data structures, meaning that 
#        the order is always the same when calling the variables unlike sets

# f = {1, "ammar","ahmed"}
# print(f)                      # {1, 'ammar', 'ahmed'}, 
# print(f)                      # {1, 'ahmed', 'ammar'}, 
# print(f)                      # {'ammar', 1, 'ahmed'} 

# x = {
#     'name':'ammar',
#     'age' : 23,
#     'country' : 'Egypt'
# }
# print(x)                    # {'name': 'ammar', 'age': 23, 'country': 'Egypt'} 
# print(x)                    # {'name': 'ammar', 'age': 23, 'country': 'Egypt'} 
# print(x)                    # {'name': 'ammar', 'age': 23, 'country': 'Egypt'} 


# [3] => dictionaries are mutable - enabling us to update these variables with new values 
#        for existing keys, add new key-value pairs and remove existing key-value pairs.

# x = {
#     'name':'ammar',
#     'age' : 23
# }
# x['sex'] = 'male'
# print(x)               # {'name': 'ammar', 'age': 23, 'sex': 'male'}

# x = {
#     'name':'ammar',
#     'age' : 23
# }
# x['age'] = 24
# print(x)               # {'name': 'ammar', 'age': 24}

# -----------------------------------------------------------------------------------------


#                          => Adding key-value pairs to the dictionary

# => We can also add additional key-value pairs to the dictionary, by using:

# [1] the normal way => dict['key'] = value  => to add only one key-value pairs in each time
# [2] update() method. => to add multible key-value pairs.
# [3] setdefault()  

# Note => There is a catch to this - the new key-value pair has to be in a dictionary-format 
#         in order to add it to the existing dictionary.


#                                   =>  dict['one key'] = value

# x = {
#     'name':'ammar',
#     'age' : 23
# }
# x['sex'] = 'male' 
# print(x)               # {'name': 'ammar', 'age': 23, 'sex': 'male'}


# x = {}
# print(type(x))                # dict not set

# --------------------------------------------------------------------------------------


#                                        [2] update()

# Adds items to dictionary

# n = {
#     "name" : "oooo"
# }
# n['age'] = 22
# print(n)                             # {'name': 'oooo', 'age': 22}

# n.update({'city' : 'minya'})
# print(n)                             # {'name': 'oooo', 'city': 'minya'}

# m ={'father' : "atef", 'salary': '150k'}
# n.update(m)
# print(n)                             # {'name': 'oooo', 'father': 'atef', 'salary': '150k'}

# -------------------------------------------------------------------------------------------


#                              [5] setdefault(key, value)  
                                                            
# Inserts key with a value if key isn't in the dictionary.
# Returns the value for key if key is in the dictionary
# a = {
#     'name' : 'ammar'
# }
# print(a)                          # {'name': 'ammar'}
# print(a.setdefault("name"))       # ammar
# print(a)                          # {'name': 'ammar'}            
                  
# a = {
#     'name' : 'ammar'
# }
# print(a)                                   # {'name': 'ammar'}
# print(a.setdefault("name", 'ahmed'))       # {'name': 'ammar'}
# print(a)                                   # {'name': 'ammar'}

# a = {
#     'name' : 'ammar'
# }
# print(a)                         # {'name': 'ammar'}
# print(a.setdefault("AGE"))       # None
# print(a)                         # {'name': 'ammar', 'AGE': None}
 
# a = {
#     'name' : 'ammar'
# }
# print(a)                         # {'name': 'ammar'}
# print(a.setdefault("age", 23))   # 23
# print(a)                         # {'name': 'ammar', 'age': 23}

# -----------------------------------------------------------------------------------------


#                          => Removing key-value pair from dictionary

#                                   => del keyword            

# => We can use the del keyword to delete a key-value pair from the dictionary.
# x = {
#     'name':'Ammar',
#     'age' : 23,
#     'father' : 'Atef'
# }
# del x['age']
# print(x)                  # {'name': 'Ammar', 'father': 'Atef'}

# -----------------------------------------------------------------------------------------


#                  Two Dimensional Dictionary ( Nested Dictionary )

# languages = { 
#     'one' : {
#         'name' : 'C#',
#         'level' : '80%'
#     }, 
#     'two' : {
#         'name' : 'Python',
#         "level" : '90%'
#     },
#     'three' : {
#         'name' : 'R',
#         "level" : "100"
#     }
# }
# print(type(languages))                  # <class 'dict'>
# print(type(languages['one']))           # <class 'dict'>

# print(languages['one'])              # {'name': 'C#', 'level': '80%'}
# print(languages['one']['level'])     # 80%

# ---------------------------------------------------------------------------------------


#                                  Dectionary length:

#                                         len()

# languages = { 
#     'one' : {
#         'name' : 'C#',
#         'level' : '80%'
#     }, 
#     'two' : {
#         'name' : 'Python',
#         "level" : '90%'
#     },
#     'three' : {
#         'name' : 'R',
#         "level" : "100"
#     }
# }
# print(len(languages))                # 3     
# print(len(languages['two']))         # 2     

# ------------------------------------------------------------------------------------------


#                          Creat dictionary from many variables:

# a = {
#     "name" : 'ammar',
#     "level" : '9'
# }

# b = {
#     "name" : 'ahmed',
#     "level" : '10'
# }

# c = {
#     "name" : 'ali',
#     "level" : '2'
# }

# All_elements = {
#     "one" : a,
#     "two" : b,
#     "three" : c
# }
# print(All_elements)
# {'one': {'name': 'ammar', 'level': '9'}, 'two': {'name': 'ahmed', 'level': '10'}, 'three': {'name': 'ali', 'level': '2'}}

# ___________________________________________________________________________________________________



# ------------------------------------ Dictionary2 Methods1 (31) ----------------------------------
# -------------------------------------------------------------------------------------------------

#                                         [1] clear()

# Removes all items from Dict => {}
# me = {
#     'name' : 'ammar'
# }
# me.clear() 
# print(me)     # {}

# -----------------------------------------------------------------------------------------


#                                           [3] copy()

# Return a shallow copy of the dictionary:
# a = { 
#     'name' : 'ammar'
# }
# b = a.copy()
# print(b)              # {'name': 'ammar'}
# a.update({'age' : 23})
# print(a)              # {'name': 'ammar', 'age': 23}
# print(b)              # {'name': 'ammar'}

# -----------------------------------------------------------------------------------------


#                                     [4] keys() + values()

# providing a view on Dictionary's keys and Dictionary's values
# c = {
#     "name" : "ammar",
#     "age" : 36,
#     "skills" : ["python", 'C#', 'R'],
#     'level' : [99.1]
# }
# print(c.keys())           # dict_keys(['name', 'age', 'skills', 'level'])
# print(c.values())         # dict_values(['ammar', 36, ['python', 'C#', 'R'], [99.1]])

# _______________________________________________________________________________________________



# --------------------------------- Dictionary3 Methods2 (32) ------------------------------
# -------------------------------------------------------------------------------------------


#                                          [6] popitem()

# Removes and returns the last (key, value) as a tuple  
# Raises KeyError if the dict is empty
# x = {
#     'name' : 'ammar',
#     "skills" : 'football'
# }
# print(x)                 # {'name': 'ammar', 'skills': 'football'}
# print(x.popitem())     # ('skills', 'football') 

# x['age'] = 23     
# x.update({'age': 23})        
# print(x)                 # {'name': 'ammar', 'skills': 'football', 'age': 23}
# print(x.popitem())       # ('age', 23)
# print(x)                 # {'name': 'ammar', 'skills': 'football'}

# x = {}
# print(x.popitem())         # KeyError: 'popitem(): dictionary is empty'

# -----------------------------------------------------------------------------------------


#                                      [7] items()     

# providing a view on Dictionary's items as lists inside tuples
# Even after edition in the main dict, the var that view the items will be updated by default
# y = {
#     'name' : 'ammar',
#     "skills" : 'football'
# }
# print(y.items())           # dict_items([('name', 'ammar'), ('skills', 'football')])
# all_items = y.items()    
# print(all_items)           # dict_items([('name', 'ammar'), ('skills', 'football')])
# y.update({'age' : 23})  
# print(y)                   # {'name': 'ammar', 'skills': 'football', 'age': 23}
# print(all_items)           # dict_items([('name', 'ammar'), ('skills', 'football'), ('age', 23)])

# -----------------------------------------------------------------------------------------


#                               [8] fromkeys(keys, values)

# Creats a new dictionary with keys from iterable and values set to value 
  
# a = ('name', "age" , 'position')
# b = "ammar"   
# print(dict.fromkeys(a, b))       # {'name': 'ammar', 'age': 'ammar', 'position': 'ammar'}  
# print(dict.fromkeys(a))          # {'name': None, 'age': None, 'position': None}  
 
# a = ('name', "age" , 'position')
# b = ("ammar", 23, 'manager')   
# print(dict.fromkeys(a, b))            
#{'name': ('ammar', 23, 'manager'), 'age': ('ammar', 23, 'manager'), 'position': ('ammar', 23, 'manager')}

# a = (('name',"ammar"), ("age", 23) , ('position', 'manager'))
# print(dict(a))            # {'name': 'ammar', 'age': 23, 'position': 'manager'}

# ________________________________________________________________________________________________



# --------------------------------------- Boolean1 (33) ----------------------------------------------
# -----------------------------------------------------------------------------------------------

# Notes:
# [1] In programming u need to know if ur output is True  or False
# [2] Bolean values are two constant objects "True" @ "False"
#--------------------------------------

# a = ''
# print(a.isspace())    # False

# a = ' '
# print(a.isspace())    # True

# print(100 > 300)      # False
# print(100 > 100)      # False
# print(100 > 50)       # Talse


# [1] bool()
# Returns True when the argument x is true, False otherwise

# True values:
# print(bool('ammar'))
# print(bool(1))
# print(bool(1.2))
# print(bool(True))
# print(bool([1, 2, 3]))            
# print(bool(('ammar', 'ahmed')))
# print(bool({1}))
# print(bool({1:2}))

# False values:
# print(bool())
# print(bool(0))
# print(bool(False))
# print(bool(None))
# print(bool(''))
# print(bool(""))
# print(bool([]))
# print(bool({}))
# print(bool(()))

# ___________________________________________________________________________________________



# ------------------------------------- Boolean (logical) Operators (33) ---------------------------
# --------------------------------------------------------------------------------------------------

# Boolean Operators:
# [1] and => Returns True if all arguments are true and False otherwise 
# [2] or => Returns True if at least one argument is true and False if all are false
# [3] not => Reverses the logic state
# ------------------------

    
# name = "ammar"
# age = 23
# country = "Egypt"

# [1] and
# print(name == "ammar" and age > 20 and country == "Egypt")    # True
# print(name == "ammar" and age == 20 and country == "Egypt")   # False

# [2] or
# print(name == "ahmed" or age > 24 or country == "Egypt")      # True
# print(name == "ahmed" or age > 24 or country == "USA")        # False

# [3] not
# print(age > 20)        # True
# print(not age > 20)    # False

# ________________________________________________________________________________________________



# --------------------------------------- Assignment Operators(=) (35)  -----------------------------
# ------------------------------------------------------------------------------------------------
  
# =  :   This the assignment operator and it assigns a value to a variable 
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# ---------------------------

# x = 10
# y = 20

# z = x + y
# print(z)


# var one = self [operator] var two     x = x + y
# var one [operator]= var two           x += y

# x = 10          # => var one
# y = 20          # => var two
# x = x + y             
# print(x)        # 30

#  
# a = 10          # => var one
# b = 20          # => var two
# a += b                   
# print(a)        # 30

# A = 20
# B = 10
# A = A - B
# print(A)        # 10

# A = 20
# B = 10
# A -= B
# print(A)        # 10

# _____________________________________________________________________________________________-



# ------------------------------------ Comparison (Relational) Operators (36) -------------------------------        
# ------------------------------------------------------------------------------------------------

# [ == ]   Equal
# [ != ]   Not Equal
# [ > ]    Greater than
# [ < ]    Less than
# [ >= ]   Greater than or Equal
# [ <= ]   Less than or Equal
# ------------------------------------

# Equal(==) , Not Equal(!=)

# print(100==100)        # True
# print(100==200)        # False
# print(100==100.00)     # True

# print(100!=100)        # False
# print(100!=200)        # True
# print(100!=100.00)     # False


# Greater than(>) + Less than(<)

# print(100 > 100)       # False
# print(100 > 200)       # False
# print(100 > 100.00)    # False
# print(100 > 40)        # True

# print(100 < 100)       # False
# print(100 < 200)       # True
# print(100 < 100.00)    # False
# print(100 < 40)        # False


# Greater than or Equal (>=) + Less than or equal(<=)

# print(100 >= 100)       # True
# print(100 >= 200)       # False
# print(100 >= 100.00)    # True
# print(100 >= 40)        # True

# print(100 <= 100)       # True
# print(100 <= 200)       # True
# print(100 <= 100.00)    # True
# print(100 <= 40)        # False

# ______________________________________________________________________________________________



# --------------------------------------- Type conversion (37) ---------------------------------
# ------------------------------------------------------------------------------------------------
#   ومحتاج اغير فيها  tuple زي immutable بستحدم التحويل مثلا لو الداتا بتاعتي داخل نوع  
#                       mutable ف كده مضطر احولها لنوع 


# [1] str()

# a = 10
# print(type(a))                # int
# print(a ,":",type(str(a)))    # 10 : str
 


# [2] tuple()

# Notes:
# These methods only work on the elements that can male iteration or loop to them:
# Set data type is stil non ordered even after conversion to any other ordered data types and also 
#                the other data types are converted to set, they will be non ordered
# Only the keys of dictionary are put in the other types after conversion


# print(tuple(500))           # TypeError: 'int' object is not iterable

# a1 = "ammar"                # String
# a2 = [1, 2, 3, 4]           # list
# a3 = {"A", "B", "C"}        # set
# a4 = {"A" : 1, "B" : 2}     # dictionary

# print(tuple(a1))            # ('a', 'm', 'm', 'a', 'r')   => Each char as an element
# print(tuple(a2))            # (1, 2, 3, 4)
# print(tuple(a3))            # ('A', 'C', 'B')  => Bcz set not ordered
# print(tuple(a4))            # ('A', 'B')       => only the keys of dictionary are in the tuple



# [3] list()

# a1 = "ammar"                # String
# a2 = (1, 2, 3, 4)           # Tuple
# a3 = {"A", "B", "C"}        # Set
# a4 = {"A" : 1, "B" : 2}     # Dictionary

# print(list(a1))            # ['a', 'm', 'm', 'a', 'r']    => Each char as an element
# print(list(a2))            # [1, 2, 3, 4] 
# print(list(a3))            # ['C', 'B', 'A']  => Bcz set not ordered
# print(list(a4))            # ['A', 'B']       => Oonly the keys of dictionary are in the tuple



# [4] set()

# a1 = "ammar"                # String
# a2 = (1, 2, 3, 4)           # Tuple
# a3 = ["A", "B", "C"]        # List
# a4 = {"A" : 1, "B" : 2}     # Dictionary

# print(set(a1))        # {'a', 'm', 'r'}  => Removes the repeat elements and put them in not ordered way    
# print(set(a2))        # {1, 2, 3, 4}     => Tuple still ordered?????!!!!!!!!!!
# print(set(a3))        # {'B', 'C', 'A'}  => Bcz set not ordered
# print(set(a4))        # {'B', 'A'}       => Bcz set not ordered
 


# [5] dict()
# To convert to dictionary u must have "key and value"    
# Strings and Sets can't be converted to dictionary BCZ THERE ARE NO "key and value " even if 
#                                     they are nested       
# Tuples and Lists to be converted into dict they must be Nested Tuples @ Nested Lists 
# Nested Tuples must contain at least two tuples  
# Nested Liss must contain at least one list  


# [1] Str to Dict: 
# => NOOOOOOOOOOOOOOOOOOO

# a1 = "ammar", 1         # String
# print(dict(a1))         # ValueError: dictionary update sequence element #0 has length 1; 2 is required

# a1 = "ammar", 1         # String
# print(dict(a1))         # ValueError: dictionary update sequence element #0 has length 1; 2 is required



# [2] Tuple to Dict:  
# => Only NESTED TUPLES (More than one Nested Tuple)

# a2 = ("A", "B")         # Tuple
# print(dict(a2))         # ValueError: dictionary update sequence element #0 has length 1; 2 is required

# a2 = (("A", "B"))         # Tuple
# print(dict(a2))           #  Must be more than one Nested Tuples

# a3 = (("A", 1), ("B", 2))       # Tuple
# print(dict(a3))                 # {'A': 1, 'B': 2}

# a4 = (("A"), ("B", 2))          # Tuple
# print(dict(a4))                 # Error => Must have key and value



# [3] List to Dict:
# => Only NESTED LISTS (at least one list)

# a5 = [1, 2, 3, 4]       # List
# print(dict(a5))         # TypeError: cannot convert dictionary update sequence element #0 to a sequence

# a5 = [['one', 1]]         # List
# print(dict(a5))           # {'one': 1}

# a6 = [['one', 1], ['two', 2]]        # List
# print(dict(a6))                      # {'one': 1, 'two': 2}
   

# Set to Dict:
# => NOOOOOOOOOOOOOOOOOOO

# a7 = {"A", "B", "C"}     # set 
# print(dict(a7))          # ValueError: dictionary update sequence element #0 has length 1; 2 is required 

# a8 = {{"A", 1}, {"B", 2}}     # set 
# print(dict(a8))               # TypeError: unhashable type: 'set'

# _________________________________________________________________________________________________



# ------------------------------------- User Input (38) --------------------------------------------
# --------------------------------------------------------------------------------------------------

# [1] This if the user wrote his name without any whitespces before his name: 

# firstname = input('What\'s Ur First Name?')# Ammar    => No spaces
# midlename = input('What\'s Ur Midle Name?')# Atef     => No spaces
# lastname = input('What\'s Ur Last Name?')# Ahmed      => No spaces

# print(f"Hello {firstname} {midlename} {lastname} Happy To see U")
# Output: Hello Ammar Atef Ahmed Happy To See U


# [2] This output if the user wrote his name with any whitespces before his name:
# We use strip() to remove any whitespaces:

# firstname = input('What\'s Ur First Name?')  # Ammar
# midlename = input('What\'s Ur Midle Name?')# Atef
# lastname = input('What\'s Ur Last Name?')       # Ahmed
 
# print(f"Hello {firstname.strip()} {midlename.strip()} {lastname.strip()} Happy To see U")
# Output: Hello Ammar Atef Ahmed Happy To see U


# [3] If the user wrote his name but not in a proper way in the capitalize (ex: aMMaR)
# We use capitalize() To capitalize the first char of each word
# We can use more than one metgod at time "Chain Methods"

# firstname = input('What\'s Ur First Name?').strip().capitalize()  # aMmAr
# midlename = input('What\'s Ur Midle Name?').strip().capitalize()# aTeF
# lastname = input('What\'s Ur Last Name?').strip().capitalize()       # AHmeD

# print(f"Hello {firstname} {midlename} {lastname}")
# Output: Hello Ammar Atef Ahmed Happy To see U


# firstname = input('What\'s Ur First Name?')  # aMmAr
# midlename = input('What\'s Ur Midle Name?')# aTeF
# lastname = input('What\'s Ur Last Name?')       # AHmeD

# print(f"Hello {firstname.strip().capitalize()} {midlename.strip().capitalize()} {lastname.strip().capitalize()}")
# # Output: Hello Ammar Atef Ahmed Happy To see U

# By another way:

# firstname = input('What\'s Ur First Name?') # aMmAr
# midlename = input('What\'s Ur Midle Name?')#aTeF
# lastname = input('What\'s Ur Last Name?')      # AHmeD

# firstname = firstname.strip().capitalize()
# idlename = midlename.strip().capitalize()
# lstname = lastname.strip().capitalize()

# print(f"Hello {firstname} {midlename} {lastname}")
# Output: Hello Ammar Atef Ahmed Happy To see U

 
# Using Truncate:

# firstname = input('What\'s Ur First Name?').strip().capitalize()  # aMmAr
# midlename = input('What\'s Ur Midle Name?').strip().capitalize()# aTeF
# lastname = input('What\'s Ur Last Name?').strip().capitalize()       # AHmeD

# print(f"Hello {firstname} {midlename:.1s} {lastname}")
# print(f"Hello {firstname} {midlename.strip().capitalize():.1s} {lastname}")
# # Output: Hello Ammar A Ahmed Happy To see U    

# ___________________________________________________________________________________________________



# ----------------------------------- Practical Slice Email (39) -------------------------------------
# ----------------------------------------------------------------------------------------------------

# email = "ammar@atef.gmail.com"
# print(email[0])        # a
# print(email[:5])       # ammar



# email = "ammaratef@gmail.com"
# print(email.index('@'))                # 9
# print(email[:email.index('@')])        # ammaratef



# thename = input("What\'s Ur Name?").strip().capitalize() # ammar
# theemail = input("What\'s Ur Email?").strip() # ammaratef@gmail.com

# username =  theemail[:theemail.index('@')].capitalize()
# website = theemail[theemail.index('@') + 1:]

# print(f"Hello {thename} Ur Email Is {theemail}")
# Output: Hello Ammar Ur Email Is ammaratef@gmail.com

# print(f"Ur Username is {username} \nUr website is {website}")
# Output: Ur Username is Ammaratef  
# Ur website is gmail.com

# ____________________________________________________________________________________________________



# -------------------------------- Practical Ur Age Full Details (40) ---------------------------------
# --------------------------------------------------------------------------------------------------

# age = input("What\'s Ur Age?").strip()    # => 23
# print(age)          # 23
# print(type(age))    # str

# age = (int(age))        
# print(age)                 # 23
# print(type(age))           # int
 

# age = int(input("What\'s Ur Age?").strip())     # => 23
# print(age)                 # 23
# print(type(age))           # int
 

# Input Age: 
# age = int(input("What\'s Ur Age?").strip())     # => 23

# Get Age in all Time Units:
# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# print("U lived for:")
# print(f'{months} months')
# print(f'{weeks:,} weeks')
# print(f'{days:,} days')
# print(f'{hours:,} hours')
# print(f'{minutes:,} minutes')
# print(f'{seconds:,} seconds')

# ___________________________________________________________________________________________________



# ---------------------------------- Control Flow ""Make Decisions" (41) -----------------------------------------
# ---------------------------------------- if, elif, else -----------------------------------------------

# user_name = input("What's Ur Name ")
# user_country = input("What's Ur country ")         
# course_name = "Bioinformatics For Begginers"
# course_price = 100
# course_discount = 20

# if user_country == "Egypt" or user_country == "Somaal" or user_country == "Sudan" :
#     print(f"Hello {user_name} Because U Are From {user_country}")
#     print(f"The Course \"{course_name}\" Price is: {course_price - 80}$")
# elif user_country == "Kuwait" or user_country == "Bahrain" or user_country == "KSA":
#     print(f"Hello {user_name} Because U Are From {user_country}")
#     print(f"The Course \"{course_name}\" Price is: {course_price - 50}$") 
# else:
#     print(f"Hello {user_name} Because U Are From {user_country}")
#     print(f"The Course \"{course_name}\" Price is: {course_price - 30}$")

# __________________________________________________________________________________________________________



# -------------------------------------- Control Flow ""Make Decisions" (42) -------------------------
# ------------------------------------------------- Nested if ------------------------------------------

# user_name = input("My name is ")
# user_country = input("My country is ")  
# isstudent =input("Are u student or Not ")         # Yes or No   
# course_name = "Bioinformatics For Begginers"
# course_price = 100
# course_discount = 20

# if user_country == "Egypt" or user_country == "Somaal" or user_country == "Sudan" :
#     if isstudent == "Yes" or "yes":
#         print(f"Hello {user_name} Because U Are From {user_country} and Student")    
#         print(f"The Course \"{course_name}\" Price is: {course_price - 90}$")
#     else:
#         print(f"Hello {user_name} Because U Are From {user_country}")
#         print(f"The Course \"{course_name}\" Price is: {course_price - 80}$")
# elif user_country == "Kuwait" or user_country == "Bahrain" or "KSA":
#     print(f"Hello {user_name} Because U Are From {user_country}")
#     print(f"The Course \"{course_name}\" Price is: {course_price - 50}$") 
# else:
#     print(f"Hello {user_name} Because U Are From {user_country}")
#     print(f"The Course \"{course_name}\" Price is: {course_price - 30}$")

# ________________________________________________________________________________________________________



# --------------------------------- Ternary Conditional Operator (43) ---------------------------------------  
# ----------------------------------------------------------------------------------------------------------

# country = input("What's Ur country ")
# if country == "Egypt":
#    print(f"The Weather in {country} is 20")
# elif country == "KSA": 
#    print(f"The Weather in {country} is 30")
# else:
#    print("{country} is out")


# The whole condition in one line:

# country = input("What's Ur country ")
# if country == "Egypt": print(f"The Weather in {country} is 20")
# elif country == "KSA": print(f"The Weather in {country} is 30")
# else: print("{country} is out")


# country = input("What's Ur country ")
# if country == "Egypt" or country == "KSA": print(f"The Weather in {country} is 20")
# else: print("{country} is out") 


# Short if:

# country = input("What's Ur country ")
# print(f"The Weather in {country} is 20" if country == "Egypt" or country == 'KSA' else print("{country} is out"))



# Ternary Conditional Operators:

# movierate = 18
# age = int(input("Enter Ur Age "))         # CONDITION IF TRUE
# if age < movierate:0
#     print("Movie IS NOT GOOD 4U")         # CONDITION IF FALSE
# else:
#     print("Movie IS GOOD 4U")


#The Formula of TERNARY CONDIONAL OPERATOR:
#                    Condition if True | If Condition | else | Condition if False

# movierate = 18
# age = int(input("Enter Ur Age ")) 
# print("Movie IS NOT GOOD 4U" if age < movierate else "Movie IS GOOD 4U" )
# CONDITION    IF     TRUE   | If     Condition | else | Condition if False

# _________________________________________________________________________________________________________



# --------------------------------- Calculate Age Advanced Version (44) -------------------------------------
# ------------------------------------------- and Training -------------------------------------------------

# Collect Age Data:
# age = int(input("What's Ur Age? "))

# Write A Pretty Note:
# print("#" * 80)
# print(" U Can Write The First Letter Or The Full Name Of The Time Unite ".center(80, "#")) 
# print("#" * 80)

# Collect Time Units:
# unit = input("Choose The Time Unite: Months, Weeks, Days, Hours, Minutes, Seconds? ").strip().lower()

# Get Time Unites:
# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes *60
# the_rest_of_units = {
#     "months" : months, 
#     'weeks'  : weeks, 
#     'days' : days,
#     "hours" : hours, 
#     "minutes" : minutes,
#     "seconds": seconds
# }
# if unit == "months" or unit == "m": 
#     print(f"U Lived for {months:,} months")
#     response = input('if u wanna know all units, write ok or k: ').lower().strip()
#     if response == 'ok' or response == 'k':
#         print("the the rest of units are: ")
#         for key, value in the_rest_of_units.items():
#             print(value, key)
#     else:
#         print(f"U Lived for {months:,} months")
# elif unit == "weeks" or unit =='w':
#     print(f"U Lived for {weeks:,} weeks.")
#     response = input('if u wanna know all units, write ok or k: ').lower().strip()
#     if response == 'ok' or response == 'k':
#         print("the the rest of units are: ")
#         for key, value in the_rest_of_units.items():
#             print(value, key)
#     else:
#         print(f"U Lived for {weeks:,} weeks")
# elif unit == "days" or unit == "d":
#     print(f"U Lived for {days:,} days.")
#     response = input('if u wanna know all units, write ok or k: ').lower().strip()
#     if response == 'ok' or response == 'k':
#         print("the the rest of units are: ")
#         for key, value in the_rest_of_units.items():
#             print(value, key)
#     else:
#         print(f"U Lived for {days:,} days")
# elif unit == "hours" or unit == "h":
#     print(f"U Lived for {hours:,} hours.")
#     response = input('if u wanna know all units, write ok or k: ').lower().strip()
#     if response == 'ok' or response == 'k':
#         print("the the rest of units are: ")
#         for key, value in the_rest_of_units.items():
#             print(value, key)
#     else:
#         print(f"U Lived for {hours:,} hours")
# elif unit == "minutes" or unit == "min":
#     print(f"U Lived for {minutes:,} minutes.")
#     response = input('if u wanna know all units, write ok or k: ').lower().strip()
#     if response == 'ok' or response == 'k':
#         print("the the rest of units are: ")
#         for key, value in the_rest_of_units.items():
#             print(value, key)
#     else:
#         print(f"U Lived for {minutes:,} minutes")
# elif unit == "seconds" or unit == "s":
#     print(f"U Lived for {seconds:,} seconds.")
#     response = input('if u wanna know all units, write ok or k: ').lower().strip()
#     if response == 'ok' or response == 'k':
#         print("the the rest of units are: ")
#         for key, value in the_rest_of_units.items():
#             print(value, key)
#     else:
#         print(f"U Lived for {seconds:,} seconds")


# => Another short way:

# age = int(input("What's Ur Age? "))
# unit = input("Choose The Time Unit: Months, Weeks, Days, Hours, Minutes, Seconds? ").strip().lower()

# time_units = {
#     "months": age * 12,
#     "weeks": age * 12 * 4,
#     "days": age * 365,
#     "hours": age * 365 * 24,
#     "minutes": age * 365 * 24 * 60,
#     "seconds": age * 365 * 24 * 60 * 60
# }

# if unit in time_units:
#     time_value = time_units[unit]
#     print(f"U Lived for {time_value:,} {unit}.")
#     response = input('if you want to know all units, write "ok" or "k": ').lower().strip()
#     if response == 'ok' or response == 'k':
#         print("the rest of the units are:")
#         for key, value in time_units.items():
#             print(value, key)
#     else:
#         print(f"U Lived for {time_value:,} {unit}")
# else:
#     print("Invalid unit entered!")

# ________________________________________________________________________________________________________



# --------------------------------- Membership Operators (45) ----------------------------------------------
# -------------------------------------- in and not in ----------------------------------------------------


# String:

# name = 'ammar'
# print("m" in name)       # True
# print("a" in name)       # True
# print("A" in name)       # False
# print("m" not in name)   # False


# List:
     
# friends = ['ammar', "abdo", "saeed", "hossam"]
# print("hossam" in friends)      # True
# print("saeed" in friends)       # True
# print("abdo" not in  friends)   # True


# Using in and not in with Condition:
 
# countries1 = ['Sudan', 'Egypt', 'Somaal', "Nigeria", 'Syria']
# countries2 = ['KSA', "Kuwait", 'USA', 'Italy']

# countries1_discount = 80
# countries2_discount = 50

# mycountry = input("Enter The Name Of Ur Country: ").strip() 

# if mycountry in countries1:
#     print(f'Hello, U have a discount= {countries1_discount} $')
# elif mycountry in countries2: 
#     print(f'Hello, U have a discount= {countries2_discount} $')
# else:
#     print("U don't have any discount")    

# ________________________________________________________________________________________________________



# ---------------------------------- Practical Membership Control (46) ------------------------------------
# -----------------------------------------------------------------------------------------------------------


## List contains admins:
# admins = ['Ahemd','Ammar','Menassah','Kareem','Omar','Ali','Saher']

## Login:
# name = input('Plz, Write Ur Name: ').strip().capitalize()

## If Name is in Admins:
# if name in admins: 
#     print(f'Hello {name} ,Welcome Back')
#     option =input('Would you choose Delete or Update ur Name? ').strip().capitalize()

##     Update Option:
#     if option == 'Update' or option == 'U':
#         the_new_name = input('Write your new name: ').strip().capitalize()
#         admins[admins.index(name)] = the_new_name
#         print('Your new name is updated')
#         print(admins)

# #      Delete Option:
#     elif option == 'Delete' or option == 'U':
#         admins.remove(name)
#         print("Your name is removed")
#         print(admins)
 
# #      Wrong Option:
#     else:
#         print("You wrote a wrong option.")
    
# else:
#     status = input('U r not admin, I can add u if u want? ').strip().capitalize()
    # if status == 'Yes' or status == 'Y':
    #     print("You have been added.")
    #     admins.append(name)
    #     print(admins)
    
    # else:
    #     print('You are not added')
        
# ________________________________________________________________________________________________________



# --------------------------------------- Loop (while and else) (47) -----------------------------------------------
# ------------------------------ While condition is true, Code will run -----------------------------------

# => While condition is true, Code will run

# a = 0
# while a < 10:
#     a += 1          # a = a + 1
#     print(a)        # 1 : 10
# print("Loop is done")            # print when the condition became False  



# a = 0
# while a < 10:
#     print(a)         # 0 : 9
#     a += 1          # a = a + 1
# else:
#     print("Loop is done")         # print when the condition became False  


 
# while False:
#     print('will not print')   # Nothing happens as the condition isn't existed and even not true

# ____________________________________________________________________________________________________________



# --------------------------------------- Loop => while Training1 (48) ---------------------------------------
# -------------- While condition is true, Code will run un untill condition becomes false -------------------


# => While condition is true, Code will run un untill condition becomes false


# myfriends = ['Ammar','Ahmed','Ali','Anas','Mo','Zein','Reda','Taha','Abdo','Darsh']
# print(len(myfriends))   # List Length = 10
# a = 0
# while a < len(myfriends):
#     print(myfriends[a])
#     a += 1                   # => a = a + 1



# myfriends = ['Ammar','Ahmed','Ali','Anas','Mo','Zein','Reda','Taha','Abdo','Darsh']
# print(myfriends[0])
# print(myfriends[1])
# print(myfriends[2])
# print(myfriends[3])
# print(myfriends[4])
# print(myfriends[5])
# print(myfriends[6])
# print(myfriends[7])
# print(myfriends[8])
# print(myfriends[9])



# myfriends = ['Ammar','Ahmed','Ali','Anas','Mo','Zein','Reda','Taha','Abdo','Darsh']
# a = 0
# while a < len(myfriends):
#     print(f'#{str(a + 1).zfill(2)} {myfriends[a]}')
#     a += 1               
# else:
#     print('All Friends are printed in the screen')
## Output:
#01 Ammar
#02 Ahmed
#03 Ali
#04 Anas
#05 Mo
#06 Zein
#07 Reda
#08 Taha
#09 Abdo
#10 Darsh

# _____________________________________________________________________________________________________________



# ---------------------------------- Loop => while Training2 (49) ---------------------------------------------
# ------------------------------------ Simple Bookmark Manage ------------------------------------------------


# # Empty List To Fill LAter:
# mywebs = []

# # Maximum Allowed Websites:
# maximumwebs = 5

# while maximumwebs > 0:
#     # Input The New Website:
#     web = input('Website Name Without https:// ')

#     # Add The New Web to the list:
#     mywebs.append(f"https://{web.strip().lower()}") 

#     # Decrease one No. from allowed websites:
#     maximumwebs -= 1   # maximumwebs = maximumwebs - 1

#     # Print the added messamge:
#     print(f"Website Added, {maximumwebs} palces left")
    
#     # Print the list:
#     print(mywebs)

# else:
#     print(('The Bookmark is Full'))

# # Check If List is not Empty:
# if len(mywebs) > 0:
#     # Sort the list:
#     mywebs.sort()
#     print("Printing the list of websites in ur bookmark:")
#     a = 0
    # while a < len(mywebs):
    #     print(mywebs[a])
    #     a += 1

# ___________________________________________________________________________________________________________



# ------------------------------------ Loop => while Training3 (50) -----------------------------------------
# --------------------------------------- Simple Password Guess --------------------------------------------


# triesnumber = 4
# mainpasssord = 'Ammar699966'
# inputpassword= input("Write Ur Password: ")

# while inputpassword != mainpasssord:
#     triesnumber -= 1
#     print (f"Wrong password, {'Last Chance' if triesnumber == 0 else triesnumber} Left of Tries")                          
#     inputpassword = input("Write Ur Password: ")

#     if triesnumber == 0:
#         print("All Tries are done")

#         break
#         print('Not Printed')    # This code not run

# print('Loop is done')



# triesnumber = 4
# mainpasssord = 'Ammar699966'
# inputpassword= input("Write Ur Password: ")

# while inputpassword != mainpasssord:     # True     
#     triesnumber -= 1
#     print (f"Wrong password, {'Last Chance' if triesnumber == 0 else triesnumber} Left of Tries")
                              
#     inputpassword = input("Write Ur Password: ")

#     if triesnumber == 0:
#         print("All Tries are done")

#         break
#         print('Not Printed')

# else: 
    # print('Correct Password')

# __________________________________________________________________________________________________________



# -------------------------------------- Loop => for and else (51) ------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# Notes:
# The syntax: for item (variable) in iterable_object (A data type as list, set,...): 
#               Do something with item
# --------------------------------------
# item is a variable u create and call whenever u want 
# item refers to the current postion and it will be run and visit all items to the end
# iterble_object => Sequence [ lsit, tuple, set, dict, string of characters, ..... ]

# Note: 
# else here is not like in while as in while it's opposite to the condition but in for it's not 
# as in for there is no condition to be met.


# mynum = [1,2,3,4,5,6,7,8,9]
# for number in mynum:
#     print(number)
# else:
#     print("The loop is finished")
# 1
# 2
# 3
# 4
# 5
# 6
# 8
# 9
# The Loop is finished



# mynum = [1,2,3,4,5,6,7,8,9]
# for number in mynum:
#     print(number * 2)
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18



# mynum = [1,2,3,4,5,6,7,8,9]
# for number in mynum:
#     if number % 2 == 0:
#         print(f"The number {number} is even")
#     else:
#         print(f"The number {number} is odd")
# else:
#     print("The loop is finished")
# The number 1 is odd
# The number 2 is even
# The number 3 is odd
# The number 4 is even
# The number 5 is odd
# The number 6 is even
# The number 7 is odd
# The number 8 is even
# The number 9 is odd
# The loop is finished



# myname = 'Ammar'
# for letter in myname:
#     print(letter)
# A
# m
# m
# a
# r



# myname = 'Ammar'
# for letter in myname:
#     print(f"[ {letter.upper()} ]")
# [ A ]
# [ M ]
# [ M ]
# [ A ]
# [ R ]

# _________________________________________________________________________________________________________



# ----------------------------------------- Loop => for Training (52) ------------------------------------
# --------------------------------------------------------------------------------------------------------


# range(start, stop): Return an object that produces a sequence of integers 
# from start (inclusive) to stop (exclusive) by step.

# myrange = range(1,11)
# for number in myrange:
#     print(number)
# 1
# 2 
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10



# Dictionary

# myskills = {
#     'Python' : '95',
#     'R' : '95',
#     'Bash' : '70',
#     'C++' : '50'
# }
# print(myskills['R'])        # 95
# print(myskills.get('R'))    # 95

# for skill in myskills:
    # print(skill)              # only print the keys of dict

    # print(f'My Progress in lang {skill} is: {myskills.get(skill)}')

    ## Both are equal
    # print(f'My Progress in lang {skill} is: {myskills[skill]}')

# My Progress in lang Python is: 95
# My Progress in lang R is: 95
# My Progress in lang Bash is: 70
# My Progress in lang C++ is: 50

# ________________________________________________________________________________________________________



# -------------------------------------- Loop => for (53) -------------------------------------------------
# ---------------------------------------- Nested loop ---------------------------------------------------


# peoples = ['Ammar', 'Ahmed', 'Omar', 'Mo']
# skills = ['R', 'Bash', 'Python']

# for name in peoples:                      # outer loop 
#     print(f"{name} skills is:")

#     for skill in skills:                  # inner loop    
#         print(f"- {skill}")

# Ammar skills is:
# - R
# - Bash
# - Python
# Ahmed skills is:
# - R
# - Bash
# - Python
# Omar skills is:
# - R
# - Bash
# - Python
# Mo skills is:
# - R
# - Bash
# - Python



# peoples = {
#     'Ammar' : {
#         'Bash' : '70',
#         'R' : '80',
#         'Python' : '90'
#     },

#     'Ahmed' : {
#         'Bash' : '50',
#         'R' : '40',
#         'Python' : '60'
#     }, 

#     'Omar' : {
#         'Bash' : '80',
#         'R' : '65',
#         'Python' : '50'
#     },

#     'Mo' : {
#         'Bash' : '75',
#         'R' : '55',
#         'Python' : '85'
#     }
# }

# print(peoples['Ammar'])           # {'Bash': '70', 'R': '80', 'Python': '90'}
# print(peoples['Ammar']['R'])      # 80

# for name in peoples:
    # print(name)                              # print only the keys: Ammar , Ahmed, Omar, Mo

    # print(f"Skills and progress for {name} is: {peoples[name]}")         # print keys and values 

    # print(f"{peoples[name]}")                                            # print only the values 


 

# peoples = {
#     'Ammar' : {
#         'Bash' : '70',
#         'R' : '80',
#         'Python' : '90'
#     },

#     'Ahmed' : {
#         'Bash' : '50',
#         'R' : '40',
#         'Python' : '60'
#     }, 

#     'Omar' : {
#         'Bash' : '80',
#         'R' : '65',
#         'Python' : '50'
#     },

#     'Mo' : {
#         'Bash' : '75',
#         'R' : '55',
#         'Python' : '85'
#     }
# }

# for name in peoples:
#     print(f"Skills and progress for {name} is:")          
#     for skill in peoples[name]:
#         print(f"{skill} => {peoples[name][skill]}")


# Skills and progress for Ammar is:
# Bash => 70
# R => 80
# Python => 90
# Skills and progress for Ahmed is:
# Bash => 50
# R => 40
# Python => 60
# Skills and progress for Omar is:
# Bash => 80
# R => 65
# Python => 50
# Skills and progress for Mo is:
# Bash => 75
# R => 55
# Python => 85

# _____________________________________________________________________________________________________



# ----------------------------------------- continue, break, pass Keywords (54) -------------------------------
# -----------------------------------------------------------------------------------------------------


#                                        continue keyword:

# It forces to excute the next iteration of the loop (for @ while) while skipping the rest of the code inside
# the loop for the current iteration only  

# mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in mynum:
#     if num == 5:
#         continue
#     print(num)  
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9

# -------------------------------------------------------------------------------------------


#                                          break keyword:

# It exits or terminates a loop when an external condition is met

# mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in mynum:
#     if num == 5:
#         break
#     print(num)
# 1
# 2
# 3
# 4

     
# mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in mynum:
#     print(num)
#     if num == 5:
#         break   
# 1
# 2
# 3
# 4
# 5

# ------------------------------------------------------------------------------------------------

 
#                                         pass keywod: called null

# ignores the code 

# mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in mynum:
#     if num == 5:
#         pass


# mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in mynum:
#     if num == 5:                       # ignored
#         pass
#     print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# _______________________________________________________________________________________________________



# -------------------------------------- Advanced Dictionary Loop (55) ---------------------------------
# -------------------------------------------------------------------------------------------------------

# => looping both key and value:

# myskills = {
#     'R' : '80',
#     'Python' : '90',
#     'Bash' : '70'
# }
# for skill in myskills:
#     print(f"{skill} => {myskills[skill]}")      
# R => 80
# Python => 90
# Bash => 70


# Another way for looping both key and value:

# myskills = {
#     'R' : '80',
#     'Python' : '90',
#     'Bash' : '70'
# }
# for skill_key, progress_value in myskills.items():
#     print(f"{skill_key} => {progress_value}")
# R => 80
# Python => 90
# Bash => 70


# myskills = {
#     'R' : '80',
#     'Python' : '90',
#     'Bash' : '70'
# }
# print(myskills.items())     # dict_items([('R', '80'), ('Python', '90'), ('Bash', '70')])


# myskills = {
#     'Python' : {
#         'Basics' : '90',
#         'Advanved' : '60'
#     },
#     'R' : {
#         'Basics' : '80',
#         'Advanced' : '50'
#     }
# }
# for skill_key, skill_value in myskills.items():
#     print(f"=> {skill_key} progress is: ")
#     for level_key, level_value in skill_value.items():
#         print(f"- {level_key} => {level_value}")
# => Python progress is: 
# - Basics => 90
# - Advanved => 60
# => R progress is:
# - Basics => 80
# - Advanced => 50

# __________________________________________________________________________________________________________



# -------------------------------- Function and Return (56) -----------------------------------
# -----------------------------------------------------------------------------------------------------

# Notes:
# Function is a reusable block of code that does a task
# Fumction only runs when u call it
# Function accepts elements called [Parameters] to deal with
# Function can do the task without returning data
# Function can return data after job done
# Function creats to prevent dry [don't repeat ur self]
# Function accepts elements called [Arguments] when u call it
# There are built-in functions and user defined functions  
# Function is for all team and all apps
# -------------------------------------------------------------


# def function_name():
#     print('Hello python from an inside function') 
# function_name()         # Runs only if I call it => Hello python from an inside function


# def function_name():
#     return'Hello python from an inside function' 
# print(function_name())           # Hello python from an inside function
# print(function_name()[0:5])      # Hello  


# def function_name():
#     return'Hello python from an inside function' 
# data_from_function = function_name()
# print(data_from_function)            # Hello python from an inside function
# print(data_from_function[7:14])      #  python 

# __________________________________________________________________________________________________________



# ----------------------------- Function Parameters and Arguments (57) ------------------------
# ----------------------------------------------------------------------------------------------------------

# a, b, c = 'Ammar', 'Atef', 'Ahmed'
# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")


# def Say_Hi(n1, n2):
# def:                        => Function Keyword [Define]
# Say_Hi()                    => Function Name
# n1, n2                      => Parameters
# print(f'Hello {name}')      => The task
# Say_Hi('Ammar')             => Ammar is the argument


# def Say_Hi(n):
#     print(f'Hello {n}')
# Say_Hi('Ammar')               # => Hello Ammar


# a, b, c = 'Ammar', 'Atef', 'Ahmed'
# Say_Hi(a)                     # => Hello Ammar
# Say_Hi(b)                     # => Hello Atef
# Say_Hi(c)                     # => Hello Ahmed


# def addition(n1, n2):
#     print(n1 + n2)
# addition(10)            # TypeError: addition() missing 1 required positional argument: 'n2'
# addition(10, 10)        # 20   
# addition(-10, 12)       # 2   
# addition(10, 20, 30)    # TypeError: addition() takes 2 positional arguments but 3 were given


# def addition(n1, n2):
#     print(int(n1) + int(n2))
# addition('10', '20')            # 30
# addition('10', 'Ammar')         # ValueError: invalid literal for int() with base 10: 'Ammar'


# => So, by using if condition, we will check the data type that given:  

# def addition(n1, n2):
#     if type(n1) == int and type(n2) == int: 
#         print(n1 + n2)           
#     elif type(n1) == float and type(n2) == float:
#         print(n1 + n2)
#     elif type(n1) == float and type(n2) == int:
#         print(n1 + n2)
#     elif type(n1) == int and type(n2) == float:
#         print(n1 + n2)
#     else: 
#         print("Only Floats Allowed")
        
# addition(1, "2.2")           # Only Floats Allowed
# addition(1, "Ammar")         # Only Floats Allowed
# addition(1, 2)               # 3
# addition(1, 2.2)             # 3.2
# addition(1.8, 2.2)           # 4.0


# def full_name(f, m, l):
#     print(f"Hello {f.strip().capitalize()} {m.capitalize():.1s} {l.capitalize()}")
# full_name('   ammar  ', 'atef', 'ahmed')       # Hello Ammar A Ahmed

# ___________________________________________________________________________________________________



# ----------------------- Function Packing, Unpacking Argumnts (*Args) (58) -------------------
# -------------------------------------------------------------------------------------------------------

# We use Astrisk sign * for unpacking:
# use * also if I don't know the exact number of the arguments


# print(1, 2, 3, 4)                # 1 2 3 4

# mylist = [1, 2, 3, 4]             
# print(mylist)                    # [1, 2, 3, 4]
# print(*mylist)                   # 1 2 3 4
# ___________________________________________


# def Say_Hello(n1, n2, n3, n4):
#     peoples = [n1, n2, n3, n4]
#     for name in peoples:
#         print(f'Hello {name}')

# Say_Hello('Ammar', 'Atef', 'Ahmed', 'Ali')
# Hello Ammar
# Hello Atef
# Hello Ahmed
# Hello Ali
# _________________________________________


# Say_Hello('Ammar', 'Atef', 'Ahmed', 'Ali', 'Mo') 
# => TypeError: Say_Hello() takes 4 positional arguments but 5 were given

# So, we use Astrisk sign * :

# def Say_Hello(*peoples):
#     for name in peoples:
#         print(f'Hello {name}')

# Say_Hello('Ammar', 'Atef', 'Ahmed', 'Ali', 'Mo', 'Jo')
# Hello Ammar
# Hello Atef
# Hello Ahmed
# Hello Ali
# Hello Mo
# Hello Jo
# _______________________________________________


# def show_details(*skills):
#     print(f"Hello Ammar ur skills are: ")
#     for skill in skills:
#         print(skill)

# show_details('Bioinformatics', 'Data Science', 'Python', 'R', 'Bash')
 
 
# def show_details(name, *skills):
#     print(f"Hello {name} ur skills are: ")
#     for skill in skills:
#         print(skill)

# show_details('Ammar', 'Bioinformatics', 'Data Science', 'Python', 'R', 'Bash')
# Hello Ammar ur skills are: 
# Bioinformatics
# Data Science
# Python
# R
# Bash

# _______________________________________________________________________________________________________



# ---------------------------------- Function Default Parameters (59) -------------------------------------
# ------------------------------------------------------------------------------------------------------

# We use default parameters when the user not write the required parametrs to replace them:

# Notes:
#[1] The default value must be in the last parameter.
#[2] If u want make a default value in the 1st parameter, u have to make defaults to 
#    all the rest of parameters.

# def say_hi(name, age, country):
#     print(f'Hello {name.capitalize()} your age is {age} and u are from {country.capitalize()}')
# say_hi('ammar', 23, 'egypt')  # Hello Ammar your age is 23 and u are from Egypt
# say_hi('ahmed', 18, 'egypt')  # Hello Ahmed your age is 18 and u are from Egypt
# say_hi('ahmed', 18)           # TypeError: say_hi() missing 1 required positional argument: 'country'


# [1]
# def say_hi(name, age, country = 'unknown'):
#     print(f'Hello {name.capitalize()} your age is {age} and ur country is {country.capitalize()}')
# say_hi('ahmed', 18, 'egypt')     # Hello Ahmed your age is 18 and ur country is Egypt   
# say_hi('ahmed', 18)              # Hello Ahmed your age is 18 and ur country is Unknown    


# def say_hi(name, age = 'unknown', country = 'unknown'):
#     print(f'Hello {name.capitalize()} your age is {age} and ur country is {country.capitalize()}')
# say_hi('ammar')         # Hello Ammar your age is unknown and ur country is Unknown

# ---------------------------------


# [2]
# def say_hi(name = 'unknown', age, country):
#     print(f'Hello {name.capitalize()} your age is {age} and ur country is {country.capitalize()}')
# say_hi('ahmed', 18)     # SyntaxError: non-default argument follows default argument       
 

# def say_hi(name = 'unknown', age = 'unknown', country):
#     print(f'Hello {name.capitalize()} your age is {age} and ur country is {country.capitalize()}')
# say_hi('ahmed', 18)      # SyntaxError: non-default argument follows default argument


# def say_hi(name = 'unknown', age = 'unknown', country = 'unknown'):
#     print(f'Hello {name.capitalize()} your age is {age} and ur country is {country.capitalize()}')
# say_hi()              # Hello Unknown your age is unknown and ur country is Unknown
# say_hi('ali')         # Hello Ali your age is unknown and ur country is Unknown


# def say_hi(name = 'unknown', age , country = 'unknown'):
#     print(f'Hello {name.capitalize()} your age is {age} and ur country is {country.capitalize()}')
# say_hi(16)   # SyntaxError: non-default argument follows default argument

# ______________________________________________________________________________________________________



# ------------------------ Function Packing, Unpacking Keyword Arguments **KWArgs (60) ------------------
# --------------------------------------------------------------------------------------------------------

# ** for Keywords of the dictionary 

# def myskills(*skills):
#     print(type(skills))     # <class 'tuple'> 
#     for skill in skills:
#         print(f'{skill}')

# myskills('Python', 'R', 'Bash')
# Python
# R
# Bash


# def myskills(**skills):
#     print(type(skills))                 #  <class 'dict'>
#     for skill, value in skills.items():
#         print(f'{skill} => {value}')

# myskills(Python ='90', R = '80', Bash ='70')
# Python => 90
# R => 80
# Bash => 70


# my_skills = {
#     "Python" : '90',
#     "R" : '80',
#     "Bash" : "70"
# }

# def myskills(**skills):
#     print(type(skills))                 #  <class 'dict'>
#     for skill, value in skills.items():
#         print(f'{skill} => {value}')

# myskills(Python ='90', R = '80', Bash ='70')    
# Python => 90
# R => 80
# Bash => 70

# print(my_skills)     # {'Python': '90', 'R': '80', 'Bash': '70'}

# print(**my_skills)   # TypeError: 'Python' is an invalid keyword argument for print()
# ----------------------------------------


# my_skills = {
#     "Python" : '90',
#     "R" : '80',
#     "Bash" : "70"
# }

# def myskills(**skills):

#     print(type(skills))                 #  <class 'dict'>

#     for skill, value in skills.items():
#         print(f'{skill} => {value}')

# myskills(my_skills)   # TypeError: it needs key and value so we make unpacking by using **

# myskills(**my_skills)
# Python => 90
# R => 80
# Bash => 70

# _________________________________________________________________________________________________________



# ---------------------- Function Packing, Unpacking Keyword Arguments Trainings (61) ----------------------
# ---------------------------------------------------------------------------------------------------------

# Notes:
# To unpack the tuble items => use *
# To unpack the dict items => use **


# def show_skills(name, *skills, **skills_with_progress):
#     print(f'Hello {name.capitalize()} \nskills without progress are: ')

#     for skill in skills:
#         print(f'- {skill}')

#     for skill_key, skill_value in skills_with_progress.items():
#         print(f'skills with progress are: \n- {skill_key} => {skill_value}')

# show_skills('ammar', 'Python', 'R', 'C++' ,Bash = '99')      
# Hello Ammar
# skills without progress are: 
# - Python
# - R
# - C++
# skills with progress are:
# - Bash => 99
# ------------------------------------------


# mytuple = ('Python', 'R', 'C++')
# myskills = {
#     'C#' : '50',
#     'Java' : '40'
# }

# def show_skills(name, *skills, **skills_with_progress):
#     print(f'Hello {name.capitalize()} \nskills without progress are: ')

#     for skill in skills:
#         print(f'- {skill}')

#     print ("skills with progress are: ")
#     for skill_key, skill_value in skills_with_progress.items():
#         print(f'{skill_key} => {skill_value}')

# show_skills('ammar', mytuple, Bash = '99')      # - ('Python', 'R', 'C++')

# show_skills('ammar', *mytuple, Bash = '99')     #  unpack the tuple by *
# - Python
# - R
# - C++

# show_skills('ammar', *mytuple, myskills)       # - {'C#': '50', 'Java': '40'}

# show_skills('ammar', *mytuple, **myskills)     # unpack the tuple by **
# C# => 50
# Java => 40

# _______________________________________________________________________________________________________



# ------------------------------------------ Function Scope (62) ----------------------------------------
# -------------------------------------------------------------------------------------------------------










 


