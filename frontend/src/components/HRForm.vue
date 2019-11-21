<template>
<form class="container-fluid">
  <h4>Personal Information</h4>
  <div class="row">
    <div class="col-md-3">
      <div class="form-group">
        <label for="firstName">First name</label>
        <input type="text" class="form-control" id="firstName" placeholder="First name">
      </div>
    </div>

    <div class="col-md-2">
      <div class="form-group">
        <label for="lastName">Last name</label>
        <input type="text" class="form-control" id="lastName" placeholder="Last name">
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-md-2">
      <div class="form-group">
        <label for="birthDate">Birthday</label>
        <datepicker :value="birthDate" placeholder="Pick a date" id="birthDate" />
      </div>
    </div>

    <div class="col-md-1">
      <div class="form-group">
        <label for="gender">Gender</label>
        <select class="form-control" id="gender">
          <option>Male</option>
          <option>Female</option>
        </select>
      </div>
    </div>

    <div class="col-md-2">
      <div class="form-group">
        <label for="civilStatus">Civil status</label>
        <select class="form-control" id="civilStatus">
          <option>Single</option>
          <option>Married</option>
          <option>"Widowed</option>
          <option>Divorced</option>
        </select>
      </div>
    </div>
  </div>
  <!-- end of personal details -->
  <hr />
  <h4>Address</h4>
  <div class="row">
    <div class="col-md-1">
      <div class="form-group">
        <label for="unitNumber">Unit</label>
        <input type="text" class="form-control" id="unitNumber" placeholder="#">
      </div>
    </div>

    <div class="col-md-2">
      <div class="form-group">
        <label for="street">Street</label>
        <input type="text" class="form-control" id="street" placeholder="Street">
      </div>
    </div>

    <div class="col-md-2">
      <div class="form-group">
        <label for="city">City</label>
        <input type="text" class="form-control" id="city" placeholder="City">
      </div>
    </div>
  </div>

  <div class="row"> 
    <div class="col-md-3">
      <div class="form-group">
        <label for="country">Country</label>
        <vue-autosuggest
          :id="country"
          :suggestions="filteredCountries"
          :input-props="{placeholder: 'Country', class: 'form-control vue-autosuggest'}"
          @input="onInputChange"
          @selected="selectHandler"
          @click="clickHandler"
        />
      </div>
    </div>

    <div class="col-md-2">
      <div class="form-group">
        <label for="zipCode">Zip code</label>
        <input type="text" class="form-control" id="zipCode" placeholder="Zip code">
      </div>
    </div>
  </div>

  <hr />
  <h4>Job details</h4>
  <div class="row">
    <div class="col-md-2">
      <div class="form-group">
        <label for="dateHired">Date hired</label>
        <datepicker :id="dateHired" :value="dateHired" placeholder="Pick a date" />
      </div>
    </div>

    <div class="col-md-2">
      <div class="form-group">
        <label for="jobPositions">Position</label>
        <vue-autosuggest
          :id="jobPositions"
          :suggestions="filteredJobPositions"
          :input-props="{placeholder: 'Position', class: 'form-control vue-autosuggest'}"
          @input="onJobPositionInputChange"
          @selected="selectHandler"
          @click="clickHandler"
        />
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-md-2">
      <div class="form-group">
        <label for="jobUnits">Unit</label>
        <vue-autosuggest
          :id="jobUnits"
          :suggestions="filteredJobUnits"
          :input-props="{placeholder: 'Unit', class: 'form-control vue-autosuggest'}"
          @input="onJobUnitInputChange"
          @selected="selectHandler"
          @click="clickHandler"
        />
      </div>
    </div>

    <div class="col-md-2">
      <div class="form-group">
        <label for="jobLocations">Location</label>
        <vue-autosuggest
          :id="jobLocations"
          :suggestions="filteredJobLocations"
          :input-props="{placeholder: 'Location', class: 'form-control vue-autosuggest'}"
          @input="onJobLocationInputChange"
          @selected="selectHandler"
          @click="clickHandler"
        />
      </div>
    </div>
  </div>

</form>
</template>
<script>
import Datepicker from 'vuejs-datepicker'
import { VueAutosuggest } from 'vue-autosuggest'
import { getData } from 'country-list'

export default {
  components: {
    Datepicker,
    VueAutosuggest
  },
  created () {
    this.countries = [{
      data: getData()
    }]
    this.filteredCountries = [{
      data: this.countries[0].data.map(item => item.name)
    }]
    this.jobUnits = [{
      data: ['Unit 1', 'Unit 2']
    }]
    this.filteredJobUnits = this.jobUnits
    this.jobPositions = [{
      data: ['Position 1', 'Position 2']
    }]
    this.filteredJobPositions = this.jobPositions
    this.jobLocations = [{
      data: ['Location 1', 'Location 2']
    }]
    this.filteredJobLocations = this.jobLocations
  },
  mounted () {
    this.$el.querySelectorAll('.vdp-datepicker input').forEach((vdp) => {
      vdp.classList.add('form-control')
    })
  },
  data () {
    return {
      birthDate: null,
      dateHired: null,
      countries: null,
      filteredCountries: null,
      jobUnits: null,
      filteredJobUnits: null,
      jobPositions: null,
      filteredJobPositions: null,
      jobLocations: null,
      filteredJobLocations: null
    }
  },
  methods: {
    onInputChange (text) {
      if (text === '' || text === undefined) {
        return
      }

      this.filteredCountries = this.countries[0].data.filter(item => {
        return item.name.toLowerCase().indexOf(text.toLowerCase()) > -1
      }).slice(0, 5).map(item => item.name)

      this.filteredCountries = [{
        data: this.filteredCountries
      }]
    },
    selectHandler () {
    },
    clickHandler () {
    }
  }
}
</script>
