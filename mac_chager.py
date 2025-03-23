import subprocess
import optparse
import re

print("mac changer basladi.....")


interface = ''
mac_adress= ''


def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help='bu secim interfaceni teyin etmek ucun istifade olunur')
    parser.add_option('-m','--mac',dest='mac_adress',help='bu secim mac adressi teyin etmek ucun istifade olunur')
    return parser.parse_args()

def control_inputs(interface,mac_adress):
    if not  interface:
        interface = input("interfaceni daxil edin:")
    if not mac_adress:
        mac_adress = input("mac adressi daxil edin:")
    return interface,mac_adress

def mac_changer(interface,mac_adress):
    subprocess.call(['ifconfig',interface,'down'])
    subprocess.call(['ifconfig',interface,'hw','ether',mac_adress])
    subprocess.call(['ifconfig',interface,'up'])

def check_mac(interface):
    ifconfig = subprocess.check_output(['ifconfig',interface])
    ifconfig_str = ifconfig.decode()
    new_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_str)
    if new_mac:
        return new_mac.group(0)
    else:
        return False


(user_inputs,args) = get_inputs()
interface,mac_adress=control_inputs(user_inputs.interface,user_inputs.mac_adress)
mac_changer(interface,mac_adress)
final_mac = check_mac(interface)
if final_mac == mac_adress:
    print('mac address i ugurla deyisdirildi')
else:
    print("xeta bas verdi!!!")







