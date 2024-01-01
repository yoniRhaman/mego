// //var ,let ,const (not ues var)
// let age =30;
// age =31;//const cant let me do this

// console.log(age)
// //use let when you want to change variable

// tipes:string, numbers,Boolean,null, undefined,Symbol(not use)

// const name ='joni';
// const age = 30;
// const rating = 4.5;
// const isCool = true;
// const x = null;//empty variable
// const y = undefined//No value exists
// let z;

// console.log(typeof(age))//check the types
//string

//  const name1 = "John"; // Replace with an actual name
// const age = 25; // Replace with an actual age
// //Templat String
// const hello = `My name is ${name1} and I am ${age} years old.`;
// console.log(hello);


// //string metods
// const s = 'Hello world';

// console.log(s.length); // Length of the string
// console.log(s.toUpperCase()); // Convert the string to uppercase
// console.log(s.toLowerCase()); // Convert the string to lowercase
// console.log(s.substring(0, 5)); // Output: Hello
// console.log(s.split('')); // Split the string into an array of characters

// const str = 'technology, computers, it, code';

// console.log(str.split(', ')); // Split the string into an array using ', ' as the separator

/*multi 
line
comment*/

//Arrays - varibals that hold multiple values
// Creating an array using the Array constructor
// const numbers = new Array(1, 2, 3, 4, 5);
// console.log(numbers);

// // Creating an array using array literal syntax
// const fruits = ['apples', 'orange', 'pears'];

// // Removing the last element from the 'fruits' array
// fruits.pop();

// // Finding the index of 'orange' in the 'fruits' array
// console.log(fruits.indexOf('orange'));

// // Assigning 'grapes' to the element at index 3 in the 'fruits' array
// fruits[3] = 'grapes';

// // Adding 'mangos' to the end of the 'fruits' array
// fruits.push('mangos');

// // Adding 'strawberries' to the beginning of the 'fruits' array
// fruits.unshift('strawberries');

// // Logging the element at index 1 in the 'fruits' array
// Array of todos


// const todos = [
//     {
//         id: 1,
//         text: 'Take out trash',
//         isCompleted: true
//     },
//     {
//         id: 2,
//         text: 'Meeting with boss',
//         isCompleted: true
//     },
//     {
//         id: 3,
//         text: 'Dentist appt',
//         isCompleted: false
//     }
// ];

// // Logging the text of the todo at index 1
// console.log(todos[1].text); // Output: Meeting with boss

// // Converting the 'todos' array into a JSON-formatted string
// const todosJSON = JSON.stringify(todos);

// // Logging the original 'todos' array
// console.log(todos);

// // Logging the JSON-formatted string
// console.log(todosJSON);

// Using a for loop
// for (let i = 0; i < 10; i++) {
//     console.log(`for loop Number: ${i}`);
// }

// // Using a while loop
// let j = 0; 
// while (j < 10) {
//     console.log(`while loop Number: ${j}`);
//     j++;
// }

// const x = '10';

// // Using the loose equality operator (==)
// if (x == 10) {
//     console.log('x is 10'); // This will be executed because '10' is loosely equal to 10
// } else {
//     console.log('x is not 10');
// }

// const y = '10';

// // Using the strict equality operator (===)
// if (y === 10) {
//     console.log('y is 10'); // This will not be executed because '10' is not strictly equal to 10
// } else {
//     console.log('y is not 10');
// // }
// //switch
// const x = 11

// const color = x > 10 ? 'red' : 'blue';

// switch(color){
//     case 'red':
//         console.log('color is red');
//         break;
//     case 'red':
//         console.log('color is red');
//         break; 
//         default:
//             console.log('color not red or blue');
//             break;
// }
// Using a regular function declaration
// function addNums(num1, num2) {
//     console.log(num1 + num2);
// }

// // Calling the regular function
// addNums(5, 5);

// // Using an arrow function
// const addNumsArrow = (num1, num2) => {
//     console.log(num1 + num2);
// }

// // Calling the arrow function
// addNumsArrow(5, 5);

// // Constructor function for creating Person objects
// function Person(firstName, lastName, dob) {
//     this.firstName = firstName;
//     this.lastName = lastName;
//     this.dob = dob;
// }

// // Creating a new person instance using the constructor
// const person1 = new Person('John', 'Doe', '15-2-1998');

// // Logging the created person object
// console.log(person1);






