import pyfiglet
import sys
import socket
from datetime import datetime
from classes import TCPScanner
import click
from utils import pre_proccess_hosts, pre_proccess_ports
import json


@click.command()
@click.option(
    "--hosts",
    prompt="Host list (separated by comma or CIDR block)",
    help="Host list (separated by comma or CIDR block)",
)
@click.option(
    "--ports",
    prompt="Port list (separated by comma or [first]-[last])",
    help="Port list (separated by comma or [first]-[last])",
    default="",
)
@click.option(
    "--timeout",
    prompt="Timeout of socker connection",
    help="Timeout of socker connection",
    default="0.1",
)
@click.option(
    "--show_known_ports",
    prompt="Show port known service (y/n)",
    help="Show port known service next to port in stdout(y/n)",
    default="y",
)
@click.option(
    "--output",
    prompt="Output file name for json file",
    help="Output file name."
)
def main(hosts, ports, timeout, show_known_ports, output):
    # Open known_ports.json as dict
    with open("known_ports.json", "r") as f:
        known_ports = json.load(f)
    port_scanner = TCPScanner(pre_proccess_hosts(
        hosts), pre_proccess_ports(ports), known_ports, timeout=float(timeout), show_known_ports=show_known_ports == "y")
    open_ports = port_scanner.scan_ports()
    if output != "":
        if not output.endswith(".json"):
            output += ".json"
        with open(output, "w") as f:
            json.dump(open_ports, f)


if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("PORT SNIFFER")
    print(ascii_banner)
    main()
