#!/usr/bin/env bash

url="${1:-https://example.com}"

result="$(curl -sS -o /dev/null \
    -w '%{http_code} %{time_total}' \
    "$url")"

curl_status=$?

if [[ "$curl_status" -ne 0 ]]; then
    echo "URL: $url"
    echo "Result: FAILED"
    echo "curl exit code: $curl_status"
    exit "$curl_status"
fi

read -r http_status response_time <<< "$result"

echo "URL: $url"
echo "HTTP status: $http_status"
echo "Response time: $response_time seconds"

if [[ "$http_status" -ge 200 && "$http_status" -lt 300 ]]; then
    echo "Result: HEALTHY"
    exit 0
else
    echo "Result: UNHEALTHY"
    exit 1
fi
