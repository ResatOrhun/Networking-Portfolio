from netmiko import ConnectHandler

# Target the HQ Router management IP
hq_router = {
    "host": "192.168.1.11", 
    "username": "developer",
    "password": "C1sco12345",
    "device_type": "cisco_ios_telnet",
    "session_timeout": 30,  # Wait 30 seconds for a response
    "timeout": 30           # Wait 30 seconds for the initial connection
}

commands = [
    "router ospf 1",
    "router-id 1.1.1.1",
    "network 10.1.1.0 0.0.0.3 area 0",
    "end"
]

try:
    print("Connecting to HQ Router...")
    with ConnectHandler(**hq_router) as net_conn:
        print("Connection successful! Pushing OSPF config...")
        output = net_conn.send_config_set(commands)
        print(output)
        
        # Verify the change
        print("\nVerifying Routing Table:")
        print(net_conn.send_command("show ip route ospf"))
        
except Exception as e:
    print(f"Error: {e}")