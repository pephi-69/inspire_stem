alert("welcome winner sikee")

let Message="welcome "
document.write(Message)   

const randomNumber = Math.floor(Math.random()*100)+1
let  attempt = 0;

function checkguess (){
    const guess = parseInt(document.getElementById("guessField").value)
    attempt ++;
    if(isNaN(guess) || guess <1 || guess >100 ){
        setMessage("please enter a valid number btn 1 to 100")
        return
    }
    if (guess === randomNumber){
        setMessage("you win")
        document.getElementById("guessField").disabled = true
    }else if(guess < randomNumber){
        setMessage("go higher")
    }else {
        setMessage("go lower")
    }
function setMessage(Message){
    document.getElementById("Message").textContent = Message
}

}