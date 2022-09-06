using Grpc.Core;
using grpc_app;

namespace grpc_server.Services
{
	public class NumsService : Nums.NumsBase
	{
		public override async Task GetNumbers(NumberRequest request, IServerStreamWriter<NumberReply> responseStream, ServerCallContext context)
		{
			while (!context.CancellationToken.IsCancellationRequested)
			{
				var randInt = new Random().Next(request.LowerLimit, request.UpperLimit);
				await responseStream.WriteAsync(new NumberReply { Num = randInt });
				await Task.Delay(1000);
			}
		}
	}
}
