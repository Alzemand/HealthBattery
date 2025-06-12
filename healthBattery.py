#!/usr/bin/python3
import os
import sys

def main(argv):
    if not argv or argv[0] == "-h" or argv[0] == "--help" or argv[0] == "":
        help()
    
    if argv and (argv[0] == "-s" or argv[0] == "--show"):
        show()
        
    elif argv and (argv[0] == "-l" or argv[0] == "--level") and os.getuid() == 0:
        if len(argv) < 2:
            print("Missing battery level parameter.")
            help()
        level = int(argv[1])
        set(level)
    else:
        print("You need to run as root!!")
        help()

def set(level: int):
    if level > 19 and level <= 100:    
        os.system(f"echo {level} | sudo tee /sys/class/power_supply/BAT1/charge_control_end_threshold > /dev/null")
        print(f"Battery level set to {level}%")
       
    else:
        print("Battery level must be between 20 and 100")
        sys.exit(1)

def show():
    print(f"Battery level setted to {os.popen('cat /sys/class/power_supply/BAT1/charge_control_end_threshold').read().strip()}%")
    sys.exit(1)

def help():
    print("usage -l --level [BATTERYLEVEL]")
    print("-l accepts one parameter between 20 and 100")
    print("that represents the max battery charge level\n")
    print("Example: ")
    print(f"sudo healthbattery -l 60")
    print("this sets max battery level to 60% to preserve battery health")
    sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])




