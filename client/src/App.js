import { useEffect, useState } from "react";
import axios from "axios";

import "./App.css";

const baseUrl = "http://127.0.0.1:5000";

function App() {
  const [msg, setMsg] = useState("");
  const [convosList, setConvosList] = useState([]);

  const fetchConvos = async () => {
    const data = await axios.get(`${baseUrl}/convos`)
    const { convos } = data.data
    setConvosList(convos);
  }

  const handleChange = (e) => {
    setMsg(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {

      const reply = await axios.post(`${baseUrl}/response`, { 'input': msg });
      const data1 = await axios.post(`${baseUrl}/convos`, { 'username': 'Deloris', msg})
      const data2 = await axios.post(`${baseUrl}/convos`, { 'username': 'AI', 'msg': reply['data']})
      setMsg('');
      const dat3 = await axios.post(`${baseUrl}/tts`, { 'text': reply['data'] })
      console.log(reply)
    } catch (err) {
      console.error(err.message)
    }
  };

  useEffect(() => {
    fetchConvos();
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label htmlfor="msg">Message</label>
          <input
            onChange={handleChange}
            type="text"
            name="msg"
            id="msg"
            value={msg}
          />
          <button type="submit">Submit</button>
        </form>
      </header>
    </div>
  );
}

export default App;
