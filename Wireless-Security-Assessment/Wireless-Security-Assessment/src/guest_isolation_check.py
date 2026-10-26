#!/usr/bin/env python3
"""Test connectivity to ONE user-authorised private IP and TCP port.

Run from an owned/authorised guest network, against an owned/authorised host.
No enumeration or exploitation. One socket connect with a bounded timeout.
"""
from __future__ import annotations

import argparse
import ipaddress
import socket


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Owned private IPv4 test host")
    parser.add_argument("--port", type=int, required=True, help="One authorised TCP service port")
    parser.add_argument("--confirm-authorised", action="store_true", help="Confirm written authorisation or ownership of source/destination")
    parser.add_argument("--confirm-on-guest", action="store_true", help="Confirm the testing device is on the guest SSID")
    args = parser.parse_args()
    if not (args.confirm_authorised and args.confirm_on_guest):
        parser.error("Both authorisation and guest-network confirmations are mandatory")
    try:
        address = ipaddress.ip_address(args.target)
    except ValueError:
        parser.error("Target must be a literal private IPv4 address, not a hostname")
    if address.version != 4 or not address.is_private or address.is_loopback or address.is_link_local or address.is_multicast or address.is_unspecified or address.is_reserved:
        parser.error("Only a non-special RFC1918 private IPv4 host is permitted")
    if not any(address in ipaddress.ip_network(n) for n in ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")):
        parser.error("Target is not within RFC1918 private ranges")
    if not 1 <= args.port <= 65535:
        parser.error("Port must be between 1 and 65535")
    print(f"Attempting ONE TCP connection from guest to {address}:{args.port} (2s timeout)...")
    try:
        with socket.create_connection((str(address), args.port), timeout=2.0):
            print("CONNECTED: TCP handshake succeeded. If trusted-only, investigate a potential isolation failure.")
    except ConnectionRefusedError:
        print("REFUSED: Target reachable or rejected, but service is not accepting the connection. Isolation is NOT proven.")
    except (socket.timeout, TimeoutError):
        print("TIMED OUT: No successful connection. Isolation is NOT proven: validate target baseline and logs.")
    except OSError as exc:
        print(f"NO CONNECTION: {type(exc).__name__}. Isolation is NOT proven: validate with logs and trusted baseline.")


if __name__ == "__main__":
    main()
