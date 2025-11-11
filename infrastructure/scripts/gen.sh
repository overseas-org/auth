#!/bin/bash

# Read argument
CERT_PATH="."

while [[ $# -gt 0 ]]; do
  case $1 in
    --path)
      CERT_PATH="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Generate 2048-bit RSA Private Key
openssl genrsa -out $CERT_PATH/private.pem 2048

# Extract Public Key
openssl rsa -in $CERT_PATH/private.pem -pubout -out $CERT_PATH/public.pem


output=$(kubectl create secret generic auth-certs-secret \
  --from-file=$CERT_PATH/private.pem \
  --from-file=$CERT_PATH/public.pem \
  --from-literal=SECRET_KEY=$(openssl rand -hex 64) \
  --from-literal=REFRESH_KEY=$(openssl rand -hex 64) \
  -n overseas 2>&1)
if [ $? -ne 0 ];then
  echo " here"
  echo "$output"
  if echo "$output" | grep -q "already exists"; then
      exit 0
  fi
fi