import os, sys, subprocess, glob

def run_wrapper():
    args = sys.argv[1:]
    print(args)
    
def main():
    run_wrapper()

if __name__ == '__main__':
    main()