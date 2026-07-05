# config_data.py

OSPF_CONFIGS = {
    "HQ": {
        "router_id": "1.1.1.1",
        "networks": [
            "network 10.1.1.0 0.0.0.3 area 0",  # Your /30 transit link
            "network 10.1.10.0 0.0.0.255 area 0",
            "network 10.1.20.0 0.0.0.255 area 0"
        ]
    },
    "BRANCH": {
        "router_id": "2.2.2.2",
        "networks": [
            "network 10.1.2.0 0.0.0.3 area 0",  # Your /30 transit link
            "network 10.2.10.0 0.0.0.255 area 0",
            "network 10.2.20.0 0.0.0.255 area 0"
        ]
    }
}