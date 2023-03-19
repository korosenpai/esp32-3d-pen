import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.121.1/examples/jsm/controls/OrbitControls.js'

let scene
let camera
let renderer
let cube
let orbit


function init() {
    scene = new THREE.Scene()

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    camera.position.z = 5

    renderer = new THREE.WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)

    orbit = new OrbitControls(camera, renderer.domElement)

    document.body.appendChild(renderer.domElement)
    adjustLighting()
    cube = createBasicCube()
    animationLoop()
}

function adjustLighting() {
    let pointLight = new THREE.PointLight(0xdddddd)
    pointLight.position.set(-5, -3, 3)
    scene.add(pointLight)

    let ambientLight = new THREE.AmbientLight(0x505050)
    scene.add(ambientLight)
}

function createBasicCube() {
    let geometry = new THREE.BoxGeometry(2, 1, 1)
    // let material = new THREE.MeshLambertMaterial()

    // TODO https://stackoverflow.com/questions/44828713/paint-cube-faces-as-a-whole-not-the-triangles-that-make-up-the-face-three-js
    // color faces
    for ( var i = 0; i < geometry.faces.length; i += 2 ) {
        var faceColor = Math.random() * 0xffffff;
        geometry.faces[i].color.setHex(faceColor);
        geometry.faces[i+1].color.setHex(faceColor);
    }
    
    var material = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        vertexColors: THREE.FaceColors
    });


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

init()



var ajaxRequest = new XMLHttpRequest();

function ajaxLoad(ajaxURL) {  
    ajaxRequest.open('GET',ajaxURL,true);  
    ajaxRequest.onreadystatechange = function() {  
        if(ajaxRequest.readyState == 4 && ajaxRequest.status==200) {  
            var ajaxResult = JSON.parse(ajaxRequest.responseText);
            cube.rotation.x = Math.round(ajaxResult.roll * Math.PI / 180)
            cube.rotation.z = Math.round(ajaxResult.pitch * Math.PI / 180)
            cube.rotation.y = Math.round(ajaxResult.heading * Math.PI / 180)

            console.log(ajaxResult)
            
        }  
    }
    ajaxRequest.send();
}

function updateValues() {   
    ajaxLoad('getUpdate');
}  
    
setInterval(updateValues, 200);