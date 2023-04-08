<template>
    <div id="container"></div>
</template>

<script setup>
import * as THREE from 'three'
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls"
import { OBJLoader } from "three/examples/jsm/loaders/OBJLoader"
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader"

// https://discourse.threejs.org/t/loading-gltf-models-in-nuxt-js-vue-js/8326/10

import { onMounted } from 'vue'
import { computed, watch } from '@vue/runtime-core'
import { useStore } from "vuex"

import { round } from "@/functions/round.js"

const store = useStore()


onMounted(() => {

let scene
let camera
let renderer
let object
let orbit

// update object orientation
let pitch = computed(() => store.getters.pitch)
watch(pitch, newPitch => object.rotation.z = round(newPitch * Math.PI / 180, 1))
let roll = computed(() => store.getters.roll)
watch(roll, newRoll => object.rotation.x = round(newRoll * Math.PI / 180, 1))
let heading = computed(() => store.getters.magnHeading)
watch(heading, newHeading => object.rotation.y = round(newHeading * Math.PI / 180, 1))


function init() {
    let container = document.getElementById( "container" )

    scene = new THREE.Scene()

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    camera.position.z = 5

    renderer = new THREE.WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)

    orbit = new OrbitControls(camera, renderer.domElement)

    container.appendChild(renderer.domElement)

    adjustLighting()

    // loadOBJModel(new URL('@/assets/3d-models/esp32.obj', import.meta.url).href)
    // loadGLTFModel(new URL('@/assets/3d-models/mpu6050/scene.gltf', import.meta.url).href)

    
    object = createBasicRect()
    animationLoop()
}

function adjustLighting() {
    // illuminate from one point
    let pointLight = new THREE.PointLight(0xdddddd)
    pointLight.position.set(-5, -3, 3)
    scene.add(pointLight)

    let ambientLight = new THREE.AmbientLight(0x505050)
    scene.add(ambientLight)

    // illuminate everywhere
    // const ambientLight = new THREE.AmbientLight('white', 2);

    // const mainLight = new THREE.DirectionalLight('white', 5);
    // mainLight.position.set(10, 10, 10);
    // scene.add(ambientLight, mainLight);
}

function createBasicRect() {
    let geometry = new THREE.BoxGeometry(2, .5, 1)
    let material = new THREE.MeshLambertMaterial()

    

    let mesh = new THREE.Mesh(geometry, material)
    // mesh.position.x = -2
    scene.add(mesh)
    return mesh
}

function animationLoop() {
    renderer.render(scene, camera)

    orbit.update() // rotate with mouse

    requestAnimationFrame(animationLoop)
}

function loadOBJModel(objPath) {
    new OBJLoader().load(
        // resource URL
        objPath,

        // called when resource is loaded
        object => {
            // object.geometry.scale( .5, .5, .5 )
            scene.add( object )
        },

        // called when loading is in progresses
        xhr => console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' ),
        
        // called when loading has errors
        error => console.log(`could not load model: '${objPath}'`)
    )

}

function loadGLTFModel(objPath) {
    new GLTFLoader().load(
        objPath,
        gltfScene => {
            scene.add(gltfScene.scene)
        }
    )
}

init()


window.addEventListener( 'resize', onWindowResize, false );
function onWindowResize(){
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
}


})

</script>

<style scoped lang="scss">
#container {
    background-color: aquamarine;
    width: 100vw;
    height: 100vh;
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    z-index: -9999;
}
</style>