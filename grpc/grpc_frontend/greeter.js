const { HelloRequest, HelloReply, TimeStreamRequest, TimestampReply } = require('./protodefs/greet_pb.js');
const { GreeterClient } = require('./protodefs/greet_grpc_web_pb.js');

var greeterClient = new GreeterClient('http://localhost:8080');

export function greeterSetup() {
    document.getElementById("say-hello-btn").addEventListener("click", greeterSayHello);
    document.getElementById("server-time-start").addEventListener("click", greeterStartStream);
    document.getElementById("server-time-stop").addEventListener("click", greeterStopStream);
}

function greeterSayHello() {
    var name = document.getElementById("say-hello-input").value;

    var request = new HelloRequest();
    request.setName(name);

    greeterClient.sayHello(request, {}, (err, response) => {
        document.getElementById("say-hello-output").value = response.getMessage();
    });
}

// -----------------------------------------------------------------------------------------

var greeterTimeStream;

function greeterStartStream() {
    greeterSetStreamButtonVisibility(false);

    var timeout = document.getElementById("server-time-timeout").value;

    var request = new TimeStreamRequest();
    request.setTimeout(timeout);

    greeterTimeStream = greeterClient.systemTime(request);

    greeterTimeStream.on('data', function (response) {
        document.getElementById("server-time-out").value = response.getTimestamp();
    });

    greeterTimeStream.on('status', function (status) {
        console.log(status);
        // console.log(status.details);
        // console.log(status.metadata);
    });

    greeterTimeStream.on('end', function (end) {
        // stream end signal
        greeterSetStreamButtonVisibility(true);
    });
}

function greeterStopStream() {
    // to close the stream (does not trigger 'end' & 'status' events)
    greeterTimeStream.cancel()
    greeterSetStreamButtonVisibility(true);
}

function greeterSetStreamButtonVisibility(startVisible) {
    document.getElementById("server-time-start").hidden = !startVisible;
    document.getElementById("server-time-stop").hidden = startVisible;
}