<template>
    <!-- <img alt="Vue logo" src="@/assets/logo.png"> -->
    
    <PrintData />
    <ThreejsDemo />
</template>

<script setup>
import { useStore } from "vuex"

import PrintData from "@/components/PrintData.vue"
import ThreejsDemo from "@/components/GyroDemo.vue"

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
        store.commit("setGyro", data.gyro)
        store.commit("setMagnHeading", data.heading)


    } catch (error) {
        // first calibrations
        console.log(data)
    }
})

</script>

<style lang="scss">
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    // text-align: center;
    // color: #2c3e50;
    // margin-top: 60px;
    margin: 0;
    padding: 0;
}
</style>
