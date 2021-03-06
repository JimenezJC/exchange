export default function Reducer(
   state={
      activelisting: {
         id: 0,
      },
      fetching: false,
      fetched: false,
      listings: [],
      error: null,
   }, action) {
   switch (action.type) {
      case "FETCH_LISTINGS_PENDING": {
         return {...state, fetching: true}
         break;
      }
      case "FETCH_LISTINGS_REJECTED":{
         return {...state, fecthing: false, error: action.payload}
         break;
      }
      case "FETCH_LISTINGS_FULFILLED": {
         return {
            ...state,
            fecthing: false,
            fetched: true,
            listings: action.payload,
            }
         break;
      }
      case "FETCH_LISTING_PENDING": {
         return {...state, fetching: true}
         break;
      }
      case "FETCH_LISTING_REJECTED":{
         return {...state, fecthing: false, error: action.payload}
         break;
      }
      case "FETCH_LISTING_FULFILLED": {
         return {
            ...state,
            fecthing: false,
            fetched: true,
            activelisting: action.payload,
            }
         break;
      }
   }
   return state;
};
