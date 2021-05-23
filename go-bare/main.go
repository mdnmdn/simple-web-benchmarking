package main

import( 
  "fmt"
  "net/http"
)

func handleRequest(res http.ResponseWriter, req *http.Request) {
  fmt.Fprint(res, "ok - go bare")
}

func main() {
  http.HandleFunc("/", handleRequest)
  http.ListenAndServe(":5000", nil)
}
