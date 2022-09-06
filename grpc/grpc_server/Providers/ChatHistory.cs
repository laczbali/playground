using grpc_app;

namespace grpc_server.Providers
{
	public class ChatHistory
	{
		public ChatHistory() { }

		public List<MessageRequest> History = new List<MessageRequest>();
	}
}
