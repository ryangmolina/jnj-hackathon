<template>
  <!-- <div class="card" v-if="accordionItemId === 'default-item'">
    <div class="card-header bg-white" :id="headerId">
      <div class="align-middle" data-toggle="collapse" :data-target="`#${accordionItemId}`" aria-expanded="true" :aria-controls="accordionItemId">
        <div class="d-flex align-items-center p-1">
          How to update employee data?
          <i class="fa ml-auto" :class="{'fa-chevron-up': isOpen, 'fa-chevron-down': !isOpen}" aria-hidden="true"></i>
        </div>
      </div>
    </div>

    <div :ref="accordionItemId" :id="accordionItemId" class="collapse" :aria-labelledby="headerId" :data-parent="`#${accordionId}`">

    </div>
  </div>
  <div class="card" v-else-if="accordionItemId === 'jcr-item'">
    <div class="card-header bg-white" :id="headerId">
      <div class="align-middle" data-toggle="collapse" :data-target="`#${accordionItemId}`" aria-expanded="true" :aria-controls="accordionItemId">
        <div class="d-flex align-items-center p-1">
          Job Change Request
          <i class="fa ml-auto" :class="{'fa-chevron-up': isOpen, 'fa-chevron-down': !isOpen}" aria-hidden="true"></i>
        </div>
      </div>
    </div>

    <div :ref="accordionItemId" :id="accordionItemId" class="collapse" :aria-labelledby="headerId" :data-parent="`#${accordionId}`">
      <div class="card-body bg-light">
      <div class="card-body bg-light">
      </div>
      </div>
    </div>
  </div> -->
  <div class="card">
    <div class="card-header bg-white" :id="headerId">
      <div class="align-middle" data-toggle="collapse" :data-target="`#${accordionItemId}`" aria-expanded="true" :aria-controls="accordionItemId">
        <div class="d-flex align-items-center p-1">
          {{ item.title }}
          <i class="fa ml-auto" :class="{'fa-chevron-up': isOpen, 'fa-chevron-down': !isOpen}" aria-hidden="true"></i>
        </div>
      </div>
    </div>

    <div :ref="accordionItemId" :id="accordionItemId" class="collapse" :aria-labelledby="headerId" :data-parent="`#${accordionId}`">
      <div v-if="item.title === 'How to update employee data?'" class="card-body bg-light">
        Click this link to edit your employee data <a :href="profileUrl">Profile page</a>.
        You might be asked by HR for additional information.
      </div>
      <div v-else-if="item.title === 'Job Change Request'" class="card-body bg-light">
        Click this link to create a <a :href="jcrUrl">Job Change Request</a>.
      </div>
      <div v-else-if="item.title === 'How to get COE?'" class="card-body bg-light">
        Click this link to create a <a :href="coeUrl">Certificate of Employment Request</a>.
      </div>
      <div v-else class="card-body bg-light">
        {{ item.text }}
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: [
    'accordionId',
    'accordionItemId',
    'headerId',
    'item'
  ],
  created () {
    this.profileUrl = window.Urls['accounts:index']()
    this.jcrUrl = window.Urls['services:job_change_request']()
    this.coeUrl = window.Urls['services:certificate_of_employment_request']()
  },
  mounted () {
    this.observer = new MutationObserver(mutations => {
      for (const m of mutations) {
        const newValue = m.target.getAttribute(m.attributeName)
        this.$nextTick(() => {
          this.onClassChange(newValue, m.oldValue)
        })
      }
    })

    this.observer.observe(this.$refs[this.accordionItemId], {
      attributes: true,
      attributeOldValue: true,
      attributeFilter: ['class']
    })
  },
  beforeDestroy () {
    this.observer.disconnect()
  },
  data () {
    return {
      isOpen: false,
      profileUrl: '',
      jcrUrl: '',
      coeUrl: ''
    }
  },
  methods: {
    onClassChange (classAttrValue) {
      const classList = classAttrValue.split(' ')
      this.isOpen = classList.includes('show')
    }
  }
}
</script>
<style scoped>
.card {
  border-radius: 0px;
  border-bottom: unset;
}

.card-header {
  border-bottom: unset;
}

.card-header:hover {
  background-color: #efefef !important;
  cursor: pointer;
}
</style>