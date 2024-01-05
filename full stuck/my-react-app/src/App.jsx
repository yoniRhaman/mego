// Importing the Header component from the specified file
import Header from "./Header.jsx";

// Importing the Footer component from the specified file
import Footer from "./Footer.jsx";

// Importing the Food component from the specified file
import Food from "./Food.jsx";

// The main App component
function App() {
  // Returning a JSX structure that includes the Header, Food, and Footer components
  return (
    <>
      {/* Rendering the Header component */}
      <Header />

      {/* Rendering the Food component */}
      <Food />

      {/* Rendering an empty footer (you might want to replace this with the actual Footer component) */}
      <footer></footer>
    </>
  );
}

// Exporting the App component as the default export
export default App;
