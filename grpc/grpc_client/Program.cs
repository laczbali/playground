using System.Threading.Tasks;
using Grpc.Net.Client;


namespace grpc_client
{
	public class Program
	{
		static async Task Main(string[] args)
		{
			using var channel = GrpcChannel.ForAddress("http://localhost:5024");
			var client = new Greeter.GreeterClient(channel);

			var reply = await client.SayHelloAsync(new HelloRequest { Name = "Balazs"});
			Console.WriteLine($"Server says: [ {reply.Message} ]");
		}	
	}
}