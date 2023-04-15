import { createApp } from 'vue'
import App from './App.vue'
import store from './store'

// Importing the global css file
import "@/assets/global.css"

createApp(App).use(store).mount('#app')
