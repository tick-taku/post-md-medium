#!/bin/bash

read -p "Integration token: " integration_token

cp secrets/secrets_sample.py ./secrets.py
sed -i -e "s/INTEGRATION_TOKEN =/INTEGRATION_TOKEN = \"$integration_token\"/" secrets.py
rm -rf secrets.py-e
