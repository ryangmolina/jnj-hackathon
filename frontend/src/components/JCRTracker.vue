<template>
  <div>
    <h1>Job Change Request</h1>
    <div v-if="!jobChangeRequest" class="progress-text">
      <h4>Create job change request</h4>
      We will guide you to your job request journey. Click 'start' if you  want to procees.
      <div class="mt-5">
        <button class="btn btn-outline-danger" @click="putData">Start</button>
      </div>
    </div>
    <transition v-else name="fade">
    <ul class="progress-tracker progress-tracker--vertical ml-5">
      <li class="progress-step is-complete">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Start</h4>
        </div>
      </li>
      <li class="progress-step" :class="{'is-active': status === 'submission', 'is-complete': isSubmissionDone}">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Employee ID and location.</h4>
          <div v-if="status === 'submission'">   
            <div class="form-group">
              <label for="lastName">Location</label>
              <select class="form-control" id="civilStatus" :readonly="isSubmitted" v-model="country">
                <option value="PHILIPPINES">Philippines</option>
                <option value="SINGAPORE">Singapore</option>
              </select>
            </div>
            <div v-if="country === 'PHILIPPINES'">
              <div class="form-group">
                <label for="lastName">Employee ID</label>
                <input type="text" class="form-control" id="lastName" placeholder="Employeed ID" :readonly="isSubmitted">
              </div>

              <div class="form-group">
                <label for="lastName">Current Position</label>
                <input type="text" class="form-control" id="lastName" placeholder="Current Position" :readonly="isSubmitted">
              </div>

              <div class="form-group">
                <label for="lastName">Proposed Position</label>
                <input type="text" class="form-control" id="lastName" placeholder="Proposed Position" :readonly="isSubmitted">
              </div>

              <div class="form-group">
                <label for="lastName">Is Compensation Changing</label>
                <select class="form-control" id="civilStatus" :readonly="isSubmitted">
                  <option value="PHILIPPINES">Yes</option>
                  <option value="SINGAPORE">No</option>
                </select>
              </div>

              <div class="form-group">
                <label for="lastName">Is exact amount</label>
                <select class="form-control" id="civilStatus" v-model="isExact" :readonly="isSubmitted">
                  <option :value="true">Yes</option>
                  <option :value="false">No</option>
                </select>
              </div>

              <div v-if="!isExact" class="form-group">
                <label for="lastName">% Increase</label>
                <input type="text" class="form-control" id="lastName" placeholder="% Increase" :readonly="isSubmitted">
              </div>

              <div v-else class="form-group">
                <label for="lastName">Amount</label>
                <input type="text" class="form-control" id="lastName" placeholder="Amount" :readonly="isSubmitted">
              </div>
            </div>
            <button v-if="status === 'submission'" class="btn btn-outline-danger mt-2" @click="setStatus('hr-check')">Submit to HR</button>
          </div>
        </div>
      </li>
      <li class="progress-step" :class="{'is-active': status === 'hr-check', 'is-complete': isHRChecked}">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">For HR Review</h4>
        </div>
      </li>
      <li class="progress-step" :class="{'is-active': status === 'manager-check', 'is-complete': isManagerChecked}">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Manager’s Final Approval</h4>
          <div v-if="status ==='manager-check'">
            <img class="img-fluid mb-2" src="/assets/images/document.png" />
          </div>
          <button v-if="status === 'manager-check'" class="btn btn-outline-danger mt-2" @click="setStatus('completed')">Approve</button>
          <button v-if="status === 'manager-check'" class="btn btn-outline-primary mt-2" @click="setStatus('completed')">Edit</button>
        </div>
      </li>
      <li class="progress-step" :class="{'is-active': status === 'completed', 'is-complete': isDone}">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Job Change Request Completed</h4>
        </div>
      </li>
    </ul>
    </transition>
  </div>
</template>

<script>
export default {
  data () {
    return {
      jobChangeRequest: null,
      isExact: false,
      status: '',
      isSubmitted: false,
      isSubmissionDone: false,
      isHRChecked: false,
      isManagerChecked: false,
      isDone: false,
      country: null
    }
  },
  methods: {
    putData () {
      this.jobChangeRequest = {
        status: 'created'
      }
      this.setStatus('submission')
    },
    setStatus (status) {
      this.status = status
      if (status === 'submission') {
        this.isSubmissionDone = true
      } else if (status === 'hr-check') {
        this.isHRChecked = true
        this.setStatus('manager-check')
      } else if (status === 'manager-check') {
        this.isManagerChecked = true
      } else if (status === 'completed') {
        this.isDone = true
      }
    }
  }
}
</script>
<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity .5s
 }

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>