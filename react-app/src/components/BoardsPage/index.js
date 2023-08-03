import React from 'react'
import { Redirect } from 'react-router-dom'
import { useSelector } from 'react-redux';
const BoardsPage = () => {


  const user = useSelector((state) => state.session.user);

  if(!user){
    return <Redirect to="/"/>
  } 
  return (
    <div>index</div>
  )
}

export default BoardsPage