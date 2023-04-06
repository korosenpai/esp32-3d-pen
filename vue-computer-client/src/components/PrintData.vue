<template>
    <span> pitch: {{ pitch }} </span> <br>
    <span> roll: {{ roll }} </span> <br>
    <span> heading: {{ heading }} </span>
</template>

<script setup>

import { computed } from '@vue/runtime-core'
import { useStore } from "vuex"

const store = useStore()

let pitch = computed(() => store.getters.pitch)
let roll = computed(() => store.getters.roll)
let heading = computed(() => store.getters.magnHeading)

</script>

<style scoped lang="scss">
span {
    color: white;
    user-select: none;
}
</style>