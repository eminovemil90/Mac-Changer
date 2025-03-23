import subprocess
import optparse
import re

mac_address = ''
interface = ''
def get_input():
    parser = optparse.OptionParser()
    parser.add_option('-i','--interface',dest= 'interface',help ='bu secim interfaceni teyin etmek ucun istifade olunur')
    parser.add_option('-m','--mac',dest= 'mac_address',help ='bu secim mac addresi teyin etmek ucun istifade olunur')
    return parser.parse_args()

def control_user_input(interface,mac_address):
    if not  interface:
        interface = input("interfaceni daxil edin:")
    if not mac_address:
        mac_address = input("mac adressi daxil edin:")
    return interface,mac_address


def mac_changer(interface, mac_address):
    subprocess.call(['ifconfig',interface,'down'])
    subprocess.call(['ifconfig',interface,'hw','ether',mac_address])
    subprocess.call(['ifconfig',interface,'up'])


def check_mac_address(interface):
    ifconfig = subprocess.check_output(['ifconfig',interface])
    ifconfig_str = ifconfig.decode()
    new_mac =  re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_str)
    if new_mac:
        return new_mac.group(0)
    else:
        return False

print("""
  __  __               _____ _
 |  \/  |             / ____| |
 | \  / | __ _  ___  | |    | |__   __ _ _ __   __ _  ___ _ __
 | |\/| |/ _` |/ __| | |    | '_ \ / _` | '_ \ / _` |/ _ \ '__|
 | |  | | (_| | (__  | |____| | | | (_| | | | | (_| |  __/ |
 |_|  |_|\__,_|\___|  \_____|_| |_|\__,_|_| |_|\__, |\___|_|
                                                __/ |
                                               |___/           by Emil Eminov

""")

(user_inputs,args) = get_input()
interface,mac_address=control_user_input(user_inputs.interface,user_inputs.mac_address)
mac_changer(interface,mac_address)
final_mac = check_mac_address(interface)
if final_mac == mac_address:
    print("mac address ugurla deyisildi.")
else:
    print("Xeta bas verdi!")





