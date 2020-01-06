<template>
<ul class="navbar-nav ml-auto">
  <li class="nav-item no-arrow mx-1 dropdown">
    <a href="#" class="nav-link dropdown-toggle"
      data-toggle="dropdown"
      role="button"
      aria-haspopup="true"
      aria-expanded="false"
      id="notifications-dropdown"
    >
      <i class="fas fa-bell fa-fw"></i>
      <span class="badge badge-danger badge-counter">9+</span>
    </a>

    <div class="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in" aria-labelledby="notifications-dropdown">
      <h6 class="dropdown-header bg-gradient-branding-color">
        Alerts Center
      </h6>
      <a class="dropdown-item d-flex align-items-center" href="#">
        <div class="mr-3">
          <div class="icon-circle">
            <i class="fas fa-file-alt text-gray-700"></i>
          </div>
        </div>
        <div>
          <div class="small text-gray-500">November 25, 2019</div>
          <span class="font-weight-bold">Welcome to Johnson & Johnson</span>
        </div>
      </a>
      <a class="dropdown-item text-center small text-gray-500" href="#">Show all</a>
    </div>
  </li>
  <li class="nav-item dropdown no-arrow">
    <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      <span class="mr-2 d-none d-lg-inline text-gray-600 small">Ryan Molina</span>
      <avatar username="Ryan Molina" :size=40></avatar>
    </a>
    <!-- Dropdown - User Information -->
    <div class="dropdown-menu dropdown-menu-right shadow animated--grow-in" aria-labelledby="userDropdown">
      <a class="dropdown-item" :href="getProfileUrl">
        <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
        Profile
      </a>
      <div class="dropdown-divider"></div>
      <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">
        <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
        Logout
      </a>
    </div>
  </li>
</ul>
</template>
<script>
import Avatar from 'vue-avatar'

export default {
  components: {
    Avatar
  },
  computed: {
    getProfileUrl () {
      return window.Urls['accounts:index']()
    }
  }
}
</script>