import { NavLink } from "react-router-dom";

import "../styles/NavBar.css";

function NavBar() {
  return (
    <nav className="navbar">
      <NavLink
        to="/"
        className={({ isActive }) => (isActive ? "active" : "")}
        end
      >
        Home
      </NavLink>

      <div className="navbar-github">
        <a
          href="https://github.com/csuchorski"
          target="_blank"
          rel="noopener noreferrer"
          title="View on GitHub"
        >
          GitHub
        </a>
      </div>
    </nav>
  );
}

export default NavBar;
