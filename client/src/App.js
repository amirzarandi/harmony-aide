import { useEffect, useState } from "react";
import axios from "axios";
import Bg from "./Bg"
import ReactAudioPlayer from 'react-audio-player';

import "./App.css";

const baseUrl = "http://127.0.0.1:5000";
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
const mic = new SpeechRecognition()

mic.continuous = true
mic.interimResults = true
mic.lang = 'en-US'

function App() {
  const [msg, setMsg] = useState("");
  const [convosList, setConvosList] = useState([]);
  const [isListening, setIsListening] = useState(false)
  const [note, setNote] = useState(null)
  const[savedNotes, setSavedNotes] = useState([])
  const [transcript, setTranscript] = useState("")

  useEffect(() => {
    handleListen()
  }, [isListening])

  const handleListen = () => {
    if(isListening) {
      mic.start()
      mic.onend = () => {
        console.log('continue..')
        mic.start()
      }
    } else {
      mic.stop()
      mic.onend = () => {
        console.log('Stopped Mic on Click')
        console.log(transcript)
        handleSubmit()
        // playBackgroundAudio();
      }
    }
    mic.onstart = () => {
      console.log('Mics on')
    }

    mic.onresult = event => {
      setTranscript(Array.from(event.results)
      .map(result => result[0])
      .map(result => result.transcript).join(''))
      mic.onerror = event => {
        console.log(event.error)
      }
    }
  }

  const playBackgroundAudio = () => {
    const audio = new Audio('../../server/data/audio_res.mp3');
    audio.play();
  };

  const fetchConvos = async () => {
    const data = await axios.get(`${baseUrl}/convos`)
    const { convos } = data.data
    setConvosList(convos);
  }

  const handleChange = (e) => {
    setMsg(e.target.value);
  };

  const handleSubmit = async () => {
    try {
      const reply = await axios.post(`${baseUrl}/response`, { 'input': transcript });
      const data1 = await axios.post(`${baseUrl}/convos`, { 'username': 'Dolores', 'msg': transcript})
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
        {/* <Bg /> */}
        <div className="container">
          <div className="box">
            {isListening ? <span>🎤</span> : <span>🔴🎤</span>}
            <button onClick={() => setIsListening(prevState => !prevState)}>Start/Stop</button>
          </div>
        </div>
        <form onSubmit={handleSubmit}>
        </form>
        <ReactAudioPlayer
  src="audio_res.mp3"
  autoPlay
  controls
/>
      </header>
    </div>
  );
}

export default App;
