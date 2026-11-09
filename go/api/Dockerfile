FROM golang:1.22-alpine AS build
WORKDIR /src
COPY . .
RUN go build -o /bin/op_dromos_api ./cmd/api

FROM alpine:3.20
COPY --from=build /bin/op_dromos_api /usr/local/bin/op_dromos_api
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/op_dromos_api"]
