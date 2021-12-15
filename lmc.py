import sys
import random
from typing import Union

KEYWORDS = [
"ADD",
"SUB",
"STA",
"LDA",
"BRA",
"BRZ",
"BRP",
"INP",
"OUT",
"HLT",
"DAT",
"RND"
]

memory = [[None, None] for _ in range(100)]
jumps = []

def get_program(filename) -> list[str]:
	with open(filename, "r") as f:
		lines = f.readlines()
	for index, line in enumerate(lines):
		
		lines[index] = lines[index].split()
		lines[index].insert(0, index)
		line_len = len(lines[index])
		if line_len == 2:
			lines[index].insert(1, None)
			lines[index].append(None)
		if line_len == 3:
			if lines[index][-1] in KEYWORDS:
				lines[index].append(None)
			else:
				lines[index].insert(1, None)
	return lines


def translate(lines: list[list[str]]) -> list[list[str]]:
	assert len(lines) <= 99, f"Program is too long! {len(lines)} lines"
	for index, line in enumerate(lines):
		if line[1]:
			jumps.append([line[0], line[1]])
		if line[3]:
			try:
				line[3] = int(line[3])
			except:
				for index, jump in jumps:
					jumped = False
					if line[3] == jump:
						jumped = True
					if jumped:
						line[3] = index
		check_line(line)
	return lines


def check_line(line) -> bool:
	for word in KEYWORDS:
		assert line[2] in KEYWORDS, f"A line does not use a valid mnemonic: {line[2]}"
	assert len(line) <= 4, f"{line} is too long"

	return True


def load_to_memory(lines):
	for index, line in enumerate(lines):
		memory[index] = [line[2], line[3]]


def output_program(lines):
	for line in lines:
		print(line)


def check_pointing(pointing, cir):
	if pointing or pointing == 0:
		return True
	assert False, f"Line {cir}: Instruction should point to a memory address but doesn't\n{memory[cir]}"
	exit(1)


def get_input() -> int:
	while True:
		try:
			inp = int(input("Enter value: "))
			if not (-999 <= inp <= 999):
				raise ValueError
			return inp
		except ValueError:
			print("Value not valid")


def run():
	cir = 0
	acc = 0
	current_instruction = ""
	while current_instruction != "HLT":
		cir = int(cir)
		current_read = memory[cir]

		current_instruction = current_read[0]
		pointing = current_read[1]
		if type(pointing) is str:
			pointing = int(pointing)
		acc = int(acc)
		# print(pointing)

		if current_instruction == "ADD":
			check_pointing(pointing, cir)
			acc += int(memory[pointing][1])
			

		if current_instruction == "SUB":
			check_pointing(pointing, cir)
			acc -= int(memory[pointing][1])
		
		if current_instruction == "STA":
			check_pointing(pointing, cir)
			memory[pointing][1] = acc
		
		if current_instruction == "LDA":
			check_pointing(pointing, cir)
			if memory[pointing][1] is None:
				acc = 0
			else:
				acc = memory[pointing][1]
		
		if current_instruction == "BRA":
			check_pointing(pointing, cir)
			cir = pointing - 1
		
		if current_instruction == "BRZ":
			check_pointing(pointing, cir)
			if acc == 0:
				cir = pointing - 1
		
		if current_instruction == "BRP":
			check_pointing(pointing, cir)
			if acc >= 0:
				cir = pointing - 1
		
		if current_instruction == "INP":
			acc = get_input()

		if current_instruction == "OUT":
			print(acc)

		if current_instruction == "HLT" or not current_instruction:
			return

		if current_instruction == "RND":
			acc = random.randint(-999, 999)
			
		if current_instruction == "DAT":
			assert False, f"Line {cir}: DAT instruction reached when it should not be run"
			exit(1)

		cir += 1


def main(filename: str):
	# output_program(translate(get_program(filename)))
	translate(get_program(filename))
	
	load_to_memory(translate(get_program(filename)))
	# prog = get_program("adder.txt")
	# prog = translate(prog)
	# load_to_memory(prog)
	run()

if __name__ == '__main__':
	main(sys.argv[1])
