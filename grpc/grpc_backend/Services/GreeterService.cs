using Grpc.Core;
using grpc_backend;
using System.Diagnostics;

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

		public override async Task<TimeStampCollection> ClientTime(IAsyncStreamReader<TimestampReply> requestStream, ServerCallContext context)
		{
			var response = new TimeStampCollection();

			await foreach (var request in requestStream.ReadAllAsync())
			{
				response.Timestamps.Add(new TimestampReply { Timestamp = request.Timestamp });
			}

			return response;
		}

		public override async Task TimeExchange(IAsyncStreamReader<TimestampReply> requestStream, IServerStreamWriter<TimestampReply> responseStream, ServerCallContext context)
		{
			var sendTask = SendTime(responseStream, context);
			var receiveTask = ReceiveTime(requestStream, context);

			await Task.WhenAll(sendTask, receiveTask);
		}

		private async Task SendTime(IServerStreamWriter<TimestampReply> responseStream, ServerCallContext contex)
		{
			while(!contex.CancellationToken.IsCancellationRequested)
			{
				await responseStream.WriteAsync(new TimestampReply
				{
					Timestamp = ((DateTimeOffset)DateTime.Now).ToUnixTimeSeconds()
				});
				await Task.Delay(3000);
			}
		}

		private async Task ReceiveTime(IAsyncStreamReader<TimestampReply> requestStream, ServerCallContext context)
		{
			while(await requestStream.MoveNext() && !context.CancellationToken.IsCancellationRequested)
			{
				Debug.WriteLine(requestStream.Current.Timestamp);
			}
		}

	}
}