<template>
<div>
  <HRForm />

  <hr />

  <div class="container-fluid">
    <div class="row">
      <div class="col-md-6">
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
      <div v-for="result in results" :key="result.question" class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ result.question | truncate(20) }}</h5>
            <p class="card-text">
              {{ result.answer | truncate(100) }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>
</template>
<script>
import HRForm from 'app/components/HRForm.vue'

export default {
  components: {
    HRForm,
  },
  data () {
    return {
      results: [
        {
          question: 'How can I change my shipping address?',
          answer: 'By default, the last used shipping address will be saved into to your Sample Store account. When you are checking out your order, the default shipping address will be displayed and you have the option to amend it if you need to.',
        },
        {
          question: "WHAT HAPPENS IF THERE'S BEEN A DELIVERY MISHAP TO MY ORDER? (DAMAGED OR LOST DELIVERY)",
          answer: `
          We take such matters very seriously and will look into individual cases thoroughly. Any sample that falls under the below categories should not be thrown away before taking photo proof and emailing the photo of the affected sample and your D.O (Delivery Order) to us at help@samplestore.com (if applicable).
          We regret to inform you that no refunds will be given for orders that fall under the below categories.
          1. In the event of damaged samples received, we will require photo proof of the affected samples and your D.O (Delivery Order) in order for us to investigate and review before a decision is made to re-send the sample to you at no cost, subject to availability. In light of this, any sample that falls into this category should not be thrown away before taking photo proof and emailing the photo to us at help@samplestore.com
          2. In the event of lost mail, we will try to locate the delivery team in Singpost and if there's a clear indication that your order is indeed lost, we'll re-send the order to you at no cost, subject to availability.
          `
        },
        {
          question: 'WHAT ARE THE PAYMENT METHODS AVAILABLE?',
          answer: 'At the moment, we only accept Credit/Debit cards and Paypal payments.'
        },
        {
          question: 'CAN I PAY USING PAYPAL WITHOUT A PAYPAL ACCOUNT?',
          answer: `
          Yes! It is commonly misunderstood that a Paypal account is needed in order to make payments through Paypal. The truth is you DO NOT need one, although we strongly recommend you sign up to enjoy the added ease of use.
          Without a Paypal account, all you need is any Debit/Credit card stated below that is supported by Paypal.
          By using Paypal, we can process & deliver your orders to you in a shorter time. Paypal is the easiest & most secure way to make payment online. No account needed.
          `
        },
        {
          question: 'WHY IS THERE A CHECKOUT LIMIT? / WHAT ARE ALL THE CHECKOUT LIMITS?',
          answer: `
          Sample Store is a popular spot and gets lots of shoppers at a time. These limits are in place to make sure everyone has a good time trying and purchasing their products. So...
          - Each member is entitled to only one (1) sample order every day.
          - Each member is entitled to one (1) bundle of sample for each product.
          - Your account must have sufficient points before you can checkout the sample products.
          - Kindly clear all pending payments before another checkout.
          `
        }
      ]
    }
  },
  filters: {
    truncate (text, length, clamp = '...') {
      return text.length > length ? text.slice(0, length) + clamp : text
    }
  }
}
</script>
<style scoped>
.card {
  margin-bottom: 30px;
}
</style>