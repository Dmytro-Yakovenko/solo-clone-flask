//constants

import { getPinById } from "./pinReducer";

const GET_COMMENTS = "comment/GET_COMMENTS";
const ADD_COMMENT = "comment/ADD_COMMENT";
const UPDATE_COMMENT = "comments/UPDATE_COMMENT";
const REMOVE_COMMENT = "comments/REMOVE_COMMENT";
const GET_ONE_COMMENT = "comments/GET_ONE_COMMENT";

//actions

const getComments = (comments) => ({
  type: GET_COMMENTS,
  payload: comments,
});

const GetOneComment = (comment) => ({
  type: GET_ONE_COMMENT,
  payload: comment,
});

const addComment = (comment) => ({
  type: ADD_COMMENT,
  payload: comment,
});

const updateComment = (comment) => ({
  type: UPDATE_COMMENT,
  payload: comment,
});

const removeComment = (id) => ({
  type: REMOVE_COMMENT,
  payload: id,
});

export const getAllComments = () => async (dispatch) => {
  const response = await fetch("/api/comments/");
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(getComments(data));
  }
};

export const getCommentById = (id) => async (dispatch) => {
  const response = await fetch(`/api/pins/${id}/comments`);
  if (response.ok) {
    const data = await response.json();

    if (data.errors) {
      return;
    }
    dispatch(GetOneComment(data));
  }
};


export const createComment = (comment, id)=>async(dispatch)=>{
    const response = await fetch(`/api/pins/${id}/comments`,{
        method:"POST", 
        headers:{
            "Content-Type": "application/json",
        },
        body:JSON.stringify(comment)
    })

    if(response.ok){
        const data = await response.json()
        dispatch(addComment(data))
        dispatch(getPinById(id))
        
    }
}


export  const editComment=(comment)=> async (dispatch)=>{
    const response = await fetch(`/api/pins/${comment.pin_id}/comments/${comment.id}`, {
        method:"PUT",
        headers:{
            "Content-Type": "application/json",
        },
        body:JSON.stringify(comment)
    })
    if(response.ok){
        const data = await response.json()
        dispatch(updateComment(data))
    }

}


export const deleteComment = (comment_id, pin_id)=> async(dispatch)=>{
    const response = await fetch(`/api/pins/${pin_id}/comments/${comment_id}`,{
        method:"DELETE",
        headers:{
            "Content-Type": "application/json",
        }
    })

    if(response.ok){
        dispatch(removeComment())
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


const initialState ={comments:{}, comment_for_pin:{}};

export default function commentReducer(state = initialState, {type, payload}){
    switch(type){
        case GET_COMMENTS:
            const comments= payload.comments.reduce((acc,curr)=>{
                acc[curr.id]= curr
                return acc
            },{})
            return{...state, comments}
        case GET_ONE_COMMENT:
            const comment = payload.comments.reduce((acc,curr)=>{
                acc[curr.id]= curr
                return acc
            },{})
            return {...state, comment_for_pin:comment}
        case ADD_COMMENT:
            const created ={...state};
            created.comments[payload.id]=payload
            return created
        case UPDATE_COMMENT:
            const updated = {...state};
            updated.comments[payload.id]=payload
            return updated
        case REMOVE_COMMENT:
            const removedState = {...state}
            delete removedState.comments[payload]
            return removedState
        default:
            return state                
    }

}