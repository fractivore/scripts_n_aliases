import subprocess, time, csv, argparse
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--prefix')
args = parser.parse_args()

prefix = args.prefix
print("prefix:",args.prefix)

class threaded_cmd(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)

airo_command = ["airodump-ng","wlan0mon"]
airo_command.append("-w")
airo_command.append(prefix)

proc = subprocess.Popen(airo_command)
time.sleep(10)
proc.terminate()

same_prefix = []
files = os.listdir()
for filename in files:
    if prefix in filename and ".cap" in filename:
        same_prefix.append(filename)

same_prefix.sort(reverse=True)
cap_filename = same_prefix[0]
csv_filename = cap_filename[:-4]+".csv"

def get_bssid_list(csv_filename,essid_list):
    bssid_list = []
    with open(csv_filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[ESSID_ROW] in essid_list:
                bssid_list.append((row[BSSID_ROW],row[CHANNEL_ROW]))
    return bssid_list

def get_bssid_traffic(bssid_list,channel):
    bssid_filename_friendly = bssid.replace(":","-")
    command = ["airodump-ng", "-c", str(channel), "--bssid", bssid, "-w", bssid_filename_friendly]
    cmd_proc = subprocess.Popen(command)


