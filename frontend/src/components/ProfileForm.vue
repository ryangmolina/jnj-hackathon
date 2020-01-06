<template>
<div class="container-fluid">
  <h4>Personal Information</h4>
  <div class="row mb-2">
    <div class="col-lg-3 col-md-6">
      <div class="form-group">
        <label for="firstName">Employee Id</label>
        <input type="text" readonly class="form-control" id="firstName" placeholder="First name" :value="employeeId">
      </div>
    </div>
  </div>
  <div class="row mb-2">
    <div class="col-lg-3 col-md-6">
      <div class="form-group">
        <label for="firstName">First name</label>
        <input type="text" class="form-control" id="firstName" placeholder="First name" v-model="formData.first_name">
      </div>
    </div>

    <div class="col-lg-2 col-md-6">
      <div class="form-group">
        <label for="lastName">Last name</label>
        <input type="text" class="form-control" id="lastName" placeholder="Last name" v-model="formData.last_name">
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-2 col-md-5">
      <div class="form-group">
        <label for="formData.birth_date">Birthday</label>
        <datepicker placeholder="Pick a date" id="birthDate" v-model="formData.birth_date" />
      </div>
    </div>

    <div class="col-lg-1 col-md-3">
      <div class="form-group">
        <label for="gender">Gender</label>
        <select class="form-control" id="gender" v-model="formData.gender">
          <option value="MALE">M</option>
          <option value="FEMALE">F</option>
        </select>
      </div>
    </div>

    <div class="col-lg-2 col-md-4">
      <div class="form-group">
        <label for="civilStatus">Civil status</label>
        <select class="form-control" id="civilStatus" v-model="formData.civil_status">
          <option value="SINGLE">Single</option>
          <option value="MARRIED">Married</option>
          <option value="WIDOW">Widow</option>
          <option value="SEPARATED">Separated</option>j
        </select>
      </div>
    </div>
  </div>

  <hr />
  <h4>Educational Background</h4>
  <div class="row">
    <div class="col-lg-3 col-md-6">
      <div class="form-group">
        <label for="educationalAttainment">Educational attainment</label>
        <select class="form-control" id="educationalAttainment" v-model="formData.highest_educational_attainment">
          <option v-for="option in educationalAttainment" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>

    <div class="col-lg-2 col-md-6">
      <div class="form-group">
        <label for="educationalStatus">Educational status</label>
        <select class="form-control" id="educationalStatus" v-model="formData.educational_status">
          <option v-for="option in educationalStatus" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
  </div>

  <!-- end of personal details -->
  <hr />
  <h4>Address</h4>
  <!--
  <div class="row">
    <div class="col-lg-1 col-md-2">
      <div class="form-group">
        <label for="unitNumber">Unit</label>
        <input type="text" class="form-control" id="unitNumber" placeholder="#" v-model="formData.unit">
      </div>
    </div>

    <div class="col-lg-2 col-md-5">
      <div class="form-group">
        <label for="street">Street</label>
        <input type="text" class="form-control" id="street" placeholder="Street" v-model="formData.street">
      </div>
    </div>
  </div>
  -->

  <div class="row"> 
    <div class="col-lg-3 col-md-4">
      <div class="form-group">
        <label for="city">City</label>
        <select class="form-control" v-model="formData.city_municipality">
          <option v-for="option in cities" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>

    <div class="col-lg-2 col-md-4">
      <div class="form-group">
        <label for="city">Province</label>
        <select class="form-control" v-model="formData.province">
          <option v-for="option in provinces" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
  </div>

  <hr />
  <h4>Job details</h4>
  <div class="row">
    <div class="col-lg-3 col-md-6">
      <div class="form-group">
        <label for="jobRanks">Rank</label>
        <select class="form-control" id="civilStatus" v-model="formData.rank">
          <option v-for="option in jobRanks" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
   <div class="col-lg-2 col-md-6">
      <div class="form-group">
        <label for="jobUnits">Pay class</label>
        <select class="form-control" id="civilStatus" v-model="formData.pay_class">
          <option v-for="option in payClasses" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-3 col-md-6">
      <div class="form-group">
        <label for="jobUnits">Job Unit</label>
        <select class="form-control" id="civilStatus" v-model="formData.job_unit">
          <option v-for="option in jobUnits" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
    <div class="col-lg-2 col-md-6">
      <div class="form-group">
        <label for="jobUnits">Job Location</label>
        <select class="form-control" id="civilStatus" v-model="formData.job_loc">
          <option v-for="option in jobLocations" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-3 col-md-5">
      <div class="form-group">
        <label for="jobUnits">Last employee movement</label>
        <select class="form-control" id="civilStatus" v-model="formData.last_employee_movement">
          <option v-for="option in lastEmployeeMovement" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
    <div class="col-lg-2 col-md-5">
      <div class="form-group">
        <label for="jobUnits">Latest performance rating</label>
        <select class="form-control" id="civilStatus" v-model="formData.latest_performance_rating">
          <option v-for="option in performanceRating" :value="option" :key="option">{{ option }}</option>
        </select>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-2 col-md-5">
      <div class="form-group">
        <label for="jobUnits">Employee status</label>
        <select class="form-control" id="civilStatus" v-model="formData.employment_status">
          <option value="REG">Regular</option>
          <option value="PRO">Probationary</option>
        </select>
      </div>
    </div>
  </div>
  <button class="btn btn-outline-danger" @click="submit">Save</button>

  <!-- <div class="alert alert-success" role="alert" v-if="isSuccess">
    Update success
  </div> -->
