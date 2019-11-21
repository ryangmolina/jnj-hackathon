<template>
  <div>
    <ul class="progress-tracker progress-tracker--vertical">
      <li class="progress-step is-complete">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Step 1</h4>
          We will guide you to your job request journey. Click 'start' if you  want to procees.
          <div>
            <button class="btn btn-primary">Start</button>
          </div>
        </div>
      </li>
      <li class="progress-step is-active">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Step 2</h4>
        </div>
      </li>
      <li class="progress-step">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Step 3</h4>
        </div>
      </li>
      <li class="progress-step">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Step 4</h4>
        </div>
      </li>
      <li class="progress-step">
        <div class="progress-marker"></div>
        <div class="progress-text">
          <h4 class="progress-title">Step 5</h4>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
}
</script>
