const { MessageRequest, HistoryReply, Empty } = require('./protodefs/chat_pb.js');
const { ChatterClient } = require('./protodefs/chat_grpc_web_pb.js');

var chatClient = new ChatterClient('http://localhost:8080');

export function chatSetup() {
    document.getElementById("chat-send").addEventListener("click", chatSendMessage);
    chatListenToHistory();
}

function chatSendMessage() {
    var username = document.getElementById("chat-username").value;
    var message = document.getElementById("chat-message").value;

    var request = new MessageRequest();
    request.setUsername(username);
    request.setMessage(message);

    chatClient.sendMessage(request, {}, (err, response) => {
        document.getElementById("chat-message").value = "";
    });
}

function chatListenToHistory() {
    var request = new Empty();
    var historyStream = chatClient.getMessages(request);

    

    historyStream.on('data', function (response) {
        var messageList = response.getHistoryList();

        var history = "";
        messageList.forEach(messageRequest => {
            history += `${messageRequest.getUsername()}  :  ${messageRequest.getMessage()}\n`;
        });

        document.getElementById("chat-textarea").value = history;
    });
}