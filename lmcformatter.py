import sys 

from lmc import get_program

def main(file):
	program = get_program(file)
	print(program)
	maximum = 4
	for line in program:
		try:
			if maximum < len(line[1]):

				maximum = len(line[1])
		except TypeError:
			pass
	with open(file, "w") as f:
		for line in program:
			if not line[1]:
				line[1] = ""
			if not line[3]:
				line[3] = ""
			f.write(f"{line[1].rjust(maximum)} {line[2]} {line[3]}\n")

if __name__ == '__main__':
	main(sys.argv[1])