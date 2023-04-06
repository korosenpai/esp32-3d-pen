import { createStore } from 'vuex'

export default createStore({
    state: {
        pitch: null,
        roll: null,
        magnHeading: null,
    },

    getters: {
        pitch(state) { return state.pitch },
        roll(state) { return state.roll },
        magnHeading(state) { return state.magnHeading },
    },

    mutations: {
        setPitch(state, pitch) { state.pitch = pitch },
        setRoll(state, roll) { state.roll = roll },
        setPMagnHeading(state, magnHeading) { state.magnHeading = magnHeading },
    },
    
    actions: {
    },
    modules: {
    }
})
