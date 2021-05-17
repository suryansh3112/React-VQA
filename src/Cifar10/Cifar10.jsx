import React, {useState} from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import Alert from 'react-bootstrap/Alert';
import './cifar10.css'

function Cifar10() {

  const [img, setImage] = useState(null)
  const [prediction, setPrediction] = useState("")
  const [preview, setPreview] = useState(null)

  const pred_cifar10 = async()=>{
    let formData = new FormData();
        const config = {
            header: { 'content-type': 'multipart/form-data' }
        }
        formData.append("file", img)
        //save the Image we chose inside the Node Server 

        
        try {
            const response = await axios.post('http://127.0.0.1:5000/cifar10', formData, config)
            setPrediction(response.data.prediction)
        }catch(error){
          console.log(error.message);
        }
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
      <h1>Cifar 10</h1>
     
        { preview ? 
          <img src={preview} className='preview-img' height='300' width='400' />
          :
          <div className="default-img">
            <p>+</p>
          </div>  
        }
        <input type='file' onChange={handleImgChange} className='file-input'/>
        
        <Button style={{marginBottom:'1rem'}} variant="success" size="lg" onClick={pred_cifar10} >
          Predict
        </Button>
        {/* <button onClick={reset}>Reset</button> */}
        {prediction && 
            <Alert variant="primary">
              Prediction: <b>{prediction}</b>
            </Alert>
        }
      
    </section>
  )
}

export default Cifar10
