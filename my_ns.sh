#!/bin/bash

echo "MY_NS LOOKUP" > ns_out.txt

# Get your current IP address for the network interface
IP_ADDRESS=$(ipconfig getifaddr en0)

if [ -z "$IP_ADDRESS" ]; then
    echo "Unable to determine your IP address."
    exit 1
fi

# Extract the first two octets
FIRST_TWO_OCTETS=$(echo "$IP_ADDRESS" | cut -d'.' -f1,2)

for i in {1..254}; do
    for j in {1..254}; do
        # Generate the IP address to check
        IP_TO_CHECK="${FIRST_TWO_OCTETS}.${i}.${j}"
        
        # Perform DNS lookup and capture the response
        resp=$(nslookup "$IP_TO_CHECK" 2>/dev/null | grep -i 'name' | awk '{print $NF}')
        
        if [ -n "$resp" ];
        then
            echo "$IP_TO_CHECK: $resp" >> ns_out.txt
        else
            echo "No domain found:  $IP_TO_CHECK"
        fi
    done
done

echo "Script completed. Results are in ns_out.txt."