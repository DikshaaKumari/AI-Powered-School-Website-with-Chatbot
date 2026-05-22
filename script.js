// SELECT ELEMENTS

const chatbotBtn =
document.querySelector(".chatbot-button");

const chatWindow =
document.getElementById("chatWindow");

const closeChat =
document.getElementById("closeChat");

const sendBtn =
document.getElementById("sendBtn");

const userInput =
document.getElementById("userInput");

const chatBody =
document.getElementById("chatBody");


// OPEN CHAT WINDOW

chatbotBtn.onclick = () => {

    chatWindow.style.display = "flex";
};


// CLOSE CHAT WINDOW

closeChat.onclick = () => {

    chatWindow.style.display = "none";
};


// SEND MESSAGE

sendBtn.onclick = () => {

    sendMessage();
};


// ENTER KEY SUPPORT

userInput.addEventListener("keypress",
function(event){

    if(event.key === "Enter"){

        sendMessage();
    }
});


// MAIN FUNCTION

function sendMessage(){

    let message = userInput.value;

    if(message === ""){

        return;
    }

    // USER MESSAGE

    let userDiv =
    document.createElement("div");

    userDiv.classList.add("user-message");

    userDiv.innerText = message;

    chatBody.appendChild(userDiv);

    // CLEAR INPUT

    userInput.value = "";

    // AUTO SCROLL

    chatBody.scrollTop =
    chatBody.scrollHeight;


    // BOT REPLY

    setTimeout(() => {

        let botDiv =
        document.createElement("div");

        botDiv.classList.add("bot-message");

        botDiv.innerText =
        getBotReply(message);

        chatBody.appendChild(botDiv);

        chatBody.scrollTop =
        chatBody.scrollHeight;

    }, 1000);
}


// SIMPLE BOT REPLIES

function getBotReply(message){

    message =
    message.toLowerCase();

    if(message.includes("admission")){

        return "Admissions are currently open.";
    }

    else if(message.includes("fee")){

        return "Please contact office for fee details.";
    }

    else if(message.includes("timing")){

        return "School timing is 8 AM to 3 PM.";
    }

    else{

        return "Sorry, I will answer better after AI integration.";
    }
}