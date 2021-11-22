import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowAltCircleUp } from '@fortawesome/free-solid-svg-icons'
import './createpin.css'
// import 'bootstrap/dist/css/bootstrap.min.css';



class CreatePin extends React.Component{
    constructor(){
        super()
        this.state={
            data:[],
            sendData:{
                title:'',
                description:'',
                image:'',
                creator:'',
                website:''
        
            },
            url:{}
        }
    }


    
    getData = async()=>{
        let api = await fetch("http://localhost:8000/create/",{
        method: 'GET',
        headers: {'Authorization': 'Token 3814ec2bc54c5e19b316580e81d138c256f90957'}})
          let data = await api.json();
          console.log(data)
          this.setState({
              data:data
          })
      }

      componentDidMount(){
        this.getData();
    };
    

    postData = (file)=>{
        const url = "http://localhost:8000/create/"
        const formdata = new FormData()
        formdata.append('image', file)
        formdata.append('title', this.state.sendData.title)
        formdata.append('description', this.state.sendData.description)
        formdata.append('creator', this.state.data.username)
        formdata.append('website', this.state.data.website)

        

        fetch(url,{
            method:"post",
            headers:{
                'Authorization': 'Token 3814ec2bc54c5e19b316580e81d138c256f90957'
            },
            body:formdata,
        }).catch(console.error)

    }

    uploadImage = (e)=>{
        let inputfile = e.target.files[0]
        
        this.setState({
        url:URL.createObjectURL(inputfile)
    })

    }


    createImage = (e)=>{

        let inputfile = e.target.image.files[0]
        this.setState({
            sendData:{
                title:e.target.title.value,
                description:e.target.description.value,
                image:e.target.image.value,
                creator:this.state.data.username,
                website:e.target.website.value,
            },
            url:URL.createObjectURL(inputfile)
       
        },()=>{ 
            this.postData(inputfile);
    
        })
    }
    render(){
        
            return ( <>
    <div className='container-fluid'>
        <div className='for-container'>
            <div className='row lable'>

                <div className="lable">
                    <div>Create a Pin</div>
                </div>


            </div>

            <form action='http://localhost:3000' onSubmit={this.createImage} >
      
            <div className='row create'>

                <div className="create">
                    <div className="row">
                        <div className="col-md-6 col-sm-12">
                            <div className="card">
                            <input className="media-upload" onChange={(e)=>this.uploadImage(e)} type="file" name='image' />
                            {this.state.url.length > 16 && <img  className="media-back" src={this.state.url} alt="."/>} 
                            
                            {this.state.url == "[object Object]" && <div className="media-back">
                                <div className="media-content">
                                    <div>
                                    <FontAwesomeIcon icon={faArrowAltCircleUp}/>
                                    <p>Click to Upload</p>
                                    </div>
                                    <div className='recommendaion'>
                                        <p>Recommendaion: Use high-quality .jpg</p>
                                        <p>files less than 20MB</p>
                                    </div>
                                </div>
                            </div> }

                            </div>
                        </div>
                        <div className="col-md-6 col-sm-12">
                        
                            <div className="card">
                            <input type="submit" href="#" value='Save' className="btn btn-primary"/>

                            <div className="card-body">
                                <input type='text' name='title' className="card-title" placeholder='Add Your Title'/>
                                <div className='user'>
                                    <img className='avatar' src={`http://localhost:8000${this.state.data.avatar}`}/>
                                    <p className='name'>{this.state.data.username}</p>
                                </div> 
                                <input type='text' name='description' className="card-text" placeholder='Tell everyone what your Pin is about'/>
                            </div>
                            </div>
                            <input type='text'  name='website' className="website" placeholder='Add a destination link'/>

                        </div>
                        </div>
                    </div>
                   
            </div>
            </form>
            
        </div>
        
    </div> 
    
    </> );
    }

    
}
export default CreatePin;






