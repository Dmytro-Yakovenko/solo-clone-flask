// constants
const GET_BOARDS = "board/GET_BOARDS";
const ADD_BOARD = "board/ADD_BOARD";
const UPDATE_BOARD = "board/UPDATE_BOARD"
const REMOVE_BOARD = "board/REMOVE_BOARD";
const GET_ONE_BOARD ="board/GET_ONE_BOARD"

//actions

const getBoards = (boards)=>({
    type:GET_BOARDS,
    payload:boards
});

const addBoard =(board)=>({
    type:ADD_BOARD,
    payload:board
})

const getOneBoard = (board)=>({
    type:GET_ONE_BOARD,
    payload:board
});

const updateBoard=(board)=>({
    type:UPDATE_BOARD,
    payload:board
});

const removeBoard = (id)=>({
    type: REMOVE_BOARD,
    payload:id

})


export const getAllBoards=()=>async (dispatch)=>{
    const response = await fetch("api/boards/")
    if(response.ok){
        const data = await response.json();
         
        if(data.errors){
            return
        }
        dispatch(getBoards(data))
    }
}


export const getBoardById=(id)=>async(dispatch)=>{
    const response = await fetch(`/api/boards/${id}`)

    if(response.ok){
        const data =await response.json()
        dispatch(getOneBoard(data))
        return null
    }else if(response.status<500){
        const data = await response.json()
        if(data.errors){
            return data.errors
        }else {
            return ["An error occurred. Please try again."];
          }
    }
}

export const createBoard=(board)=>async(dispatch)=>{
    const response = await fetch("/api/boards/", {
        method:"POST",
        headers:{
            "Content-Type": "application/json",
        },
        body:JSON.stringify(board)
    })

    if(response.ok){
        const data = await response.json();
        dispatch(addBoard(data))
    }
};

export const editBoard =(board, id)=>async(dispatch)=>{
    const response = await fetch(`/api/boards/${id}`,{
        method:"PUT",
        headers: {
            "Content-Type": "application/json",
          },
          body:JSON.stringify(board)

    });

    if(response.ok){
        const data = await response.json();
        dispatch(updateBoard(data))
    }
}


export const deleteBoard = (id)=> async (dispatch)=>{
const response = await fetch (`/api/boards/${id}`,{
    method:"DELETE",
    headers:{
        "Content-Type": "application/json",
    }
});

if (response.ok){
    dispatch(removeBoard(id))
    return null
}else if(response.status<500){
    const data = await response.json();
    if(data.errors){
        return data.errors
    }
}else{
    return ["An error occurred. Please try again."];
}

}


const initialState ={boards:{}, board:{}};

export default function boardsReducer(state= initialState, {type, payload}){
    switch(type){
        case GET_BOARDS:
            const boards= payload.boards.reduce((acc,curr)=>{
                acc[curr.id]=curr;
                return acc
            },{});
            return {...state, boards}
        case GET_ONE_BOARD:
            const board = {}
           
            board[payload.id]=payload;
           
            return {...state, board}
        case ADD_BOARD:
            const created ={...state};
            
            created.boards[payload.id]=payload
            return created  
        case UPDATE_BOARD:
            const updated ={...state};
            updated.boards[payload.id]=payload;
            return updated    
        case REMOVE_BOARD:
            const removedState={...state};
            delete removedState.boards[payload]
            return removedState
        default:
            return state          
    }
}



