<template>
  <div class="mt-3">
    <b-form-select v-model="selected" :options="options" v-on:change="selectItem"></b-form-select>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        selected: null,
        options: [
          { value: null, text: 'Please select an option' },
          { value: 'Amazon Web Services', text: 'Amazon Web Services' },
          { value: 'Google Cloud Platform', text: 'Google Cloud Platform' },
          { value:'Microsoft Azure Cloud', text: 'Microsoft Azure Cloud' }
        ]
      }
    },
    methods:{
      selectItem (e){
        this.$emit('selected', this.selected)
      }
    }
  }
</script>