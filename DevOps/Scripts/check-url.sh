#!/usr/bin/env bash

url="${1:-https://example.com}"

if curl -fsS -o /dev/null "$url"; then
    echo "Website check: OK - $url"
else
    status=$?
    echo "Website check: FAILED - $url"
    echo "curl exit code: $status"
    exit "$status"
fi
