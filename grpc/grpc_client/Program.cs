using Grpc.Core;
using Grpc.Net.Client;
using grpc_app;

using var channel = GrpcChannel.ForAddress("http://localhost:5116");
var client = new Nums.NumsClient(channel);

var stream = client.GetEvenNumbers(new NumberRequest { LowerLimit = 0, UpperLimit = 10});
var numcount = 0;
await foreach (var incomingResponse in stream.ResponseStream.ReadAllAsync())
{
	Console.WriteLine(incomingResponse.Num);

	numcount++;
	if (numcount == 5) break;
}

stream.Dispose();
