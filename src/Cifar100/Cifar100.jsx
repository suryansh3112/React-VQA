import React, {useState} from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import Alert from 'react-bootstrap/Alert';
// import './cifar10.css'
import spk from '../speaker.png'


var msg = new SpeechSynthesisUtterance();


function Cifar100() {

  const [img, setImage] = useState(null)
  const [prediction, setPrediction] = useState("")
  const [preview, setPreview] = useState(null)
  const [predicting, setPredicting] = useState(false)


  const pred_cifar100 = async()=>{
    setPredicting(true)
    let formData = new FormData();
        const config = {
            header: { 'content-type': 'multipart/form-data' }
        }
        formData.append("file", img)
        //save the Image we chose inside the Node Server 

        
        try {
            const response = await axios.post('http://127.0.0.1:5000/cifar100', formData, config)
            setPrediction(response.data.prediction)
            msg.text = response.data.prediction;
            window.speechSynthesis.speak(msg);

        }catch(error){
          console.log(error.message);
        }
        setPredicting(false)
  }

  const reset = ()=>{
    setPrediction("")
    setImage(null)
  }

  const handleImgChange = e =>{
    setPrediction("")
    setImage(e.target.files[0])
    setPreview(URL.createObjectURL(e.target.files[0]))
  }

  return (
    <section className='root'>
      <h1>Cifar 100</h1>
     
        { preview ? 
          <img src={preview} className='preview-img' height='300' width='400' />
          :
          <div className="default-img">
            <p>+</p>
          </div>  
        }
        <input type='file' onChange={handleImgChange} className='file-input'/>
        
        {
          predicting ? 
          <Button style={{marginBottom:'1rem'}} variant="success" size="lg" disable >
            Predicting...
          </Button>
          : 
          <Button style={{marginBottom:'1rem'}} variant="success" size="lg" onClick={pred_cifar100} >
            Predict
          </Button>
        }
        
        {prediction && <div style={{display:"flex"}}>
            <Alert variant="primary">
              Prediction: <b>{prediction}</b>
            </Alert>
            <Button variant="light" style={{height:"3rem",marginLeft:"10px"}} onClick={()=>{msg.text=prediction; window.speechSynthesis.speak(msg)}}>
              <img src={spk} width='20' height='20'/>
            </Button>
          </div>
        }
      
    </section>
  )
}

export default Cifar100
