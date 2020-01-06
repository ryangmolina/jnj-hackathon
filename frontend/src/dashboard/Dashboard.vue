<template>
<div>
  <hr />
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-6">
        <h3 class="text-primary">How can we help you?</h3>
        <div class="p-1 bg-white shadow-sm mb-4">
          <div class="input-group">
            <input type="search" placeholder="Describe your issue" aria-describedby="button-addon1" class="form-control border-0 bg-white searchbar">
            <div class="input-group-append">
              <button id="button-addon1" type="submit" class="btn btn-link text-default"><i class="fa fa-search"></i></button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <h5>Search results</h5>
    <div class="row">
      <div class="col-lg-6">
        <accordion :items="results" />
      </div>
    </div>
    <!--
    <hr />
    <h5>Check this out!</h5>
    <masonry :tiles="results" />
    -->
  </div>

</div>
</template>
<script>
import axios from 'axios'

import Accordion from 'app/components/Accordion.vue'
import Masonry from 'app/components/Masonry.vue'

export default {
  components: {
    Accordion,
    Masonry
  },
  data () {
    return {
      results: [
      ]
    }
  },
  created () {
    const personalizedQuestionUrl = window.Urls['api:personalizedQuestions']()
    axios
      .get(personalizedQuestionUrl)
      .then((response) => {
        const data = response.data.map(item => {
          return {
            title: item,
            text: ''
          }
        })
        this.results = [...this.results, ...data]
      })
  },
  filters: {
    truncate (text, length, clamp = '...') {
      return text.length > length ? text.slice(0, length) + clamp : text
    }
  }
}
</script>
<style scoped>
.searchbar {
  box-shadow: none;
}
</style>