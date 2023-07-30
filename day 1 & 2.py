// python fundamentals

# Brackets
    () - Arg, Expressions, Tuple        brackets are not mandetory for making tuple but comma is
    {} - dictionary or set
    [] - indexing/subscripting/slicing, list
    <> - NA

# Identifiers
    - It must contain alpha-numeric only
    - Special character not allowed
    - cannot start from number
    - keywords can't be used

# operators
    1. Arithmetic: +, -, *, /, %(modulo), **(power), //(floor div)
    2. Assignment: =, +=, -=, ........
    3. Relational: <, >, >=, <=, ==, !=
    4. Logical: and, or, not                                                       (use on boolean data only)
    5. Bitwise: &, |, ~(negation), ^(xor), >> (right shift     m >> n => m / 2^n), << (left shift     m << n => m * 2^n)  (boolean calculation)
    6. Membership: in, not in                                                      (use to check something in collection)
    7. Identity: is, is not                                                         (used for memory management)

# Data & types
    1. int      10
    2. float    3.3
    3. complex  10 + 0j
    4. string   'hi', "hi", '''hiiiii''' triple quote used to create multiple lines string 
                immutable
    5. list     [4,3, "hi", 9.0]
                unstructured, mutable collection of heterogeneous data
    6. tuple      (3,5,4.3, "hi")    4,5,5
                unstructured, immutable collection of heterogeneous data
    7. dictionary   {3:5, 'a':[9,38,9]}
                structured, mutable collection of key value pairs

    8. set      {4,3,3,"ji"}
                unstructured collection of unique items           (we can't do any of 4 operation in set, we can't perform fundamental operatoins, set is  prohibited in programming)
    9. bool     True False
    10. NoneType None

#Concept of Mutability
                     Search for this           Why constant is variable is used for memory management???
    Works on Collections only
            i. Item Access
                - Indexing / Sub-scripting
                - Slicing
            ii. Item insertion
            iii. Item Assignment
            iv. Item Deletion


    a. Mutable
        (i), ii, iii, iv - possible

    b. Immutable    
        (i), ii - possible     iii, iv - Not possible



# Built-in Functions for Data types
# control Statements
## conditional
## Looping
## Comprehensions
# user defined functions
## function Parameterization
## Lambda Expressins
## Generators
## Decorators
# Object Oriented Programming
# Modules & Packages in python


# GUI Development using Python


## GIT setup
    # website   ---->    git-csm.com

# Create Repository - Done
# Initialize Repo - Done
    # this can be done by clicking source control tab and click initialize repo
    #      or 
    # by using command prompt   --->    git init

# user configuration 
    #    git config --global user.name "AKSHAY7877"
    #    git config --global user.email "2020pietcsakshay19@poornima.org"

# Remote Repository Connect
    # git remote add origin "https://github.com/AKSHAY7877/AI-ML-day1.git"    this is link from git

# Daily process
    # save & commit all changes
    # command is         ----->      git add .        use to make file stage
    #                    ----->      git commit -m "First time commit"
  # push the changes to github
    #                    ----->  git push origin main                      # git is software    push is process      origin  refer to things present at server side        main is the name of branch


https://github.com/sanampeeyush/piet_ai_7_23