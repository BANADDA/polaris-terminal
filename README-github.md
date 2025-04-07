# Polaris Terminal

A command-line tool for connecting to Polaris containers via terminal.

## Overview

Polaris Terminal provides a seamless way to:
- Connect to container terminals via WebSocket
- List all available containers 
- View detailed container information
- Work with containers across different miners

## Features

- **Smart Container Name Handling**: Works with full container names, pod IDs, or partial names
- **Automatic Miner ID Detection**: Automatically detects the correct miner ID for each container
- **WebSocket Terminal**: Connect to container terminals via WebSocket
- **Detailed Container Information**: View complete details about containers
- **Configuration Management**: Persistent configuration stored in JSON file
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Installation

```bash
# Clone the repository
git clone https://github.com/BANADDA/polaris-terminal.git
cd polaris-terminal

# Install the package
pip install -e .
```

## Quick Start

```bash
# List all containers
polaris list

# Show details for a container
polaris info pod-1

# Connect to a container terminal
polaris connect polaris-pod-1743999981-pod-1
```

For more detailed documentation, see the [README.md](./README.md) file in the package directory.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 