<template>
    <!-- <img alt="Vue logo" src="@/assets/logo.png"> -->
    <ThreejsDemo />
</template>

<script setup>
import ThreejsDemo from "@/components/ThreejsDemoSpin.vue"


const { SerialPort } = require('serialport')
const { ReadlineParser } = require("@serialport/parser-readline")

// TODO check validity of https://stackoverflow.com/questions/66062682/serial-port-with-electron-vue-js

const port = new SerialPort({
    path: "com10",
    baudRate: 115200,
})

const parser = port.pipe(new ReadlineParser({ delimiter: '\n' }))

parser.on("data", data => {
    console.log(data)
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
