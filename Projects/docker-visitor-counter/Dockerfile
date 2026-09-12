# syntax=docker/dockerfile:1

FROM golang:1.26-alpine AS builder

WORKDIR /src
COPY main.go .
RUN CGO_ENABLED=0 go build -o /app main.go

FROM alpine:3.22

COPY --from=builder /app /app

EXPOSE 8080
CMD ["/app"]
