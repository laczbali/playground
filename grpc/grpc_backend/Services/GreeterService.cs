using Grpc.Core;
using grpc_backend;

namespace grpc_backend.Services
{
	public class GreeterService : Greeter.GreeterBase
	{
		private readonly ILogger<GreeterService> _logger;
		public GreeterService(ILogger<GreeterService> logger) 
		{
			_logger = logger;
		}

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
	}
}