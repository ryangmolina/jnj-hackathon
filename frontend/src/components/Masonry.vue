<template>

  <div v-masonry="containerId" transition-duration="0.3s" item-selector=".item">
    <div v-masonry-tile v-for="(tile, index) in tiles" :key="index" class="col-lg-4 col-md-6 item">
      <div class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">
            {{ tile.title }}
          </h5>
          <p class="card-text">
            {{ tile.text }}
          </p>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
import Vue from 'vue'
import { VueMasonryPlugin } from 'vue-masonry'

Vue.use(VueMasonryPlugin)

export default {
  props: [
    'tiles'
  ],
  created () {
    console.log(this.tiles)
  }
}
</script>