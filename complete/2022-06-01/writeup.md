This confused me until it finally clicked.

`cons(a, b)` returns a function - `pair`.

The `pair` function takes another function as input.

Then, the pair function calls the input function, and returns its output.

So by passing a function `(lambda a, b: ...)`, it will call the function and return the result of the function that was input.

By passing it a function with parameters (a, b) in the case of the lambda, the lambda then returns either `a` or `b`, and the pair function returns what the lambda returns, thus getting us what we want.
