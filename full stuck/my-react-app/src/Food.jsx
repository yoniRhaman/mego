// Defining a functional component named Food
function Food() {
    // Declaring two constant variables, food1 and food2, to store food names
    const food1 = "Orange";
    const food2 = "Banana";
  
    // Returning a JSX structure with an unordered list
    return (
      <ul>
        {/* List item for the fixed food "Apple" */}
        <li>Apple</li>
  
        {/* List item for the dynamically assigned value of food1 */}
        <li>{food1}</li>
  
        {/* List item for the dynamically assigned value of food2, converted to uppercase */}
        <li>{food2.toUpperCase()}</li>
      </ul>
    );
  }
  
  // Exporting the Food component as the default export
  export default Food;
  