import React, { useState, useEffect } from 'react';

function AudioRecorder() {
  const [audioChunks, setAudioChunks] = useState([]);
  const [audioRecorder, setAudioRecorder] = useState(null);
  const [isAudioRecording, setIsAudioRecording] = useState(false);

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
      const rec = new MediaRecorder(stream);

      rec.ondataavailable = (e) => {
        setAudioChunks([...audioChunks, e.data]);

        if (rec.state === 'inactive') {
          const mimeType = 'audio/wav';
          const audioBlob = new Blob(audioChunks, { type: mimeType });
          const audioURL = URL.createObjectURL(audioBlob);

          const recordedAudio = document.getElementById('recordedAudio');
          recordedAudio.srcObject = null; // Reset srcObject
          recordedAudio.src = audioURL;
          recordedAudio.controls = true;
          recordedAudio.play();
        }
      };

      setAudioRecorder(rec);
    });
  }, [audioChunks]);

  const toggleAudioRecording = () => {
    if (isAudioRecording) {
      setIsAudioRecording(false);
      audioRecorder.stop();
    } else {
      setIsAudioRecording(true);
      setAudioChunks([]);
      audioRecorder.start();
    }
  };

  return (
    <div>
      <button
        id="recordAudio"
        value={isAudioRecording ? 'ON' : 'OFF'}
        onClick={toggleAudioRecording}
        style={{
          borderRadius: '50%',
          maxWidth: '50%',
          maxHeight: '30%',
          backgroundColor: isAudioRecording ? 'blue' : 'red',
        }}
      ></button>
      <audio id="recordedAudio"></audio>
    </div>
  );
}

function VideoRecorder() {
  const [videoChunks, setVideoChunks] = useState([]);
  const [videoRecorder, setVideoRecorder] = useState(null);
  const [isVideoRecording, setIsVideoRecording] = useState(false);

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
      const rec = new MediaRecorder(stream);

      rec.ondataavailable = (e) => {
        setVideoChunks([...videoChunks, e.data]);

        if (rec.state === 'inactive') {
          const mimeType = 'video/mp4';
          const videoBlob = new Blob(videoChunks, { type: mimeType });
          const videoURL = URL.createObjectURL(videoBlob);

          const recordedVideo = document.getElementById('recordedVideo');
          recordedVideo.srcObject = null; // Reset srcObject
          recordedVideo.src = videoURL;
          recordedVideo.controls = true;
          recordedVideo.play();
        }
      };

      setVideoRecorder(rec);
    });
  }, [videoChunks]);

  const toggleVideoRecording = () => {
    if (isVideoRecording) {
      setIsVideoRecording(false);
      videoRecorder.stop();
    } else {
      setIsVideoRecording(true);
      setVideoChunks([]);
      videoRecorder.start();
    }
  };

  return (
    <div>
      <button
        id="recordVideo"
        value={isVideoRecording ? 'ON' : 'OFF'}
        onClick={toggleVideoRecording}
        style={{
          borderRadius: '50%',
          maxWidth: '50%',
          maxHeight: '30%',
          backgroundColor: isVideoRecording ? 'blue' : 'red',
        }}
      ></button>
      <video id="recordedVideo"></video>
    </div>
  );
}

export { AudioRecorder, VideoRecorder };
