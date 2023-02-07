import os
def hashes():
    print('\n#################################################################################################################################################################')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

hashes()
print('Conservation mode: \n1. 0 - OFF (Battery will charge till 100%)')
print('2. 1 - ON (Battery will charge till 60%)')

prompt = int(input('Enter your option (0/1): '))
hashes()
if prompt == 1:
    os.system('echo 1  | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode')
    print('Conservation mode is "ON", battery will charge till 60%')
    hashes()
elif prompt == 0:
    os.system('echo 0  | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode')
    print('Conservation mode is "OFF", battery will charge till 100%')
    hashes()
else:
    print('Wrong input "',prompt,'". Valid inputs: 0 or 1 (int)')
    hashes()
    exit()