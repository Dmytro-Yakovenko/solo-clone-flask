import { getBoardById } from "./boardReducer";

// constants
const GET_PINS = "pin/GET_PINS";
const ADD_PIN = "pin/ADD_PIN";
const UPDATE_PIN = "pin/UPDATE_PIN";
const REMOVE_PIN = "pin/REMOVE_PIN";
const GET_ONE_PIN = "pin/GET_ONE_PIN";

//actions

const getPins = (pins) => ({
  type: GET_PINS,
  payload: pins,
});

const getOnePin = (pin) => ({
  type: GET_ONE_PIN,
  payload: pin,
});

const addPin = (pin) => ({
  type: ADD_PIN,
  payload: pin,
});

const updatePin = (pin) => ({
  type: UPDATE_PIN,
  payload: pin,
});

const removePin = (id) => ({
  type: REMOVE_PIN,
  payload: id,
});

export const getAllPins = () => async (dispatch) => {
  const response = await fetch(`/api/pins/search?is_saved=False`);

  if (response.ok) {
    const data = await response.json();

    if (data.errors) {
      return;
    }

    dispatch(getPins(data));
  }
};

export const getPinById = (id) => async (dispatch) => {
  const response = await fetch(`/api/pins/${id}`);

  if (response.ok) {
    const data = await response.json();
    dispatch(getOnePin(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

export const createPin = (pin, boardId) => async (dispatch) => {
  const response = await fetch(`/api/boards/${boardId}/pins`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(pin),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addPin(data));
    dispatch(getBoardById(boardId))
    return data.id
  }
};

export const editPin = (pin, id) => async (dispatch) => {
  const response = await fetch(`/api/pins/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(pin),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(getOnePin(data))
    dispatch(updatePin(data));
  }
};

export const deletePin = (id) => async (dispatch) => {
  const response = await fetch(`/api/pins/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    dispatch(removePin(id));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

const initialState = { pins: {}, pin: {} };

export default function pinsReducer(state = initialState, { type, payload }) {
  switch (type) {
    case GET_PINS:
      const pins = payload.pins.reduce((acc, curr) => {
        acc[curr.id] = curr;
        return acc;
      }, {});
      return { ...state, pins };
    case GET_ONE_PIN:
    
      return { ...state, pin:payload };
    case ADD_PIN:
      const created = { ...state };
      created.pins[payload.id] = payload;
      return created;
    case UPDATE_PIN:
      const updated = { ...state };
      updated.pins[payload.id] = payload;
      return updated;

    case REMOVE_PIN:
      
      const removedState = { ...state };
      delete removedState.pins[payload];
      
      return removedState;
    default:
      return state;
  }
}
