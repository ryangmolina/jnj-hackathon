<template>
  <div>
    <div id="faqAccordion">
      <!-- <accordion-item accordionItemId="default-item" headerId="default-item-header" accordionId="faqAccordion" /> -->
      <!-- <accordion-item accordionItemId="jcr-item" headerId="jcr-header" accordionId="faqAccordion" /> -->
      <accordion-item
        v-for="(item, index) in items"
        :item="item"
        :key="index"
        accordionId="faqAccordion"
        :accordionItemId="`collapse-item-${index}`"
        :headerId="`header-id-${index}`"
      />
    </div>
  </div>
</template>
<script>
import AccordionItem from 'app/components/AccordionItem.vue'

export default {
  props: [
    'items'
  ],
  components: {
    AccordionItem
  }
}
</script>