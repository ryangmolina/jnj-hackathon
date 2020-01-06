<template>
  <div>
    <h1>Certificate of Employment Request</h1>
    <div v-if="!jobChangeRequest" class="progress-text">
      <h4>Create request</h4>
      Click 'start' if you want to procees.
      <div class="mt-5">
        <button class="btn btn-outline-danger" @click="putData">Start</button>
      </div>
    </div>
    <transition v-else name="fade" class="row">
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
              <select class="form-control" id="civilStatus" v-model="country">
                <option value="PHILIPPINES">Philippines</option>
                <option value="SINGAPORE">Singapore</option>
              </select>
            </div>
            <div v-if="country === 'PHILIPPINES'">
              <div class="form-group">
                <label for="lastName">Employee ID</label>
                <input type="text" class="form-control" id="lastName" placeholder="Employeed ID" value="1923123" readonly>
              </div>

              <div class="form-group">
                <label for="lastName">Type of Letter Request</label>
                <select class="form-control" id="civilStatus">
                  <option value="PHILIPPINES">Employment Verification</option>
                  <option value="PHILIPPINES">Business Visa</option>
                  <option value="PHILIPPINES">Business Visa + Employee Verification</option>
                  <option value="PHILIPPINES">Personal Visa</option>
                </select>
              </div>

              <div class="form-group">
                <label for="lastName">Purpose of Request</label>

                <input type="text" class="form-control" id="lastName" placeholder="Purpose">
              </div>

              <div class="form-group">
                <label for="lastName">Compensation Information</label>
                <select class="form-control" id="civilStatus">
                  <option>Not Required</option>
                  <option>Monthly Basic Only</option>
                  <option>Annual Basic Only</option>
                  <option>Monthly Basic Only + Allowance</option>
                  <option>Annual Basic Only + Allowance</option>
                </select>
              </div>

              <div class="form-group">
                <div class="form-check">
                  <input type="checkbox" class="form-check-input" id="exampleCheck1" v-model="addressToSomeone">
                  <label class="form-check-label" for="exampleCheck1">Address to someone</label>
                </div>
              </div>

              <div v-if="addressToSomeone" class="form-group" style="width: 285px;">
                <p class="text-muted text-small">Please indicate in the box provided below to whom/where the letter should be addressed.</p>
                <textarea style="width: 285px;" class="form-control" />
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
          <h4 class="progress-title">Your Certificate of Employment</h4>
          <div v-if="status ==='manager-check'">
            <img class="img-fluid mb-2" src="/assets/images/coe.png" />
          </div>
          <button v-if="status === 'manager-check'" class="btn btn-outline-danger mt-2" @click="setStatus('completed')">Approve</button>
          <button v-if="status === 'manager-check'" class="btn btn-outline-primary mt-2" @click="setStatus('completed')">Edit</button>
        </div>
      </li>
      <li class="progress-step" :class="{'is-active': status === 'completed', 'is-complete': isDone}">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Download Certificate of Employment</h4>
          <a v-if="status === 'completed'" href="#" class="btn btn-link">Certificate_of_Employment-Moline.pdf</a>
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
      country: null,
      addressToSomeone: false
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