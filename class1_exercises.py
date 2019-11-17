#! /usr/bin/env python3

ip_addr = input("Please enter an IP address: ")

ip_addr_split = ip_addr.split(".")

ip_addr_oct1 = int(ip_addr_split[0])
ip_addr_oct2 = int(ip_addr_split[1])
ip_addr_oct3 = int(ip_addr_split[2])
ip_addr_oct4 = int(ip_addr_split[3])

print("{:^20}|{:^20}|{:^20}|{:^20}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 80)
print("{:^20}|{:^20}|{:^20}|{:^20}".format(ip_addr_split[0], ip_addr_split[1], ip_addr_split[2], ip_addr_split[3]))
print("{:^20}|{:^20}|{:^20}|{:^20}".format(bin(ip_addr_oct1), bin(ip_addr_oct2), bin(ip_addr_oct3), bin(ip_addr_oct4)))
print("{:^20}|{:^20}|{:^20}|{:^20}".format(hex(ip_addr_oct1), hex(ip_addr_oct2), hex(ip_addr_oct3), hex(ip_addr_oct4)))
print("-" * 80)

