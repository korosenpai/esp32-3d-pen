<template>
    <div id="container"></div>
</template>

<script setup>
import * as THREE from 'three'
import { onMounted } from 'vue';

let scene
let camera
let renderer
let sceneObjects = []

onMounted(() => {

function init() {
    let container = document.getElementById( "container" )

    scene = new THREE.Scene()

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    camera.position.z = 5

    renderer = new THREE.WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)

    container.appendChild(renderer.domElement)
    adjustLighting()
    addBasicCube()
    animationLoop()
}

function adjustLighting() {
    let pointLight = new THREE.PointLight(0xdddddd)
    pointLight.position.set(-5, -3, 3)
    scene.add(pointLight)

    let ambientLight = new THREE.AmbientLight(0x505050)
    scene.add(ambientLight)
}

function addBasicCube() {
    let geometry = new THREE.BoxGeometry(1, 1, 1)
    let material = new THREE.MeshLambertMaterial()  

    let mesh = new THREE.Mesh(geometry, material)
    // mesh.position.x = -2
    scene.add(mesh)
    sceneObjects.push(mesh)
}

function animationLoop() {
    renderer.render(scene, camera)

    for(let object of sceneObjects) {
        object.rotation.x += 0.01
        object.rotation.y += 0.03
        // object.rotation.z += 0.03
    }

    requestAnimationFrame(animationLoop)
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
    // z-index: -9999;
}
</style>