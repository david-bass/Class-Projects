#! /usr/bin/env python3

print('hello world')

hello_world = ('hello world')

ip_addr = input("Enter an IP address: ")
print (ip_addr)

hello = hello_world.capitalize()
print(hello)

hello2 = hello_world.upper()
print(hello2)

hello3 = hello2.lower()
print(hello3)

s_ip_addr = ip_addr.split('.')
print(s_ip_addr)

#new variable with each octet converted to an integer so it can be changed to hex or binary
i_f_ip_addr = int(s_ip_addr[0])
i_s_ip_addr = int(s_ip_addr[1])
i_t_ip_addr = int(s_ip_addr[2])
i_fr_ip_addr = int(s_ip_addr[3])

# new variable with each octet as hex
h_i_f_ip_addr = hex(i_f_ip_addr)
h_i_s_ip_addr = hex(i_s_ip_addr)
h_i_t_ip_addr = hex(i_t_ip_addr)
h_i_fr_ip_addr = hex(i_fr_ip_addr)

print(i_f_ip_addr, h_i_f_ip_addr)
print(i_s_ip_addr, h_i_s_ip_addr)
print(i_t_ip_addr, h_i_t_ip_addr)
print(i_fr_ip_addr, h_i_fr_ip_addr)

#formatting addresses
ip_addr1 = '1.1.1.1'
ip_addr2 = '2.2.2.2'
ip_addr3 = '3.3.3.3'

print("\n")
#print("-" * 80)
print(ip_addr1, ip_addr2, ip_addr3)
#print("-" * 80)

print("\n")
#print("-" * 80)
#print("{:^20},{:^20},{:^20}".format(ip_addr1, ip_addr2, ip_addr3)
#print("-" * 80)
