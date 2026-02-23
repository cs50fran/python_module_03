import sys

def command_quest():
    program_name:str =  sys.argv[0]
    total_args: int = len(sys.argv)

    if len(sys.argv) == 1:
        print ("No arguments provided!")
        print(f"Program name: {program_name}")
        print (f"Total arguments: {total_args}")

    else:
        print(f"Program name: {program_name}")
        print(f"Arguments Received: {total_args - 1}")
        for i in range(1, total_args):
            print(f"Argument {i}: {sys.argv[i]}")
        print (f"Total arguments: {total_args}")

if __name__ == "__main__":
    command_quest()