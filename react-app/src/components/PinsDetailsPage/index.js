import React, { useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getPinById } from '../../store/pinReducer';
import "./PinsDetailsPage.css"
const PinsDetailsPage = () => {
    const dispatch=useDispatch()
    const {id}=useParams()
    const pin = useSelector(state=>state.pins.pin)
    const user = useSelector(state=>state.user)
    console.log(pin)
    useEffect(()=>{

    dispatch(getPinById(id))   
    },[dispatch, id])
  return (
    <>
   
    <div className='container pins-details-page'>
        <img className='image-page-details' src={pin.images} alt={pin.title} />
<div>
    <h2 className='title-pins-details-page'>{pin.title}</h2>
    <p className='title-pins-details-page'> Cooking time: {pin.time}</p>
   
    <ol className='pins-details-page-order-list'>
        {
            pin?.description?.split(".").map((item,index)=>(<li className= 'pins-details-page-text' key={index}>{item} </li>))
        }
    </ol>

   
    <div className='user-pins-details-page'>
      <img  className='user-image-pins-details' src={pin?.user?.user_image} alt={pin?.user?.usarname}/>  
      <p>
        {pin?.user?.first_name} {pin?.user?.last_name}
      </p>

    </div>

    <h6>Ingredients</h6>
    <ul>
        {
            pin?.ingredients?.split(".").map((item,index)=>(<li key={index}>{item} </li>))
        }
    </ul>

</div>
    </div>
    
    </>
   
  )
}

export default PinsDetailsPage