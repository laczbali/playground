using Grpc.Core;
using grpc_app;
using grpc_server.Providers;

namespace grpc_server.Services
{
	public class ChatterService : Chatter.ChatterBase
	{
		private readonly ChatHistory _history;
		private int _chatLength = 0;

		public ChatterService(ChatHistory history)
		{
			_history = history;
		}

		public override Task<Empty> SendMessage(MessageRequest request, ServerCallContext context)
		{
			_history.History.Add(request);

			return Task.FromResult(new Empty());
		}

		public override async Task GetMessages(Empty request, IServerStreamWriter<HistoryReply> responseStream, ServerCallContext context)
		{
			while(!context.CancellationToken.IsCancellationRequested)
			{
				if (_chatLength == _history.History.Count) continue;

				_chatLength = _history.History.Count;

				var replyObject = new HistoryReply();
				replyObject.History.AddRange(_history.History);
				await responseStream.WriteAsync(replyObject);
			}
		}
	}
}
