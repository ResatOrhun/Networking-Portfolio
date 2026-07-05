from netmiko import ConnectHandler
from config_data import OSPF_CONFIGS

# Your Out-of-Band management IPs
devices = [
    {"name": "HQ", "host": "192.168.1.11", "device_type": "cisco_ios"},
    {"name": "BRANCH", "host": "192.168.1.12", "device_type": "cisco_ios"}
]

def deploy_ospf():
    for dev in devices:
        name = dev['name']
        config = OSPF_CONFIGS[name]
        
        # Build the command list dynamically
        commands = [
            f"router ospf 1",
            f"router-id {config['router_id']}",
            *config['networks'],
            "redistribute connected subnets"
        ]
        
        # Netmiko connection block
        try:
            with ConnectHandler(host=dev['host'], username="developer", 
                                password="C1sco12345", device_type=dev['device_type']) as net_conn:
                print(f"Pushing OSPF to {name}...")
                output = net_conn.send_config_set(commands)
                print(output)
                net_conn.send_command("write memory")
                print(f"SUCCESS: {name} updated.")
        except Exception as e:
            print(f"FAILED {name}: {e}")

if __name__ == "__main__":
    deploy_ospf()