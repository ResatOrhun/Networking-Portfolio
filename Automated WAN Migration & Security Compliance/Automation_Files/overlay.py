# overlay.py

# Data structure for your VLAN/SVI requirements
VLAN_CONFIGS = {
    "CORE_SW1": {
        "vlan_data": [
            {"id": "10", "name": "IT_DEPT", "ip": "192.168.10.1 255.255.255.0"},
            {"id": "20", "name": "HR_DEPT", "ip": "192.168.20.1 255.255.255.0"}
        ]
    }
}

def deploy_overlays(net_conn, device_name):
    config = VLAN_CONFIGS.get(device_name)
    if not config:
        return
    
    commands = []
    for vlan in config['vlan_data']:
        commands.extend([
            f"vlan {vlan['id']}",
            f"name {vlan['name']}",
            f"interface Vlan{vlan['id']}",
            f"ip address {vlan['ip']}",
            "no shutdown"
        ])
    
    print(f"Deploying VLANs/SVIs to {device_name}...")
    net_conn.send_config_set(commands)