console.log("The Random Name Generator is Connected!")

const listOfNames = [];

//get names from user 

let newName = prompt("Please enter a name:");

//push name into array

listOfNames.push(newName);

function addAName() {
    let additionalName = prompt("Please enter another name:");
    listOfNames.push(additionalName);
    let yesOrNo = ""

    do {
      yesOrNo = prompt("Do you have another name to add? Please enter yes or no:");
    } while (yesOrNo == "yes" && addAName());

}

addAName();

//run the addAName function until the user tells you not to

// let continuePrompting = prompt("Do you have another name to add? Please enter yes or no:")

    // function continuePrompting() {
    //     let yesOrNo = prompt("Do you have another name to add? Please enter yes or no:");

    //     if (continuePrompting == "yes") {
    //         addAName();
    //     } else {
    //         console.log("Value did not == yes")
    //     }
    // }

    // continuePrompting()



console.log(`Here are all the names you entered:`)

for (i=0; i < listOfNames.length; i++) {
    console.log(listOfNames[i]);
}

let min = Math.ceil(0);
let max = Math.floor(listOfNames.length) - 1;

    console.log(`This is the max: ${max}`)

let positionInArray = (Math.floor(Math.random() * (max - min + 1) + min)); 

    console.log(`Here is the position in the array ${positionInArray}`);

    console.log(`Here is the same random name: ${listOfNames[positionInArray]}`)