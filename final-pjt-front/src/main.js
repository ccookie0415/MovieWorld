import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faBell } from "@fortawesome/free-regular-svg-icons";
import { faBell as faBellSolid } from "@fortawesome/free-solid-svg-icons";
import { faHouse } from "@fortawesome/free-solid-svg-icons";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import { faXmark } from "@fortawesome/free-solid-svg-icons";
import { faPen } from "@fortawesome/free-solid-svg-icons";
import { faClapperboard } from "@fortawesome/free-solid-svg-icons";
import { faHeart } from "@fortawesome/free-solid-svg-icons";
import { faChevronLeft } from "@fortawesome/free-solid-svg-icons";
import { faChevronRight } from "@fortawesome/free-solid-svg-icons";
import { faEllipsisVertical } from "@fortawesome/free-solid-svg-icons";
import { faAnglesLeft } from "@fortawesome/free-solid-svg-icons";
import { faImage } from "@fortawesome/free-solid-svg-icons";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { faChevronUp } from "@fortawesome/free-solid-svg-icons";
import { faHeart as faHeartNone } from "@fortawesome/free-regular-svg-icons";
import 'animate.css';
import Popover from 'vue-js-popover'
import VPopover from 'vue-js-popover'


import Paginate from 'vuejs-paginate'
Vue.component('paginate', Paginate)


Vue.use(BootstrapVue)
Vue.use(Popover)
Vue.use(VPopover, { tooltip: true })
Vue.component('font-awesome-icon', FontAwesomeIcon)
library.add(faBell)
library.add(faBellSolid)
library.add(faHouse)
library.add(faBars)
library.add(faXmark)
library.add(faPen)
library.add(faClapperboard)
library.add(faHeart)
library.add(faChevronLeft)
library.add(faChevronRight)
library.add(faHeartNone)
library.add(faEllipsisVertical)
library.add(faAnglesLeft)
library.add(faImage)
library.add(faMagnifyingGlass)
library.add(faChevronUp)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
