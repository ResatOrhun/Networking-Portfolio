# provision.py
from netmiko import ConnectHandler
from ospf import deploy_ospf  # Import from your OSPF logic
from overlay import deploy_overlays

# Unified Inventory
ALL_DEVICES = [
    {"name": "HQ", "host": "192.168.1.11", "role": "router"},
    {"name": "CORE_SW1", "host": "192.168.1.10", "role": "switch"}
]

def main():
    for dev in ALL_DEVICES:
        with ConnectHandler(host=dev['host'], username="developer", 
                            password="C1sco12345", device_type="cisco_ios") as net_conn:
            
            # Step 1: Deploy Routing
            if dev['role'] == "router":
                deploy_ospf(net_conn, dev['name'])
            
            # Step 2: Deploy Services/VLANs
            if dev['role'] == "switch":
                deploy_overlays(net_conn, dev['name'])
                
            net_conn.send_command("write memory")

if __name__ == "__main__":
    main()