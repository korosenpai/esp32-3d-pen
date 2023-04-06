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
        setGyro(state, gyro) {
            state.pitch = gyro[0]
            state.roll = gyro[1]
        },
        setMagnHeading(state, magnHeading) { state.magnHeading = magnHeading },
    },
    
    actions: {
    },
    modules: {
    }
})
