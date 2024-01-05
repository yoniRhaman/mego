// Footer component representing the footer section of a website
function Footer() {
    // Return JSX structure for the footer
    return (
      <footer>
        {/* Paragraph with a copyright symbol, current year, and website name */}
        <p>&copy;{new Date().getFullYear()} your website name</p>
      </footer>
    );
  }
  
  // Exporting the Footer component as the default export
  export default Footer;
  