# No Time

The challenge give us a link to a website url.
This website do have a `robot.txt` which send us to an `openapi` file.

The OpenAPI standart try to give the tool needed to write precise specifications of API's.

So in this file, we discover that there is a route where we can send a pin code in the body of the request.

It appears that everytime a number of the pincode is right, the response delay increases.

The solution is then to write a small python script that will measure the response time and check at worst 100 differents numbers.

The solution was the pin `141520091305` which give us the flag.
