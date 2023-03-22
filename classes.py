
import socket
from typing import List, Dict


class TCPScanner:
    def __init__(self, target_hosts: List[str], target_ports: List[int], known_ports: Dict[int, str], timeout: float = 0.1, show_known_ports: bool = True):
        self.target_hosts = target_hosts
        self.target_ports = target_ports
        self.timeout = timeout
        self.known_ports = known_ports
        self.show_known_ports = show_known_ports

    def scan_ports(self) -> Dict[str, List[int]]:
        open_ports = {}
        for host in self.target_hosts:
            open_ports[host] = []
            for port in self.target_ports:
                try:
                    with socket.create_connection((host, port), timeout=self.timeout):
                        open_ports[host].append(port)
                        if self.show_known_ports:
                            try:
                                print(
                                    f"Port {port} is open on {host} ({self.known_ports[str(port)]})")
                            except KeyError:
                                print(f"Port {port} is open on {host}")
                        else:
                            print(f"Port {port} is open on {host}")
                except:
                    pass
        return open_ports
