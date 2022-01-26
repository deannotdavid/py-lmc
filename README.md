# LMC in python

i made an lmc interpreter in python because i was learning lmc assembly in school

it doesn't really work in the same way as an actual lmc, but it has the same result (i think)

i also added a random mnemonic (RND) which generates a random number from -999 to 999 and stores that value in the accumulator

the lmc i learned in school can be accessed at https://peterhigginson.co.uk/lmc/

while the example files use the extension .lmc, any text file will be accepted.

HLT statements should be used if DAT statements are used. for example: a simple program such as `random.lmc` in the example files does not need one.

comments are also not supported: they will raise an error if they are included in your code.

# how to run:

## to run a lmc program:

in the terminal, type `python lmc.py {filename}`

example: `python lmc.py square.lmc`

a max memory space of 99 is enforced by default. use flag `-nml` (no memory limit) to remove the limit.

example: `python lmc.py toolong.lmc` would return an error, but `python lmc.py toolong.lmc -nml` will run.

## to format an lmc program:

in the terminal, type `python lmcformatter.py {filename}`

example: `python lmcformatter.py comparison.lmc`

note that this overwrites the file. if your file/program breaks that's on you :)