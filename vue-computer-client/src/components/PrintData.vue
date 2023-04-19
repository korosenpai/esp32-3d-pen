<template>
    <div id="print-data">
        <span> accel: {{ accel }} </span> <br>
        <span> pitch: {{ pitch }} </span> <br>
        <span> roll: {{ roll }} </span> <br>
        <span> heading: {{ heading }} </span>
    </div>
</template>

<script setup>

import { computed } from '@vue/runtime-core'
import { useStore } from "vuex"

const store = useStore()

let accel = computed(() => store.getters.accel)
let pitch = computed(() => store.getters.pitch)
let roll = computed(() => store.getters.roll)
let heading = computed(() => store.getters.magnHeading)

</script>

<style scoped lang="scss">
#print-data {
    position: absolute; // TODO make it stick to upper part of page -> add to sidebar?
    margin: 2vw;
    padding: 1vw;
    border: solid .5vw white;
    border-radius: 7%;

    span {
        user-select: none;
    }
}
</style>