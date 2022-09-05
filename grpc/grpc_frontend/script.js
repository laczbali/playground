const {HelloRequest, HelloReply} = require('./protodefs/greet_pb.js');
const {GreeterClient} = require('./protodefs/greet_grpc_web_pb.js');

var client = new GreeterClient('http://localhost:8080');

var request = new HelloRequest();
request.setName('World');

client.sayHello(request, {}, (err, response) => {
  console.log(response.getMessage());
});
