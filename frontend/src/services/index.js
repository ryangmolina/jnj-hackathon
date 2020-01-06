import Vue from 'vue'

import JobChangeRequest from './JobChangeRequest.vue'
import CertificateOfEmploymentRequest from './CertificateOfEmploymentRequest.vue'

new Vue({
  el: '#page-job-change-request',
  render: h => h(JobChangeRequest)
})

new Vue({
  el: '#page-certificate-of-employment-request',
  render: h => h(CertificateOfEmploymentRequest)
})