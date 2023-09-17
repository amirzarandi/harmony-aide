import { useEffect, useState } from "react";
import axios from "axios";

import "./App.css";

const baseUrl = "http://127.0.0.1:5000";

function App() {
  const [msg, setMsg] = useState("");

  const handleChange = (e) => {
    setMsg(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(msg);
  };

  return (
    <div className="App">
      <header className="App-header">
        <form>
          <label htmlfor="msg">Message</label>
          <input
            onChange={handleChange}
            type="text"
            name="msg"
            id="msg"
            value={msg}
          />
        </form>
      </header>
    </div>
  );
}

export default App;
