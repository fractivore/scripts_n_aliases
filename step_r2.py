import sys, r2pipe, argparse, threading
from os.path import exists

parser = argparse.ArgumentParser()
parser.add_argument('--filename')
parser.add_argument('--dbg', action='store_true')
args = parser.parse_args()


filename_in = args.filename
print("filename_in:",filename_in)
if not exists(filename_in):
    print("Please enter a valid filename.")
    exit()

class threadstep(threading.Thread):
    def __init__(self,filename):
        threading.Thread.__init__(self) #open new thread
        self.r2 = r2pipe.open(filename) #define open instance of r2pipe in this new thread
        self.ci = self.r2.cmdj("pdj 1")[0]
        self.ii = self.ci

    def step(self):
        self.r2.cmd("ds") #step one instruction
        self.r2.cmd("sr rip") #seek to the current value of rip register in r2
    def disaseek(self):
        self.step()
        self.ii = self.r2.cmdj("pdj 1")
        if type(self.ii) == list:
            #self.current_instruction = intermed_instruct 
            #print(intermed_instruct)
            self.ci=self.ii[0]
            #print(self.ci)

    def run(self):
        if args.dbg:
            print(f'Attempting to open {filename_in} in debug mode')
            self.r2.cmd("doo")

        while self.ci['type'] != 'invalid':
            self.disaseek()
            #if type(self.current_instruction)==list:
            print(self.ci)
    
instance = threadstep(filename_in)
instance.start()
instance.run()

