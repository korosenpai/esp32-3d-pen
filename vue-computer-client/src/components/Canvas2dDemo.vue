<template>
    <canvas id="canvas"></canvas>
</template>

<script setup>

/*

// CANVAS PREP //
identify irl range of canvas -> 1m
irlwidth = 1m
to calculate proportion of height -> height irl meters : canvas height = width irl meters: canvas width
    -> height irl meters = canvas height * width irl meters / canvas width
canvasPosition will be mpu position rappresented on canvas

// CALCULATE DISTANCE MOVED //
to consider this calculation for both axis
IMPORTANT -> MPU IS 90 DEG RELATIVE TO PEN
    -> x axis is imu negative y
    -> y axis is imu x axis

raw data -> unit of measurement of accel: m/(s^2)
time -> get variation from cicle of time before // in seconds
use formula "d = a * t^2" to calculate irl distance moved
calc how much to move on canvas -> width irl meters : canvas width = irl distance moved : canvas distance moved
    -> canvas distance moved X = canvas width * irl distance moved / width irl meters
    -> canvas distance moved y = canvas height * irl distance moved / height irl meters

*/

import { onMounted } from 'vue'
import { computed, watch } from '@vue/runtime-core'
import { useStore } from "vuex"

import { round } from "@/functions/round.js"

const store = useStore()

const irlWidth = 1 // canvas will be range of 1m in width
let irlHeight // will be calculated in init()
let canvasCenter
let canvasPosition = [null, null]

let dt
let time = performance.now()
let distanceIRLTravX
let distanceIRLTravY
let canvasDistanceX
let canvasDistanceY


onMounted(() => {

let accel = computed(() => store.getters.accel)
let initalAccelBias = null

watch(accel, newAccel => {
    if (!initalAccelBias) initalAccelBias = newAccel // must initialize here because store sucks ( in line before catches default store value )

    dt = (performance.now() - time) / 1000 // calculate time passed in second

    distanceIRLTravX = (-newAccel[1] + initalAccelBias[1]) * Math.pow(dt, 2)
    distanceIRLTravY = (-newAccel[0] + initalAccelBias[0]) * Math.pow(dt, 2)

    canvasDistanceX = canvas.width * distanceIRLTravX / irlWidth
    canvasDistanceY = canvas.height * distanceIRLTravY / irlWidth

    canvasPosition[0] += canvasDistanceX
    canvasPosition[1] += canvasDistanceY

    // avoid going out of bounds
    if (canvasPosition[0] < 0) canvasPosition[0] = 0
    if (canvasPosition[0] > canvas.width) canvasPosition[0] = canvas.width
    if (canvasPosition[1] < 0) canvasPosition[1] = 0
    if (canvasPosition[1] > canvas.height) canvasPosition[1] = canvas.height

    context.lineTo(...canvasPosition)
    context.stroke()

    


    time = performance.now()
})

    
let canvas = document.getElementById("canvas")
let context = canvas.getContext("2d")

window.addEventListener('resize', init, false)
init()


// called in resize canvas
function init() {
    canvas.height = window.innerHeight
    canvas.width = window.innerWidth

    irlHeight = canvas.height * irlWidth / canvas.width

    console.log("height", window.innerHeight)
    console.log("width", window.innerWidth)

    canvasCenter = [canvas.width / 2, canvas.height / 2]
    console.log("center", canvasCenter)
    canvasPosition = canvasCenter

    context.beginPath()
    context.lineWidth = 3
    context.strokeStyle = "#f56"
}


})

</script>

<style scoped lang = "scss">
#canvas {
    background-color: burlywood;
    
}
</style>