
function TypingAccuracy(sentence , typedWord, timeTaken){

let words = sentence.split();
let typedWords = typedWord.split();
let count = 0;
let correct = 0;
if(typedWords.length == words.length){

for(word of words){
	
	if(word == typedWords[count]){correct += 1;}
count += 1;
}

}

else{console.log("Incorrect sentence");}


let accuracy = correct / count * 100;


wordPerMinute = count / (timeTaken / 60);

return{
accurate : accuracy,
word : wordPerMinute
}
}


const sentence = "I love programming";
const prompt = require('prompt-sync')();

const start = Date.now();
let typed = prompt(`Enter the sentence '${sentence}' : `);
const end = Date.now();

const timeTaken = (start - end) / 1000;

TypingAccuracy(sentence , typed , timeTaken)

console.log(`Timetake: ${timeTaken * -1}`);
console.log(`Words per minute: ${TypingAccuracy(sentence , typed , timeTaken).word}`);
console.log(`Typing accuracy: ${TypingAccuracy(sentence , typed , timeTaken).accurate}`);







