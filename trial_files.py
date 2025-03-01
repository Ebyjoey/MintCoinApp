import os
import json

# Create a folder to store trial files
os.makedirs('trial_files', exist_ok=True)

# Create trial .txt files simulating blockchain activity
for i in range(1, 11):  # 10 trial files
    with open(f"trial_files/trial_file_{i}.txt", "w") as file:
        file.write(f"Trial file {i}: This file represents simulated blockchain activity or state.\n")
        file.write("It can include minting, transaction, or contract-related information.\n")
        file.write(f"Example Address: 0x{hex(i)[2:].zfill(40)}\n")
        file.write(f"Example Balance: {i * 100} Mintcoins\n")
        file.write(f"Transaction: 0x{hex(i*12345)[2:].zfill(64)}\n")

# Create a trial .json file to simulate Mintcoin data
trial_data = {
    "name": "Mintcoin (FMC)",
    "symbol": "FMC",
    "totalSupply": 1000000,
    "holders": [
        {"address": "0x1234567890abcdef1234567890abcdef12345678", "balance": 5000},
        {"address": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef", "balance": 10000},
        {"address": "0x7890123456789012345678901234567890123456", "balance": 2500}
    ],
    "transactions": [
        {"from": "0x1234567890abcdef1234567890abcdef12345678", "to": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef", "amount": 500, "txHash": "0x112233445566778899aabbccddeeff0011223344"},
        {"from": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef", "to": "0x7890123456789012345678901234567890123456", "amount": 1000, "txHash": "0x5566778899aabbccddeeff001122334455667788"},
        {"from": "0x7890123456789012345678901234567890123456", "to": "0x1234567890abcdef1234567890abcdef12345678", "amount": 250, "txHash": "0x99aabbccddeeff112233445566778899aabbccdd"}
    ]
}

# Save the trial data to a trial JSON file
with open('trial_files/trial_data.json', 'w') as json_file:
    json.dump(trial_data, json_file, indent=4)

print("Trial files created successfully!")
