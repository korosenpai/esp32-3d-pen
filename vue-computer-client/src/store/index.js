import { createStore } from 'vuex'

export default createStore({
    state: {
        accel: [0, 0, 0],
        pitch: 0,
        roll: 0,
        magnHeading: 0,
    },

    getters: {
        accel(state) { return state.accel },
        pitch(state) { return state.pitch },
        roll(state) { return state.roll },
        magnHeading(state) { return state.magnHeading },
    },

    mutations: {
        setAccel(state, accel) { state.accel = accel },
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
