const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true
})

// serialport -> https://stackoverflow.com/questions/66062682/serial-port-with-electron-vue-js
module.exports = {
    pluginOptions: {
        electronBuilder: {
            externals: ["serialport"],
            customFileProtocol: './',
            nodeIntegration: true
        }
    }
}
