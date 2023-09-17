import { useEffect, useState } from "react";
import axios from "axios";

import "./App.css";
import { AudioRecorder, VideoRecorder } from './record';

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
      const data = await axios.post(`${baseUrl}/convos`, { 'username': 'amir', msg });
      setConvosList([...convosList, data.data])
      setMsg('');
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
          <AudioRecorder /> {/* Audio recording */}
          <VideoRecorder /> {/* Video recording */}
        </form>
      </header>
    </div>
  );
}

export default App;
