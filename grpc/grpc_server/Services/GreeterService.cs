using Grpc.Core;
using grpc_app;

namespace grpc_server.Services
{
	public class GreeterService : Greeter.GreeterBase
	{
		public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
		{
			return Task.FromResult(new HelloReply
			{
				Message = "Hello " + request.Name
			});
		}

		public override async Task SystemTime(TimeStreamRequest request, IServerStreamWriter<TimestampReply> responseStream, ServerCallContext context)
		{
			int TIMEOUTSEC = request.Timeout;
			for (int i = 0; i < TIMEOUTSEC; i++)
			{
				if (context.CancellationToken.IsCancellationRequested) break;

				await responseStream.WriteAsync(new TimestampReply
				{
					Timestamp = ((DateTimeOffset)DateTime.Now).ToUnixTimeSeconds()
				});
				await Task.Delay(1000);
			}
		}

		public override Task<TimeStampCollection> ClientTime(IAsyncStreamReader<TimestampReply> requestStream, ServerCallContext context)
		{
			return base.ClientTime(requestStream, context);
		}

		public override Task TimeExchange(IAsyncStreamReader<TimestampReply> requestStream, IServerStreamWriter<TimestampReply> responseStream, ServerCallContext context)
		{
			return base.TimeExchange(requestStream, responseStream, context);
		}
	}
}