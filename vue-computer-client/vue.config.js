const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  pluginOptions: {
    electronBuilder: {
      customFileProtocol: './',
      nodeIntegration: true
    }
  }
}
