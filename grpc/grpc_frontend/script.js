const { HelloRequest, HelloReply, TimeStreamRequest, TimestampReply } = require('./protodefs/greet_pb.js');
const { GreeterClient } = require('./protodefs/greet_grpc_web_pb.js');

var client = new GreeterClient('http://localhost:8080');

window.onload = (event) => {
  document.getElementById("say-hello-btn").addEventListener("click", sayHello);
  document.getElementById("server-time-start").addEventListener("click", startStream);
  document.getElementById("server-time-stop").addEventListener("click", stopStream);
};

// -----------------------------------------------------------------------------------------

function sayHello() {
  var name = document.getElementById("say-hello-input").value;

  var request = new HelloRequest();
  request.setName(name);

  client.sayHello(request, {}, (err, response) => {
    document.getElementById("say-hello-output").value = response.getMessage();
  });
}

// -----------------------------------------------------------------------------------------

var timeStream;

function startStream() {
  setStreamButtonVisibility(false);

  var timeout = document.getElementById("server-time-timeout").value;
  
  var request = new TimeStreamRequest();
  request.setTimeout(timeout);

  timeStream = client.systemTime(request);
  
  timeStream.on('data', function(response) {
    console.log(response.getTimestamp());
  });

  timeStream.on('status', function(status) {
    console.log(status);
    // console.log(status.details);
    // console.log(status.metadata);
  });

  timeStream.on('end', function(end) {
    // stream end signal
    setStreamButtonVisibility(true);
  });
}

function stopStream() {
  // to close the stream (does not trigger 'end' & 'status' events)
  timeStream.cancel()
  setStreamButtonVisibility(true);
}

function setStreamButtonVisibility(startVisible) {
  document.getElementById("server-time-start").hidden = !startVisible;
  document.getElementById("server-time-stop").hidden = startVisible;
}
