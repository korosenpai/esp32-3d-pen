<template>
    <!-- <img alt="Vue logo" src="@/assets/logo.png"> -->
    <PrintData />
    <!-- <ThreejsDemo /> -->
    <Canvas2dDemo />
</template>

<script setup>
import { useStore } from "vuex"

import PrintData from "@/components/PrintData.vue"
import ThreejsDemo from "@/components/GyroDemo.vue"
import Canvas2dDemo from "./components/Canvas2dDemo.vue";


const { SerialPort } = require('serialport')
const { ReadlineParser } = require("@serialport/parser-readline")

const store = useStore()



// TODO check validity of https://stackoverflow.com/questions/66062682/serial-port-with-electron-vue-js

const port = new SerialPort({
    path: "com10",
    baudRate: 115200,
})

const parser = port.pipe(new ReadlineParser({ delimiter: '\n' }))
// port.open()


parser.on("data", data => {
    try {
        data = JSON.parse(data)

        if (data.accel) { store.commit("setAccel", data.accel) }
        if (data.gyro) { store.commit("setGyro", data.gyro) }
        if (data.heading) { store.commit("setMagnHeading", data.heading) }


    } catch (error) {
        // first calibrations, data not yet send via json format
        // TODO check if error is json and if other error raise it
        console.log(data)
    }
})

</script>

<style lang="scss">

</style>
