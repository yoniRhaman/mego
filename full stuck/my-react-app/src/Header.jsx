// Header component representing the header section of a website
function Header() {
    // Return JSX structure for the header
    return (
      <header>
        {/* Main heading for the website */}
        <h1>My website</h1>
  
        {/* Navigation menu with a list of links */}
        <nav>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
  
        {/* Horizontal line for visual separation */}
        <hr></hr>
      </header>
    );
  }
  
  // Exporting the Header component as the default export
  export default Header;
  