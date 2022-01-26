# LMC in python

i made an lmc interpreter in python because i was learning lmc assembly in school

it doesn't really work in the same way as an actual lmc, but it has the same result (i think)

i also added a random mnemonic (RND) which generates a random number from -999 to 999 and stores that value in the accumulator

the lmc i learned in school can be accessed at https://peterhigginson.co.uk/lmc/

while the example files use the extension .lmc, any text file will be accepted.

NOTE: HLT statements are enforced in this implementation. please use HLT statements in your program to prevent errors

# how to run:

## to run a lmc program:

in the terminal, type `python lmc.py {filename}`

example: `python lmc.py square.lmc`

## to format an lmc program:

in the terminal, type `python lmcformatter.py {filename}`

example: `python lmcformatter.py comparison.lmc`

note that this overwrites the file. if your file/program breaks that's on you :)