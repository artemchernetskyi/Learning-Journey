package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"net/http"
	"os"
	"strings"
	"time"
)

func envOrDefault(name, fallback string) string {
	value := os.Getenv(name)
	if value == "" {
		return fallback
	}
	return value
}

func incrementVisits(address string) (string, error) {
	conn, err := net.DialTimeout("tcp", address, 2*time.Second)
	if err != nil {
		return "", err
	}
	defer conn.Close()

	if err := conn.SetDeadline(time.Now().Add(2 * time.Second)); err != nil {
		return "", err
	}

	// Redis protocol: INCR visits
	if _, err := fmt.Fprint(conn, "*2\r\n$4\r\nINCR\r\n$6\r\nvisits\r\n"); err != nil {
		return "", err
	}

	reply, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		return "", err
	}

	if !strings.HasPrefix(reply, ":") {
		return "", fmt.Errorf("unexpected Redis response: %q", reply)
	}

	return strings.TrimSpace(strings.TrimPrefix(reply, ":")), nil
}

func main() {
	redisAddress := envOrDefault("REDIS_ADDR", "cache:6379")
	message := envOrDefault("APP_MESSAGE", "Docker mini-project")

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "healthy")
	})

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		visits, err := incrementVisits(redisAddress)
		if err != nil {
			log.Printf("Redis error: %v", err)
			http.Error(w, "Redis is unavailable", http.StatusServiceUnavailable)
			return
		}

		w.Header().Set("Content-Type", "text/plain; charset=utf-8")
		fmt.Fprintf(w, "%s\nVisits: %s\n", message, visits)
	})

	log.Printf("Application listening on :8080; Redis: %s", redisAddress)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
