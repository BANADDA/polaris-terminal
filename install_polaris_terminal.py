import os

from install_polaris_terminal import print_step


def create_config():
    """Create a default configuration file"""
    print_step("Creating configuration file")
    
    config_dir = os.path.expanduser("~/.polaris")
    os.makedirs(config_dir, exist_ok=True)
    
    config_file = os.path.join(config_dir, "config.json")
    
    if not os.path.exists(config_file):
        import json
        config = {
            "server_url": "https://polaris-test-server.onrender.com",
            "miner_id": "EXAMPLE-MINER-ID-REPLACE-THIS"
        }
        
        with open(config_file, "w") as f:
            json.dump(config, f, indent=2)
        
        print(f"Created default configuration file: {config_file}")
        print("\nIMPORTANT: For security reasons, you must configure your miner ID:")
        print("  polaris config --miner-id YOUR_MINER_ID")
    else:
        print(f"Configuration file already exists: {config_file}") 