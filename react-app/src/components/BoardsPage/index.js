import React, { useEffect } from 'react'
import { Redirect, NavLink } from 'react-router-dom'
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";
import { useDispatch, useSelector } from 'react-redux';
import { getAllBoards } from '../../store/boardReducer';
import "./BoardsPage.css"
const BoardsPage = () => {


  const user = useSelector((state) => state.session.user);
  const boards = useSelector((state)=>Object.values(state.boards.boards))
  console.log(boards)
  const dispatch = useDispatch()
  useEffect(()=>{
    dispatch(getAllBoards(user.id))
  },[dispatch, user.id])

  if(!user){
    return <Redirect to="/"/>
  } 
  return (
    <>
      <div className="container boards-page">
        <h1 className="boards-page-title">All your boards </h1>

        <ResponsiveMasonry
          columnsCountBreakPoints={{ 350: 1, 700: 2, 900: 3, 1000: 3 }}
        >
          <Masonry columnsCount={3}>
            {boards.map((item) => (
              <NavLink
                to={`/boards/${item.id}`}
                key={item.id}
                className="board-page-link"
              >
                <img
                  className="boards-images"
                  src={item.board_image_url}
                  alt={item.title}
                />

                <h4>{item.title}</h4>
              </NavLink>
            ))}
          </Masonry>
        </ResponsiveMasonry>
      </div>
    </>
  )
}

export default BoardsPage