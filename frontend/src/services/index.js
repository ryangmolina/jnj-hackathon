import Vue from 'vue'

import Services from './Services.vue'
import JobChangeRequest from './JobChangeRequest.vue'

new Vue({
  el: '#page-services',
  render: h => h(Services)
})


new Vue({
  el: '#page-job-change-request',
  render: h => h(JobChangeRequest)
})