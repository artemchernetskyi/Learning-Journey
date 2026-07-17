#!/usr/bin/env bash

check_url() {
    local url="$1"
    local result
    local curl_status
    local http_status
    local response_time

    result="$(curl -sS -o /dev/null \
        -w '%{http_code} %{time_total}' \
        "$url")"

    curl_status=$?

    if [[ "$curl_status" -ne 0 ]]; then
        echo "URL: $url"
        echo "Result: FAILED"
        echo "curl exit code: $curl_status"
        return "$curl_status"
    fi

    read -r http_status response_time <<< "$result"

    echo "URL: $url"
    echo "HTTP status: $http_status"
    echo "Response time: $response_time seconds"

    if [[ "$http_status" -ge 200 && "$http_status" -lt 300 ]]; then
        echo "Result: HEALTHY"
        return 0
    else
        echo "Result: UNHEALTHY"
        return 1
    fi
}

if [[ "$#" -gt 0 ]]; then
    urls=("$@")
else
    urls=(
        "https://example.com"
        "https://example.com/not-existing-page"
        "https://this-domain-should-not-exist-987654321.com"
    )
fi

healthy_count=0
unhealthy_count=0
failed_count=0
overall_status=0

for url in "${urls[@]}"; do
    echo "--------------------"

    check_url "$url"
    function_status=$?

    echo "Function exit code: $function_status"

if [[ "$function_status" -eq 0 ]]; then
    ((healthy_count++))
elif [[ "$function_status" -eq 1 ]]; then
    ((unhealthy_count++))

    if [[ "$overall_status" -eq 0 ]]; then
        overall_status=1
    fi
else
    ((failed_count++))
    overall_status=2
fi
done

echo "===================="
echo "Summary"
echo "Total URLs: ${#urls[@]}"
echo "Healthy: $healthy_count"
echo "Unhealthy: $unhealthy_count"
echo "Failed: $failed_count"

exit "$overall_status"
