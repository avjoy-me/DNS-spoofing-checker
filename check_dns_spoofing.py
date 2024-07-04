import dns.resolver
import dns.exception
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load the list of DNS servers from the provided file
with open('taiwanDNS.txt') as f:
    dns_servers = f.read().splitlines()

# Domain to check
domain = "avjoy.me"

# Correct IP address of the domain (Replace this with the actual correct IP)
correct_ip = "35.58.100.6"  # Replace this with the actual correct IP

# Function to check DNS server
def check_dns_server(server, domain, correct_ip):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [server]
    try:
        answer = resolver.resolve(domain, 'A', lifetime=5)  # Set a timeout of 5 seconds
        for rdata in answer:
            if rdata.address != correct_ip:
                return server, rdata.address
            else:
                return server, "correct"
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return server, "no_answer"
    except Exception as e:
        return server, str(e)

# Check DNS servers in parallel
results = []
with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_server = {executor.submit(check_dns_server, server, domain, correct_ip): server for server in dns_servers}
    for future in as_completed(future_to_server):
        server = future_to_server[future]
        try:
            result = future.result()
            results.append(result)
        except Exception as e:
            results.append((server, str(e)))

# Convert results to DataFrame
df = pd.DataFrame(results, columns=["DNS Server", "Result"])

# Save results to a text file
df.to_csv('dns_spoofing_results.txt', index=False)

# Display results in terminal
print(df)
