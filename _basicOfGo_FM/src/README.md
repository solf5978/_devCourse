
#### fmt.Scanf Jumping out the second scan

> Requires NewLine in present in order to
have consequent Scanf in use.
```go
fmt.printf ("1st Input")
// Have a newline "\n"
fmt.scanf ("%f\n", &num1)
fmt.printf ("Report number")
// Have a newline "\n"
fmt.scanf ("%f\n", &num2)
```

Reference 
- [StackOverflow - 1](https://stackoverflow.com/questions/54651199/second-scanf-jump-scan-in-go)
- [StackOverflow - 2](https://stackoverflow.com/questions/13846522/golang-scanf-error)

