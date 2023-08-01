import React, {useEffect} from 'react'
import "./BoardDetailsPage.css"
import { useDispatch, useSelector } from 'react-redux'
import { getBoardById } from '../../store/boardReducer'
import { useParams, Link } from 'react-router-dom'

const BoardDetailsPage = () => {
const dispatch = useDispatch()
const {id}= useParams()
const board = useSelector(state=>state.boards.board)
const user = useSelector(state=>state.session.user)
console.log(user,33333)

useEffect(()=>{
    dispatch(getBoardById(id))
},[dispatch, id])

  return (
    <main className='main'>
        <div className='container'>
            <h2>{board.title}</h2>
            <img src={board.board_image_url} alt={board.title}/>
            <section >
                <img src={user.user_image} alt={user.username}/>
                <h3>{user.first_name} {user.last_name}</h3>
                <p>{user.email}</p>
                <button>
                    Edit Profile
                </button>

                <button>
                    Delete Profile
                </button>

            </section>
            <section>
                <ul>
                   {board?.pins.map(item=>(
                    <li>
                        <Link to={`/pins/${item.id}`}>
                        <img src={item.images} alt={item.title}/>
                        </Link>
                        
                    </li>
                   ))} 
                </ul>
            
            </section>
        </div>

    </main>
  )
}

export default BoardDetailsPage