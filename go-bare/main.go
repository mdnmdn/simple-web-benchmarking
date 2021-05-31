package main

import (
	"context"
	"fmt"
	"github.com/go-redis/redis/v8"
	"math/rand"
	"net/http"
)

var rdb *redis.Client

func randomKey() string {
	num := rand.Int31n(300)
	return fmt.Sprintf("key_%v", num)
}

func handleRequest(res http.ResponseWriter, req *http.Request) {
	fmt.Fprint(res, "ok - go bare")
}

func handleRequestRedisIncr(res http.ResponseWriter, req *http.Request) {
	ctx := context.Background()

	key := randomKey()

	val := rdb.Incr(ctx, key)

	fmt.Fprint(res, "go bare ", key, val)
}

func main() {
	rdb = redis.NewClient(&redis.Options{
		Addr: "redis:6379",
		// Password: "", // no password set
		// DB:       0,  // use default DB
	})

	http.HandleFunc("/", handleRequest)
	http.HandleFunc("/redis/incr", handleRequestRedisIncr)
	http.ListenAndServe(":5000", nil)
}
