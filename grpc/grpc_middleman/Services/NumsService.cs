using Grpc.Core;
using Grpc.Net.Client;
using grpc_app;

namespace grpc_middleman.Services
{
	public class NumsService : Nums.NumsBase
	{
		public override async Task GetEvenNumbers(NumberRequest request, IServerStreamWriter<NumberReply> responseStream, ServerCallContext context)
		{
			using var channel = GrpcChannel.ForAddress("http://localhost:5178");
			var client = new Nums.NumsClient(channel);

			var stream = client.GetNumbers(request);
			await foreach (var incomingResponse in stream.ResponseStream.ReadAllAsync())
			{
				if (incomingResponse.Num % 2 != 0) continue;
				await responseStream.WriteAsync(incomingResponse);
			}
		}
	}
}
