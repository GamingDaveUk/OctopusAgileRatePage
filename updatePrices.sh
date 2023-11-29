#!/bin/bash

# Run the curl command and capture the output
response=$(curl -s https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-A/standard-unit-rates/)

# Write the response to a file, blanking the file first
echo "$response" > data.json

echo "Data has been saved to data.json"