</div>
</template>
<script>
import axios from 'axios'

import Datepicker from 'vuejs-datepicker'
import { VueAutosuggest } from 'vue-autosuggest'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  components: {
    Datepicker,
    VueAutosuggest
  },
  created () {
    this.jobUnits = [
      'FINANCE',
      'SALES',
      'HUMAN RESOURCES',
      'OPERATIONS'
    ]
    this.jobRanks = [
      'SUPERVISOR',
      'STAFF',
      'MANAGER',
      'ASST MANAGER',
      'OFFICER'
    ]

    const profileUrl = window.Urls['api:profiles']()
    axios
      .get(profileUrl)
      .then((response) => {
        this.formData = { ...this.formData, ...response.data }
        this.cityQuery = this.formData['city_municipality']
        this.provinceQuery = this.formData['province']
      })
  },
  mounted () {
    this.$el.querySelectorAll('.vdp-datepicker input').forEach((vdp) => {
      vdp.classList.add('form-control')
    })
  },
  data () {
    return {
      cityQuery: '',
      provinceQuery: '',
      educationalAttainment: [
        'COLLEGE',
        'JUNIOR HIGHSCHOOL',
        'VOCATIONAL'
      ],
      educationalStatus: [
        'UNDERGRADUATE',
        'GRADUATE'
      ],
      payClasses: [
        'S IV-B',
        'S III-B',
        'S VI',
        'S II-B',
        'BC VI',
        'S III-A',
        'S IV-A',
        'S V-B',
        'S V-A',
        'S II-A',
        'S VIII',
        'S VII',
        'S IX',
        'BC II',
        'BC III',
        'WC V',
        'WC IV',
        'WC III',
        'BC IV',
        'BC VIII',
        'BC IX',
        'BC V',
        'BC VII',
        'WC II',
        'S X',
        'S I',
        'S XII',
        'WC I',
        'S XIII',
        'S XI',
        'WC VI'
      ],
      jobUnits: [
        'FINANCE',
        'SALES',
        'HUMAN RESOURCES',
        'OPERATIONS'
      ],
      performanceRating: [
        'FULLY COMPLIES',
        'EXCEEDS',
        'EXCELS',
        'PARTIALLY MEETS',
        'TOO NEW TO RATE',
        'REQUIRES ACTION'
      ],
      jobRanks: [
        'SUPERVISOR',
        'STAFF',
        'MANAGER',
        'ASST MANAGER',
        'OFFICER'
      ],
      employeeStatus: [
        'REG',
        'PRO'
      ],
      jobLocations: [
        'PHILIPPINES',
        'SINGAPORE'
      ],
      lastEmployeeMovement: [
        'TRANSFER',
        'CORPORATE PROMOTION',
        'CONVERSION TO REGULAR',
        'PROBATIONARY APPOINTMENT'
      ],
      cities: [
        'VALENZUELA CITY',
        'TAGUIG CITY',
        'GUAGUA',
        'PANDACAN',
        'GUIGUINTO',
        'QUEZON CITY',
        'MARIKINA CITY',
        'CAINTA',
        'CALUMPIT',
        'SAN JUAN CITY',
        'MANDALUYONG CITY',
        'BAUAN',
        'ANTIPOLO CITY',
        'DAGUPAN CITY',
        'CALOOCAN CITY',
        'MAKATI CITY',
        'STA. CRUZ',
        'BINANGONAN',
        'PASIG CITY',
        'SAMPALOC',
        'LAS PINAS CITY',
        'LUISIANA',
        'BALIUAG',
        'MUNTINLUPA CITY',
        'MALOLOS CITY',
        'CAGAYAN DE ORO CITY',
        'BACOOR',
        'BATANGAS CITY',
        'SAN JOSE DEL MONTE',
        'SANTA',
        'TONDO NORTH',
        'SANTA CRUZ SOUTH',
        'MONTALBAN',
        'SURIGAO CITY',
        'SANPANG PALAY',
        'STO TOMA',
        'DASMARINAS',
        'LAOANG',
        'IMUS',
        'SAN MATEO',
        'TAYTAY',
        'IBAAN',
        'BINAN',
        'SANTA ANA',
        'PATEROS',
        'PASAY CITY',
        'SAMPALOC WEST',
        'STA. ANA',
        'SAN JOSE',
        'STO. TOMAS',
        'LUCENA',
        'MAGALLANES',
        'TANAY',
        'CANDELARIA',
        'LUCENA CITY',
        'SAN RAFAEL',
        'PARANAQUE CITY',
        'GUIMBA',
        'MALABON CITY',
        'MARILAO',
        'STO TOMAS',
        'PALAYAN CITY',
        'BALINGASAG',
        'PAETE',
        'SIGMA',
        'LINGAYEN',
        'STA ROSA CITY',
        'AGUILAR',
        'TANJAY CITY',
        'STA. MESA',
        'LIMAY',
        'MOGPOG',
        'RODRIGUEZ',
        'CALACA',
        'BAMBAN',
        'GAPAN CITY',
        'NABUA',
        'SAN LEONARDO',
        'BOCAUE',
        'NOVALICHES',
        'MALABON',
        'PLARIDEL',
        'SAN PABLO CITY',
        'SAMPALOC EAST',
        'URDANETA CITY',
        'LOBO',
        'MANILA',
        'MORONG',
        'MAASIN',
        'VALDEZ F. BLANCA',
        'PILILLA',
        'MEYCAUAYAN',
        'SAN FERNANDO',
        'SALAY',
        'ALITAGTAG',
        'LUYAN',
        'CEBU CITY',
        'TAYABAS',
        'CAIAO',
        'MALATE',
        'BALANGA CITY',
        'MALAY',
        'PILA',
        'ANGONO',
        'ILIGAN CITY',
        'ISABELA CITY',
        'SAN PEDRO',
        'SANTA MESA',
        'MABINI',
        'BARAS',
        'SAN MIGUEL',
        'CAVITE',
        'SAN NARCISO',
        'CITY OF SAN FERNANDO',
        'BAGUIO CITY',
        'HERMOSA',
        'BARUGO',
        'PINAGBUHATAN',
        'MANAOG',
        'EULOGIO RODRIGUEZ (MONTALBAN)',
        'CALAMBA CITY',
        'NORZAGARAY',
        'TAAL',
        'JAEN',
        'PILILIA',
        'VILLANUEVA',
        'LA PAZ',
        'NOVELETA',
        'PAVIA',
        'APALIT',
        'BONGABON',
        'MANAOAG',
        'CANDON CITY',
        'CALOOCAN CITY NORTH',
        'IGBARAS',
        'DON CARLOS',
        'ROSARIO',
        'URDANETA',
        'STO DOMINGO',
        'SAN ANDRES BUKID',
        'JASAAN',
        'ORION',
        'CABUYAO',
        'SILANG',
        'PACO',
        'HAGONOY',
        'TARLAC',
        'AMADEO',
        'TERNATE',
        'MATEO',
        'SAN JUAN',
        'CARDONA',
        'LABO',
        'STA. MARIA',
        'TONDO SOUTH',
        'SAN ROQUE-CALUMPANG',
        'ECHAGUE',
        'ORMOC CITY',
        'GENERAL TRIAS',
        'MACARTHUR',
        'CAN-AVID',
        'BATARAZA',
        'TAGUDIN',
        'SANTOLAN',
        'PUERTO PRINCESA CITY',
        'FLORIDA BLANCA',
        'MEXICO',
        'MACABEBE',
        'LIPA CITY',
        'STA MARGARITA',
        'MADRID',
        'CUYAPO',
        'BALAOAN',
        'PAGBILAO',
        'NORTHERN',
        'MALAYBALAY CITY',
        'PORT AREA SOUTH',
        'PAAGAN SANTOL',
        'STO TOMAS SOUTH',
        'SAN CARLOS CITY',
        'BACNOTAN',
        'SAN ILDEFONSO',
        'ALBAY CITY',
        'SANTA ROSA',
        'NAVOTAS'

      ],
      provinces: [
        'METRO MANILA',
        'PAMPANGA',
        'MANILA',
        'BULACAN',
        'RIZAL',
        'LA UNION PROVINCE',
        'PANGASINAN',
        'LAGUNA',
        'MISAMIS ORIENTAL',
        'CAVITE',
        'BATANGAS',
        'ILOCOS SUR',
        'SURIGAO DEL NORTE',
        'NORTHERN SAMAR',
        'LUCENA CITY',
        'ZAMBALES',
        'QUEZON PROVINCE',
        'NUEVA ECIJA',
        'CAPIZ',
        'NEGROS ORIENTAL',
        'BATAAN',
        'MARINDUQUE',
        'TARLAC',
        'CAMARINES SUR',
        'PASIG CITY',
        'SOUTHERN LEYTE',
        'QUEZON CITY',
        'CEBU',
        'MALAY',
        'LANAO DEL NORTE',
        'BASILAN',
        'BACOOR',
        'BENGUET',
        'LEYTE',
        'ILOILO',
        'BUKIDNON',
        'MUNTINLUPA',
        'CAMARINES NORTE',
        'MARIKINA CITY',
        'ISABELA',
        'EASTERN SAMAR',
        'PALAWAN',
        'MALABON CITY',
        'WESTERN SAMAR',
        'SURIGAO DEL SUR',
        'QUEZON',
        'ALBAY'
      ],
      formData: {
        first_name: '',
        last_name: '',
        birth_date: '',
        age: 0,
        generation: '',
        gender: '',
        civil_status: '',
        city_municipality: '',
        province: '',
        highest_educational_attainment: '',
        educational_status: '',
        tenure: 0,
        employment_status: '',
        pay_class: '',
        last_employee_movement: '',
        latest_performance_rating: '',
        job_loc: '',
        rank: '',
        job_unit: ''
      },
      isSuccess: false
    }
  },
  computed: {
    employeeId () {
      return String(this.formData.id).padStart(8, '0')
    }
  },
  methods: {
    submit () {
      const profileUrl = window.Urls['api:profiles']()
      this.formData['birth_date'] = new Date(this.formData['birth_date']).toISOString().split('T')[0]
      axios
        .patch(profileUrl, this.formData)
        .then((response) => {
          console.log(response.data)
          this.isSuccess = true
          const dashboardUrl = window.Urls['dashboard:index']()
          window.location = dashboardUrl
        })
    },
    getGeneration (year) {

    }
  }
}
</script>
